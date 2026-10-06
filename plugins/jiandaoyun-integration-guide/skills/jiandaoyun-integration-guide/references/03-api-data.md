# 应用 / 表单 / 数据 / 文件接口

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 应用接口

- 官方文档：https://hc.jiandaoyun.com/open/12481

1. 简介

应用接口包括：

用户应用查询接口
用户表单查询接口
开发前，请仔细阅读 开发指南。

注：以下所有接口路径中的 app_id 和 entry_id 分别表示应用ID和该应用内的表单 ID，因此 app_id+entry_id 表示全局唯一的表单 ID，可以前往开放平台内的 API 文档进行查看。

2. 接口列表

应用接口主要包括以下接口：

接口名称

 | 释义

 |
用户应用查询接口

 | 仅获取 API Key 当中应用授权范围内的应用信息。

 |
用户表单查询接口

 | 获取当前应用下所有表单信息。

 |


---

## 用户应用查询接口

- 官方文档：https://hc.jiandaoyun.com/open/18538

1. 简介

1.1 接口简介

仅获取 API Key 当中应用授权范围内的应用信息。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.6.1

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口调用频率由 5 次/秒提升至 30 次/秒；

接口路由 POST app/retrieve_all 修改为 POST app/list

 |
2. 接口调用

仅获取 API Key 当中应用授权范围内的应用信息。

请求地址：https://api.jiandaoyun.com/api/v5/app/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
limit

 | Number

 | 否

 | 单次取数的数据条数，1~100，默认 100。

 |
skip

 | Number

 | 否

 | 需要跳过的数据条数，默认 0 。

 |
参数释义：

目的：想要查询数据库中第 500～599 的数据；
分析：查询的数据条数为 100 条；需要跳过的数据条数为 499；
参数：那么请求参数 skip 可以设置为：499；limit 设置为100

响应内容：

参数

 | 含义

 |
apps

 | 应用信息

 |
apps[].name

 | 应用名称

 |
apps[].app_id

 | 应用id

 |

响应示例：

{
    "apps": [
        {
            "name": "应用名称1",
            "app_id": "5d5a5bbb850a6d0604ab119"
        },
        {
            "name": "应用名称2",
            "app_id": "5d5a5c14850a6d0604ab11a4"
        }
    ]
}


---

## 用户表单查询接口

- 官方文档：https://hc.jiandaoyun.com/open/18539

1. 简介

1.1 接口简介

获取当前应用下所有表单信息。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.6.1

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口调用频率由 5 次/秒提升至 30 次/秒；

参数 app_id 放入 body，接口路由 POST app/{app_id}//entry_retrieve 修改为 POST app/entry/list。

 |
2. 接口调用

获取当前应用下所有表单信息。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID。

 |
limit

 | Number

 | 否

 | 单次取数的数据条数，1~100，默认 100。

 |
skip

 | Number

 | 否

 | 需要跳过的数据条数，默认 0 。

 |
{
          "app_id": "5e0dca0cc9a2790006c11e02"
 }

响应内容：

参数

 | 含义

 |
forms

 | 表单信息

 |
forms[].name

 | 表单名称

 |
forms[].app_id

 | 应用id

 |
forms[].entry_id

 | 表单id

 |

响应示例：

{
    "forms": [
        {
            "name": "表单名称1",
            "app_id": "5e0dca0cc9a2790006c11e02",
            "entry_id": "56fcab0f02c4675e3fe9694a"
        },
        {
            "name": "表单名称2",
            "app_id": "5e0dca0cc9a2790006c11e02",
            "entry_id": "5ed750af3c07c70f9c6eef78"
        }
    ]
}


---

## 表单接口

- 官方文档：https://hc.jiandaoyun.com/open/14216

1. 简介

1.1 接口简介

表单接口包括：

表单字段查询接口V1
表单字段查询接口V2
表单字段查询接口V5
开发前，请仔细阅读 开发指南。

以下所有接口路径中的 app_id 和 entry_id 分别表示应用 ID 和该应用内的表单 ID，因此 app_id+entry_id 表示全局唯一的表单 ID，可以前往开放平台内的 API 文档进行查看。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.6.1

 | 原始接口

 |
v2

 | 2021.10.26

 | V2 在 V1 的基础之上新增了系统字段及表单数据修改时间的获取。

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口调用频率由 5 次/秒提升至 30 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/widget/list。

 |

2. 接口调用

2.1 表单字段查询接口V5

获取指定表单的字段/字段信息，除分割线字段和查询字段以外。具体可以查阅文档最后的 字段与数据类型对照表。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/widget/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID

 |
entry_id

 | String

 | 是

 | 表单ID

 |
{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd"
}

注：响应参数同「表单字段查询接口v2 」，此处不在赘述。

2.2 表单字段查询接口V2

获取指定表单的字段/字段信息，除分割线字段和查询字段以外。具体可以查阅文档最后的 字段与数据类型对照表。

请求地址：https://api.jiandaoyun.com/api/v2/app/{app_id}/entry/{entry_id}/widgets

请求频率：5 次/秒

请求方式：POST

请求参数：

无

响应内容：

只要每一个表单字段不删除，字段 ID 就不会变化：

参数

 | 含义

 |
widgets

 | 字段信息

 |
widgets[].label

 | 字段标题

 |
widgets[].name

 | 字段名（设置了字段别名则采用别名，未设置则采用字段ID）

 |
widgets[].widgetName

 | 字段 ID

 |
widgets[].type

 | 字段类型；每种字段类型都有对应的数据类型

 |
widgets[].items

 | 仅子表单控件有；数组里包含了每个子字段的信息

 |
sysWidgets

 | 系统字段列表（扩展字段、流程字段受功能开关影响，微信增强一旦开启会始终返回）

 |
sysWidgets[].name

 | 系统字段名称

 |
dataModifyTime

 | 表单内数据最新修改时间（可用于判断表单内的数据是否发生变更）

 |

响应示例：

{
    "widgets": [
        {
            "name": "_widget_1529400746031",
            "widgetName": "_widget_1529400746031",
            "label": "单行文本",
            "type": "text"
        },
        {
            "name": "_widget_1529400746045",
            "widgetName": "_widget_1529400746045",
            "label": "多行文本",
            "type": "textarea"
        },
        {
            "name": "_widget_1529400746056",
            "widgetName": "_widget_1529400746056",
            "label": "数字",
            "type": "number"
        },
        {
            "name": "_widget_1529400746068",
            "widgetName": "_widget_1529400746068",
            "label": "日期",
            "type": "datetime"
        },
        {
            "name": "_widget_1529400746079",
            "widgetName": "_widget_1529400746079",
            "label": "日期时间",
            "type": "datetime"
        },
        {
            "name": "_widget_1529400746090",
            "widgetName": "_widget_1529400746090",
            "label": "单选按钮组",
            "type": "radiogroup"
        },
        {
            "name": "_widget_1529400746105",
            "widgetName": "_widget_1529400746105",
            "label": "复选框组",
            "type": "checkboxgroup"
        },
        {
            "name": "_widget_1529400746119",
            "widgetName": "_widget_1529400746119",
            "label": "下拉框",
            "type": "combo"
        },
        {
            "name": "_widget_1529400746136",
            "widgetName": "_widget_1529400746136",
            "label": "下拉复选框",
            "type": "combocheck"
        },
        {
            "name": "_widget_1529400746157",
            "widgetName": "_widget_1529400746157",
            "label": "地址",
            "type": "address"
        },
        {
            "name": "_widget_1529400746173",
            "widgetName": "_widget_1529400746173",
            "label": "定位",
            "type": "location"
        },
        {
            "name": "_widget_1529400746191",
            "widgetName": "_widget_1529400746191",
            "label": "图片",
            "type": "image"
        },
        {
            "name": "_widget_1529400746209",
            "widgetName": "_widget_1529400746209",
            "label": "附件",
            "type": "upload"
        },
        {
            "name": "_widget_1529400746221",
            "widgetName": "_widget_1529400746221",
            "label": "子表单",
            "type": "subform",
            "items": [
                // 同主表
            ]
        },
        {
            "name": "_widget_1529400746242",
            "widgetName": "_widget_1529400746242",
            "label": "选择数据",
            "type": "linkdata"
        },
        {
            "name": "_widget_1529400746242",
            "widgetName": "_widget_1529400746242",
            "label": "关联数据",
            "type": "lookup"
        },
        {
            "name": "_widget_1529400746254",
            "widgetName": "_widget_1529400746254",
            "label": "手写签名",
            "type": "signature"
        },
        {
            "name": "_widget_1529400746696",
            "widgetName": "_widget_1529400746696",
            "label": "成员单选",
            "type": "user"
        },
        {
            "name": "_widget_1529400746713",
            "widgetName": "_widget_1529400746713",
            "label": "成员多选",
            "type": "usergroup"
        },
        {
            "name": "_widget_1529400746729",
            "widgetName": "_widget_1529400746729",
            "label": "部门单选",
            "type": "dept"
        },
        {
            "name": "_widget_1529400746746",
            "widgetName": "_widget_1529400746746",
            "label": "部门多选",
            "type": "deptgroup"
        }
    ],
    "sysWidgets": [
        {
            "name": "flowState"
        },
        {
            "name": "wx_open_id"
        },
        {
            "name": "wx_nickname"
        },
        {
            "name": "wx_gender"
        },
        {
            "name": "creator"
        },
        {
            "name": "updater"
        },
        {
            "name": "deleter"
        },
        {
            "name": "ext"
        },
        {
            "name": "createTime"
        },
        {
            "name": "updateTime"
        },
        {
            "name": "deleteTime"
        }
    ],
    "dataModifyTime": "2021-09-08T03:40:26.586Z"
}

