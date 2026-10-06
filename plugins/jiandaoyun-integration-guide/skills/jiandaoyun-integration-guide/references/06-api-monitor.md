# 资源用量与审计日志接口

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 资源用量接口

- 官方文档：https://hc.jiandaoyun.com/open/25778

1. 简介

1.1 接口简介

资源用量接口提供了一套用于监控和分析企业内部资源消耗情况的工具，帮助企业管理员或相关团队清晰了解各维度下的资源使用状况，实现精细化的资源管理，有效控制成本，提升资源利用效率，并为未来的资源规划和决策提供数据支持。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

2. 接口类型

序号

 | 接口名称

 | 接口描述

 |
1

 | 获取平台资源用量统计接口

 | 获取当前企业在指定日期的平台资源用量概览。

 |
2

 | 获取应用资源用量统计接口

 | 获取当前企业在指定日期的应用维度资源用量统计。

 |
3

 | 获取成员资源用量统计接口

 | 获取当前企业在指定日期的成员维度资源用量统计。

 |


---

## 获取平台资源用量统计接口

- 官方文档：https://hc.jiandaoyun.com/open/25795

1. 简介

1.1 接口简介

获取当前企业在指定日期的平台资源用量概览。

注：接口只返回企业维度的汇总指标，不返回应用或成员明细。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

1.3 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2026.05.28

 | 原始接口

 |
v2

 | 2026.06.29

 | 新增响应字段：

daily_automation_exec：智能助手 Pro 日执行次数
daily_attachment_upload：日附件上传量
 |
2. 接口调用

请求地址：https://api.jiandaoyun.com/api/v1/corp_usage/overview

请求频率：1 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
date

 | String

 | 否

 | 统计日期，格式 yyyy-MM-dd。

不传或传空字符串表示查询当前日期的前一日（T-1）的统计信息

 |
注：

1）date 默认为东八区时间，即中国时间。

2）指定 date 时，不能晚于当前日期的前一日（T-1），最多支持查询最近 180 天。

3）使用该接口时，若从未使用过「管理后台 > 管理工具 > 使用统计」功能，将无法获取相关数据，指标字段返回值为 0。

4）当 date 合法但传入时间早于第一次使用「管理后台 > 管理工具 > 使用统计」功能时，也无法获取相关数据

请求示例：

{
  "date": "2026-05-08"
}

响应参数：

参数

 | 含义

 |
date

 | 统计日期。

 |
metrics

 | 企业用量指标。指标字段如下所示：

app：应用数
form_coop：普通表单数
form_workflow：流程表单数
dash：仪表盘数
etl：数据工厂数
aggregate：聚合表数
public_link：外链开启数
data_trigger：智能助手数
automation：智能助手 Pro 数
bpa：流程分析数
data：数据总量
daily_automation_exec：智能助手 Pro 日执行次数
daily_attachment_upload：日附件上传量，单位：byte
 |
响应示例：

{
  "date": "2026-06-29",
  "metrics": {
    "app": 34,
    "form_coop": 245,
    "form_workflow": 109,
    "dash": 75,
    "etl": 52,
    "aggregate": 29,
    "public_link": 0,
    "data_trigger": 100,
    "automation": 43,
    "bpa": 0,
    "data": 353,
    "daily_attachment_upload": 0,
    "daily_automation_exec": 0
  }
}


---

## 获取应用资源用量统计接口

- 官方文档：https://hc.jiandaoyun.com/open/25791

1. 简介

1.1 接口简介

获取当前企业在指定日期的应用维度资源用量统计。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

1.3 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2026.05.28

 | 原始接口

 |
v2

 | 2026.06.29

 | 新增响应字段：

daily_automation_exec：智能助手 Pro 日执行次数
daily_attachment_upload：日附件上传量
 |
2. 接口调用

请求地址：https://api.jiandaoyun.com/api/v1/corp_usage/app_metrics

请求频率：1 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
date

 | String

 | 否

 | 统计日期，格式 yyyy-MM-dd。

不传或传空字符串表示查询当前日期的前一日（T-1）的统计信息

 |
app_ids

 | String[]

 | 否

 | 应用 ID 列表，最多 10 个。

空数组或不传表示分页查询全部应用

 |
skip

 | Number

 | 否

 | 分页偏移，默认 0

 |
limit

 | Number

 | 否

 | 分页大小，默认 20，最大 100

 |
注：

1）date 默认为东八区时间，即中国时间。

2）指定 date 时，不能晚于当前日期的前一日（T-1），最多支持查询最近 180 天。

3）使用该接口时，若从未使用过「管理后台＞＞管理工具＞>使用统计」功能，将无法获取相关数据，指标字段返回值为 0。

4）当 date 合法但传入时间早于第一次使用「管理后台 >> 管理工具 >> 使用统计」功能时，也无法获取相关数据

请求示例：

{
  "date": "2026-05-08",
  "app_ids": [
    "65f000000000000000000001"
  ],
  "skip": 0,
  "limit": 20
}

响应参数：

参数

 | 含义

 |
date

 | 统计日期。

 |
has_next

 | 是否存在下一页

 |
items

 | 应用统计列表

 |
items[].app_id

 | 应用 ID

 |
items[].app_name

 | 应用名称

 |
