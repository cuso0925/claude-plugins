# 流程接口

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 流程接口

- 官方文档：https://hc.jiandaoyun.com/open/12344

1. 开发准备

开发前，请仔细阅读 开发指南。

2. 接口列表

流程接口主要包括以下接口：

接口名称

 | 释义

 |
获取单条流程表单数据的审批意见

 | 该接口用来获取单条表单流程数据的审批意见。

 |
查询流程实例信息

 | 该接口用来查询流程实例信息。

 |
结束流程实例

 | 该接口用于结束当前流程实例。

 |
流程待办查询

 | 该接口用来获取当前用户待办信息。

 |
流程待办提交

 | 该接口用来提交流程待办。

 |
流程待办回退

 | 该接口用来回退流程待办。

 |
流程待办转交

 | 该接口用来转交流程待办。

 |
流程激活

 | 该接口用于激活当前流程实例。

 |
流程待办撤回

 | 该接口用于将流程待办撤回。

 |
流程待办加签

 | 该接口用于对当前流程的待办加签。

 |
3. 流程错误代码列表

错误码

 | 说明

 |
4005

 | 操作失败，不允许撤回

 |
4007

 | 操作失败，没有流程处理人

 |
4008

 | 操作失败，流程已经关闭

 |
4009

 | 操作失败，无权限

 |
4016

 | 操作失败，流程不能转交给自己

 |
4026

 | 流程状态，进行中流程无法激活

 |
5003

 | 流程节点不存在

 |
5004

 | 未提交流程审批意见

 |
5006

 | 无法将数据流转到抄送节点

 |
5008

 | 找不到对应的负责人

 |
5009

 | 找不到回退后的负责人

 |
5010

 | 无效的流程数据

 |
5011

 | 找不到流转节点

 |
5012

 | 未提交流程手写签名

 |
5024

 | 当前用户对该节点无提交权限

 |
5025

 | 当前节点已经流转完成

 |
5026

 | 流程节点批量审批失败

 |
5034

 | 目标节点包含子流程/插件节点

 |
5044

 | 子流程配置错误或找不到发起人

 |
5045

 | 发起子流程数据超过上限 200

 |
5049

 | 当前流程节点未开启转交

 |
5053

 | 流入多级主管审批节点失败，未指定发起部门

 |
5056

 | 不能对非流程表单进行流程操作

 |
5058

 | 数据已关联流程，不可重复发起

 |
5059

 | 数据提交人已被删除

 |
5060

 | 非流程表单，不支持该操作

 |
50000

 | 目标节点不存在

 |
50004

 | 待办任务不存在

 |
50009

 | 流程已被处理，不允许撤回

 |
50013

 | 负责人调整前后数目必须一致

 |
50015

 | 负责人调整前后无实际变化

 |
50016

 | 流程实例不存在

 |
50019

 | 不支持的审批行为

 |
50024

 | 调整后负责人不能为空

 |
50031

 | 流程数据不存在

 |
50034

 | 不支持的流程操作类型

 |
50040

 | 当前节点禁止回退

 |
50041

 | 回退节点为当前节点

 |
50046

 | 历史待办（子流程）过多，不允许激活

 |
50049

 | 不允许回退到没有创建者的发起节点

 |
50052

 | 节点不支持该加签行为

 |
50053

 | 加签候选人列表不能为空

 |
50054

 | 不支持嵌套加签

 |
50057

 | 加签配置未开启

 |
50059

 | 加签候选人不能选择节点负责人

 |
50060

 | 加签候选人非法

 |
50061

 | 不支持多人加签

 |
50062

 | 待被加签人处理中

 |
50063

 | 被加签待办不可批量提交

 |
50064

 | 异步子流程成环，请调整流程配置

 |
50070

 | 不允许回退到插件节点

 |
50071

 | 版本不支持插件节点

 |
50073

 | 禁止回退到进行中节点

 |
50076

 | 该节点不可激活

 |


---

## 查询流程实例审批意见

- 官方文档：https://hc.jiandaoyun.com/open/16050

1. 简介

该接口用来获取单条表单流程数据的审批意见。

2. 接口调用

该接口用来获取单条表单流程数据的审批意见。

接口版本说明：

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2020.7.7

 | 原始接口

 |
请求地址：https://api.jiandaoyun.com/api/v1/app/{app_id}/entry/{entry_id}/data/{data_id}/approval_comments

请求频率：30 次/秒

请求方式：POST

URL 参数:

参数

 | 类型

 | 说明

 |
appId

 | String

 | 应用 ID

 |