2.3 表单字段查询接口V1

获取指定表单的字段/字段信息，除分割线字段和查询字段以外。具体可以查阅文档中 字段与数据类型对照表。

请求地址：https://api.jiandaoyun.com/api/v1/app/{app_id}/entry/{entry_id}/widgets

请求频率：5 次/秒

请求方式：POST

请求参数：

无

响应内容：

参数

 | 含义

 |
widgets

 | 字段信息

 |
widgets[].label

 | 字段标题

 |
widgets[].name

 | 字段名（设置了字段别名则采用别名，未设置则采用字段 ID）

 |
widgets[].widgetName

 | 字段 ID

 |
widgets[].type

 | 字段类型；每种字段类型都有对应的数据类型

 |
widgets[].items

 | 仅子表单字段有；数组里包含了每个子字段的信息

 |

响应示例：

{
    "widgets": [
        {
            "name": "_widget_1529400746031",
            "widgetName": "_widget_1529400746031",
            "label": "单行文本",
            "type": "text"
        },
        {
            "name": "_widget_1529400746045",
            "widgetName": "_widget_1529400746045",
            "label": "多行文本",
            "type": "textarea"
        },
        {
            "name": "_widget_1529400746056",
            "widgetName": "_widget_1529400746056",
            "label": "数字",
            "type": "number"
        },
        {
            "name": "_widget_1529400746068",
            "widgetName": "_widget_1529400746068",
            "label": "日期",
            "type": "datetime"
        },
        {
            "name": "_widget_1529400746221",
            "widgetName": "_widget_1529400746221",
            "label": "子表单",
            "type": "subform",
            "items": [
                {
                    "name": "_widget_1529400746259",
                    "widgetName": "_widget_1529400746259",
                    "label": "手写签名",
                    "type": "signature"
                 },{
                    "name": "_widget_1529400746077",
                    "widgetName": "_widget_1529400746077",
                    "label": "日期",
                    "type": "datetime"
                }
            ]
        }
    ]
}


---

## 数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14217

1. 简介

数据接口也叫数据API，通过数据接口，可以实现数据的增、删、改、查等操作。

2. 接口类型

数据接口目前包括以下 7 个接口：

序号

 | 接口名称

 | 接口描述

 |
1

 | 查询单条数据接口

 | 按照指定数据 ID 获取表单中的数据。

 |
2

 | 查询多条数据接口

 | 该接口的返回数据，始终按照数据 ID 正序排列。

 |
3

 | 新建单条数据接口

 | 在指定表单中添加一条数据。

 |
4

 | 新建多条数据接口

 | 批量添加数据，一次最多支持添加 100 条数据。

 |
5

 | 修改单条数据接口

 | 按照指定数据 ID 修改表单中的数据。

 |
6

 | 修改多条数据接口

 | 批量修改表单中的数据，一次最多支持修改 100 条数据。

 |
7

 | 删除单条数据接口

 | 按照指定数据 ID 从表单中删除数据。

 |
8

 | 删除多条数据接口

 | 批量删除表单中的数据，一次最多支持删除 100 条数据。

 |


---

## 查询单条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14221

1. 简介

1.1 接口简介

通过查询单条数据接口，可以查询表单中的指定数据。

1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.6.21

 | 原始接口

 |
v2

 | 2021.3.11

 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID（以下简称数据 ID）

 |
v3

 | -

 | 无 v3 版本

 |
v4

 | 2022.4.21

 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：

0：内部
2：外部
 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/get。

 |
2. 接口调用

按照指定数据 ID 获取表单中的数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/get

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID

 |
entry_id

 | String

 | 是

 | 表单ID

 |
data_id

 | String

 | 是

 | 数据 ID

 |

请求示例：

{
   "app_id": "59264073a2a60c0c08e20bfb",
   "entry_id": "59264073a2a60c0c08e20bfd",
   "data_id": "59e9a2fe283ffa7c11b1ddbf"
}

响应内容：

参数

 | 类型

 | 说明

 |
data

 | JSON

 | 单条数据

 |

响应示例：