items[].creator

 | 创建者基础信息

 |
items[].created_at

 | 创建时间

 |
items[].last_edit_at

 | 最近一次编辑时间

 |
items[].last_visit_at

 | 最近一次访问时间

 |
items[].metrics

 | 应用维度指标。指标字段如下所示：

app：应用数，应用维度通常为 1
form_coop：普通表单数
form_workflow：流程表单数
dash：仪表盘数
etl：数据工厂数
aggregate：聚合表数
public_link：外链开启数
data_trigger：智能助手数
automation：智能助手 Pro 数
bpa：流程分析数
data：数据总量
daily_automation_exec：智能助手 Pro 日执行次数
daily_attachment_upload：日附件上传量，单位：byte
 |
响应示例：

{
  "date": "2026-05-08",
  "has_next": false,
  "items": [
    {
      "app_id": "65f000000000000000000001",
      "app_name": "CRM",
      "creator": {
        "member_id": "65f000000000000000000011",
        "name": "张三"
      },
      "created_at": "2026-01-01T00:00:00+08:00",
      "last_edit_at": "2026-05-06T12:00:00+08:00",
      "last_visit_at": "2026-05-06T18:00:00+08:00",
      "metrics": {
        "app": 1,
        "form_coop": 20,
        "form_workflow": 3,
        "dash": 2,
        "etl": 1,
        "aggregate": 1,
        "public_link": 5,
        "data_trigger": 2,
        "automation": 1,
        "bpa": 0,
        "data": 2,
        "daily_attachment_upload": 0,
        "daily_automation_exec": 0
      }
    }
  ]
}


---

## 获取成员资源用量统计接口

- 官方文档：https://hc.jiandaoyun.com/open/25796

1. 简介

1.1 接口简介

获取当前企业在指定日期的成员维度资源用量统计。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

1.3 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2026.05.28

 | 原始接口

 |
2. 接口调用

请求地址：https://api.jiandaoyun.com/api/v1/corp_usage/member_metrics

请求频率：1 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
date

 | String

 | 否

 | 统计日期，格式 yyyy-MM-dd。

不传或传空字符串表示查询当前日期的前一日（T-1）的统计信息

 |
member_ids

 | String[]

 | 否

 | 成员 ID 列表，最多 10 个。

空数组或不传表示分页查询全部成员

 |
skip

 | Number

 | 否

 | 分页偏移，默认 0

 |
limit

 | Number

 | 否

 | 分页大小，默认 20，最大 100

 |
注：

1）date 默认为东八区时间，即中国时间。

2）指定 date 时，不能晚于当前日期的前一日（T-1），最多支持查询最近 180 天。

3）使用该接口时，若从未使用过「管理后台＞＞管理工具＞>使用统计」功能，将无法获取相关数据，指标字段返回值为 0。

4）当 date 合法但传入时间早于第一次使用「管理后台 >> 管理工具 >> 使用统计」功能时，也无法获取相关数据

请求示例：

{
  "date": "2026-05-08",
  "member_ids": [
    "65f000000000000000000011"
  ],
  "skip": 0,
  "limit": 20
}

响应参数：

参数

 | 含义

 |
date

 | 统计日期。

 |
has_next

 | 是否存在下一页

 |
items

 | 成员统计列表

 |
items[].member

 | 成员基础信息

 |
items[].member.member_id

 | 成员 ID

 |
items[].member.name

 | 成员名称

 |
items[].metrics

 | 成员维度指标。指标字段如下所示：

app：应用数；
form_coop：普通表单数；
form_workflow：流程表单数；
dash：仪表盘数；
etl：数据工厂数；
aggregate：聚合表数；
public_link：外链开启数；
data_trigger：智能助手数；
automation：智能助手 Pro 数；
bpa：流程分析数；
data：数据总量
 |
响应示例：

{
  "date": "2026-05-08",
  "has_next": false,
  "items": [
    {
      "member": {
        "member_id": "65f000000000000000000011",
        "name": "张三"
      },
      "metrics": {
        "app": 2,
        "form_coop": 10,
        "form_workflow": 1,
        "dash": 3,
        "etl": 1,
        "aggregate": 0,
        "public_link": 2,
        "data_trigger": 1,
        "automation": 1,
        "bpa": 0
      }
    }
  ]
}


---

## 审计日志接口

- 官方文档：https://hc.jiandaoyun.com/open/25779

1. 简介

1.1 接口简介

审计日志接口提供了一套用于管理和查询企业内关键操作记录的工具。帮助企业管理员或安全团队追溯用户行为、监控系统活动、满足合规性要求以及进行安全事件分析。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

2. 接口类型

序号

 | 接口名称

 | 接口描述

 |
1

 | 获取审计日志类型定义接口

 | 获取当前企业的审计日志范围和事件类型定义

 |
2

 | 获取审计日志明细接口

 | 按范围查询当前企业的审计日志明细

 |


---

## 审计事件列表

- 官方文档：https://hc.jiandaoyun.com/open/25784

💡审计事件列表是指用户获取到的日志范围（domain）中的具体事件名称。

⚽️文档有两个个标记：

内测功能：当用户加入功能内测时，才能获取到对应的数据，否则取不到数据；
独享版功能：当简道云版本为独享版时才能获取到对应数据，否则取不到数据。

