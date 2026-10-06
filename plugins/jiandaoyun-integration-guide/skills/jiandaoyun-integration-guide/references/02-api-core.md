# API 对接基础：密钥、鉴权、调试、错误码

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 密钥管理

- 官方文档：https://hc.jiandaoyun.com/open/13038

1. 简介

1.1 功能简介

密钥管理 包括 API Key 的管理以及其他第三方授权的管理。

1.2 应用场景

配置部分需要调用 API 功能的插件时，可在密钥管理处获得对应的 API Key；
与其他平台对接数据获取简道云授权时，可在密钥管理处查看第三方授权关系，并可按需解除授权。
2. 设置步骤

2.1 管理入口

从工作台进入开放平台后，可看到 密钥管理 界面。如下图所示：

2.2 API Key

API Key 即 API 密钥，是赋予某种形式的秘密令牌的名称，与 Web 服务（或类似的）请求一起提交以识别请求的来源。密钥可以包含在请求内容的某个摘要中，以进一步验证来源并防止篡改这些值。详情可参见文档：API Key。

2.3 API调用日志

API 调用日志，是指记录接口调用 API key 时的相关操作日志。日志中包含了调用 API Key 的接口名称、调用时间、API Key 名称、IP 地址以及返回状态等内容。详情可参见文档：API 调用日志。

2.4 第三方授权

第三方授权中展示了简道云同其他第三方平台授权对接的明细，在这里可以对授权的平台进行解绑。详情可参见文档：第三方授权。


---

## API Key

- 官方文档：https://hc.jiandaoyun.com/open/16782

1. 简介

1.1 功能简介

API Key，即 API 密钥，是赋予某种形式的秘密令牌的名称，与 Web 服务（或类似的）请求一起提交以识别请求的来源。密钥可以包含在请求内容的某个摘要中，以进一步验证来源并防止篡改这些值。

1.2 使用场景

如在配置前端事件调用部分插件时，需要开启 API 功能后，才能成功配置使用插件。

1.3 预期效果

以天聚数行插件配置中，需要配置简道云 API 后才能开启插件为例。如下所示：

2. 设置步骤

2.1 设置入口

在「开放平台 >> 密钥管理」处，选择「API Key」，即可对 API Key 进行创建、设置等操作。

2.2 创建API

1）点击「创建API Key」，设置好 API Key 的名称、应用/接口授权范围后，即可创建出一条 API Key。如下所示：

注：

1）一个账户最多创建 500 个 API Key。

2）系统自动生成的 API Key 数据不可修改。

2）API Key 默认隐藏不显示，点击旁边的小眼睛图标即可显示 API Key 全部内容。

2.3 修改API名称

API Key 生成后，点击生成的 API Key所在行，进入 API Key 信息详情页面，在「名称」处，可以修改 API 名称，以便区分多个 API。

2.4 授权范围

点击 API Key 所在行，进入 API Key 信息详情页面，可对「应用授权范围」和「接口授权范围」进行设置。如下所示：

2.4.1 应用授权范围

应用授权范围支持「全部应用」和「部分应用」两种范围：

若选择「全部应用」，则简道云工作台中所有应用都可使用该API Key；
若选择「部分应用」，则仅添加进应用列表中的应用可以使用该 API Key。

2.4.2 接口授权范围

接口授权范围支持「全部接口」和「部分接口」两种范围：

若选择「全部接口」，则简道云中所有接口都可使用该API Key。包括通讯录接口、应用接口、表单接口、数据接口、文件接口、流程接口和 CRM 接口。
若选择「部分接口」，则仅添加进接口列表中的接口可以使用该 API Key。

2.5 IP 白名单

设置 IP 白名单后，只有来自白名单范围内的IP地址的请求才会被正常处理，不在白名单内的 IP 地址的请求不会成功。

点击 API Key 所在行，进入 API Key 信息详情页面，在「IP 白名单」处，点击「添加 IP」。如下所示：

在 IP 白名单内，支持设置单个 IP 地址或 IP 地址段。设置 IP 地址段时仅支持带一个 * 号通配符的 IP 格式。如下所示：

注：

1）若未设置任何白名单，则任何 IP 均可使用对应的 API Key。

2）若未设置任何白名单的情况下，所有插件都可调用该 API Key；若已设置了白名单时，所有插件都不可调用该 API Key。