entryId

 | String

 | 表单 ID

 |
dataId

 | String

 | 流程表单数据 ID

 |
Body 参数:

参数

 | 类型

 | 说明

 |
skip

 | Number

 | 偏移量,，即跳过多少条审批意见。由于每次最多返回 100 条审批意见，因此如果要查询第 100 条之后的结果，需要将该参数设定为 100，如果需要查询第 200 条之后的结果，需要将该参数设定为 200，以此类推。

 |
属性说明:

属性

 | 类型

 | 说明

 |
approveCommentList

 | [JSON]

 | 审批意见列表

 |
approveCommentList[*].flowNodeName

 | String

 | 流程节点名称

 |
approveCommentList[*].flowAction

 | String

 | 动作, 枚举:

forward - 提交

transfer - 转交

back - 回退

close - 结束

sign_before - 前加签

sign_after - 后加签

sign_parallel - 添加审批人

 |
approveCommentList[*].comment

 | String

 | 审批意见评论

 |
approveCommentList[*].signature_url?

 | String

 | 审批意见手写签名 URL, 可选, 15 天有效期

 |
响应示例:

POST - /api/v1/app/{app_id}/entry/{entry_id}/data/{data_id}/approval_comments
{
    "approveCommentList": [
        {
            "operator": {
                "_id": "5ed78abead7b951a243cc828",
                "username": "jdy-y69rlimdfquz",
                "status": 1，
                "name": "AngelMsger"
            },
            "flowAction": "forward",
            "comment": "一条审批意见",
            "flowNodeName": "必须手写签名",
            "signature_url": "https://files.jiandaoyun.com/FtMNaGofTPeLMFW5_5SCs8w2mX8h?e=1595347199&token=bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:iac5fKQqYDZkF1YyvJUm4YRDPzg="
        }
    ]
}


---

## 查询流程实例信息

- 官方文档：https://hc.jiandaoyun.com/open/16051

1. 简介

1.1 接口简介

该接口用来查询流程实例信息。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.28

 | 原始接口

 |
V2

 | 2023.03.02

 | 调整部分参数名：

新增应用 id：app_id；
表单 id 的参数由entry_id 变更为form_id。
 |
V3

 | 2023.04.17

 | 1）新增实例访问链接和待办列表参数名：

实例访问链接：url；
应用 id：tasks[].app_id；
表单 id：tasks[].form_id；
表单名称：tasks[].form_title；
实例 id：tasks[].instance_id；
待办 id：tasks[].task_id；
待办访问链接：tasks[].url；
实例创建者信息：tasks[].creator。
2）调整待办列表信息参数名

待办列表参数由原来的 node_list 变更为 tasks；
当前处理人信息 assignee_list 变更为待办人信息 tasks[].assignee；
待办列表中，节点名称 node_list[].name 变更为 tasks[].flow_name；
待办列表中，节点id node_list[].flow_id 变更为 tasks[].flow_id。
3）取消节点类型参数 node_list[].type。

 |
V4

 | 2023.09.18

 | 1）新增请求参数

返回待办种类：tasks_type；
2）新增响应参数，如下所示：

结束时间：finish_time
待办名称：tasks[].title
待办开始时间：tasks[].create_time
待办结束时间：tasks[].finish_time
待办状态：tasks[].status
 |
V5

 | 2023.12.01

 | 新增 2 个响应参数，如下所示：

创建待办的流程动作：tasks[].create_action
完成待办的流程动作：tasks[].finish_action
 |
v6

 | 2024.12.26

 | 1）新增响应参数

审批结果：result
2）响应参数 tasks[].finish_action 完成待办的流程动作新增动作类型

否决：reject
 |
2. 接口调用

该接口用来查询流程实例信息。

请求地址：https://api.jiandaoyun.com/api/v6/workflow/instance/get

请求频率：30 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | String

 | 实例 id，同 data_id

 |
tasks_type

 | 否

 | number

 | 返回待办种类，0 表示不返回；1 表示全部返回

 |

请求示例：

{
    "instance_id": "63ff32d918fbc20007a4a082",
    "tasks_type":1
}

响应参数：

参数

 | 类型

 | 说明

 |
app_id

 | String

 | 应用 id

 |
form_id

 | String

 | 表单 id

 |
form_title

 | String

 | 表单名称

 |
instance_id

 | String

 | 实例 id

 |
url

 | String

 | 实例访问链接

 |
update_time

 | String

 | 实例修改时间

 |
create_time

 | String

 | 创建时间

 |
finish_time

 | String

 | 结束时间

 |