登录日志（login）

用户在简道云平台上的登录行为

功能模块

 | 事件名称

 | 事件参数

 |
登录登出

 | 用户登录

 | auth.session.login

 |
知识库管理（kms）

审计知识库管理员对知识库的操作行为

功能模块

 | 事件名称

 | 事件参数

 |
知识库

 | 开启知识库

 | admin.kms.enable

 |
知识库

 | 关闭知识库

 | admin.kms.disable

 |
知识库

 | 创建知识库

 | admin.kms.space_create

 |
知识库

 | 修改知识库基本信息

 | admin.kms.space_update

 |
知识库

 | 删除知识库

 | admin.kms.space_delete

 |
知识库

 | 新建知识库权限组

 | admin.kms.perm_group_create

 |
知识库

 | 修改知识库权限组

 | admin.kms.perm_group_update

 |
知识库

 | 删除知识库权限组

 | admin.kms.perm_group_delete

 |
应用管理日志（app_builder）

审计应用管理员对应用的操作行为

功能模块

 | 事件名称

 | 事件参数

 | 备注

 |
应用管理

 | 创建应用

 | admin.app.create

 |

 |
应用管理

 | 删除应用

 | admin.app.delete

 |

 |
应用管理

 | 修改应用名称

 | admin.app.rename

 |

 |
应用管理

 | 恢复应用

 | admin.app.recover

 |

 |
应用管理

 | 调整跨应用设置

 | admin.app.ref_forms_set_update

 |

 |
应用管理

 | 调整应用首页

 | admin.app.home_update

 |

 |
应用管理

 | 调整应用 URL

 | admin.app.url_update

 |

 |
应用管理

 | 开启应用水印

 | admin.app.watermark_enable

 |

 |
应用管理

 | 关闭应用水印

 | admin.app.watermark_disable

 |

 |
应用管理

 | 开启应用附件管控

 | admin.app.attachment_control_enable

 |

 |
应用管理

 | 关闭应用附件管控

 | admin.app.attachment_control_disable

 |

 |
应用管理

 | 修改应用附件管控

 | admin.app.attachment_control_update

 |

 |
应用管理

 | 添加应用管理员

 | admin.app.manager_add

 |

 |
应用管理

 | 删除应用管理员

 | admin.app.manager_remove

 |

 |
应用管理

 | 添加应用管理组

 | admin.app.manage_group_create

 |

 |
应用管理

 | 删除应用管理组

 | admin.app.manage_group_delete

 |

 |
应用管理

 | 修改应用管理组名称

 | admin.app.manage_group_rename

 |

 |
应用管理

 | 开启应用管理组

 | admin.app.manage_group_enable

 |

 |
应用管理

 | 关闭应用管理组

 | admin.app.manage_group_disable

 |

 |
应用管理

 | 修改产品风格

 | admin.app.style_update

 |

 |
应用管理

 | 开启多语言管理

 | admin.app.locale_enable

 | 该功能为内测功能

 |
应用管理

 | 修改「多语言管理」默认语言

 | admin.app.locale_change_locale

 | 该功能为内测功能

 |
应用管理

 | 修改「多语言管理」支持语言

 | admin.app.locale_change_locales

 | 该功能为内测功能

 |
应用管理

 | 导出产品日志

 | admin.app.log_export

 |

 |
应用管理

 | 导出历史产品日志

 | admin.app.history_log_export

 |

 |
表单管理

 | 创建表单

 | admin.form.create

 |

 |
表单管理

 | 删除表单

 | admin.form.delete

 |

 |
表单管理

 | 修改表单名称

 | admin.form.rename

 |

 |
表单管理

 | 修改表单设计

 | admin.form.update

 |

 |
表单管理

 | 恢复表单

 | admin.form.recover

 |

 |
表单管理

 | 修改流程设计

 | admin.form.flow_update

 |

 |
表单管理

 | 调整表单权限

 | admin.form.auth_update

 |

 |
表单管理

 | 批量调整表单/仪表盘权限

 | admin.form.auth_batch_update

 |

 |
表单管理

 | 调整表单公开链接

 | admin.form.public_link

 |

 |
表单管理

 | 调整表单公开查询

 | admin.form.public_query

 |

 |
表单管理

 | 调整表单在线支付

 | admin.form.online_pay

 |

 |
表单管理

 | 切换表单类型

 | admin.form.type_change

 |

 |
表单管理

 | 编辑数据详情页

 | admin.form.data_page_update

 |

 |
表单管理

 | 切换数据详情页

 | admin.form.data_page_switch

 |

 |
表单管理

 | 删除数据详情页

 | admin.form.data_page_delete

 |

 |
表单管理

 | 开启流程分析

 | admin.form.flow_analysis_enable

 |

 |
表单管理

 | 关闭流程分析

 | admin.form.flow_analysis_disable

 |

 |
数据操作

 | 创建数据

 | data.record.create

 |

 |
数据操作

 | 修改数据

 | data.record.update

 |

 |
数据操作

 | 批量修改数据

 | data.record.batch_update

 |

 |
数据操作

 | 删除数据

 | data.record.delete

 |

 |
