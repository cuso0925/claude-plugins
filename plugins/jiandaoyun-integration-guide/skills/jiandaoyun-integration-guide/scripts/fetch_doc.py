#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拉取简道云官方文档正文，用于刷新技能的 references/ 知识库。

用法：
  python3 fetch_doc.py 14220                  # 打印文档 14220 的正文（markdown 化）
  python3 fetch_doc.py 14220 --save out.md    # 保存到文件
  python3 fetch_doc.py doc/11019              # doc 分类下的文档

文档 ID 可从 references/12-doc-index.md 查到，或从 https://hc.jiandaoyun.com/<分类>/<ID> 的 URL 中取。
"""
import argparse
import html
import re
import subprocess
import sys

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def fetch(doc_id):
    url = f"https://hc.jiandaoyun.com/{doc_id}" if "/" in doc_id else f"https://hc.jiandaoyun.com/open/{doc_id}"
    proc = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True)
    return url, proc.stdout.decode("utf-8", "ignore")


def extract(page):
    i = page.find("markdown-body")
    if i < 0:
        return None
    j = page.find(">", i) + 1
    k = page.find("<script", j)
    seg = page[j:k if k > j else len(page)]
    seg = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", seg, flags=re.S | re.I)
    seg = re.sub(r"<br\s*/?>", "\n", seg, flags=re.I)
    seg = re.sub(r"</(p|div|li|tr|h[1-6]|pre)>", "\n", seg, flags=re.I)
    seg = re.sub(r"</t[dh]>", " | ", seg, flags=re.I)
    seg = re.sub(r"<[^>]+>", "", seg)
    seg = html.unescape(seg)
    seg = re.sub(r"[ \t]+\n", "\n", seg)
    seg = re.sub(r"\n{3,}", "\n\n", seg)
    seg = re.sub(r"文档内容是否对您有帮助？.*$", "", seg, flags=re.S)
    return seg.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc_id", help="文档 ID，如 14220，或 doc/11019")
    ap.add_argument("--save", help="保存路径")
    a = ap.parse_args()

    url, page = fetch(a.doc_id)
    body = extract(page)
    if not body:
        print("未提取到正文，可能页面结构变化或需要登录。URL: " + url, file=sys.stderr)
        sys.exit(1)
    text = f"<!-- 来源: {url} -->\n\n{body}\n"
    if a.save:
        open(a.save, "w", encoding="utf-8").write(text)
        print(f"已保存 -> {a.save}")
    else:
        print(text)


if __name__ == "__main__":
    main()