creator

 | Object

 | 创建者信息 同 成员实体结构

 |
status

 | Number

 | 实例状态，枚举：

0 - 进行中

1 - 流程已完成

2 - 手动结束

 |
result

 | Number

 | 审批结果（仅已完成时存在）

0 - 否决

1 - 流转完成

 |
tasks

 | Object

 | 待办任务列表

 |
tasks[].app_id

 | String

 | 应用 id

 |
tasks[].form_id

 | String

 | 表单 id

 |
tasks[].form_title

 | String

 | 表单名称

 |
tasks[].title

 | String

 | 待办名称

 |
tasks[].instance_id

 | String

 | 实例 id

 |
tasks[].task_id

 | String

 | 待办 id

 |
tasks[].flow_id

 | Number

 | 节点 id

 |
tasks[].flow_name

 | String

 | 节点名称

 |
tasks[].url

 | String

 | 待办访问链接

 |
tasks[].assignee

 | Object

 | 待办人信息 同 成员实体结构

 |
tasks[].creator

 | Object

 | 实例创建者信息 同 成员实体结构

 |
tasks[].create_time

 | String

 | 待办开始时间

 |
tasks[].create_action

 | String

 | 创建待办的流程动作，枚举：

auto_approve： 去重审批
forward：提交
back：回退
transfer：转交
revoke：撤回
activate：激活
auto_forward：超时自动提交
auto_back：超时自动回退
batch_forward：批量提交
batch_transfer：批量调整负责人
sign_before：前加签
sign_after：后加签
sign_parallel：并加签
invoke_plugin：插件执行
 |
tasks[].finish_time

 | String

 | 完成待办时间

 |
tasks[].finish_action

 | String

 | 完成待办的流程动作，枚举：

auto_approve：去重审批
forward：提交
back：回退
close：关闭
transfer：转交
batch_forward：批量提交
sign_after：后加签
reject：否决
 |
tasks[].status

 | Number

 | 待办状态

0-进行中

1-已完成

2-手动结束

4-被激活

5-任务被暂停

 |
响应示例：

{
    "app_id": "628d8c0d73544c0006a54bfd",
    "form_id": "63f31ae8144f4a09ec197163",
    "form_title": "物品信息借用",
    "instance_id": "63ff32d918fbc20007a4a082",
    "url": "https://www.jiandaoyun.com/workflow/process_instance/63ff32d918fbc20007a4a082",
    "update_time": "2022-10-26T13:18:57.605Z",
    "create_time": "2022-10-26T13:11:45.087Z",
    "finish_time": null,
    "status": 0,
    "creator": {
        "username": "xiaojian",
        "name": "小简",
        "departments": [
            1
        ],
        "type": 0,
        "status": 1
    },
    "tasks": [
        {
            "app_id": "628d8c0d73544c0006a54bfd",
            "form_id": "63f31ae8144f4a09ec197163",
            "form_title": "物品信息借用",
            "title": "流程发起节点",
            "instance_id": "63ff32d918fbc20007a4a082",
            "task_id": "63f31ae8144f4a09ec197162",
            "flow_id": 0,
            "flow_name": "流程发起节点",
            "url": "https://www.jiandaoyun.com/workflow/process_instance/63ff32d918fbc20007a4a082/task/63f31ae8144f4a09ec197162",
            "assignee": {
                "username": "xiaoyun",
                "name": "小云",
                "departments": [
                    1
                ],
                "type": 0,
                "status": 1
            },
            "creator": {
                "username": "xiaojian",
                "name": "小简",
                "departments": [
                    1
                ],
                "type": 0,
                "status": 1
            },
            "create_time": "2022-10-26T13:11:45.087Z",
            "create_action": "forward",
            "finish_time": 2022-10-26T13:11:45.087Z,
            "finish_action": "forward",
            "status": 1
         },
        {
            "app_id": "628d8c0d73544c0006a54bfd",
            "form_id": "63f31ae8144f4a09ec197163",
            "form_title": "物品信息借用",
            "title": "审批",
            "instance_id": "63ff32d918fbc20007a4a082",
            "task_id": "63f31ae8144f4a09ec197163",
            "flow_id": 2,
            "flow_name": "审批",
            "url": "https://www.jiandaoyun.com/workflow/process_instance/63ff32d918fbc20007a4a082/task/63f31ae8144f4a09ec197163",
            "assignee": {
                "username": "xiaoyun",
                "name": "小云",
                "departments": [
                    1
                ],
                "type": 0,
                "status": 1
            },
            "creator": {
                "username": "xiaojian",
                "name": "小简",
                "departments": [
                    1
                ],
                "type": 0,
                "status": 1
            },
            "create_time": "2022-10-26T13:18:57.605Z",
            "create_action": "forward",
            "finish_time": null,
            "finish_action": null,
            "status": 0
        }
    ]
}