数据操作

 | 批量删除数据

 | data.record.batch_delete

 |

 |
数据操作

 | 恢复数据

 | data.record.recover

 |

 |
数据操作

 | 批量恢复数据

 | data.record.batch_recover

 |

 |
数据操作

 | 导入-新增数据

 | data.record.import

 |

 |
数据操作

 | 导入-更新数据

 | data.record.import_update

 |

 |
数据操作

 | 导入-更新和新增数据

 | data.record.import_upsert

 |

 |
数据操作

 | 导入附件

 | data.record.import_file

 |

 |
数据操作

 | 导出数据

 | data.record.export

 |

 |
数据操作

 | 打印数据

 | data.record.print

 |

 |
数据操作

 | 批量打印

 | data.record.batch_print

 |

 |
数据操作

 | 打印二维码/条形码

 | data.record.print_qr

 |

 |
数据操作

 | 下载文件

 | data.file.download

 |

 |
数据操作

 | 归档数据

 | data.record.archive

 | 该功能为内测功能

 |
数据操作

 | 恢复归档数据

 | data.record.unarchive

 | 该功能为内测功能

 |
仪表盘

 | 创建仪表盘

 | admin.dash.create

 |

 |
仪表盘

 | 删除仪表盘

 | admin.dash.delete

 |

 |
仪表盘

 | 恢复仪表盘

 | admin.dash.recover

 |

 |
仪表盘

 | 修改仪表盘设计

 | admin.dash.update

 |

 |
仪表盘

 | 修改仪表盘名称

 | admin.dash.rename

 |

 |
仪表盘

 | 调整仪表盘权限

 | admin.dash.auth_update

 |

 |
仪表盘

 | 调整仪表盘公开链接

 | admin.dash.public_link

 |

 |
聚合表

 | 创建聚合表

 | admin.aggregate.create

 |

 |
聚合表

 | 删除聚合表

 | admin.aggregate.delete

 |

 |
聚合表

 | 修改聚合表名称

 | admin.aggregate.rename

 |

 |
聚合表

 | 修改聚合表设计

 | admin.aggregate.update

 |

 |
聚合表

 | 迁移聚合表

 | admin.aggregate.migrate

 |

 |
智能助手

 | 创建智能助手

 | system.automation.create

 |

 |
智能助手

 | 删除智能助手

 | system.automation.delete

 |

 |
智能助手

 | 修改智能助手

 | system.automation.update

 |

 |
智能助手

 | 开启智能助手

 | system.automation.start

 |

 |
智能助手

 | 关闭智能助手

 | system.automation.stop

 |

 |
数据工厂

 | 创建数据流

 | system.etl.create

 |

 |
数据工厂

 | 删除数据流

 | system.etl.delete

 |

 |
数据工厂

 | 修改数据流名称

 | system.etl.rename

 |

 |
数据工厂

 | 修改数据流设计

 | system.etl.update

 |

 |
其他应用能力

 | 添加普通管理组

 | admin.manage_group.create

 |

 |
其他应用能力

 | 删除普通管理组

 | admin.manage_group.delete

 |

 |
其他应用能力

 | 修改普通管理组名称

 | admin.manage_group.rename

 |

 |
其他应用能力

 | 添加普通管理员

 | admin.manage_group.manager_add

 |

 |
其他应用能力

 | 删除普通管理员

 | admin.manage_group.manager_remove

 |

 |
其他应用能力

 | 修改企业工作台

 | admin.workbench.update

 |

 |
其他应用能力

 | 开启消息推送

 | admin.webhook.enable

 |

 |
其他应用能力

 | 关闭消息推送

 | admin.webhook.disable

 |

 |
其他应用能力

 | 修改消息推送

 | admin.webhook.update

 |

 |
其他应用能力

 | 开启待办委托

 | admin.bpm.delegation_enable

 |

 |
其他应用能力

 | 关闭待办委托

 | admin.bpm.delegation_disable

 |

 |
其他应用能力

 | 调整待办委托

 | admin.bpm.delegation_update

 |

 |
其他应用能力

 | 设置支付服务

 | admin.pay.update

 |

 |
平台管理日志（platform）

审计平台管理员在平台中的操作行为

功能模块

 | 事件名称

 | 事件参数

 | 备注

 |
平台管理员与企业设置

 | 添加管理员

 | admin.platform.manager_add

 |

 |
平台管理员与企业设置

 | 移除管理员

 | admin.platform.manager_remove

 |

 |
平台管理员与企业设置

 | 添加通讯录管理组

 | admin.platform.group_create

 |

 |
平台管理员与企业设置

 | 删除通讯录管理组

 | admin.platform.group_remove

 |

 |
平台管理员与企业设置

 | 修改通讯录管理组名称

 | admin.platform.group_rename

 |

 |
平台管理员与企业设置

 | 修改企业名称

 | admin.corp.rename

 |

 |
平台管理员与企业设置

 | 修改绑定信息

 | admin.corp.integrate_update

 |

 |
平台管理员与企业设置

 | 修改企业账号 URL

 | admin.corp.url_update

 |

 |
平台管理员与企业设置

 | 修改时区

 | admin.corp.timezone_update

 |

 |
平台管理员与企业设置

 | 修改系统区域

 | admin.corp.region_update

 | 该功能为内测功能

 |