3）不对企业内所有 IP 总数量设置上限，而是对每个 API Key 内的白名单IP数量设置上限。每个 API Key 内的白名单 IP 数量上限为 50 个。

4）IP 白名单内，暂不支持 IPV6 地址。

2.6 停用/启用

在「状态」处，通过关闭/开启状态开关，对于已经创建的密钥可以进行停用，停用的密钥也可以重新开启使用。

2.7 复制

2.7.1 复制密钥值

在 API Key 的密钥值处，点击复制图标，即可快捷复制密钥值后并进行应用。如下所示：

2.7.2 复制整条API Key

在 API Key 的操作处，点击复制图标，即可复制整条 API Key。复制后，API Key 的授权范围和 IP 白名单会同步复制，但复制后的 API Key 会生成新的密钥值。如下所示：

2.8 删除

对于不需要使用的 API Key 可以进行删除。由于API Key 的重要性，也可以通过删除再新建的方式进行 API Key 的定期更换。

注：删除前请确认该 API Key 没有被使用。


---

## API调用日志

- 官方文档：https://hc.jiandaoyun.com/open/16725

1. 简介

1.1 功能简介

API 调用日志，是指记录接口调用 API key 时的相关操作日志。日志中包含了调用 API Key 的接口名称、调用时间、API Key 名称、IP 地址以及返回状态等内容。

1.2 使用场景

当 API 调用失败时，可以通过 API 调用日志排查失败的具体原因，从而优化接口调用设置，提高开发效率。

1.3 预期效果

以查看全部 API 调用日志为例，效果如下所示：

2. 操作步骤

2.1 查询入口

在「开放平台>>密钥管理 >> API 调用日志」处，即可对API的相关调用操作进行查询。如下所示：

2.2 日志筛选

API 调用日志可根据以下条件进行筛选：

接口名称；
API Key 名称；
调用时间。

2.3 日志信息

日志信息包含了调用 API 的接口名称、调用时间、API Key 名称、IP 地址以及返回状态等内容。设置好对应的筛选条件后，即可根据筛选条件查询对应的 API 调用日志信息。

以查询「用户表单查询接口」的API调用日志为例，效果如下所示：

2.4 返回状态

返回状态分为成功和失败两种状态。

当返回状态为失败时，在返回状态处可以同步查看失败原因。更多错误信息可参见文档：开发指南【6.2 错误码】。

注：除上述开发指南【6.2 错误码】中描述外，其他返回失败情况暂无具体失败原因。

3. 注意事项

1）API 调用日志中仅保留近 7 天的操作日志。

2）当密钥名称发生修改时，API 调用日志内历史日志中的密钥名称不会同步修改。


---

## 开发指南

- 官方文档：https://hc.jiandaoyun.com/open/11261

1. 简介

简道云的 API 接口包含以下接口：

应用接口
表单&数据接口
文件接口
流程接口
通讯录接口
注：

1）v4 版本及以前的接口文档点击这里：点击查阅。

2）从 v6 版本开始，开放 API 在保证兼容性的情况下，简道云可能会增加（不会减少）相应的出入参数，请开发者考虑参数增加的情况，保证代码的稳定性。如 v6 版本部门接口的更新，添加了seq的入参以及出参，其实不影响 v5 版本的相关逻辑，后续类似处理不会再增加版本。

2. 规则

API 的统一访问地址为：https://api.jiandaoyun.com/api（非直接访问 URL，结合后文 appid 等一起访问）
所有 API 请求都必须通过 HTTPS 进行身份验证和发起
统一采用 POST 请求的形式
数据传输编码为 UTF-8
文件上传接口为 form_data 格式，其他均为 JSON 格式
3. 频率限制

全局最多接受请求：50 次/秒

各个接口的请求频率限制参见各个接口的接口文档：

应用接口
表单&数据接口
文件接口
流程接口
通讯录接口
4. 鉴权方式

简道云使用基于简单令牌的身份验证 ，API KEY 默认未生成，需要点击创建 API KEY 去生成。

生成方式：「开放平台>>密钥管理>>创建 API KEY」；一个企业最多生成 500 个 API KEY。

对于已创建的 API KEY 还可以进行启用、停用和删除。

开发文档中的 参数说明 是专门根据当前表单的配置生成的，可以点开查看详细的说明。也可在参数说明点击 API 调试台 进行接口的查看和调试。

