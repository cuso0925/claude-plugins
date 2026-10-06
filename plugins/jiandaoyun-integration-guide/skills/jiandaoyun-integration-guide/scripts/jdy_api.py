#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简道云开放 API 客户端模板（v5 路由）

安全约定：
  - API Key 只从环境变量 JDY_API_KEY 读取，禁止硬编码、禁止上传云端/第三方。
  - 用法：export JDY_API_KEY="你的密钥"

常用命令：
  python3 jdy_api.py widgets <app_id> <entry_id>              # 查表单字段（先做这个）
  python3 jdy_api.py list <app_id> <entry_id> --limit 100 --all
  python3 jdy_api.py get <app_id> <entry_id> <data_id>
  python3 jdy_api.py create <app_id> <entry_id> --data-file data.json
  python3 jdy_api.py update <app_id> <entry_id> <data_id> --data-file data.json
  python3 jdy_api.py delete <app_id> <entry_id> <data_id>
  python3 jdy_api.py apps                                     # 用户应用查询
  python3 jdy_api.py entries <app_id>                         # 用户表单查询
  python3 jdy_api.py member <username>                        # 获取成员信息
  python3 jdy_api.py dept-list [dept_no]                      # （递归）获取部门列表
  python3 jdy_api.py tasks                                    # 查询我的待办

data.json 格式（字段名用 _widget_xxx，值放在 value 里）：
  {
    "_widget_1432728651402": {"value": "简道云"},
    "_widget_1432728651403": {"value": 100}
  }
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE = "https://api.jiandaoyun.com/api"
TIMEOUT = 30


class JdyError(Exception):
    pass


def _api_key():
    key = os.environ.get("JDY_API_KEY")
    if not key:
        raise JdyError("未设置环境变量 JDY_API_KEY（export JDY_API_KEY='你的密钥'）")
    return key


def call(path, payload=None, retries=3, backoff=1.5):
    """调用简道云 API。path 形如 /v5/app/entry/data/list"""
    url = BASE + path
    body = json.dumps(payload or {}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Authorization", "Bearer " + _api_key())
    req.add_header("Content-Type", "application/json; charset=utf-8")

    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                text = resp.read().decode("utf-8")
                return json.loads(text) if text else {}
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")
            try:
                err = json.loads(detail)
            except Exception:
                err = {"code": e.code, "msg": detail}
            # 8303 为超频，退避后重试；其余直接抛错
            if err.get("code") == 8303 and attempt < retries - 1:
                time.sleep(backoff ** (attempt + 1))
                last = err
                continue
            raise JdyError("HTTP %s  code=%s  msg=%s" % (e.code, err.get("code"), err.get("msg")))
        except urllib.error.URLError as e:
            last = e
            time.sleep(backoff ** (attempt + 1))
    raise JdyError("请求失败（已重试 %d 次）：%s" % (retries, last))


def out(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def load_json(path, what):
    try:
        return json.load(open(path, encoding="utf-8"))
    except FileNotFoundError:
        raise JdyError("%s 文件不存在：%s" % (what, path))
    except json.JSONDecodeError as e:
        raise JdyError("%s 不是合法 JSON（%s）：%s" % (what, e, path))


def main():
    p = argparse.ArgumentParser(description="简道云开放 API 客户端（v5）")
    sub = p.add_subparsers(dest="cmd", required=True)

    def s(name, *args):
        sp = sub.add_parser(name)
        for a in args:
            sp.add_argument(a)
        sp.add_argument("--data-file", help="JSON 文件路径，内容为 data 字段的值")
        sp.add_argument("--limit", type=int, default=100)
        sp.add_argument("--all", action="store_true", help="自动翻页拉取全部（仅 list）")
        return sp

    s("widgets", "app_id", "entry_id")
    s("list", "app_id", "entry_id")
    s("get", "app_id", "entry_id", "data_id")
    s("create", "app_id", "entry_id")
    s("update", "app_id", "entry_id", "data_id")
    s("delete", "app_id", "entry_id", "data_id")
    s("apps")
    s("entries", "app_id")
    s("member", "username")
    s("dept-list").add_argument("dept_no", nargs="?", default="1")
    s("tasks")

    # create/update 常用开关
    for name in ("create", "update"):
        sub.choices[name].add_argument("--creator", help="数据提交人 username")
        sub.choices[name].add_argument("--start-workflow", action="store_true", help="发起流程（默认否）")
        sub.choices[name].add_argument("--start-trigger", action="store_true", help="触发智能助手（默认否）")
    sub.choices["list"].add_argument("--filter-file", help="filter JSON 文件路径")

    a = p.parse_args()

    try:
        if a.cmd == "widgets":
            out(call("/v5/app/entry/widget/list", {"app_id": a.app_id, "entry_id": a.entry_id}))

        elif a.cmd == "list":
            payload = {"app_id": a.app_id, "entry_id": a.entry_id, "limit": min(a.limit, 100)}
            if a.filter_file:
                payload["filter"] = load_json(a.filter_file, "filter")
            rows, cursor = [], None
            while True:
                if cursor:
                    payload["data_id"] = cursor
                res = call("/v5/app/entry/data/list", payload)
                batch = res.get("data", [])
                rows.extend(batch)
                if not a.all or not batch or len(batch) < payload["limit"]:
                    break
                cursor = batch[-1].get("_id")
                if not cursor:
                    break
            out({"count": len(rows), "data": rows})

        elif a.cmd == "get":
            out(call("/v5/app/entry/data/get",
                     {"app_id": a.app_id, "entry_id": a.entry_id, "data_id": a.data_id}))

        elif a.cmd in ("create", "update"):
            if not a.data_file:
                raise JdyError("需要 --data-file 指定数据 JSON 文件")
            data = load_json(a.data_file, "data")
            payload = {"app_id": a.app_id, "entry_id": a.entry_id, "data": data}
            if a.creator:
                payload["data_creator"] = a.creator
            if a.start_workflow:
                payload["is_start_workflow"] = True
            if a.start_trigger:
                payload["is_start_trigger"] = True
            if a.cmd == "create":
                out(call("/v5/app/entry/data/create", payload))
            else:
                payload["data_id"] = a.data_id
                out(call("/v5/app/entry/data/update", payload))

        elif a.cmd == "delete":
            out(call("/v5/app/entry/data/delete",
                     {"app_id": a.app_id, "entry_id": a.entry_id, "data_id": a.data_id}))

        elif a.cmd == "apps":
            out(call("/v5/user/app/list", {"skip": 0, "limit": 100}))

        elif a.cmd == "entries":
            out(call("/v5/app/entry/list", {"app_id": a.app_id}))

        elif a.cmd == "member":
            out(call("/v5/corp/member/get", {"username": a.username}))

        elif a.cmd == "dept-list":
            out(call("/v5/corp/department/list", {"dept_no": int(a.dept_no), "has_child": True}))

        elif a.cmd == "tasks":
            out(call("/v5/processInstance/task/list", {"skip": 0, "limit": 100}))

    except JdyError as e:
        print("ERROR: %s" % e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