平台管理员与企业设置

 | 修改语言

 | admin.corp.locale_update

 | 该功能为内测功能

 |
平台管理员与企业设置

 | 身份认证

 | admin.corp.verify

 |

 |
平台管理员与企业设置

 | 开启企业风格

 | admin.corp.theme_enable

 |

 |
平台管理员与企业设置

 | 关闭企业风格

 | admin.corp.theme_disable

 |

 |
平台管理员与企业设置

 | 修改企业风格

 | admin.corp.theme_update

 |

 |
订单与云币

 | 修改云币支付设置

 | admin.coin.config_update

 |

 |
订单与云币

 | 创建订单

 | admin.order.create

 |

 |
订单与云币

 | 支付订单

 | admin.order.pay

 |

 |
订单与云币

 | 取消订单

 | admin.order.cancel

 |

 |
订单与云币

 | 删除订单

 | admin.order.delete

 |

 |
订单与云币

 | 订单开票

 | admin.order.receipt

 |

 |
集成、安全和套件

 | 开启微信服务号集成

 | admin.integration.wx_enable

 |

 |
集成、安全和套件

 | 关闭微信服务号集成

 | admin.integration.wx_disable

 |

 |
集成、安全和套件

 | 开启自定义登录页

 | admin.security.custom_login_enable

 |

 |
集成、安全和套件

 | 关闭自定义登录页

 | admin.security.custom_login_disable

 |

 |
集成、安全和套件

 | 开启全局水印

 | admin.security.watermark_enable

 |

 |
集成、安全和套件

 | 关闭全局水印

 | admin.security.watermark_disable

 |

 |
集成、安全和套件

 | 开启全局附件管控

 | admin.security.attachment_control_enable

 |

 |
集成、安全和套件

 | 关闭全局附件管控

 | admin.security.attachment_control_disable

 |

 |
集成、安全和套件

 | 调整待办委托

 | admin.bpm.delegation_update

 |

 |
集成、安全和套件

 | 开启 AI 能力

 | admin.ai.lab_enable

 |

 |
集成、安全和套件

 | 关闭 AI 能力

 | admin.ai.lab_disable

 |

 |
集成、安全和套件

 | 启用产品

 | admin.suite.enable

 | 该功能为内测功能

 |
集成、安全和套件

 | 停用产品

 | admin.suite.disable

 | 该功能为内测功能

 |
集成、安全和套件

 | 设置产品可见范围

 | admin.suite.scope_update

 | 该功能为内测功能

 |
集成、安全和套件

 | 调整提醒屏蔽

 | admin.security.executive_update

 |

 |
审计与文件

 | 恢复附件

 | admin.file.recover

 | 该功能为独享版功能

 |
审计与文件

 | 清理附件

 | admin.file.trash

 | 该功能为独享版功能

 |
审计与文件

 | 彻底删除附件

 | admin.file.delete

 | 该功能为独享版功能

 |
审计与文件

 | 导出登录日志

 | admin.audit.login_log_export

 |

 |
审计与文件

 | 导出操作日志

 | admin.audit.operate_log_export

 |

 |
审计与文件

 | 导出云币使用日志

 | admin.audit.coin_log_export

 |

 |
通讯录与角色

 | 邀请成员

 | admin.member.invite

 |

 |
通讯录与角色

 | 主动退出企业

 | admin.member.exit

 |

 |
通讯录与角色

 | 转为离职

 | admin.member.remove

 |

 |
通讯录与角色

 | 修改成员信息

 | admin.member.update

 |

 |
通讯录与角色

 | 导出通讯录

 | admin.member.export

 |

 |
通讯录与角色

 | 停用成员

 | admin.member.freeze

 |

 |
通讯录与角色

 | 启用成员

 | admin.member.recover

 |

 |
通讯录与角色

 | 删除成员

 | admin.member.hard_delete

 |

 |
通讯录与角色

 | 添加部门

 | admin.dept.create

 |

 |
通讯录与角色

 | 删除部门

 | admin.dept.delete

 |

 |
通讯录与角色

 | 修改部门名称

 | admin.dept.rename

 |

 |
通讯录与角色

 | 修改部门主管

 | admin.dept.manager_update

 |

 |
通讯录与角色

 | 创建角色组

 | admin.role_group.create

 |

 |
通讯录与角色

 | 删除角色组

 | admin.role_group.delete

 |

 |
通讯录与角色

 | 修改角色组名称

 | admin.role_group.rename

 |

 |
通讯录与角色

 | 创建角色

 | admin.role.create

 |

 |
通讯录与角色

 | 删除角色

 | admin.role.delete

 |

 |
通讯录与角色

 | 修改角色名称

 | admin.role.rename

 |

 |
通讯录与角色

 | 调整角色分组

 | admin.role.change_group

 |

 |
通讯录与角色

 | 调整角色成员

 | admin.role.member_update

 |

 |
通讯录与角色

 | 设置分管部门

 | admin.role.rel_update

 |

 |
通讯录与角色

 | 交接工作

 | admin.member.handover

 |

 |
通讯录与角色

 | 导入角色

 | admin.role.rel_import

 |

 |