通过 HTTP Headers 设置 Authorization 的值为"Bearer YOUR_APIKEY"来进行安全性验证，

示例如下：

$ curl -i https://jiandaoyun.com/api/v1/callback \
  -H "Authorization: Bearer YOUR_APIKEY"

5. 代码示例

我们为开发者提供了一些不同语言版本的代码样例，仅供参考：

python
C#
go
java
node
6. 错误对照表

所有 API 使用状态码+错误码的响应方式来表示错误原因。接口正确统一返回HTTP 状态码为 2xx 的正确响应。接口错误则统一返回 HTTP 状态码为 400 的错误响应，同时响应内容会返回错误码（code）和错误信息（msg）

HTTP/1.1 400
Content-Type: application/json
{
  "code": 8303,
  "msg": "超出请求频率限制"
}

6.1 状态码

状态返回码对照表如下：

状态返回码

 | 说明

 |
2xx

 | 响应成功

 |
400

 | 接口错误统一返回

 |
429

 | 超出请求并发限制

 |
502

 | 网关异常

 |
579

 | 文件上传失败

 |
6.2 错误码

当状态返回码为 400 时，服务器会返回具体的错误码（code）和错误信息（msg），对照表如下：

错误码

 | 说明

 | 排查建议

 |
1

 | The request is invalid.

 | 错误的请求，检查参数是否缺失。

 |
1005

 | The email already exists.

 | 邮箱已存在，可尝试邮箱验证码登录确认是否已注册。

 |
1010

 | The member doesn't exist.

 | 用户不存在，检查成员参数是否正确传入。

 |
1017

 | The username is in an invalid format.

 | 用户名不符合格式要求，常规格式为字母数字下划线任意组合，长度50个字符以内。

 |
1018

 | The email is in an invalid format.

 | 用户邮箱不符合格式要求，检查邮件地址。

 |
1019

 | The member's nickname is in an invalid format.

 | 用户昵称不符合格式要求，检查是否长度在80个字符以下且无特殊字符。

 |
1022

 | The member's current company/team doesn't exist.

 | 用户团队不存在，稍后重试，仍然出现可以咨询 技术支持。

 |
1024

 | The mobile number is invalid. Enter a new number and try again.

 | 手机号码不正确，请重新输入手机号。

 |
1027

 | The phone number already exists.

 | 手机号码已存在，使用手机号验证码登录确认是否已注册。

 |
1058

 | Do not have permission to call the task list.

 | 用户操作权限不足。

 |
1065

 | The member has already been added to the team.

 | 当前用户已加入团队，检查当前团队内是否已经有当前用户。

 |
1082

 | The phone number/email is required.

 | 手机号和邮箱不能同时为空。

 |
1085

 | The member's nickname is required.

 | 昵称不能为空。

 |
1087

 | Duplicate unique fields.

 | 唯一性字段重复，检查成员 ID 的重复情况。

 |
1092

 | The length of the username has exceeded the limit.

 | 工号长度超出限制，确认工号长度在 50 个字符以内。

 |
1096

 | The request contains invalid member parameter(s).

 | 用户参数不合法，请检查后重试。

 |
1201

 | The role doesn't exist.

 | 企业角色信息不存在，检查参数后重试。

 |
1202

 | Unable to operate synchronized role or role groups

 | 无法操作同步的角色/角色组，确认当前角色/角色组非其他平台同步而来。

 |
1203

 | The role group/role information is invalid.

 | 角色/角色组信息不合法，检查参数后重试。

 |
1205

 | The role group is required.

 | 必须指定角色组，检查参数后重试。

 |
1206

 | The role group doesn't exist.

 | 指定的角色组不存在，检查参数后重试。

 |
1207

 | The length of the role group name has exceeded the limit.

 | 角色/角色组名称长度超限，确保长度在 24 个字符以内。

 |
1208

 | Can't delete a role group with member(s).

 | 非空角色组不能删除，确保删除角色组下角色后重试。

 |
2004

 | The app doesn't exist.

 | 应用不存在，检查参数后重试。

 |
3000

 | The form doesn't exist.

 | 表单不存在，检查参数后重试。

 |
3001

 | The member or department name is required.

 | 名称不能为空。

 |
3005

 | The request contains invalid parameter(s).

 | 参数不正确。

 |