3. 注意事项

部分流程动态，如子流程、插件节点以及抄送节点，无法用该接口获取到。


---

## 查询流程日志

- 官方文档：https://hc.jiandaoyun.com/open/18793

1. 简介

1.1 接口简介

该接口用来查询流程日志信息，目前仅支持返回包含审批意见的流程日志。

1.2 接口版本

接口版本

 | 更新时间

 | 接口说明

 |
v1

 | 2024.01.19

 | 原始接口

 |
2. 接口调用

该接口用来查询流程日志信息。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/instance/logs

请求频率：30 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | string

 | 实例 id，同 data_id

 |
types

 | 是

 | string[]

 | 返回的日志类型，可选项；

审批意见：“comment”

 |
limit

 | 否

 | number

 | 分页参数

页大小默认 100 ，最大 100

 |
skip

 | 否

 | number

 | 分页参数，跳过前面数据条数

默认为 0

 |
请求示例：

{
    "instance_id": "659cba93489a49c06f7d4281",
    "types": [
        "comment"
    ],
    "skip": 0,
    "limit": 10
}

响应参数：

参数

 | 类型

 | 说明

 |
logs

 | object[]

 | 日志列表

 |
logs[].flow_id

 | number

 | 节点 ID

 |
logs[].flow_name

 | string

 | 节点名称

 |
logs[].create_action

 | string

 | 创建待办的流程动作

 |
logs[].create_time

 | Date

 | 待办开始时间

 |
logs[].finish_action

 | string

 | 完成待办的流程动作

 |
logs[].finish_time

 | Date

 | 待办完成时间

 |
logs[].comment

 | string

 | 审批意见内容

 |
logs[].signature

 | object

 | 审批意见手写签名

 |
logs[].signature.url

 | string

 | 审批意见手写签名URL，15 天有效期

 |
logs[].attachments

 | object[]

 | 附件列表

 |
logs[].attachments[].name

 | string

 | 附件文件名

 |
logs[].attachments[].size

 | number

 | 附件文件大小

 |
logs[].attachments[].mime

 | string

 | 附件文件类型

 |
logs[].attachments[].url

 | string

 | 附件文件URL，15 天有效期

 |
logs[].operator

 | object

 | 审批/操作人信息，同 成员实体结构

 |
响应示例：

{
    "logs": [
        {
            "flow_id": 1,
            "flow_name": "必须手写签名",
            "create_time": "2024-01-09T03:16:35.447Z",
            "create_action": "forward",
            "finish_time": "2024-01-09T03:17:03.239Z",
            "finish_action": "forward",
            "operator": {
                "username": "xiaojian",
                "name": "小简",
                "departments": [
                    1
                ],
                "type": 0,
                "status": 1
            },
            "comment": "一条审批意见",
            "signature": {
                "url": "https://files.jiandaoyun.com/FtMNaGofTPeLMFW5_5SCs8w2mX8h?e=1595347199&token=bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:iac5fKQqYDZkF1YyvJUm4YRDPzg="
            },
            "attachments": [
                {
                    "name": "WechatIMG21.jpeg",
                    "size": 74935,
                    "mime": "image/jpeg",
                    "url": "https://files.jiandaoyun.com/FtMNaGofTPeLMFW5_5SCs8w2mX8h?e=1595347199&token=bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:iac5fKQqYDZkF1YyvJUm4YRDPzg="
                },
                {
                    "name": "6b2cc009-141d-44c4-b5fc-5d01667ee0f8.jpg",
                    "size": 33174,
                    "mime": "image/jpeg",
                    "url": "https://files.jiandaoyun.com/FtMNaGofTPeLMFW5_5SCs8w2mX8h?e=1595347199&token=bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:iac5fKQqYDZkF1YyvJUm4YRDPzg="
                },
                {
                    "name": "24x24.png",
                    "size": 34281,
                    "mime": "image/png",
                    "url": "https://files.jiandaoyun.com/FtMNaGofTPeLMFW5_5SCs8w2mX8h?e=1595347199&token=bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:iac5fKQqYDZkF1YyvJUm4YRDPzg="
                }
            ]
        }
    ]
}


---

## 结束流程实例

- 官方文档：https://hc.jiandaoyun.com/open/16052

1. 简介