{
    "data": {
        "_id": "59e9a2fe283ffa7c11b1ddbf",
        "appId": "59264073a2a60c0c08e20bfb",
        "entryId": "59264073a2a60c0c08e20bfd",
        "creator": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "updater": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "createTime": "2017-10-20T22:41:51.430Z", // 创建时间
        "updateTime": "2017-10-20T11:12:15.293Z", // 修改时间
        "_widget_1725969783950": "67221b4fac0a62ac8f43a1c2",//关联数据
        "_widget_1432728651402": "简道云",  // 单行文本
        "_widget_1432728651403": 100, // 数字
        "_widget_1432728651404": "简道云是一个强大易用的应用搭建工具，可以快速把你的想法变成应用", // 多行文本
        "_widget_1432728651405": "选项一", // 单选按钮组、下拉框
        "_widget_1432728651406": [ // 复选框组、下拉复选框
            "选项一",
            "选项二",
            "选项三"
        ],
        "_widget_1432728651407": "2018-01-01T10:10:10.000Z", // 日期时间
        "_widget_1432728651408": {
            "id": "5b28effa49b561455dfda91e"
        },// 选择数据
        "_widget_1432728651409": [ // 图片
            {
                "name": "image.jpg",
                "size": 262144,
                "mime": "image/jpeg",
                "url": "https://files.jiandaoyun.com/lepxaifzcapghupffcaswikmhnyp"
            }
        ],
        "_widget_1432728651410": [ // 附件
            {
                "name": "产品说明文档.pdf",
                "size": 524288,
                "mime": "application/pdf",
                "url": "https://files.jiandaoyun.com/bogrebbkdbkfsbuldnjujoenclle"
            }
        ],
        "_widget_1432728651411": { // 手写签名
            "name": "image.png",
            "size": 262144,
            "mime": "image/png",
            "url": "https://files.jiandaoyun.com/sxbikbrchwlylrgqwyfkjbjmuncp"
        },
        "_widget_1432728651412": { // 地址
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地"
        },
        "_widget_1432728651413": { // 定位
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地",
            "lnglatXY": [
                120.31237,
                31.49099
            ]
        },
        "_widget_1652345009097": { // 手机字段
            "verified": false,
            "phone": "15852540044"
        },
        "_widget_1432728651414": { // 成员单选
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "_widget_1432728651415": [ // 成员多选
            {
                "name": "小简",
                "username": "xiaojian",
                "status": 1,
                "type": 0,
                "departments": [1, 3],
                "integrate_id": "xiaojian"
            }
        ],
        "_widget_1432728651416": {  // 部门单选
            "name": "经理部",
            "dept_no": 1,
            "type": 0,
            "parent_no": 2,
            "status": 1,
            "integrate_id": 1
        },
        "_widget_1432728651417": [ // 部门多选
            {
                "name": "经理部",
                "dept_no": 1,
                "type": 0,
                "parent_no": 2,
                "status": 1,
                "integrate_id": 1
            }
        ],
        "_widget_1432728651408": [ // 子表单
            {
                // ... 同前面
            }
        ],
        "_widget_1432728651528": {
    		"html": "<p>Hello, world!<img src=\"https://files.xxxxxx.com/xxx\" /></p>",
    		"attachments": [
        		{
            		"name": "image1.png",
           			"size": 262144,
            		"mime": "image/png",
            		"url": "https://files.xxxxx.com/xxx"
        		}
    		]
		},
        "wx_open_id": "wx98fb14481b3ab5a3",
        "wx_nickname": "jiandaoyun",
        "wx_gender": "男"
    }
}


---

## 查询多条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14220

1. 简介

1.1 接口简介

通过查询多条数据接口，可以一次查询表单中的多条数据。

1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.6.21

 | 原始接口

 |
v2

 | 2021.3.11

 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID（以下简称数据 ID）

 |
v3

 | -

 | 无 v3 版本

 |
v4

 | 2022.4.21

 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：

0：内部
2：外部
 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/list。

 |

2. 接口调用

该接口的返回数据，始终按照数据 ID 正序排列。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/list

请求频率：30  次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID

 |
entry_id

 | String

 | 是

 | 表单ID

 |
data_id

 | String

 | 否

 | 分页符，上一次查询数据结果的最后一条数据的 ID，没有则留空

 |
fields

 | Array

 | 否

 | 需要查询的数据字段

 |
filter

 | JSON

 | 否

 | 数据筛选器

 |
limit

 | Number

 | 否

 | 查询的数据条数，1~100，默认10

 |
数据筛选器

查询多条数据接口同时也支持过滤，可通过 filter 参数进行数据过滤。

筛选结构：

参数

 | 必需

 | 类型

 | 说明

 |
rel

 | 是

 | String

 | 筛选组合关系；“and”(满足所有过滤条件), “or”(满足任一过滤条件)

 |
cond

 | 是

 | [JSON]

 | 过滤条件列表

 |

筛选示例：

{
    "rel": "and", // 或者 "or"
    "cond": [
        // 过滤条件
    ]
}

过滤条件结构：

参数

 | 必需

 | 类型

 | 说明

 |
field

 | 是

 | String

 | 字段名

 |
type

 | 否

 | String

 | 字段类型

 |
method

 | 是

 | String

 | 过滤方法：

not_empty：不为空
empty：为空
eq：等于
ne：不等于
in：等于任意一个，最多可传递 1000 个
range：在 x 与 y 之间，并且包含 x 和 y 本身
nin：不等于任意一个，最多可传递 1000 个
like：包含
verified：表示填写了手机号且已验证的值
unverified：表示填写了手机号但未验证值
all：同时包含，最多可传递 1000 个
gt：大于
lt：小于
注：当成员字段使用的过滤方法为 nin（不等于任意一个）时，若查询的 username 不存在，则整个 nin 过滤条件将失效。

 |
value

 | 否

 | Array

 | 过滤值

 |

过滤条件示例：

// 没有参数的过滤条件
{
    "field": "_widget_1508400000001",
    "type": "text",
    "method": "empty"
}
// 有参数的过滤条件
{
    "field": "flowState",
    "type": "flowstate",
    "method": "eq",
    "value": [1]
}

目前支持如下字段：

字段类型

 | 支持的过滤方式

 | 说明

 |
flowState

 | eq，ne，in，nin，empty，not_empty

 | 流程状态，仅对流程表单有效

 |
data_id

 | eq， in， empty， not_empty

 | 数据 id 字段，是数据唯一性的标识

 |
提交人

 | eq， ne， in， nin，empty，not_empty

 | ——

 |
日期时间

 | eq，ne，range，empty，not_empty

 | 包含日期时间字段和提交时间字段

 |
数字

 | eq，ne，range，empty，not_empty，gt，lt

 | ——

 |
文本

 | eq，ne，in，nin，empty，not_empty

 | 包括单行文本、下拉框、单选按钮组

 |
复选框组/下拉复选框

 | in，all，empty，not_empty

 | ——

 |
手机

 | like, verified, unverified, empty, not_empty

 | verified表示填写了手机号且已验证的值；unverified表示填写了手机号但未验证值

 |
成员单选/部门单选

 | eq，ne，in，nin，empty，not_empty

 | 支持筛选内部组织成员、外部组织对接人、内部组织部门、外部组织互联企业

 |
成员多选/部门多选

 | in，all，empty，not_empty

 |
流水号

 | en，ne，in，nin，like，empty，not_empty

 | ——

 |
关联数据

 | eq，ne，in，nin，empty，not_empty

 |
其他表单字段

（不支持子表单字段）

 | empty，not_empty

 |

请求示例：

 {
    "app_id": "59264073a2a60c0c08e20bfb",
     "entry_id": "59264073a2a60c0c08e20bfd",
   "data_id": "59e9a2fe283ffa7c11b1ddbf", //此处 data_id 用于分页
    "limit": 100,
    "fields": ["_widget_1508400000001", "_widget_1508400000002", "_widget_1508400000003"],
    "filter": {
        "rel": "and", // 或者 "or"
        "cond": [
          {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"eq",//过滤方式为 eq
                "value":[0]
            } ,
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"ne",//过滤方式为 ne
                "value":[0]
            } ,
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"in",//过滤方式为 in
                "value":[0,1]
            } ,
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"nin",//过滤方式为 nin
                "value":[0,1]
             } ,
            {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"empty",//过滤方式为 empty
             } ,
            {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"not_empty",//过滤方式为 not_empty
             } ,
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "range",//过滤方式为 range
                "value":["2024-11-20","2024-11-21"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "eq",//过滤方式为 eq
                "value":["2024-11-30"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "ne",//过滤方式为 ne
                "value":["2024-11-30"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "empty",//过滤方式为 empty
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "eq",//过滤方式为 eq
                "value":[1]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "ne",//过滤方式为 ne
                "value":[1]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "range",//过滤方式为 range
                "value":[100,200]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "empty",//过滤方式为 empty
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387201",
                "type": "number", //字段类型为 number
                "method": "gt", //过滤方式为 gt
                "value": [1000]
        	 },
            {
              "field": "_widget_1732071387202",
              "type": "number", //字段类型为 number
              "method": "lt", //过滤方式为 lt
              "value": [1000]
             },
            {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "eq",//过滤方式为 eq
                "value":["111"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "ne",//过滤方式为 ne
                "value":["111"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "in",//过滤方式为 in
                "value":["111","2222"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "nin",//过滤方式为 nin
                "value":["111","2222"]
             },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "empty",//过滤方式为 empty
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387219",
                "type": "text", //字段类型为流水号
                "method": "like", //过滤方式为 like
                "value": ["SN2024"]
             },
            {
                "field": "_widget_1732071387203",
                "type": "combocheck", //字段类型为 combocheck
                "method": "in", //过滤方式为 in
                "value": ["选项1", "选项2", "选项3"]
              },
             {
                "field": "_widget_1732071387204",
                "type": "combocheck", //字段类型为 combocheck
                "method": "all", //过滤方式为 all
                "value": ["选项A", "选项B"]
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "like",//过滤方式为 like
                "value":["188"]
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "verified",//过滤方式为 verified
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "unverified",//过滤方式为 unverified
             },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "empty",//过滤方式为 empty
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "not_empty",//过滤方式为 not_empty
              },
             {
                "field": "_widget_1732071387206",
                "type": "user",//字段类型为 user
                "method": "empty"//过滤方式为 empty
              },
             {
                "field": "_widget_1732071387206",
                "type": "user",//字段类型为 user
                "method": "not_empty"//过滤方式为 not_empty
             },
          	{
                "field": "_widget_1732071387207",
                "type": "user", //字段类型为 user
                "method": "eq", //过滤方式为 eq
                "value": ["R-3XcOLjhg"] //成员编号
              },
             {
                "field": "_widget_1732071387208",
                "type": "user", //字段类型为 user
                "method": "ne", //过滤方式为 ne
                "value": ["R-3XcOLjhg"] //成员编号
              },
             {
                "field": "_widget_1732071387209",
                "type": "user", //字段类型为 user
                "method": "in", //过滤方式为 in
                "value": ["R-3XcOLjhg", "R-3XcOLpho"] //成员编号
              },
             {
                "field": "_widget_1732071387210",
                "type": "user", //字段类型为 user
                "method": "nin", //过滤方式为 nin
                "value": ["R-3XcOLjhg", "R-3XcOLpho"] //成员编号
              },
          	 {
                "field": "_widget_1732071387211",
                "type": "usergroup", //字段类型为 usergroup
                "method": "in", //过滤方式为 in
                "value": ["R-3XcOLpho", "R-3XcOLjhg"] //成员编号
              },
             {
                "field": "_widget_1732071387212",
                "type": "usergroup", //字段类型为 usergroup
                "method": "all", //过滤方式为 all
                "value": ["R-3XcOLjhg", "R-3XcOLhpo"] //成员编号
              },
             {
                "field": "_widget_1732071387213",
                "type": "dept", //字段类型为 dept
                "method": "eq", //过滤方式为 eq
                "value": [1] //部门编号
              },
             {
                "field": "_widget_1732071387214",
                "type": "dept", //字段类型为 dept
                "method": "ne", //过滤方式为 ne
                "value": [1] //部门编号
              },
             {
                "field": "_widget_1732071387215",
                "type": "dept", //字段类型为 dept
                "method": "in", //过滤方式为 in
                "value": [1, 2] //部门编号
              },
             {
                "field": "_widget_1732071387216",
                "type": "dept", //字段类型为 dept
                "method": "nin", //过滤方式为 nin
                "value": [1, 2] //部门编号
              },
             {
                "field": "_widget_1732071387217",
                "type": "deptgroup", //字段类型为 deptgroup
                "method": "in", //过滤方式为 in
                "value": [1, 3] //部门编号
              },
             {
                "field": "_widget_1732071387218",
                "type": "deptgroup", //字段类型为 deptgroup
                "method": "all", //过滤方式为 all
                "value": [3, 4] //部门编号
              },
            {
                "field": "_widget_1732071387220",
                "type": "lookup", //字段类型为 lookup
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439031"]
              },
            {
                "field": "_widget_1732071387221",
                "type": "lookup", //字段类型为 lookup
                "method": "ne", //过滤方式为 ne
                "value": ["507f1f77bcf86cd799439032"]
              },
            {
                "field": "_widget_1732071387222",
                "type": "lookup", //字段类型为 lookup
                "method": "in", //过滤方式为 in
                "value": ["507f1f77bcf86cd799439033", "507f1f77bcf86cd799439034"]
              },
             {
                "field": "_widget_1732071387223",
                "type": "lookup", //字段类型为 lookup
                "method": "nin", //过滤方式为 nin
                "value": ["507f1f77bcf86cd799439035", "507f1f77bcf86cd799439036"]
              },
             {
                "field": "_widget_1732071387224",
                "type": "lookup", //字段类型为 lookup
                "method": "empty", //过滤方式为 empty
              },
             {
                "field": "_widget_1732071387225",
                "type": "lookup", //字段类型为 lookup
                "method": "not_empty", //过滤方式为 not_empty
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid",//字段类型为 dataid
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439037"]
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid", //字段类型为 dataid
                "method": "in", //过滤方式为 in
                "value": ["507f1f77bcf86cd799439038", "507f1f77bcf86cd799439039", "507f1f77bcf86cd799439040"]
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid", //字段类型为 dataid
                "method": "empty", //过滤方式为 empty
              },
             {
                "field": "data_id",
                "type": "dataid", //字段类型为 dataid
                "method": "not_empty",//过滤方式为 not_empty
              },
             {
                "field": "creator", //此处的 data_id 用筛选
                "type": "user", //字段类型为 user
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439041"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "ne", //过滤方式为 ne
                "value": ["507f1f77bcf86cd799439042"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "in", //过滤方式为 in
                "value": ["R-3XcOLpho", "R-3XcOLjhg"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "nin", //过滤方式为 nin
                "value": ["R-3XcOLpho", "R-3XcOLjgh"]
              }
        ]
    }
}

响应参数：

参数

 | 类型

 | 说明

 |
data

 | Array

 | 多条数据的集合

 |

响应数据样例：

{
    "data": [{
            "_id": "59e9a2fe283ffa7c11b1ddbe",
            "appId": "59264073a2a60c0c08e20bfb",
            "entryId": "59264073a2a60c0c08e20bfd",
            "creator": {
                "name": "小简",
                "username": "xiaojian",
                "status": 1,
                "type": 0,
                "departments": [1, 3],
                "integrate_id": "xiaojian"
            },
            "createTime": "2017-10-20T22:41:51.430Z",
            "updateTime": "2017-10-20T11:12:15.293Z",
   			"_widget_1741589364098": {
        			"id": "67ce8c18705dfcd1eef5c070"
      		},//选择数据字段
            "_widget_1432728651402": "A班",
            "_widget_1615777739673": [{
                    "_id": "604ed0298e2ade077c7245f1",
                    "_widget_1615777739744": "子表单数据1"
                },
                {
                    "_id": "604ed0298e2ade077c7245f2",
                    "_widget_1615777739744": "子表单数据2"
                }
            ]
        },
        {
            "_id": "59e9a2fe283ffa7c11b1ddbf",
            "appId": "59264073a2a60c0c08e20bfb",
            "entryId": "59264073a2a60c0c08e20bfd",
            "creator": {
                "name": "小简",
                "username": "xiaojian",
                "status": 1,
                "type": 0,
                "departments": [1, 3],
               "integrate_id": "xiaojian"
            },
            "createTime": "2017-10-20T22:41:51.430Z",
            "updateTime": "2017-10-20T11:12:15.293Z",
            "_widget_1725969783950": "67221b4fac0a62ac8f43a1c2",//关联数据字段
            "_widget_1741589364098": {
        			"id": "67ce8c18705dfcd1eef5c070"
      		},//选择数据字段
            "_widget_1432728651402": "B班",
            "_widget_1615777739673": [{
                    "_id": "604ed0298e2ade077c7245f3",
                    "_widget_1615777739744": "子表单数据1"
                },
                {
                    "_id": "604ed0298e2ade077c7245f4",
                    "_widget_1615777739744": "子表单数据2"
                }
            ]
        }
    ]
}

3. 注意事项

若要设置循环调取数据，可以利用 data_id 字段来设置参数避免调取重复数据。

如需要查询 230 条数据：

第一次查询时可以不传 data_id 字段，若设置 limit 为 100 ，则第一次返回了前 100 条数据；
第二次，用第 100 条数据的 data_id 进行查询，若设置 limit 为100，则第二次返回 101～200 这 100 条数据；
第三次，用第 200 条数据的 data_id 进行查询，若设置 limit 为100，则第三次返回 201～230 这 30 条数据。
由于第三次返回结果只有 30 条，未达到设置的 limit 上限100，则说明查询结束。


---

## 新建单条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14222

1. 简介

1.1 接口简介

通过新建单条数据接口，可以向指定的表单中添加单条数据。

注：使用 API 添加数据时，会触发的事件有新数据提交提醒、聚合表计算&校验、数据操作日志、数据量统计。也可以通过请求参数来控制是否发起流程。但是不会触发重复值校验、必填校验。

另外，系统字段 和以下所列举的字段不支持添加和修改数据：

分割线
手写签名
选择数据、查询
流水号（提交后系统生成）
1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.6.21

 | 部门和成员均使用_id为主键

 |
v2

 | 2019.6.21

 | 在 v1 的基础上，成员字段使用 username 为主键，部门字段使用 dept_no 为主键

 |
v3

 | 2021.3.31

 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID

 |
v4

 | 2022.4.21

 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：

0：内部
2：外部
 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/create。

 |
2023.08.31

 | 新增请求参数，数据提交人：data_creator

 |
2. 接口调用

在指定表单中添加一条数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/create

请求频率：20  次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 | 默认

 |
app_id

 | String

 | 是

 | 应用ID

 |

 |
entry_id

 | String

 | 是

 | 表单ID

 |

 |
data

 | JSON

 | 是

 | 数据内容

 |

 |
data_creator

 | String

 | 否

 | 数据提交人（取成员编号 username，可从通讯录接口获取）

注：不能使用外链人员的 username

 | 企业创建者

 |
is_start_workflow

 | Bool

 | 否

 | 是否发起流程（仅流程表单有效）

 | false

 |
is_start_trigger

 | Bool

 | 否

 | 是否触发智能助手

 | false

 |
transaction_id

 | String

 | 否

 | 事务ID；transaction_id 用于绑定一批上传的文件，若数据中包含附件或图片控件，则 transaction_id 必须与“获取文件上传凭证和上传地址接口”中的 transaction_id 参数相同。

 |

 |

请求示例：

{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_creator":"Yonne",      //数据提交人
     "data": {
        "_widget_1432728651402": { // 单行文本
            "value": "简道云"
        },
          "_widget_1725969783950": {
      		"value": "67221b4fac0a62ac8f43a1c3"//关联数据字段ID
    	},
        "_widget_1432728651403": { // 数字
            "value": 100
        },
        "_widget_1432728651404": { // 多行文本
            "value": "简道云是一个强大易用的应用搭建工具，\n可以快速把你的想法变成应用"
        },
        "_widget_1432728651405": { // 单选按钮组、下拉框
            "value": "选项一"
        },
        "_widget_1432728651406": { // 复选框组、下拉复选框
            "value": [
                "选项一","选项二","选项三"
            ]
        },
        "_widget_1432728651407": { // 日期时间
            "value": "2018-01-01T10:10:10.000Z"
        },
        "_widget_1432728651412": {  // 地址
            "value": {
                "province": "江苏省",
                "city": "无锡市",
                "district": "梁溪区",
                "detail": "清扬路138号茂业天地"
            }
        },
        "_widget_1432728651413": { // 定位
            "value": {
                "province": "江苏省",
                "city": "无锡市",
                "district": "梁溪区",
                "detail": "清扬路138号茂业天地",
                "lnglatXY": [
                    120.31237,
                    31.49099
                ]
            }
        },
        "_widget_1528854613291": { // 子表单
            "value": [
                { // 子表单子记录结构跟主表一致
                    "_widget_1528854614409": {
                        "value": "子表单数据1"
                    },
                    "_widget_1528854615499": {
                        "value": 1001
                    }
                },
                {
                    "_widget_1528854614410": {
                        "value": "子表单数据2"
                    },
                    "_widget_1528854615419": {
                        "value": 1002
                    }
                }
            ]
        },
        "_widget_1652345009097": { //手机字段
            "value": {
                "phone": "15852540044"
            }
        },
        "_widget_1652345009126": { //成员单选（成员的username）
            "value": "jian"
        },
        "_widget_1652345009143": { //成员多选（成员的username数组）
            "value": [
                "jian",
                "dao"
            ]
        },
        "_widget_1652345009157": { //部门单选（部门的dept_no）
            "value": 12
        },
        "_widget_1652345009174": { //部门多选（部门的dept_no数组）
            "value": [
                12,
                13
            ]
        },
        "_widget_1432728651408": { // 附件（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-8fa8fdeae2ef","6b559cf1-b16c-43bd-a211-646ab85da8cb"]
        },
        "_widget_1432728652567": { // 图片（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-74389cd8ae76","6b559cf1-b16c-43bd-a211-564e56a65bd6"]
        },
        "_widget_1432728651408": { // 附件（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-8fa8fdeae2ef","6b559cf1-b16c-43bd-a211-646ab85da8cb"]
        },
        "_widget_1432728652567": { // 图片（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-74389cd8ae76","6b559cf1-b16c-43bd-a211-564e56a65bd6"]
        },
        "_widget_1432728651528": { // 富文本（img标签中的data-key是文件key）
    		"value": "<p>Hello, world!<img data-key=\"6b559cf1-b16c-43bd-a211-74389cd8ae76\" width=\"100\" height=\"100\" /></p>"
		}
    }
}

响应内容：

参数

 | 类型

 | 说明

 |
data

 | JSON

 | 返回提交后的完整数据，内容同查询单条数据接口

 |

响应示例：

{
    "data": {
        "_id": "59e9a2fe283ffa7c11b1ddbf",
        "appId": "59264073a2a60c0c08e20bfb",
        "entryId": "59264073a2a60c0c08e20bfd",
        "creator": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "updater": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "createTime": "2017-10-20T22:41:51.430Z", // 创建时间
        "updateTime": "2017-10-20T11:12:15.293Z", // 修改时间
        "_widget_1432728651402": "简道云",  // 单行文本
        "_widget_1725969783950": "67221b4fac0a62ac8f43a1c3",//关联数据
        "_widget_1432728651403": 100, // 数字
        "_widget_1432728651404": "简道云是一个强大易用的应用搭建工具，可以快速把你的想法变成应用", // 多行文本
        "_widget_1432728651405": "选项一", // 单选按钮组、下拉框
        "_widget_1432728651406": [ // 复选框组、下拉复选框
            "选项一、选项二、选项三"
        ],
        "_widget_1432728651407": "2018-01-01T10:10:10.000Z", // 日期时间
        "_widget_1432728651409": [ // 图片
            {
                "name": "image.jpg",
                "size": 262144,
                "mime": "image/jpeg",
                "url": "https://files.jiandaoyun.com/lepxaifzcapghupffcaswikmhnyp"
            }
        ],
        "_widget_1432728651410": [ // 附件
            {
                "name": "产品说明文档.pdf",
                "size": 524288,
                "mime": "application/pdf",
                "url": "https://files.jiandaoyun.com/bogrebbkdbkfsbuldnjujoenclle"
            }
        ],
        "_widget_1432728651411": { // 手写签名
            "name": "image.png",
            "size": 262144,
            "mime": "image/png",
            "url": "https://files.jiandaoyun.com/sxbikbrchwlylrgqwyfkjbjmuncp"
        },
        "_widget_1432728651412": { // 地址
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地"
        },
        "_widget_1432728651413": { // 定位
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地",
            "lnglatXY": [
                120.31237,
                31.49099
            ]
        },
        "_widget_1652345009097": { // 手机字段
            "verified": false,
            "phone": "15852540044"
        },
        "_widget_1432728651414": { // 成员单选
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "_widget_1432728651415": [ // 成员多选
            {
                "name": "小简",
                "username": "xiaojian",
                "status": 1,
                "type": 0,
                "departments": [1, 3],
                "integrate_id": "xiaojian"
            }
        ],
        "_widget_1432728651416": {  // 部门单选
            "name": "经理部",
            "dept_no": 1,
            "type": 0,
            "parent_no": 2,
            "status": 1,
            "integrate_id": 1
        },
        "_widget_1432728651417": [ // 部门多选
            {
                "name": "经理部",
                "dept_no": 1,
                "type": 0,
                "parent_no": 2,
                "status": 1,
                "integrate_id": 1
            }
        ],
        "_widget_1432728651408": [ // 子表单
            {
                // ... 同前面
            }
        ],
        "_widget_1432728651528": {
    		"html": "<p>Hello, world!<img src=\"https://files.xxxxxx.com/xxx\" /></p>",
    		"attachments": [
        		{
            		"name": "image1.png",
            		"size": 262144,
            		"mime": "image/png",
            		"url": "https://files.xxxxx.com/xxx"
        		}
    		]
		},
        "wx_open_id": "wx98fb14481b3ab5a3",
        "wx_nickname": "jiandaoyun",
        "wx_gender": "男"
    }
}

3. 注意事项

如果请求中指定了 data_creator，则关联触发的以下成员也会被记录为 data_creator，如下所示：

智能助手执行人
流程发起人
CRM 相关关联修改
由跟进记录关联修改的客户表、线索表和商机表的修改人
由商机表关联修改的客户表的修改人


---

## 新建多条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14223

1. 简介

1.1 接口简介

通过新建多条数据接口，可以向指定的表单中添加多条数据。

注：使用 API 添加数据时，会触发的事件有新数据提交提醒、聚合表计算&校验、数据操作日志、数据量统计。也可以通过请求参数来控制是否发起流程。但是不会触发重复值校验、必填校验。

另外，系统字段 和以下所列举的字段不支持添加和修改数据：

分割线
手写签名
选择数据、查询
流水号（提交后系统生成）
1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.12.30

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/batch_create。

 |
2023.08.31

 | 新增请求参数

数据提交人：data_creator
 |
2. 接口调用

创建多条数据接口最多支持 100 条数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/batch_create

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 | 默认

 |
app_id

 | String

 | 是

 | 应用ID

 | ——

 |
entry_id

 | String

 | 是

 | 表单ID

 |

 |
data_list

 | Array

 | 是

 | 数据内容数组

 |

 |
data_creator

 | String

 | 否

 | 数据提交人（取成员编号 username，可从通讯录接口获取）

 | 企业创建者

 |
transaction_id

 | String

 | 否

 | 事务ID；transaction_id 用于表示一次事务，用于防止因重试而导致重复创建同一批数据，也用于绑定一批文件，建议使用 UUID 以免重复。

 |

 |
is_start_workflow

 | Bool

 | 否

 | 是否发起流程（仅流程表单有效）

 | false

 |

请求示例：

{
  "app_id": "59264073a2a60c0c08e20bfb",
  "entry_id": "59264073a2a60c0c08e20bfd",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_list": [
        {
            "_widget_1432728651402": { // 单行文本
                "value": "简道云1"
            },
            "_widget_1432728651403": { // 数字
                "value": 100
            },
         	"_widget_1725969783950": {
          		"value": "67221b4fac0a62ac8f43a1c4"//关联数据
      		},
            "_widget_1528854613291": { // 子表单
                "value": [
                    { // 子表单子记录结构跟主表一致
                        "_widget_1528854614409": {
                            "value": "子表单数据11"
                        },
                        "_widget_1528854615499": {
                            "value": 1001
                        }
                    },
                    {
                        "_widget_1528854614410": {
                            "value": "子表单数据12"
                        },
                        "_widget_1528854615419": {
                            "value": 1002
                        }
                    }
                ]
            }
        },
        {
            "_widget_1432728651402": {
                "value": "简道云2"
            },
            "_widget_1432728651403": {
                "value": 200
            },
            "_widget_1528854613291": {
                "value": [
                    {
                        "_widget_1528854614409": {
                            "value": "子表单数据21"
                        },
                        "_widget_1528854615499": {
                            "value": 2001
                        }
                    }
                ]
            }
        },
        {
            "_widget_1432728651402": {
                "value": "简道云3"
            },
            "_widget_1432728651403": {
                "value": 300
            },
            "_widget_1528854613291": {
                "value": [
                    {
                        "_widget_1528854614410": {
                            "value": "子表单数据31"
                        },
                        "_widget_1528854615419": {
                            "value": 3001
                        }
                    }
                ]
            }
        }
    ],
    "is_start_workflow": true
}

响应内容：

参数

 | 类型

 | 说明

 |
status

 | String

 | 返回请求结果

 |
success_count

 | Number

 | 该 transaction_id 创建成功的数据条数

 |
success_ids

 | Array

 | 本次请求创建成功的数据的 ID 列表

 |

响应示例：

{
    "status": "success",
    "success_count": 3,
    "success_ids": [
        "200001181fe09728936510eb",
        "200001181fe09728936510ec",
        "200001181fe09728936510ed"
    ]
}

3. 注意事项

1）新建多条数据，部分数据新建时可能出现失败的情况。处理方法如下所示：

使用同一个 transaction_id 再次请求新建多条，传入全部数据。传入后，第二次执行的数据将会完全覆盖掉第一次执行的数据。
注：transaction_id 的有效期为 1 小时。1 小时内传入相同的 id 将按照同一批任务处理，会覆盖掉前一次的数据；超过 1 小时后不会按照同一批任务处理，将会创建一批新数据。

2）如果请求中指定了 data_creator，则关联触发的以下成员也会被记录为 data_creator，如下所示：

智能助手执行人
流程发起人
CRM 相关关联修改
由跟进记录关联修改的客户表、线索表和商机表的修改人
由商机表关联修改的客户表的修改人


---

## 修改单条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14224

1. 简介

1.1 接口简介

通过修改单条数据接口，可以对指定的单条数据进行修改。

注：使用 API 添加数据时，会触发的事件有新数据提交提醒、聚合表计算&校验、数据操作日志、数据量统计。也可以通过请求参数来控制是否发起流程。但是不会触发重复值校验、必填校验。

另外，系统字段 和以下所列举的字段不支持添加和修改数据：

分割线
手写签名
选择数据、查询
流水号（提交后系统生成）
1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.6.21

 | 部门和成员均使用_id为主键

 |
v2

 | 2019.6.21

 | 在 v1 的基础上，成员字段使用 username 为主键，部门字段使用 dept_no 为主键

 |
v3

 | 2021.3.31

 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID

 |
v4

 | 2022.4.21

 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：

0：内部
2：外部
 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/update。

 |
2. 接口调用

按照指定数据 ID 修改表单中的数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/update

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 | 默认

 |
app_id

 | String

 | 是

 | 应用ID

 |

 |
entry_id

 | String

 | 是

 | 表单ID

 |

 |
data_id

 | String

 | 是

 | 数据 ID

 |

 |
data

 | JSON

 | 是

 | 数据内容，其他同新建单条数据接口，子表单需要注明子表单数据 ID

 |

 |
is_start_trigger

 | Bool

 | 否

 | 是否触发智能助手

 | false

 |
transaction_id

 | String

 | 否

 | 事务 ID；transaction_id 用于绑定一批上传的文件，若数据中包含附件或图片控件，则 transaction_id 必须与“获取文件上传凭证和上传地址接口”中的 transaction_id 参数相同。

 |

 |

请求示例：

{
   "app_id": "604eb6eea71d720006e1336e",
   "entry_id": "604ecfca8e2ade077c72453a",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_id": "6052e8072315c0075001d65e",
    "data": {
        "_widget_1615777739654": {
            "value": "张三"
        },
        "_widget_1725969783950": {
      		"value": "67221b4fac0a62ac8f43a1c3"//关联数据
    	},
        "_widget_1615777739673": {
            "value": [
                {
                    "_widget_1615777739744": {   // 未传子表单数据ID
                        "value": "张三"
                    }
                },
                {
                    "_id": {
                        "value": "606290aba392ca00076da000"   // 错误的子表单数据ID
                    },
                    "_widget_1615777739744": {
                        "value": "李四"
                    }
                },
                {
                    "_id": {
                        "value": "606290aba392ca00076da0a9"     // 正确的子表单数据ID
                    },
                    "_widget_1615777739744": {
                        "value": "王五"
                    }
                }
            ]
        }
    },
    "is_start_trigger": true
}

响应内容：

参数

 | 类型

 | 说明

 |
data

 | JSON

 | 返回修改后的新数据，内容同查询单条数据接口

 |

响应示例：

{
    "data": {
        "creator": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "updater": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "deleter": null,
        "createTime": "2021-03-18T05:41:27.760Z",
        "updateTime": "2021-03-30T02:46:21.563Z",
        "deleteTime": null,
        "_widget_1615777739654": "张三",
        "_widget_1725969783950": "67221b4fac0a62ac8f43a1c3",//关联数据
        "_widget_1616052516346": "",
        "_widget_1615777739673": [
            {
                "_id": "606290fd0094210006e97551",   // 未传子表单数据ID则新建
                "_widget_1615777739744": "张三"
            },
            {
                "_id": "606290fd0094210006e97552",   // 传入错误的子表单数据ID则新建
                "_widget_1615777739744": "李四"
            },
            {
                "_id": "606290aba392ca00076da0a9",   // 传入正确的子表单数据ID则保持
                "_widget_1615777739744": "王五"
            }
        ],
        "_id": "6052e8072315c0075001d65e",
        "appId": "604eb6eea71d720006e1336e",
        "entryId": "604ecfca8e2ade077c72453a",
        "wx_open_id": "wx98fb14481b3ab5a3",
        "wx_nickname": "jiandaoyun",
        "wx_gender": "男"
    }
}

3. 注意事项

1）如果调用修改单条数据 v3/v4/v5 接口时，未传递子表单数据 ID 或者 传递了错误的子表单数据 ID：

每次调用会清空请求的那条数据中原本的子表单数据，填入新请求的子表单数据；
给未传递子表单数据 ID 或传递了错误的子表单数据 ID 的子表单数据生成新的子表单数据 ID；
数据管理的数据日志中将会记录「子表单变更」，即使子表单内容没有发生任何变化。
注：

1）仅重置未传递或者传递错误的子表单数据 ID，调用一次重置一次。

2）若传递了正确的子表单数据 ID，则维持原本的子表单数据 ID 不变。

3）v1、v2 接口不发生变化。

示例如下：

原本的子表单中有 3 行数据，结构如下：

{
    "_id": "605b5f68255d4845a73d3c0a",  // <= 数据 ID
    "_widget_1616600963783": "单行文本",
    "_widget_1616600980550": [{
        "_id": "605b5fa6255d4845a73d3c0b", // <= 子表单数据ID
        "_widget_1616601008197": "子表单内的单行文本字段值1"
    }, {
        "_id": "605b5fdc255d4845a73d3c0c", // <= 子表单数据ID
        "_widget_1616601008197": "子表单内的单行文本字段值2"
    }, {
        "_id": "605b5fdc255d4845a73d3c0d", // <= 子表单数据ID
        "_widget_1616601008197": "子表单内的单行文本字段值3"
    }]
}

假设在调用修改单条数据 v3/v4/v5 接口的过程中有一个子表单数据 ID 传递错误，有一个未传递，有一个传递正确，请求参数如下：

{
    "data_id": "605b5f68255d4845a73d3c0a", // <= 数据 ID
    "data": {
        "_widget_1616600963783": {
            "value": "单行文本修改"
        },
        "_widget_1616600980550": {
            "value": [{
                                                            // <= 未传递子表单数据ID
                "_widget_1616601008197": {
                    "value": "子表单内的单行文本字段值1修改"
                }
            }, {
                "_id": {
                    "value": "jiandaoyun" // <= 传递了错误的子表单数据ID
                },
                "_widget_1616601008197": {
                    "value": "子表单内的单行文本字段值2修改"
                }
            }, {
                "_id": {
                    "value": "605b5fdc255d4845a73d3c0d" // <= 传递了正确的子表单数据ID
                },
                "_widget_1616601008197": {
                    "value": "子表单内的单行文本字段值3修改"
                }
            }]
        },
    //... 其余参数
    }
}

那么修改之后的数据结构如下，子表单中原本的第 1、2 行的数据 ID 发生变化：

{
    "_id": "605b5f68255d4845a73d3c0a",  // <= 数据 ID
    "_widget_1616600963783": "单行文本",
    "_widget_1616600980550": [{
        "_id": "605b5fa6255d4845a73d3c0e", // <= 新的子表单数据ID
        "_widget_1616601008197": "子表单内的单行文本字段值1修改"
    }, {
        "_id": "605b5fdc255d4845a73d3c0f", // <= 新的子表单数据ID
        "_widget_1616601008197": "子表单内的单行文本字段值2修改"
    }, {
        "_id": "605b5fdc255d4845a73d3c0d", // <= 子表单数据ID不变
        "_widget_1616601008197": "子表单内的单行文本字段值3修改"
    }]
}

2）调用修改单条数据 v3/v4/v5 接口时，子表单及子字段必须整体请求和修改，不支持按照子表单数据 ID 只修改子表单对应行的数据，也不支持按照子字段的字段 ID 只修改对应子字段的数据。

如原子表单中原本有 3 条数据，请求参数中只写了 2 条数据，即使这 2 条数据的子表单行 ID 传递正确，修改后的子表单数据也只有 2 条。
原子表单中原本有 1 条数据，该条数据包含了 3 个子字段，若请求参数中只写了 2 个子字段，即使这 2 个子字段的字段 ID 传递正确，修改后的子表单数据也只有 2 个子字段。


---

## 修改多条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14225

1. 简介

1.1 接口简介

通过修改多条数据接口，可以批量修改多条数据。

注：

1）修改多条数据接口暂不支持子表单。

2）最多支持修改 100 条数据。

3）附件和图片字段更新时会清除字段中原有的文件。

4）修改多条数据是指把多条数据的字段修改成一个固定值。

1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.12.30

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/batch_update。

 |
2. 接口调用

批量更新多条数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/batch_update

请求频率：10 次秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID

 |
entry_id

 | String

 | 是

 | 表单ID

 |
data_ids

 | Array

 | 是

 | 要更新的数据 ID 数组

 |
data

 | JSON

 | 是

 | 数据内容，暂不支持子表单

 |
transaction_id

 | String

 | 否

 | 事务 ID；transaction_id 用于绑定一批上传的文件，若数据中包含附件或图片控件，则 transaction_id 必须与“获取文件上传凭证和上传地址接口”中的 transaction_id 参数相同

 |

请求示例：

{
  "app_id": "59264073a2a60c0c08e20bfb",
  "entry_id": "59264073a2a60c0c08e20bfd",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_ids": [
        "200001181fe09728936510eb",
        "200001181fe09728936510ec",
        "200001181fe09728936510ed"
    ],
    "data": {
        "_widget_1432728651402": { // 单行文本
            "value": "简道云1"
        },
        "_widget_1432728651403": { // 数字
            "value": 100
        },
        "_widget_1725969783950": {
      		"value": "67221b4fac0a62ac8f43a1c4"//关联数据
    	}
    }
}

响应内容：

参数

 | 类型

 | 说明

 |
status

 | String

 | 返回请求结果

 |
success_count

 | Number

 | 修改成功的数据条数

 |

响应示例：

{
    "status": "success",
    "success_count": 3
}


---

## 删除单条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14226

1. 简介

1.1 接口简介

通过删除单条数据接口，可以对指定的数据进行删除。

1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.6.21

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/delete。

 |
2. 接口调用

按照指定数据 ID 从表单中删除数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/delete

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 | 默认

 |
app_id

 | String

 | 是

 | 应用ID

 |

 |
entry_id

 | String

 | 是

 | 表单ID

 |

 |
data_id

 | String

 | 是

 | 数据 ID

 |

 |
is_start_trigger

 | Bool

 | 否

 | 是否触发智能助手

 | false

 |

请求示例：

{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "data_id": "6052e8072315c0075001d65e"
}

响应内容：

参数

 | 类型

 | 说明

 |
status

 | String

 | 返回请求结果

 |

响应示例：

{
    "status": "success"
}


---

## 删除多条数据接口

- 官方文档：https://hc.jiandaoyun.com/open/14527

1. 简介

1.1 接口简介

通过删除多条数据接口，可以批量删除数据。

删除多条数据接口一次最多支持删除 100 条数据。

1.2 接口版本说明

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2022.6.14

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/data/batch_delete。

 |
2. 接口调用

按照指定数据 ID 批量从表单中删除数据。

请求地址：https://api.jiandaoyun.com/api/v5/app/entry/data/batch_delete

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
app_id

 | 是

 | String

 | 应用ID

 |
entry_id

 | 是

 | String

 | 表单ID

 |
data_ids

 | 是

 | String[]

 | 要删除的数据ID数组

 |

请求示例：

{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "data_ids": [
        "200001181fe09728936510eb",
        "200001181fe09728936510ec",
        "200001181fe09728936510ed"
    ]
}

响应参数：

参数

 | 类型

 | 说明

 |
status

 | String

 | 成功返回‘success’

 |
success_count

 | number

 | 删除成功的数据条数

 |

响应示例：

{
    "status": "success",
    "success_count": 3
}


---

## 文件接口

- 官方文档：https://hc.jiandaoyun.com/open/13287

1. 开发准备

开发前，请仔细阅读 开发指南。

2. 文件API

2.1 获取文件上传凭证和上传地址接口

获取文件上传凭证和上传地址接口

接口版本说明：

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.12.30

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 app_id 和 entry_id 放入 body，接口路由修改为 POST app/entry/file/get_upload_token。

 |
请求地址：https://api.jiandaoyun.com/api/v5/app/entry/file/get_upload_token

请求频率： 20 次/秒

请求方式：POST

接口说明：

每次请求会获取 100 个文件上传凭证和上传地址，上传的文件会与 transaction_id 绑定，只有相同 transaction_id 的创建或修改请求才能使用该文件。

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
app_id

 | String

 | 是

 | 应用ID

 |
entry_id

 | String

 | 是

 | 表单ID

 |
transaction_id

 | String

 | 是

 | 事务ID

 |
注：

1）transaction_id 参数需用户自己生成，推荐使用 UUID 格式。

2）transaction_id 中，不允许包含 ${var}、$(var)、$(var}、${var) 模式的文本，否则将无法通过格式校验，导致接口调用失败。

请求数据样例：

{
 "app_id": "59264073a2a60c0c08e20bfb",
  "entry_id": "59264073a2a60c0c08e20bfd",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677"   //事务ID
}

响应内容：

参数

 | 类型

 | 说明

 |
token_and_url_list

 | JSON

 | 文件上传凭证和上传地址

 |
token_and_url_list[].url

 | String

 | 文件上传地址

 |
token_and_url_list[].token

 | String

 | 文件上传凭证

 |
响应示例：

{
    "token_and_url_list": [
        {
            "url": "https://upload.qiniup.com",
            "token": "bM7UwVPyBBdPaleBZt21SWKzMy2qPUpn-05jZlas:ELIqACNut-t52UMPD-DZNrX8hTU=:eyJmc2l6ZU1pbiI6MSwiZnNpemVMaW1pdCI6MjA5NzE1MjAwLCJjYWxsYmFja0JvZHlUeXBlIjoiYXBwbGljYXRpb24vanNvbiIsImNhbGxiYWNrQm9keSI6IntcImFwcElkXCI6XCI2MWFjNzcxNTE0MjU3NDM2ODhlZWMwYzRcIixcImVudHJ5SWRcIjpcIjYxYWM3NzNhMTQyNTc0MzY4OGVlYzBjN1wiLFwia2V5XCI6XCIkKGtleSlcIixcImhhc2hcIjpcIiQoZXRhZylcIixcIm5hbWVcIjpcIiQoZm5hbWUpXCIsXCJzaXplXCI6XCIkKGZzaXplKVwiLFwibWltZVwiOlwiJChtaW1lVHlwZSlcIixcImJ1Y2tldFwiOlwiamR5LWZpbGVcIixcInVwbG9hZGVyXCI6XCI2MTFhMmQzNjRmMzQ3MDAwMDY3NWM5ZGRcIixcInNlc3Npb25JZFwiOlwic3NkXCJ9IiwiY2FsbGJhY2tIb3N0IjoiNTA3NS0xMTQtMjI0LTE3LTIxNi5uZ3Jvay5pbyIsImNhbGxiYWNrVXJsIjoiaHR0cDovLzUwNzUtMTE0LTIyNC0xNy0yMTYubmdyb2suaW8vZmlsZS91cGxvYWQvYXBpX2NhbGxiYWNrIiwiZm9yY2VTYXZlS2V5Ijp0cnVlLCJzYXZlS2V5IjoiYTJjOTkwY2ItMTlhZS00NDgwLTkyYzYtZDI3N2I5ZGQ2MmFhIiwic2NvcGUiOiJkbi1qZHktdXBsb2FkIiwiZGVhZGxpbmUiOjE2Mzk0ODU2NjV9"
        },
        {
            "url": "https://upload.qiniup.com",
            "token": "bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:inKpUPPCKIWJ6CnZzHrRPnjXwio=:eyJmc226ZU1pbiI6MSwiZnNpemVMaW1pdCI6MjA5NzE1MjAwLCJjYWxsYmFja0JvZHlUeXBlIjoiYXBwbGljYXRpb24vanNvbiIsImNhbGxiYWNrQm9keSI6IntcImFwcElkXCI6XCI2MWFjNzcxNTE0MjU3NDM2ODhlZWMwYzRcIixcImVudHJ5SWRcIjpcIjYxYWM3NzNhMTQyNTc0MzY4OGVlYzBjN1wiLFwia2V5XCI6XCIkKGtleSlcIixcImhhc2hcIjpcIiQoZXRhZylcIixcIm5hbWVcIjpcIiQoZm5hbWUpXCIsXCJzaXplXCI6XCIkKGZzaXplKVwiLFwibWltZVwiOlwiJChtaW1lVHlwZSlcIixcImJ1Y2tldFwiOlwiamR5LWZpbGVcIixcInVwbG9hZGVyXCI6XCI2MTFhMmQzNjRmMzQ3MDAwMDY3NWM5ZGRcIixcInNlc3Npb25JZFwiOlwic3NkXCJ9IiwiY2FsbGJhY2tIb3N0IjoiNTA3NS0xMTQtMjI0LTE3LTIxNi5uZ3Jvay5pbyIsImNhbGxiYWNrVXJsIjoiaHR0cDovLzUwNzUtMTE0LTIyNC0xNy0yMTYubmdyb2suaW8vZmlsZS91cGxvYWQvYXBpX2NhbGxiYWNrIiwiZm9yY2VTYXZlS2V5Ijp0cnVlLCJzYXZlS2V5IjoiN2Y4Yzk3NDAtNmI2YS00OTQ0LWE0MzgtNjQ1Y2IzN2ViNmQ0Iiwic2NvcGUiOiJkbi1qZHktdXBsb2FkIiwiZGVhZGxpbmUiOjE2Mzk0ODU2NjV9"
        },
        ……
    ]
}

2.2 文件上传接口

用于上传文件的接口。

接口版本说明：

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2021.12.30

 | 原始接口

 |
v5

 | 2022.10.28

 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒

 |
请求地址：{url}

请求频率： 20 次/秒

请求方式：POST

接口说明：

此处的 url 为获取文件上传凭证和上传地址接口中获取到的上传地址。

该接口一个 token 只能上传一个文件，不允许覆盖，返回的 key 用于创建和修改接口填写在附件或图片控件值中。

请求参数：

参数

 | 必需

 | 类型

 | 说明

 |
token

 | 是

 | String

 | 文件上传凭证

 |
file

 | 是

 | 文件

 | 要上传的文件

 |
注：

1）由于请求中需要上传文件，所以参数为 form-data 形式。

2）file 需要作为最后一个参数。

3）需要正确指定 mime 类型，例如上传 PDF 文件需要指定为 application/pdf。

响应内容：

参数

 | 类型

 | 说明

 |
key

 | String

 | 文件key

 |
响应数据样例：

{
    "key": "6b559cf1-b16c-43bd-a211-8fa8fdeae2ef"
}

3. 注意事项

1）token 的有效时间为 1 小时。

2）transaction_id 和 key 配合使用，transaction_id 有效时间也为 1 小时，失效后，key 也将无法使用。