3041

 | The number of Serial No. fields has exceeded the limit in the form.

 | 单个表单流水号控件数量超出上限，有且只能有一个。

 |
3042

 | Failed to verify the field alias.

 | 字段别名校验失败，检查别名是否含有特殊字符，常规格式为字母数字下划线任意组合。

 |
3083

 | The number of widgets has exceeded the limit in the form.

 | 控件数量超过上限，一般情况下这个值为 500。

 |
3091

 | The number of characters in the form name exceeds 100.

 | 表单名称不能超过 100 个字符。

 |
3092

 | The number of characters in the title exceeds 100.

 | 标题不能超过 100 个字符。

 |
4000

 | Failed to submit data.

 | 数据提交失败。

 |
4001

 | Data doesn‘t exist.

 | 数据不存在。

 |
4007

 | No approver for the workflow.

 | 操作失败，没有流程处理人。

 |
4008

 | The workflow was closed.

 | 操作失败，流程已经关闭。

 |
4009

 | Do not have permission to approve.

 | 操作失败，无权限。

 |
4012

 | Operation failed. This form is being used in other batch editing tasks. Try again later.

 | 操作失败，当前表单正在执行其他批量编辑任务，请稍后重试。

 |
4015

 | The approver of the transferred node is invalid.

 | 操作失败，当前节点不存在该候选人。

 |
4016

 | The workflow can't be transferred to oneself.

 | 操作失败，流程不能转交给自己。

 |
4025

 | Do not have permission for the workflow.

 | 您没有数据流程权限。

 |
4042

 | Failed to delete the data.

 | 数据删除失败，检查参数后重试。

 |
4402

 | Failed to validate the aggregation calculation.

 | 聚合计算校验失败，检查参数后重试。

 |
4815

 | The filter condition is invalid.

 | 过滤条件设置有误，可能是过滤条件过于冗长导致，可咨询 技术支持。

 |
5003

 | The workflow node doesn't exist.

 | 流程节点不存在。

 |
5004

 | No comment for approval.

 | 未提交流程审批意见。

 |
5009

 | The approver of the returned node is invalid.

 | 找不到回退后的负责人。

 |
5011

 | The target node is invalid.

 | 找不到流转节点。

 |
5012

 | No signature for approval.

 | 未提交流程手写签名。

 |
5034

 | This node has child workflow(s)/plugin node(s).

 | 目标节点包含子流程/插件节点。

 |
5044

 | The child workflow is wrongly configured. For example, no initiator for the child workflow.

 | 子流程配置错误或找不到发起人。

 |
5045

 | The number of child workflow exceeds 200.

 | 发起子流程数据超过上限 200。

 |
5049

 | The Transfer feature hasn't been enabled at this node.

 | 当前流程节点未开启转交。

 |
5053

 | The initial department is invalid. Can't flow to the node with multi-level approval.

 | 流入多级主管审批节点失败，未指定发起部门。

 |
6000

 | There is a sub-department with the same name within the same-level department.

 | 已存在同名部门，检查同级的父部门下所有子部门，排查同名情况。

 |
6001

 | The parent department doesn't exist.

 | 父部门不存在。

 |
6002

 | The department doesn't exist.

 | 部门不存在，检查参数后重试。

 |
6003

 | Can't delete a department with sub-department(s).

 | 存在子部门，不能删除。

 |
6004

 | Failed to update the department.

 | 部门修改失败。

 |
6005

 | Failed to create the department.

 | 部门创建失败，稍后重试，仍然出现可以咨询 技术支持。

 |
6006

 | Can't delete a department with member(s).

 | 部门内存在成员，不能删除。

 |
6010

 | The department ID is in an invalid format.

 | 部门编号不在合法范围内，结合自身部门路径以及父部门，检查参数后重试。

 |
6011

 | There is a circular relationship among departments.

 | 部门关系存在循环，不允许的部门树关系，检查参数后重试。

 |
6012

 | The department name is invalid.

 | 部门名称不合法，检查参数后重试。

 |
6013

 | The department ID already exists.

 | 部门编号重复，检查同级的父部门下所有子部门，排查编号重复情况。

 |
6014

 | There must be at least one sub-department belonging to the root department.

 | 至少需要一个子部门属于根部门。

 |
6015

 | Can't delete a root department.

 | 根部门不能被删除。

 |