通讯录与角色

 | 导出角色

 | admin.role.rel_export

 |

 |
互联组织与标签

 | 邀请外部企业

 | admin.coop.guest_connect

 |

 |
互联组织与标签

 | 添加外部企业邀请链接

 | admin.coop.link_create

 |

 |
互联组织与标签

 | 删除外部企业邀请链接

 | admin.coop.link_delete

 |

 |
互联组织与标签

 | 编辑外部企业邀请链接

 | admin.coop.link_update

 |

 |
互联组织与标签

 | 修改外部企业信息

 | admin.coop.guest_update

 |

 |
互联组织与标签

 | 添加企业标签

 | admin.dept_label.create

 |

 |
互联组织与标签

 | 删除企业标签

 | admin.dept_label.delete

 |

 |
互联组织与标签

 | 修改企业标签名称

 | admin.dept_label.update

 |

 |
互联组织与标签

 | 调整企业标签内企业

 | admin.dept_label.dept_update

 |

 |
互联组织与标签

 | 修改外部对接人信息

 | admin.coop.guest_docker_update

 |

 |
互联组织与标签

 | 导出外部对接人

 | admin.coop.guest_docker_export

 |

 |
互联组织与标签

 | 添加外部对接人角色

 | admin.coop.role_create

 |

 |
互联组织与标签

 | 修改外部对接人角色名称

 | admin.coop.role_rename

 |

 |
互联组织与标签

 | 删除外部对接人角色

 | admin.coop.role_delete

 |

 |
互联组织与标签

 | 调整外部对接人角色成员

 | admin.coop.role_update

 |

 |
互联组织与标签

 | 添加我方对接人

 | admin.coop.host_docker_create

 |

 |
互联组织与标签

 | 移除我方对接人

 | admin.coop.host_docker_delete

 |

 |
互联组织与标签

 | 修改我方对接人信息

 | admin.coop.host_docker_update

 |

 |
互联组织与标签

 | 解除邀请我协作的企业的连接

 | admin.coop.host_disconnect

 |

 |
互联组织与标签

 | 申请代管通讯录

 | admin.contact.tmp_owner_apply

 |

 |
互联组织与标签

 | 移交代管权限

 | admin.contact.tmp_owner_transfer

 |

 |
API、插件和开放应用

 | 新增密钥

 | api.key.create

 |

 |
API、插件和开放应用

 | 启用密钥

 | api.key.enable

 |

 |
API、插件和开放应用

 | 停用密钥

 | api.key.disable

 |

 |
API、插件和开放应用

 | 删除密钥

 | api.key.delete

 |

 |
API、插件和开放应用

 | 修改密钥

 | api.key.update

 |

 |
API、插件和开放应用

 | 安装插件

 | api.plugin.install

 |

 |
API、插件和开放应用

 | 启用插件

 | api.agent.enable

 |

 |
API、插件和开放应用

 | 停用插件

 | api.agent.disable

 |

 |
API、插件和开放应用

 | 删除插件

 | api.agent.uninstall

 |

 |
API、插件和开放应用

 | 新建插件

 | api.plugin.create

 |

 |
API、插件和开放应用

 | 修改插件

 | api.plugin.update

 |

 |
API、插件和开放应用

 | 发布插件

 | api.plugin.pull_request

 |

 |
API、插件和开放应用

 | 复制插件

 | api.plugin.duplicate

 |

 |
API、插件和开放应用

 | 导出插件

 | api.plugin.export

 |

 |
API、插件和开放应用

 | 导入插件

 | api.plugin.import

 |

 |
API、插件和开放应用

 | 导入更新插件

 | api.plugin.import_overwrite

 |

 |
API、插件和开放应用

 | 创建数据连接

 | api.data_source.connection_create

 |

 |
API、插件和开放应用

 | 修改数据连接

 | api.data_source.connection_update

 |

 |
API、插件和开放应用

 | 删除数据连接

 | api.data_source.connection_delete

 |

 |
API、插件和开放应用

 | 创建同步表

 | api.data_source.sync_table_create

 |

 |
API、插件和开放应用

 | 修改同步细节

 | api.data_source.sync_table_update

 |

 |
API、插件和开放应用

 | 删除同步表

 | api.data_source.sync_table_delete

 |

 |
API、插件和开放应用

 | 设置同步表定时

 | api.data_source.sync_table_schedule_update

 |

 |
API、插件和开放应用

 | 批量定时同步

 | api.data_source.sync_table_schedule_batch_update

 |

 |
API、插件和开放应用

 | 同步数据

 | api.data_source.sync_table_trigger_sync

 |

 |
API、插件和开放应用

 | 停止同步

 | api.data_source.sync_table_stop_sync

 |

 |
API、插件和开放应用

 | 同步指定范围数据

 | api.data_source.sync_table_range_sync

 |

 |
API、插件和开放应用

 | 批量同步表

 | api.data_source.sync_table_batch_sync

 |

 |
API、插件和开放应用

 | 新增授权

 | api.oauth.create

 |

 |
API、插件和开放应用

 | 解除授权

 | api.oauth.delete

 |

 |
API、插件和开放应用

 | 创建集成应用

 | api.open_application.create

 |

 |
API、插件和开放应用

 | 修改集成应用

 | api.open_application.update

 |

 |