1.1 接口简介

该接口用于管理员结束当前流程实例。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.28

 | 原始接口

 |
2. 接口调用

该接口用于管理员结束当前流程实例。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/instance/close

请求频率：20 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | String

 | 实例 id，同 data_id。结束对应的流程实例。

 |

请求示例：

{
    "instance_id": "6358a65878b1fb0007aba61b"
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | String

 | success：表示接口调用成功

failure：表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | Number

 | 错误码

 |
message

 | String

 | 返回码的描述

 |

响应示例：

成功示例
{
    "status": "success"
}

失败示例
{
    "code": 4008,
    "message": "操作失败,流程已经关闭",
    "status": "failure"
}


---

## 激活流程实例

- 官方文档：https://hc.jiandaoyun.com/open/17366

1. 简介

1.1 接口简介

流程激活接口用于激活当前流程实例。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2023.08.01

 | 原始接口

 |
2. 接口调用

该接口用于激活当前流程实例。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/instance/activate

请求频率：20 次/s

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | string

 | 激活对应的流程实例

 |
flow_id

 | 是

 | number

 | 激活的节点 id

 |
请求示例：

{
    "instance_id": "64c7274cd172150007f2533d",
    "flow_id": 1
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | string

 | success 表示接口调用成功

failure 表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | number

 | 错误码（仅 failure 时返回）

 |
message

 | string

 | 返回码的描述（仅 failure 时返回）

 |
响应示例：

{
    "status": "success"
}


---

## 查询我的待办

- 官方文档：https://hc.jiandaoyun.com/open/16053

1. 简介

1.1 接口简介

该接口可以获取用户当前的流程待办信息。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.12

 | 原始接口

 |
v1

 | 2022.10.28

 | 接口频率由 5 次/秒调整为 30 次/秒

 |
v2

 | 2023.03.02

 | 调整部分参数名：

新增应用 id： tasks[].app_id ；
新增表单 id：tasks[].form_id；
调整 tasks[].task_id 名称为待办 id。
 |
v3

 | 2023.03.17

 | 新增 flow_id、flow_name 两个响应参数。

 |
v4

 | 2023.09.18

 | 新增 3 个响应参数，如下所示：

待办开始时间：tasks[].create_time
待办结束时间：tasks[].finish_time
待办状态：tasks[].status
 |
v5

 | 2023.12.01

 | 新增 2 个响应参数，如下所示：

创建待办的流程动作：tasks[].create_action
完成待办的流程动作：tasks[].finish_action
 |
v6

 | 2026.05.28

 | 调整请求参数：

取消分页参数 skip
新增请求参数：待办 id： task_id
请求频率由 30 次/秒调整为 20 次/秒。

 |
2. 接口调用

该接口用来获取用户当前待办信息。

请求地址：https://api.jiandaoyun.com/api/v6/workflow/task/list

请求频率：20 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 用户名，即成员编号

 |
limit

 | 否

 | Number

 | 分页参数，页大小 默认 10 最大 100

 |
task_id

 | 否

 | Number

 | 分页符，上一次查询待办列表时最后一条数据的 task_id，没有则留空。

 |
请求示例：

{
    "username": "xiaoyun",
    "task_id": "63f31ae8144f4a09ec197163",
    "limit": 10
}

响应参数：

参数

 | 类型

 | 说明

 |
has_more

 | Boolean

 | 后面是否还有数据

 |
tasks

 | Object[]

 | 待办列表

 |
tasks[].app_id

 | String

 | 应用 id

 |
tasks[].form_id

 | String

 | 表单 id

 |
tasks[].task_id

 | String

 | 待办 id

 |
tasks[].instance_id

 | String

 | 实例 id，同 data_id

 |
tasks[].form_title

 | String

 | 表单名称

 |
tasks[].title

 | String

 | 待办名称

 |
tasks[].flow_id

 | Number

 | 节点 id

 |
tasks[].flow_name

 | String

 | 节点名称

 |
tasks[].url

 | String

 | 待办访问链接

 |
tasks[].assignee

 | Object

 | 待办人信息同 成员实体结构

 |
tasks[].creator

 | Object

 | 待办创建者信息同 成员实体结构

 |
tasks[].create_time

 | String

 | 待办开始时间

 |
tasks[].create_action

 | String

 | 创建待办的流程动作，枚举：

auto_approve： 去重审批
forward：提交
back：回退
transfer：转交
revoke：撤回
activate：激活
auto_forward：超时自动提交
auto_back：超时自动回退
batch_forward：批量提交
batch_transfer：批量调整负责人
sign_before：前加签
sign_after：后加签
sign_parallel：并加签
invoke_plugin：插件执行
 |
tasks[].finish_time

 | String

 | 待办结束时间

 |
tasks[].finish_action

 | String

 | 完成待办的流程动作，恒为 null

 |
tasks[].status

 | Number

 | 待办状态，恒为 0（进行中）

 |
响应示例：

{
    "has_more": false,
    "tasks": [
        {
            "app_id": "628d8c0d73544c0006a54bfd",
            "task_id": "63f31ae8144f4a09ec197163",
            "form_id": "63ff33531c2f7e5fe8789b4b",
            "instance_id": "628d8c0d73544c0006a54bfc",
            "form_title": "待办测试表单标题",
            "title": "待办标题",
            "flow_id": 1,
            "flow_name": "节点1",
            "url": "",
            "assignee": {
                "username": "xiaoyun",
                "name": "小云",
                "departments": [
                    1,
                    3
                ],
                "type": 0,
                "status": 1,
                "integrate_id": "xiaoyun"
            },
            "creator": {
                "username": "xiaojian",
                "name": "小简",
                "departments": [
                    1,
                    3
                ],
                "type": 0,
                "status": 1,
                "integrate_id": "xiaojian"
            },
            "create_time": "2022-10-26T13:18:57.605Z",
            "create_action": "forward",
            "finish_time": null,
            "finish_action": null,
            "status": 0
        }
    ]
}


---

## 流程待办提交

- 官方文档：https://hc.jiandaoyun.com/open/16054

1. 简介

1.1 接口简介

该接口用来提交流程待办。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.28

 | 原始接口

 |
2. 接口调用

该接口用来提交流程待办。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/task/approve

请求频率：20 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 用户名，即成员编号

 |
instance_id

 | 是

 | String

 | 实例 id，同 data_id

 |
task_id

 | 是

 | String

 | 任务 id（需要和 username 一一对应）

 |
comment

 | 否

 | String

 | 审批意见

 |

请求示例：

{
    "username": "xiaoyun",
    "instance_id":  "6358a65878b1fb0007aba61b",
    "task_id": "6358a65878b1fb0007aba63c"
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | String

 | success：表示接口调用成功

failure：表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | Number

 | 错误码

 |
message

 | String

 | 返回码的描述

 |

响应示例：

成功示例
{
    "status": "success"
}

失败示例
{
    "code": 1010,
    "message": "用户不存在",
    "status": "failure"
}


---

## 流程待办回退

- 官方文档：https://hc.jiandaoyun.com/open/16055

1. 简介

1.1 接口简介

该接口用来回退流程待办。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.28

 | 原始接口

 |
v2

 | 2025.12.17

 | 新增请求参数：

back_type
 |
2. 接口调用

该接口用来回退流程待办。

请求地址：https://api.jiandaoyun.com/api/v2/workflow/task/rollback

请求频率：20 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 用户名，即成员编号

 |
instance_id

 | 是

 | String

 | 实例 id，同 data_id

 |
task_id

 | 是

 | String

 | 任务 id（需要和 username 一一对应）

 |
flow_id

 | 否

 | Number

 | 回退目标节点：

节点配置为回退到指定节点时需要设置 flow_id，根据设置的节点进行回退；
节点配置为回退到上一节点时无需设置 flow_id，即使设置了flow_id  也不根据设置的节点回退。
 |
comment

 | 否

 | String

 | 审批意见

 |
back_type

 | 否

 | Number

 | 回退人选择

节点回退操作配置「回退人选择」时，执行回退需要带该参数：

1：正常流转
2：直达目标节点
 |

请求示例：

{
    "username": "xiaojian",
    "instance_id": "635919d1a2cca9000734511c",
    "task_id": "635919d1a2cca9000734513b",
    "comment": ""回退",
    "back_type": 1
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | String

 | success：表示接口调用成功

failure：表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | Number

 | 错误码

 |
message

 | String

 | 返回码的描述

 |
响应示例：

成功示例
{
    "status": "success"
}

失败示例
{
    "code": 1010,
    "message": "用户不存在",
    "status": "failure"
}


---

## 流程待办转交

- 官方文档：https://hc.jiandaoyun.com/open/16056

1. 简介

1.1 接口简介

该接口用来转交流程待办。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.10.28

 | 原始接口

 |
2. 接口调用

该接口用来转交流程待办。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/task/transfer

请求频率：20 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 用户名，即成员编号

注：此处用户名指的是当前节点的负责人，而非流程表单的创建者

 |
instance_id

 | 是

 | String

 | 实例 id，同 data_id

 |
task_id

 | 是

 | String

 | 任务 id（需要和 username 一一对应）

 |
transfer_username

 | 是

 | String

 | 转交用户

 |
comment

 | 否

 | String

 | 审批意见

 |

请求示例：

{
    "username":"xiaoyun",
    "instance_id": "6358af7c1f4eab0007704076",
    "task_id":"6358af8446f8db00072d6121",
    "transfer_username":"xiaojian"
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | String

 | success：表示接口调用成功

failure：表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | Number

 | 错误码

 |
message

 | String

 | 返回码的描述

 |

响应示例：

成功示例
{
    "status": "success"
}

失败示例
{
    "code": 1010,
    "message": "用户不存在",
    "status": "failure"
}


---

## 流程待办加签

- 官方文档：https://hc.jiandaoyun.com/open/17368

1. 简介

1.1 接口简介

流程待办加签是指，对当前流程的待办加签。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2023.08.01

 | 原始接口

 |
v2

 | 2026.06.12

 | 请求参数 add_sign_username 更新，如下：

参数更名为 add_sign_usernames；
参数类型更新为 string[]
 |
2. 接口调用

该接口用于对当前的流程待办加签。

请求地址：https://api.jiandaoyun.com/api/v2/workflow/task/add_sign

请求频率：20 次/s

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | string

 | 对应的流程实例

 |
task_id

 | 是

 | string

 | 待办实例 id

 |
username

 | 是

 | string

 | 待办对应的用户名

 |
comment

 | 否

 | String

 | （选填）审批意见

 |
add_sign_type

 | 是

 | number

 | 加签类型（0 前加签 / 1 后加签 / 2 并加签）

 |
add_sign_usernames

 | 是

 | string[]

 | 被加签人的用户名

 |
请求示例：

{
  "instance_id": "64c72a03561073000755afd8",
  "task_id": "64c72a03561073000755b001",
  "username": "jdy-90ahnts5a6rh",
  "comment": "Approval",
  "add_sign_type": 1,
  "add_sign_usernames": [
    "R-vmTE0o3N",
    "R-vmTE0o3P"
  ]
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | string

 | success 表示接口调用成功

failure 表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | number

 | 错误码（仅 failure 时返回）

 |
message

 | string

 | 返回码的描述（仅 failure 时返回）

 |
响应示例：

{
    "status": "success"
}


---

## 流程待办撤回

- 官方文档：https://hc.jiandaoyun.com/open/17367

1. 简介

1.1 接口简介

流程待办撤回接口用于将流程待办撤回。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2023.08.01

 | 原始接口

 |
v2

 | 2026.04.21

 | 新增请求参数：

撤回理由：comment
 |
2. 接口调用

该接口用于撤回流程待办。

请求地址：https://api.jiandaoyun.com/api/v2/workflow/task/revoke

请求频率：20 次/s

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | string

 | 对应的流程实例

 |
task_id

 | 否

 | string

 | 需要撤回的待办实例 id (是指之前进行提交操作过的待办 id，不是当前的待办实例 id，选填：不传默认进行发起节点的撤回操作)

 |
username

 | 是

 | string

 | 处理待办对应的用户名

 |
comment

 | 否

 | string

 | 撤回理由

当流程节点为「仅允许发起节点撤回」，且流程流转到不与发起节点相连的节点时，发起人在发起节点撤回流程时必填撤回理由。

 |
请求示例：

{
    "instance_id": "64c72910561073000755af52",
    "task_id": "64c72910561073000755af7c",
    "username": "jdy-90ahnts5a6rh",
    "comment": "因XXX需要撤回至发起节点"
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | string

 | success 表示接口调用成功

failure 表示接口调用失败（失败时会有错误码，错误码描述等信息）

 |
code

 | number

 | 错误码(仅 failure 时返回)

 |
message

 | string

 | 返回码的描述(仅 failure 时返回)

 |
响应示例：

{
    "status": "success"
}


---

## 流程待办否决

- 官方文档：https://hc.jiandaoyun.com/open/21608

1. 简介

1.1 接口简介

流程待办否决接口用于将流程待办否决。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
V1

 | 2024.12.26

 | 原始接口

 |
2. 接口调用

该接口用于否决流程待办。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/task/reject

请求频率：20 次/s

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
instance_id

 | 是

 | string

 | 对应的流程实例

 |
task_id

 | 是

 | string

 | 待办实例id

 |
username

 | 是

 | string

 | 待办对应的用户名

 |
comment

 | 否

 | String

 | 审批意见（选填）

 |
请求示例：

{
    "instance_id": "64c72a03561073000755afd8",
    "task_id": "64c72a03561073000755b001",
    "username": "jdy-90ahnts5a6rh",
    "comment": "不同意"
}

响应参数：

参数

 | 类型

 | 类型

 |
status

 | string

 | 请求结果状态

success：接口调用成功
failure：接口调用失败（失败时会有错误码，错误码描述等信息）
 |
code

 | number

 | 错误码

 |
message

 | string

 | 错误码描述信息

 |
响应示例：

{
    "status": "success"
}

错误响应示例：

{
    "status": "failure",
    "code": 5004,
    // 未提交流程审批意见
    "message": "No comment for approval."
}


---

## 查询抄送列表

- 官方文档：https://hc.jiandaoyun.com/open/22875

1. 简介

1.1 接口简介

该插件用于查询抄送列表，目前仅支持查询 90 天内的抄送数据。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
V1

 | 2025.07.22

 | 原始接口

 |
2. 接口调用

该插件用于查询抄送列表。

请求地址：https://api.jiandaoyun.com/api/v1/workflow/cc/list

请求频率：5 次/秒

请求方式：POST

请求参数:

参数

 | 必须

 | 类型

 | 说明

 |
username

 | 是

 | string

 | 用户名，即成员编号

 |
skip

 | 否

 | number

 | 分页参数，跳过前面数据条数

 默认 0

 |
limit

 | 否

 | number

 | 分页参数

页大小默认 10， 最大 100

 |
read_status

 | 否

 | string

 | 已读状态，

已读：“read”

未读：“unread”

全部：“all”（默认）

 |
请求示例：

{
    "username":"xiaoyun",
    "skip": 0,
    "limit": 1,
    "read_status": "all"
}

响应参数：

参数

 | 类型

 | 说明

 |
has_more

 | boolean

 | 后面是否还有数据

 |
cc_list

 | object[]

 | 抄送列表

注：仅支持查询 90 天内的抄送数据

 |
cc_list[].app_id

 | string

 | 应用 ID

 |
cc_list[].form_id

 | string

 | 表单 ID

 |
cc_list[].task_id

 | string

 | 抄送 ID

 |
cc_list[].instance_id

 | string

 | 实例 ID，同数据 ID

 |
cc_list[].form_title

 | string

 | 表单名称

 |
cc_list[].title

 | string

 | 提醒标题（节点名称）

 |
cc_list[].flow_id

 | number

 | 节点 ID

 |
cc_list[].flow_name

 | string

 | 节点名称

 |
cc_list[].url

 | string

 | 抄送访问链接

 |
cc_list[].assignee

 | object

 | 抄送人（同成员实体结构）

 |
cc_list[].creator

 | object

 | 流程发起人（同成员实体结构）

 |
cc_list[].create_time

 | Date

 | 流程发起时间

 |
cc_list[].status

 | number

 | 状态

0：未读
1：已读
 |
cc_list[].start_time

 | Date

 | 提醒创建时间

 |
cc_list[].start_action

 | string

 | 创建提醒的流程动作

 |
cc_list[].finish_time

 | Date

 | 标记已读时间，仅 status 为 1 时存在

 |

响应示例：

{
    "cc_list": [
        {
            "app_id": "67c1584ea70e38aa41a9b466",
            "form_id": "67c1649dfee1fc583c98be20",
            "task_id": "67c164a8fee1fc583c98be7f",
            "instance_id": "67c164a8fee1fc583c98be59",
            "form_title": "抄送全部已读",
            "title": "节点1",
            "flow_id": 1,
            "flow_name": "节点1",
            "url": "https://www.jiandaoyun.com/workflow/process_instance/67c164a8fee1fc583c98be59/task/67c164a8fee1fc583c98be7f",
            "assignee": {
                "username": "xiaoyun",
                "name": "小云",
                "departments": [
                    1,
                    3
                ],
                "type": 0,
                "status": 1,
                "integrate_id": "xiaoyun"
            },
            "creator": {
                "username": "xiaojian",
                "name": "小简",
                "departments": [
                    1,
                    3
                ],
                "type": 0,
                "status": 1,
                "integrate_id": "xiaojian"
            },
            "create_time": "2025-02-28T07:24:24.321Z",
            "status": 1,
            "start_time": "2025-02-28T07:24:24.323Z",
            "finish_time": "2025-02-28T07:24:27.608Z",
            "start_action": "forward"
        }
    ],
    "has_more": true
}