6017

 | The number of cascade levels in the department exceeds the limit.

 | 部门级联层数超出限制，部门树深度限制为 16。

 |
6019

 | The member list is required.

 | 成员列表不能为空，检查参数后重试。

 |
6020

 | The number of departments in a single import exceeds the limit.

 | 单次导入部门数量超出限制，上限为 10w。

 |
6021

 | The number of members in a single import exceeds the limit.

 | 单次导入成员数量超出限制，上限为 2w。

 |
6064

 | The parent department already exists.

 | 已是目标部门的子部门。

 |
7103

 | System usage exceeds the limit. The system has been suspended. Go to Management > Plan Details to view the usage details and upgrade plan to restore the system.

 | 系统用量超出限制，系统已暂停使用。您可以至「企业管理-版本信息」查看版本使用详情和升级版本以恢复系统。

 |
7206

 | System limit exceeded.The system has been disabled.Contact the link creator to upgrade the plan or reduce the usage.

 | 系统用量超出限制，系统已暂停使用，请尽快联系贵司简道云管理者升级版本以恢复系统。

 |
7212

 | Monthly data exceeds the limit. Can't submit new data. Contact the business owner to upgrade the plan.

 | 该账号的本月数据流量已用完，无法提交新数据，请联系账号创建者升级版本。

 |
7216

 | Attachment upload limit exceeded. Contact the link creator to enable cloud coin payment

 | 附件上传量超过当前版本限制，请联系链接发布者开启云币支付。

 |
7217

 | Attachment upload limit exceeded. Contact the business owner to enable cloud coin payment.

 | 附件上传量超过当前版本限制，请联系企业创建者开启云币支付。

 |
7218

 | Attachment upload limit exceeded. Contact the link creator to purchase more cloud coins.

 | 附件上传量超过当前版本限制，请联系链接发布者充值云币。

 |
7219

 | Attachment upload limit exceeded. Contact the business owner to purchase more cloud coins.

 | 附件上传量超过当前版本限制，请联系企业创建者充值云币。

 |
7221

 | This form has exceeded the limit and is temporarily suspended. Please contact the company creator or system administrator

 |  API 新增数据超出当前版本限制，请联系企业创建者或系统管理员。

 |
8017

 | Company/Team doesn't exist or has been closed.

 | 企业不存在或者已经被解散，检查参数后重试。

 |
8301

 | Failed to verify the API key for authorization.

 | API 签名校验失败，检查参数后重试。

 |
8302

 | Do not have permission for the API calls.

 | 没有接口请求权限，检查参数后重试。

 |
8303

 | The call frequency of the company/team exceeds the frequency limit.

 | 企业 API 请求次数达到频率上限，可等待 1s 后重试，频繁发生可以排查一下企业 API 请求占用情况，或者添加频率限制。

 |
8304

 | The call frequency exceeds the frequency limit.

 | 当前接口请求次数达到频率上限，可等待 1s 后重试当前接口，频繁发生可以添加频率限制。

 |
9004

 | Failed to create the task.

 | 队列任务创建失败，稍后重试，仍然出现可以咨询 技术支持。

 |
9007

 | Failed to obtain the lock.

 | 锁获取失败，稍后重试，仍然出现可以咨询 技术支持。

 |
17017

 | The request contains invalid parameter(s).

 | 平台 API 的参数异常，检查参数后重试。

 |
17018

 | The API key is invalid.

 | 无效的 API Key。

 |
17023

 | The batch update at one time exceeds the limit.

 | 单次批量修改数量超出限制，上限为 100。

 |
17024

 | The batch creation at one time exceeds the limit.

 | 单次批量创建数量超出限制，上限为 100。

 |
17025

 | The transaction_id contains invalid parameter(s).

 | transaction_id 参数格式不正确。

 |
17026

 | The transaction_id already exists.

 | transaction_id 重复，请修改后重试。

 |
17027

 | Failed to upload the API file.

 | API文件上传失败，稍后重试，仍然出现可以咨询 技术支持。

 |
17032

 | The field type isn't supported.

 | 不支持的字段类型，检查参数后重试。

 |
17033

 | The limit for batch deletion quantity has been exceeded

 | 批量删除数据超出数量限制，请调整数量后重试。

 |
17034

 | The sub-field type isn't supported.

 | 不支持的子表单字段类型，检查参数后重试。

 |