API、插件和开放应用

 | 删除集成应用

 | api.open_application.delete

 |

 |
API、插件和开放应用

 | 启用集成应用

 | api.open_application.enable

 |

 |
API、插件和开放应用

 | 停用集成应用

 | api.open_application.disable

 |

 |
API、插件和开放应用

 | 启用 MCP 服务

 | api.member_mcp.enable

 |

 |
API、插件和开放应用

 | 停用 MCP 服务

 | api.member_mcp.disable

 |

 |
API、插件和开放应用

 | 创建 MCP 服务

 | api.member_mcp.create

 |

 |
API、插件和开放应用

 | 修改 MCP 服务

 | api.member_mcp.update

 |

 |
API、插件和开放应用

 | 删除 MCP 服务

 | api.member_mcp.delete

 |

 |
API、插件和开放应用

 | 重新授权 MCP 服务

 | api.member_mcp.renew

 |

 |
API、插件和开放应用

 | 重置 MCP 服务链接

 | api.member_mcp.refresh

 |

 |
API、插件和开放应用

 | 新建自定义环境

 | api.custom_runtime.create

 |

 |
API、插件和开放应用

 | 删除自定义环境

 | api.custom_runtime.delete

 |

 |
API、插件和开放应用

 | 修改自定义环境名称

 | api.custom_runtime.rename

 |

 |


---

## 获取审计日志类型定义接口

- 官方文档：https://hc.jiandaoyun.com/open/25780

1. 简介

1.1 接口简介

获取当前企业支持的审计日志范围和事件类型定义。调用时可先调用本接口，获取 「日志范围（domain）」与 「事件名称（event_types）」后，再调用审计日志明细接口按范围查询日志。

支持获取的日志范围如下所示：

日志范围（domain）

 | 说明

 | 可用过滤字段

 |
login

 | 用户登录日志

 | filters.actor_ids
 |
platform

 | 企业、通讯录、API 配置、插件、开放平台的管理日志

 | filters.actor_ids
 |
app_builder

 | 应用、表单、仪表盘、聚合表、智能助手、数据工厂等应用搭建日志

 | filters.actor_ids
filters.app_ids
filters.entry_ids
 |
kms

 | 知识库管理日志

 | filters.actor_ids
 |
注：日志范围（domain）中的具体事件名称可参见：审计事件列表。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

1.3 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
V1

 | 2026.05.28

 | 原始接口

 |
2. 接口调用

仅获取当前 API Key 所属企业可查询的审计日志类型定义。

请求地址：https://api.jiandaoyun.com/api/v1/audit_log/domains

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 必须

 | 类型

 | 说明

 |
——

 | 请求体传入空对象{}

 |

响应参数：

参数

 | 类型

 | 说明

 |
domains

 | String

 | 审计日志范围列表

 |
domains[].domain

 | String

 | 范围标识，查询明细时传入 domain

 |
domains[].event_types

 | String

 | 当前范围支持的事件类型列表，查询明细时可传入 event_types

 |
响应示例：

{
  "domains": [
    {
      "domain": "login",
      "event_types": [
        "auth.session.login"
      ]
    },
    {
      "domain": "app_builder",
      "event_types": [
        "admin.app.create",
        "admin.app.watermark_enable"
      ]
    }
  ]
}


---

## 获取审计日志明细接口

- 官方文档：https://hc.jiandaoyun.com/open/25786

1. 简介

1.1 接口简介

按范围查询当前企业的审计日志明细。

1.2 版本说明

本功能为付费高级功能，简道云旗舰版、独享版可用，其他版本请联系销售增购。详情参见：官网定价。

1.3 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2026.05.28

 | 原始接口

 |
2. 接口调用

请求地址：https://api.jiandaoyun.com/api/v1/audit_log/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必需

 | 说明

 |
domain

 | String

 | 是

 | 日志范围。

 |
time_range.start

 | String

 | 是

 | 查询开始时间，UTC 时间

格式示例：2026-04-01T00:00:00.000Z
 |
time_range.end

 | String

 | 是

 | 查询结束时间，UTC 时间

格式示例：2026-04-13T23:59:59.000Z
 |
event_types

 | String[]

 | 否

 | 事件类型列表。

不传表示查询当前日志范围（domain） 支持的全部事件类型（event_types）

 |
limit

 | Number

 | 否

 | 单次返回条数，默认 200，最大 200

 |
cursor

 | String

 | 否

 | 分页游标

首次查询不传；下一页使用上次响应的 cursor

 |
filters

 | Object

 | 否

 | 过滤条件，取值见【3. 过滤条件】

 |
注：

1）time_range 的跨度不能超过 31 天。

2）一次请求只能查询一个日志范围（ domain）。

3）传入当前日志范围（domain）不支持的 filters 字段会返回参数错误。

4）分页按事件时间倒序。

请求示例：

//查询登录日志
{
  "domain": "login",
  "time_range": {
    "start": "2026-04-01T00:00:00.000Z",
    "end": "2026-04-13T23:59:59.000Z"
  },
  "event_types": [
    "auth.session.login"
  ],
  "filters": {
    "actor_ids": [
      "660000000000000000000010",
      "660000000000000000000011"
    ]
  },
  "limit": 100,
  "cursor": ""
}

//查询平台管理日志
{
  "domain": "platform",
  "time_range": {
    "start": "2026-04-01T00:00:00.000Z",
    "end": "2026-04-13T23:59:59.000Z"
  },
  "event_types": [
    "admin.member.invite",
    "admin.member.remove",
    "admin.dept.create",
    "api.key.create"
  ],
  "filters": {
    "actor_ids": [
      "660000000000000000000020",
      "660000000000000000000021"
    ]
  },
  "limit": 100,
  "cursor": ""
}

//查询应用搭建日志
{
  "domain": "app_builder",
  "time_range": {
    "start": "2026-04-01T00:00:00.000Z",
    "end": "2026-04-13T23:59:59.000Z"
  },
  "event_types": [
    "data.record.create",
    "data.record.update",
    "data.record.batch_update",
    "data.record.delete",
    "data.record.import",
    "data.record.export",
    "admin.form.update",
    "admin.dash.export"
  ],
  "filters": {
    "actor_ids": [
      "660000000000000000000030",
      "660000000000000000000031"
    ],
    "app_ids": [
      "59264073a2a60c0c08e20bfb"
    ],
    "entry_ids": [
      "59264073a2a60c0c08e20bfd"
    ]
  },
  "limit": 100,
  "cursor": ""
}

//查询知识库日志
{
  "domain": "kms",
  "time_range": {
    "start": "2026-04-01T00:00:00.000Z",
    "end": "2026-04-13T23:59:59.000Z"
  },
  "event_types": [
    "admin.kms.enable",
    "admin.kms.space_create",
    "admin.kms.space_update",
    "admin.kms.perm_group_update"
  ],
  "filters": {
    "actor_ids": [
      "660000000000000000000040",
      "660000000000000000000041"
    ]
  },
  "limit": 100,
  "cursor": ""
}

响应参数：

参数

 | 含义

 |
has_more

 | 是否有下一页

 |
cursor

 | 下一页游标

has_more 为 true 时返回

 |
items

 | 审计日志列表

 |
items[].event_id

 | 事件 ID

 |
items[].event_time

 | 事件发生时间，UTC 时间字符串

 |
items[].event_type

 | 标准事件类型

 |
items[].domain

 | 审计日志范围

 |
items[].tenant

 | 企业的租户 ID

 |
items[].actor

 | 操作人信息

type：操作人类型，一般为 user
id：操作人 ID
name：操作人名称
ip：操作客户端i p 地址
user_agent：客户端用户代理信息
geo：地理位置，仅在日志范围是 login 时有值
 |
items[].event

 | 事件属性

category：事件分类
action：执行动作
outcome：执行结果
severity：严重等级
 |
items[].resource

 | 被操作资源信息

type：被操作资源类型
id：被操作资源 id
name：被操作资源名称
parent_id：被操作资源所属父资源 id
parent_type：被操作所属父资源类型
 |
items[].detail

 | 事件详情

 |
响应示例：

{
  "has_more": true,
  "cursor": "MTc3NjE1OTAwMDAwMCw2NjExMjIzMzQ0NTU2Njc3ODg5OWFhYmI=",
  "items": [
    {
      "event_id": "681f2de2-9722-34ca-bd2a-dda99b615e46",
      "event_time": "2026-05-11T09:09:38.792Z",
      "event_type": "data.record.print",
      "domain": "app_builder",
      "tenant": {
        "id": "68665cf9f8acef49b8e29917"
      },
      "actor": {
        "type": "user",
        "id": "68665cf9f8acef49b8e29917",
        "name": "z3",
        "ip": "172.24.72.2",
        "user_agent": "Mozilla/5.0",
        "geo": null
      },
      "event": {
        "category": "data",
        "action": "print",
        "outcome": "success",
        "severity": "info"
      },
      "resource": {
        "type": "form",
        "id": "689d59d8d241955ee4908625",
        "name": "车辆信息基础表",
        "parent_id": "68994cb727cc65376feb985d",
        "parent_type": "app"
      },
      "detail": {
        "template": "data_print",
        "params": {
          "template_name": "系统模板",
          "data_label": "A",
          "link": "/dashboard/app/68994cb727cc65376feb985d/form/689d59d8d241955ee4908625/data/69c6297fbf7965a4d21e5ec2/qr_link"
        }
      }
    }
  ]
}

3. 过滤条件

日志范围（domain）

 | 支持的过滤字段

 | 说明

 |
login

 | actor_ids

 | 按操作人成员 ID 过滤

 |
platform

 | actor_ids

 |
app_builder

 | actor_ids
app_ids
entry_ids
 | 按操作人成员 ID、应用 ID、表单/仪表盘 ID、操作对象过滤

 |
kms

 | actor_ids

 | 按操作人成员 ID 过滤

 |
过滤字段说明：

参数

 | 类型

 | 说明

 |
filters.actor_ids

 | String[]

 | 操作人成员 ID 列表

 |
filters.app_ids

 | String[]

 | 应用 ID 列表，仅日志范围为应用管理时支持

 |
filters.entry_ids

 | String[]

 | 表单、仪表盘等 ID 列表，仅当日志范围为应用管理（app_builder）时支持

 |