17052

 | Not included in the IP whitelist.

 | 不在 IP 白名单内，检查对应API Key相关配置。

 |
17053

 | Not among the authorized apps.

 | 不在应用授权范围内，检查对应API Key相关配置。

 |
17054

 | Not among the authorized APIs.

 | 不在接口授权范围内，检查对应API Key相关配置。

 |
30002

 | Unable to retrieve the pre-set CRM form now.

 | CRM 预设表单暂不支持调用

 |
50000

 | The target node doesn't exist.

 | 目标节点不存在

 |
50004

 | The task doesn't exist.

 | 待办任务不存在

 |
50008

 | Workflow processing error.

 | 流转异常，稍后重试，仍然出现可以咨询 技术支持。

 |
50011

 | The task doesn't exist.

 | 执行实例不存在。

 |
50014

 | No permission to close the task.

 | 操作人不能为空。

 |
50016

 | The instance_id is invalid.

 | 流程实例不存在。

 |
50019

 | The action is not supported.

 | 不支持的审批行为，检查参数后重试。

 |
50021

 | The data_id is invalid.

 | 关联业务对象不存在。

 |
50031

 | The data_id is invalid.

 | 流程数据不存在。

 |
50040

 | This node can't be returned.

 | 当前节点禁止回退，检查节点配置并确认节点未在执行。

 |
50041

 | Can't return to the current node.

 | 回退节点为当前节点。

 |
50047

 | Workflow being migrated. Try again later.

 | 流程迁移中，请稍后再试。

 |
50049

 | Can't return to the Start Node without an initiator.

 | 不允许回退到没有创建者的发起节点。

 |
50051

 | The workflow has been approved/transferred/returned.

 | 流程已被处理，请刷新后查看。

 |
50053

 | No approver to add.

 | 加签候选人列表不能为空，检查参数后重试。

 |
50054

 | Can't add nested approval. For example, after approver A has added approver B, approver B can't add approver C.

 | 不支持嵌套加签，检查参数后重试。

 |
50055

 | No pre-approver or post-approver was added.

 | 仅支持前后加签任务处理，检查参数后重试。

 |
50056

 | The parent task is lost. For example, approver A has added approver B. After approver B had approved the assigned task, the initial task for approver A was lost.

 | 加签父任务丢失，可能已经被处理，检查参数后重试。

 |
50057

 | The Add Approver feature hasn't been enabled.

 | 加签配置未开启。

 |
50059

 | The member has been added as an approver.

 | 加签候选人不能选择节点负责人。

 |
50060

 | The approver is invalid.

 | 加签候选人非法。

 |
50061

 | Can't add more than one approver.

 | 不支持多人加签。。

 |
50062

 | The added approver is reviewing the task.

 | 待被加签人处理中

 |
50070

 | Can't return to the plugin node.

 | 不允许回退到插件节点。

 |
50073

 | Can't return to the in-progress node.

 | 禁止回退到进行中节点。

 |
50082

 | The choice of back type is missing.

 | 缺少回退人选择

 |


---

## 参数说明

- 官方文档：https://hc.jiandaoyun.com/open/18556

1. 简介

1.1 功能简介

在参数说明文档中，通过切换应用及表单可以快速查询接口调试所需要的参数。同时为开发人员提供一体式的文档、调试、代码示例生成功能，以支撑高效的开发与查阅。

1.2 使用说明

适用于有一定开发能力的企业，能够通过接口自定义开发内容，进行简道云平台对接等。

1.3 预期效果

以在参数说明界面，查看产品管理系统中的表单及字段信息为例，效果如下所示：

2. 操作步骤

2.1 操作入口

进入「开放平台 >> 开发文档」中，点击「参数说明」即可进入到参数说明详情页中。

2.2 应用切换

进入参数说明详情页后，在左上角「应用切换」处，可通过下拉框选择不同的应用。

2.3 表单信息查看

1）选择好应用之后，在左侧表单列表中选择好表单之后，即可查看到表单的相关信息。如表单所属的应用ID、表单ID、字段名称、字段ID、字段类型等。

2）若表单内的字段过多，还可通过右上角的搜索框，搜索出字段名称后进行字段信息的查看。如下所示：

2.4 API调试台

在 API 调试平台中，选择需要调试的接口，并输入相应的 API 密钥及请求参数即可进行调试。详情可参见文档：API 调试台。

2.5 设置字段别名

点击「设置字段别名」，可以对表单内的字段设置字段别名。

注：字段别名仅允许使用「小写字母」「数字」和「下划线」组合，且必须以「小写字母」开头。

2.6 字段JSON样例

点击「字段 JSON 样例」，可以查看表单内字段的 JSON 代码。企业可根据自身需求，复制 JSON 代码进行接口调试。​


---

## API调试台

- 官方文档：https://hc.jiandaoyun.com/open/18557

1. 简介

1.1 功能简介

API 调试台 是指，开发者在调试台中选择需要调试的接口，并输入相应的 API 密钥及请求参数即可进行调试。能够降低开发者的开发成本，让开发者可以快速上手、完成开发。

1.2 使用场景

适用于开发人员在开发过程中，根据接口信息发送请求、查看响应和调整参数。如：

使用调试台测试 API 的不同端点和功能，确保 API 按照预期工作，参数被正确传递，且响应符合预期；
开发者可以轻松调整请求参数，以查看不同输入对 API 的影响，以便找到最佳配置；
查看详细的错误信息，有助于快速定位和解决问题。
1.3 预期效果

以「获取成员信息」接口调试为例，效果如下所示：

2. 操作步骤

2.1 操作入口

1）参数说明处入口

通过「参数说明 >> API 调试台」处，可以进入 API 调试平台直接进行接口调试：

2）接口文档内入口

除了参数说明文档中可以进入到 API 调试平台，帮助文档对应的接口文档也可以直接进入到 API 调试平台，如下图所示：

3）链接访问

点击链接：API 调试台，即可进入到 API 调试平台，进行调试。

2.2 选择接口

在左侧「API 列表」中，选择需要进行调试的接口。如选择「获取成员信息」接口，如下所示：

2.3 设置请求头

选择接口后，设置如下所示内容：

Authorization：设置为简道云的 API Key，可在「开放平台 >> 密钥管理」处创建并复制 API Key。
服务地址：接口调用的服务地址。

2.4 设置请求体

在请求体中修改必填参数，以便对接口进行调试。如在「获取成员信息」接口当中，需将参数 username 替换为简道云企业内要查询的成员编号，如下所示：

2.5 查看调试结果

1）请求头和请求体都设置完成后，点击「开始调试」，即可查看调试结果。如下所示：

2）API 调试台还会根据开发者输入的请求参数实时生成多语言调用示例，开发者可以一键拷贝示例代码，复用到自己的业务代码中，从而提高开发效率。

3）若调用失败，可以直接查看帮助文档和错误码等信息来快速定位和分析问题，从而降低开发成本。以查看错误码为例，效果如下所示：

2.6 效果演示

效果参见本文【1.3 预期效果】。


---

## 第三方授权

- 官方文档：https://hc.jiandaoyun.com/open/16827

1. 简介

1.1 功能简介

第三方授权中展示了简道云同其他第三方平台授权对接的明细，在这里可以对授权的平台进行解绑。

1.2 使用场景

如在与九数云对接过程中，需要得到简道云的授权信息。此时授权成功后，可在简道云的第三方授权处，查看授权明细。能够管理简道云与第三方平台的授权关系，提高业务管理的规范性，保证了企业数据安全。

1.3 预期效果

以 九数云 授权为例，授权成功后，在简道云「开放平台 >> 密钥管理 >> 第三方授权」处，显示授权信息。如下所示：

2. 设置步骤

2.1 进行授权

目前简道云完成了同 九数云 这款零代码云端数据分析产品的对接，对接方式参考文档：导入简道云数据源。

经九数云分析后的数据，还可以将分析结果回填至简道云：自动化-数据回填。

授权完成后，在简道云「开放平台 >> 密钥管理 >> 第三方授权」处，显示九数云相关授权信息。如下所示：

2.2 解除授权

若确认无需与第三方平台继续对接，可解除第三方平台的授权。解除授权后第三方平台将无法继续同步简道云中的数据。

在「操作」处，点击「解除授权」，即可解除授权。如下所示：

2.3 操作日志

在 企业日志 中可以查询解除授权和授权的操作日志。

2.4 系统通知

在消息管理的系统日志中，可以查询有关授权/解绑的系统通知。
