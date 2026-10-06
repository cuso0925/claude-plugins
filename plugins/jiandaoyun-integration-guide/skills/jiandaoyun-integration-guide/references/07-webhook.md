# Webhook 数据推送

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 数据推送

- 官方文档：https://hc.jiandaoyun.com/open/11500

1. 简介

1.1 功能简介

数据推送（Webhook）是一种由开发人员自定义的回调机制，俗称“钩子”。它允许开发者通过配置自定义回调地址的方式，将 Web 应用中发生的特定事件实时推送至指定的服务器或 URL，从而实现跨平台、跨系统的数据联动与消息通知。

在简道云中，当表单数据或结构发生变更，亦或是流程状态与待办事项发生变化时，系统便会自动将相关操作及变更后的数据推送至您预先配置好的服务器地址。这些回调函数无需由 Web 应用官方维护，第三方开发人员同样可以对其进行自定义与管理，极大地提升了系统集成的灵活性。

1.2 使用场景

数据推送广泛适用于需要实时响应、自动触发、跨系统协作等场景中，如：

系统集成：将简道云与第三方系统（ERP、OA 等）打通，实现数据自动同步，无需人工手动导入导出；
消息通知：当表单中数据发生变更或流程状态更新时，自动触发通知，将信息推送到第三方系统中；
数据实时同步：将简道云中的表单数据实时同步至企业自有数据库或其他业务系统，保证多端数据一致性。
1.3 版本说明

本功能为付费高级功能，需简道云企业版及以上版本可用。详情参见：官网定价。

2. 设置步骤

2.1 设置入口

选择要设置数据推送的表单，点击「编辑表单 >> 扩展功能 >> 数据推送」，即可新建数据推送。

2.2 设置字段别名

字段别名是为表单字段设置的另一个名称标识，常用在数据推送、发送 API 请求和返回响应数据时，使用字段别名来替换字段 ID。提升数据的可读性、简化开发工作。

点击「设置字段别名」，在字段别名处填写对应字段的别名即可。如下所示：

注：

1）字段别名仅允许使用「小写字母」、「数字」和「下划线」组合，且必须以「小写字母」开头。

2）不允许设置字段别名为「data_id」。

2.3 字段对照表及JSON样例

字段对照表及 JSON 样例分别包含数据、表单、流程事件中全部字段，以及每个字段对应的字段名称、字段 ID/别名、字段类型、说明。开发人员写代码时可参照「字段对照表及 JSON 样例」进行书写。

2.4 表单数据结构

表单数据结构是指简道云在通过 Webhook 或 API 向外部系统推送数据时，数据所呈现的组织形式与层级关系。它以 JSON 格式为载体，完整描述了一条表单记录的所有信息，包括表单的基础元数据（如表单 ID、操作类型、时间戳等）以及各字段的具体取值。

3. 申请试用

标准版不包含 API 及 Webhook 功能，企业版及以上的用户可直接体验该功能，无需额外开通。

点击申请试用 - API & Webhook（价格咨询 / 功能测试 / 售前支持）
点击在线咨询


---

## 开发指南

- 官方文档：https://hc.jiandaoyun.com/open/11507

1. 简介

本指南旨在帮助开发者在自有服务器上快速搭建 Webhook 消息接收服务，以便实时获取并处理简道云通过数据推送发出的表单数据。指南涵盖服务端接口的推送方式、签名验证和响应规则，并提供了代码示例。无论您使用何种开发语言或技术栈，均可参照本指南完成对接，实现简道云与自由系统之间的数据互通。

2. 开发步骤

2.1 推送方式

简道云目前仅支持 POST 请求，请求参数如下所示：

Header ：
Content-type：类型为 application/json；
X-JDY-DeliverId：推送事件 ID。每次推送的 ID 是唯一的。可以通过该字段完成请求的去重，防止重复接收同一个事件；
X-JDY-Signature：签名内容，使用方式可参考【2.3 签名验证】；
op：推送事件；
data：具体数据内容；
send_time：推送事件；仅进行消息推送时推送该参数。
代码示例如下所示：

POST http://example.com/jdy/hook?timestamp=1498586609&nonce=0f5ade
Headers: {
    "X-JDY-Signature": "72d3162e-cc78-11e3-81ab-4c9367dc0958",
    "X-JDY-DeliverId": "sha1=7d38cdd689735b008b3c702edd92eea23791c5f6"
}
{
    op: "data_create",
    data: {}
}

2.2 签名验证

为了防止 webhook 的接收服务器被第三方恶意攻击，用户在开发回调接口时，建议对回调请求进行签名校验，以确保回调请求来源来自于简道云。hook 会以 POST 的形式、将内容以 JSON 格式发送给指定地址。具体步骤如下所示：

1）在界面上随机生成一个 secret 或者自己指定一个 secret，并保存。这样，数据推送时就会把加密前的内容和通过secret加密后的内容一起推送到指定地址。

2）把 http 请求体字符串作为 payload，将其和 secret，请求参数里的 nonce、timestamp 按照 “{nonce}:{payload}:{secret}:{timestamp}” 的形式（用冒号分隔），组合为校验字符串 signature。

3）以 utf-8 编码形式计算 signature 的 sha-1 散列。

4）将 signature 散列的十六进制字符串与 POST 请求 header 中的 ‘X-JDY-Signature’ 做比较，若比较结果相同，则通过签名验证；若比较结果不同，则无法通过检查。

以 Python 为例，代码如下所示：

def get_signature(nonce, payload, secret, timestamp):
    content = ':'.join([nonce, payload, secret, timestamp]).encode('utf-8')
    m = hashlib.sha1()
    m.update(content)
    return m.hexdigest()

@app.route('/callback', methods=['POST'])
def callback():
    payload = request.data.decode('utf-8')
    nonce = request.args['nonce']
    timestamp = request.args['timestamp']
    if request.headers['x-jdy-signature'] != get_signature(nonce, payload, 'test-secret', timestamp):
        return 'fail', 401
    threading.Thread(target=handle, args=(json.loads(payload), )).start()
    return 'success'

2.3 响应规则

1）简道云向对应目标服务器推送请求后，该服务器需在 2 秒内使用 2xx 作为响应的状态码进行响应，即认为数据推送成功。

2）一次推送重试最多 5 次，如果单次推送连续重试 5 次均失败，则该次推送失败，此时会记录该数据在失败记录里，当连续失败达到 100 次时，该推送功能将被关闭，管理会获得消息通知，则需要管理员在推送设置中重新启动推送。

3. 代码示例

简道云为您提供了 Webhook server 多语言 调用示例，您可通过参考以下代码示例完成开发：

c#：示例代码
go：示例代码
java：示例代码
node：示例代码
php：示例代码
python：示例代码
ruby：示例代码
4. 注意事项

1）webhook推送错误说明

接收到推送后需要返回给简道云 2xx 表示推送接收成功。其他的返回结果则为返回信息错误，用户可以根据 HTTP 状态码自行定义推送错误的情况给简道云的返回码，简道云接受后，可在推送日志中显示出。

2）开发注意点

由于我们会对接口做各种扩展，为了保证每个对接的应用服务接收到更多样的推送数据时，不出现异常。所以请在接收到更多的 op 参数的数据类型时，直接响应成功，不要响应为失败。


---

## 数据事件推送

- 官方文档：https://hc.jiandaoyun.com/open/10732

1. 简介

1.1 功能简介

数据事件推送是指，当表单中的数据发生如下所示变更时，可将变更后的数据推送至对应的服务器中：

有新数据提交时；
有数据被修改时；
有数据被删除时；
有数据被恢复时。
1.2 使用场景

适用于需要将数据变更（新增、修改、删除或恢复）情况推送至企业所需服务器等场景中，以便及时获取最新、最准确的数据状态：

实时库存与订单管理：表单中的数据（地址、数量、订单状态等）发生变更时，立即推送到库存管理系统、物流系统、订单管理系统中；
动态销售线索管理与分配：客户信息实时推送到 crm 创建线索记录，自动推送新线索至服务器中；
实时数据看板与决策支持：将新增或变更的数据实时推送至 BI 工具或数据看板中，帮助企业实时监控业务动态，快速发现机会或问题，做出更及时的决策。
2. 操作步骤

2.1 新建数据推送

在「扩展功能 >> 数据推送」处，点击「新建数据推送」，在数据推送页面修改推送名称为「考勤数据推送」。

2.2 设置服务器

2.2.1 选择目标服务器

进入数据推送设置页面后，根据企业需求选择对应的目标服务器。系统支持选择自定义服务器推送，也支持选择 Finereport 服务器进行推送：

与 Finereport 对接选择 Finereport 服务器：FineReport 报表对接简道云插件；
与 FineBI 对接选择 Finereport 服务器：FineBI 报表对接简道云插件；
与九数云对接选择自定义服务器：同步数据源【7. 接受简道云实时推送】；

2.2.2 设置服务器地址

企业根据自身的企业需求，可填写指定的服务器地址，数据会以 HTTP POST 请求的形式，推送至目标服务器地址。

2.2.3 生成Secret

服务器地址填写完成后，点击「生成 Secret」，系统将自动生成对应的 Secret。

2.2.4 服务器连接测试

1）服务器地址确认无误及生成 Secret 后，点击「服务器连接测试」，系统将自动进行服务器连接测试，测试成功后，则显示「服务器连接成功」。

2）若服务器连接失败，也可查看错误详情，并根据错误详情进行调整后重新连接。

2.3 设置推送事件

进行数据事件推送设置时，企业可根据自身需求来勾选对应的数据推送事件，不同事件含义如下：

有新数据提交时：当表单中新增一条数据时推送；
有数据被修改时：当表单中数据被修改时推送；
有数据被删除时：当表单中数据被删除时推送；
有数据被恢复时：当表单中数据被恢复时推送。
全部设置完成后，点击「保存」。

注：批量修改、删除和恢复时不支持推送。导入数据不支持触发推送事件。

2.4 设置备注

若有多个数据推送，可在「备注」中填写推送说明，以区分不同的数据推送，便于识别和管理。

3. 注意事项

3.1 推送数据结构

数据事件推送时，数据结构定义如下：

参数

 | 说明

 |
op

 | 推送事件。包括 data_create(数据提交)、data_update(数据修改)、data_remove(数据删除)、data_recover(数据恢复)

 |
opTime

 | 推送事件触发时间戳，精确到毫秒

 |
data

 | 具体数据内容

 |
3.2 数据事件推送内容

可根据数据推送配置界面的「字段对照表及 JSON 样例」参考当前表单推送数据的格式及内容。

1）新数据提交/数据修改/数据恢复时

所属模块

 | 字段类型

 | 数据类型

 | 说明

 |
表单字段

 | 单行文本

 | string

 | ——

 |
多行文本

 | string

 |
流水号

 | string

 | 表单新增流水号控件时，历史数据无流水号

 |
数字

 | number

 | ——

 |
日期时间

 | string

 |
单选按钮组

 | string

 |
复选框组

 | array

 |
下拉框

 | string

 |
下拉复选框

 | array

 |
分割线

 |

 | 不推送

 |
地址

 | json

 | 格式为

{

    “province”: “江苏省”,

    “city”: “无锡市”,

    “district”: “梁溪区”,

    “detail”: “清扬路 138 号茂业天地”

}

如果选择了部分属性，则未选择的属性以空字符串补齐。如未选择区和地址详情时，格式为

{

    “province”: “江苏省”,

    “city”: “无锡市”,

    “district”: “”,

    “detail”: “”

}

 |
定位

 | json

 | 格式为

{

    “province”: “江苏省”,

    “city”: “无锡市”,

    “district”: “梁溪区”,

    “detail”: “清扬路 138 号茂业天地”,

    “lnglatXY”: [120.31237,31.49099]

}

省、市、区、地址详情属性中如果只输入了部分属性，则其中未输入属性以空字符串补齐 (API 接口推送数据时可以仅输入部分属性)

 |
图片

 | array

 | 推送数据中包含的url为图片链接，15 天内有效

 |
附件

 | array

 | 推送数据中包含的url为附件链接，15 天内有效

 |
手写签名

 | json

 | 推送数据中包含的url为手写签名的图片链接，15 天内有效

 |
子表单

 | array

 | ——

 |
查询

 |

 | 不推送

 |
关联数据

 | json

 | ——

 |
计算

 | number/string

 |
成员单选

 | json

 | status 对应的逻辑:

-1 离职
0 未加入
1 已加入
 |
成员多选

 | array

 | status 对应的逻辑:

-1 离职
0 未加入
1 已加入
 |
部门单选

 | json

 | ——

 |
部门多选

 | array

 |
手机

 | json

 | 格式为

{

    “phone”:“15852540044”,

    “verified”:false

}

 |
流程状态(仅流程表单)

 | number

 | 2 表示流程手动结束
1 表示流程已完成
0 表示流程进行中
 |
表单名称

 | string

 | ——

 |
数据id

 | string

 |
提交人

 | json

 | status 对应的逻辑:

-1 离职
0 未加入
1 已加入
 |
修改人

 | json

 | status 对应的逻辑:

-1 离职
0 未加入
1 已加入
 |
删除人

 | json

 | status 对应的逻辑:

-1 离职
0 未加入
1 已加入
 |
提交时间

 | string

 | 使用 utc 时间戳，请根据所在时区处理

 |
修改时间

 | string

 | 使用 utc 时间戳，请根据所在时区处理

 |
删除时间

 | string

 | 使用 utc 时间戳，请根据所在时区处理

 |
微信OpenID

 | string

 | ——

 |
用户昵称

 | string

 |
用户性别

 | string

 |
CRM 特殊字段

 | 客户名称

 | string

 | ——

 |
线索池

 | json

 |
所属公海

 | json

 |
销售阶段

 | json

 |
联系人

 | string

 |
跟进主体

 | json

 |
跟进商机

 | json

 |
注：字符串类型数据为空时可能为 null 或空字符串， json 格式数据为空时可能为 null 或空 json。在解析数据时，将 null、空字符串、空 json 均作为控件空值处理。

2）数据删除时

字段

 | 数据类型

 | 说明

 |
formName

 | String

 | 表单名称

 |
_id

 | String

 | 删除数据的 ID

 |
deleter

 | json

 | 删除操作执行人

 |
deleteTime

 | String

 | 删除时间

 |
3.3 推送失败

当数据推送失败时，管理员会收到通知。管理员可调整配置后，在「数据推送」处点击「重新推送」，重新推送失败的数据。

注：

1）数据推送失败时，管理员可以选择重新推送失败缓存里的数据，也可以放弃缓存。失败数据仅可保留 7 天，超时后无法再进行重新推送。

2）当失败记录达到 100 条，会关闭数据推送功能，同时管理员会收到一条数据推送关闭的消息提醒，需要在数据推送设置中重新启动数据推送，数据推送才会继续推送。


---

## 表单事件推送

- 官方文档：https://hc.jiandaoyun.com/open/11501

1. 简介

1.1 功能简介

表单事件推送是指，当表单结构发生变更（包括表单保存、字段别名修改）时，可将变更后的表单内容推送至对应的服务器中。

1.2 使用场景

适用于拥有多个系统，且对简道云表单结构有依赖关系的场景中。如：

第三方系统集成与数据映射同步：字段别名修改时，实时推送到服务器中，以便及时更新依赖系统的映射规则；
自动化工作流规则更新：表单字段被删除时，自动推送至服务器中，以便及时更新工作流的失效规则；
BI 报表与数据分析平台同步：表单结构变更时，实时推送至 BI 平台或数据仓库管理工具中，平台可以及时通知负责人以便更新报表逻辑、标记依赖项等。
2. 操作步骤

2.1 新建数据推送

在「扩展功能 >> 数据推送」处，点击「新建数据推送」，在数据推送页面修改推送名称为「考勤数据推送」。

2.2 设置服务器

2.2.1 选择目标服务器

进入数据推送设置页面后，根据企业需求选择对应的目标服务器。系统支持选择自定义服务器推送，也支持选择 Finereport 服务器进行推送：

与 Finereport 对接选择 Finereport 服务器：FineReport 报表对接简道云插件；
与 FineBI 对接选择 Finereport 服务器：FineBI 报表对接简道云插件；
与九数云对接选择自定义服务器：同步数据源【7. 接受简道云实时推送】；

2.2.2 设置服务器地址

企业根据自身的企业需求，可填写指定的服务器地址，数据会以 HTTP POST 请求的形式，推送至目标服务器地址。

2.2.3 生成Secret

服务器地址填写完成后，点击「生成 Secret」，系统将自动生成对应的 Secret。

2.2.4 服务器连接测试

1）服务器地址确认无误及生成 Secret 后，点击「服务器连接测试」，系统将自动进行服务器连接测试，测试成功后，则显示「服务器连接成功」。

2）若服务器连接失败，也可查看错误详情，并根据错误详情进行调整后重新连接。

2.3 设置推送事件

进行表单事件推送时，企业可根据自身需求来勾选对应的表单推送事件，如下所示：

表单结构有变化时：表单保存或字段别名变更时推送。
注：

1）表单上的任何修改，如增删改字段、修改字段属性、表单属性等内容都属于表单结构变化。

2）表单不做任何修改，只要点击了保存按钮，也属于表单结构变化。

2.4 设置备注

若有多个数据推送，可在「备注」中填写推送说明，以区分不同的数据推送，便于识别和管理。

3. 注意事项

3.1 推送数据结构

表单事件推送时，数据结构定义如下：

参数

 | 说明

 |
op

 | 推送事件。

表单更新：form_update
 |
opTime

 | 推送事件触发时间戳，精确到毫秒

 |
data

 | 具体数据内容

 |
3.2 表单事件推送内容

字段

 | 字段类型

 | 说明

 |
appId

 | string

 | 应用ID，全局唯一

 |
entryId

 | string

 | 表单ID，在应用内唯一

 |
name

 | string

 | 表单名称

 |
widgets

 | array

 | 用户控件列表，不包含系统字段

 |
widgets[].label

 | string

 | 控件名称

 |
widgets[].name

 | string

 | 字段名（设置了字段别名则采用别名，未设置字段别名则采用字段 ID）

 |
widgets[].widgetName

 | string

 | 字段 ID

 |
widgets[].type

 | string

 | 控件类型

 |
widgets[].items

 | array

 | 可选，当控件类型为子表单时存在

 |
3.3 推送失败

当数据推送失败时，管理员会收到通知。管理员可调整配置后，在「数据推送」处点击「重新推送」，重新推送失败的数据。

注：

1）数据推送失败时，管理员可以选择重新推送失败缓存里的数据，也可以放弃缓存。失败数据仅可保留 7 天，超时后无法再进行重新推送。

2）当失败记录达到 100 条，会关闭数据推送功能，同时管理员会收到一条数据推送关闭的消息提醒，需要在数据推送设置中重新启动数据推送，数据推送才会继续推送。


---

## 流程推送

- 官方文档：https://hc.jiandaoyun.com/open/23345

1. 简介

1.1 功能简介

流程变更时推送，指的是当流程状态变更、流程待办变更以及产生抄送时，自动将流程推送到指定服务器，实现简道云与第三方系统的实时对接。

1.2 使用场景

适用于需要将简道云流程相关信息同步到第三方系统中处理的场景。

1.3 预期效果

以「流程状态变更时」推送为例，当管理员结束流程时，系统会自动将该变更推送至指定服务器。效果如下所示：

2. 设置步骤

2.1 新建数据推送

在「扩展功能 >> 数据推送」处，点击「新建数据推送」，在数据推送页面修改推送名称为「供应商信息推送」。

2.2 设置服务器

2.2.1 选择目标服务器

进入数据推送设置页面后，选择目标服务器为「自定义服务器」。

注：流程推送中，目标服务器仅支持选择「自定义服务器」。

2.2.2 设置服务器地址

企业根据自身的企业需求，可填写指定的服务器地址。

2.2.3 生成Secret

服务器地址填写完成后，点击「生成 Secret」，系统将自动生成对应的 Secret。

2.2.4 服务器连接测试

服务器地址确认无误及生成 Secret 后，点击「服务器连接测试」，系统将自动进行服务器连接测试，测试成功后，则显示「服务器连接成功」。

2.3 设置推送类型和事件

进行流程推送设置时，推送类型和推送事件选择如下所示：

推送类型：选择「流程变更时推送」；
推送事件：企业可根据自身需求进行勾选，不同事件含义如下：
流程状态变更时：在流程状态变化时推送；
流程待办变更时：在待办产生、被处理（如提交、加签、回退等）时推送；
产生抄送时：有抄送产生时推送。
全部设置完成后，点击「保存」。

2.4 查看推送日志

数据推送完成后，点击数据推送事件右侧的「推送日志」，即可查看推送详情。支持查看以下数据推送详情：

推送失败日志
推送成功日志
全部日志

注：流程推送失败后，不支持手动重新推送，系统将间隔 5min、15min、1h 和 2h 自动重试。

2.5 设置备注

若有多个数据推送，可在「备注」中填写推送说明，以区分不同的数据推送，便于识别和管理。

3. 注意事项

简道云提供 3 种流程数据与外部系统互通的方式，以满足不同场景下的业务需求。详情可查看：流程数据对接第三方系统指南。


---

## 消息推送

- 官方文档：https://hc.jiandaoyun.com/open/11497

1. 功能简介

消息推送可以将简道云中的待办通知、消息通知、抄送通知等消息同步到自己的服务器，便于企业的业务整合。

2. 推送服务器配置方法

2.1 配置入口

点击右上角头像，进入「企业管理 >>消息推送」，开启消息推送的开关：

2.2 服务器配置

点击「配置」，进入消息推送的配置页面，填写服务器地址后，可通过「服务器连接测试」测试连接是否成功，点击「生成 Secret」，即可自动生成消息推送的 Secret，设置好后点击「保存」：

3. 推送数据结构说明

字段

 | 类型

 | 说明

 |
op

 | string

 | 推送事件

 |
data

 | json

 | 推送内容

 |
send_time

 | string

 | 推送时间

 |
数据样例如下：

{
    op: "flow_message", //推送事件
    data: {
        to: [{
            username: "jiandaoyun",
            name: "小云"
        }],
        entry_name: "请假审批",
        notify_text: "小云本周五请假1天",
        url: "https://abc.com/xyz"
    }, //推送内容
    send_time: "2017-10-20T22:41:51.430Z" //推送时间
}

4. 推送事件

4.1 表单自定义时间提醒

4.1.1 配置方式

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「自定义时间提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

4.1.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “form_schedule_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源表单名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“已到提醒时间，请及时处理”，可在提醒设置中自定义

 |
data.url

 | string

 | 表单内链，需表单授权才可访问

 |
send_time

 | string

 | 推送时间

 |
4.1.3 推送数据样例

{
	op: "form_schedule_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}, {
				username: "dao",
				name: "小道"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云提出请假申请，请审批",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}

4.2 表单新数据提交提醒

4.2.1 配置方式

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「新数据提交时提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

4.2.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “data_create_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源表单名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“有新数据提交，请及时处理”，可在提醒设置中自定义

 |
data.content

 | string

 | 详细内容，有值的表单字段标题和字段值。例如：“单行文本: 123\n多行文本: 1233\n数字: 123\n成员单选: codingmagic1\n部门单选: 研发\n日期时间: 2019-06-13”

 |
data.url

 | string

 | 静态消息链接，属于被提醒人的个人消息，登录后可访问

 |
send_time

 | string

 | 推送时间

 |
4.2.3 推送数据样例

{
	op: "data_create_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}, {
				username: "dao",
				name: "小道"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云提出请假申请，请审批",
		content: "请假人: 小云\n请假原因: 病假",
		url: "https://jiandaoyun.com/message/1/data"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}

4.3 表单数据修改后提醒

4.3.1 配置方式

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「数据修改后提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

4.3.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “data_update_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源表单名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“有数据被修改，请及时处理”，可在提醒设置中自定义

 |
data.content

 | string

 | 详细内容，修改人、数据标题、被修改的字段。例如：“修改人: test_li\n数据标题: 1231\n单行文本: 123→1231\n成员单选: codingmagic1→codingjun”

 |
data.url

 | string

 | 数据内链，需表单授权才可访问

 |
send_time

 | string

 | 推送时间

 |
4.3.3 推送数据样例

{
	op: "data_update_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云修改了请假日期",
		content: "修改人: 小云\n数据标题: 病假申请\n请假日期: 2018-5-1→2018-5-2",
		url: "https://jiandaoyun.com/dashboard/app/1/form/2/data/3/qr_link"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}

4.4 根据表单内日期时间字段提醒

4.4.1 配置方式

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「根据表单内日期时间字段提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

4.4.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “form_widget_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源表单名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“有数据到期，请及时处理”，可在提醒设置中自定义

 |
data.content

 | string

 | 详细内容，数据标题

 |
data.url

 | string

 | 数据内链，单表单超出 10 条后发送表单内链，需表单授权才可访问

 |
send_time

 | string

 | 推送时间

 |
4.4.3 推送数据样例

{
	op: "form_widget_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "生日提醒",
		notify_text: "小云的生日到了",
		content: "小云的生日到了",
		url: "https://jiandaoyun.com/dashboard/app/1/form/2/data/3/qr_link"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}

4.5 表单流程消息提醒

当流程发起、抄送、转交、回退、超时、激活、调整负责人时，都会给当前流程负责人推送流程提醒信息。

4.5.1 配置方式

进入流程表单的「流程设定」，在「流程属性 >> 流程提醒」处勾选「推送至我的服务器」：

4.5.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “flow_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.flow_action

 | string

 | 流程操作

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源表单名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“有数据被修改，请及时处理”

 |
data.content

 | string

 | 详细内容，流程简报

 |
data.url

 | string

 | 数据内链，需表单授权才可访问

 |
send_time

 | string

 | 推送时间

 |
不同的流程操作（flow_action）对应不同的推送内容，具体如下表所示：

流程操作

 | 含义

 | 提醒文字

 | 详细内容

 |
flow_forward

 | 提交

 | 有新的流程待办事项

 | 流程简报，例如：“单行文本: 123\n多行文本: 123\n数字: 123”

 |
flow_auto_forward

 | 系统自动提交

 | 有新的流程待办事项

 | 同上

 |
flow_back

 | 回退

 | 提交的流程事项被回退

 | 同上

 |
flow_auto_back

 | 系统自动回退

 | 提交的流程事项被回退

 | 同上

 |
flow_cc

 | 抄送

 | 有新的流程处理结果抄送给您

 | 同上

 |
flow_timeout

 | 流程超时

 | 默认为“有待办未完成，请及时处理”，可在超时提醒设置中自定义

 | 同上

 |
flow_member_transfer

 | 成员转交

 | 由「~$转交人」转交给您1条待办事项

 | 同上

 |
flow_admin_transfer

 | 一条流程数据被管理员调整负责人

 | 由系统管理员转交给您1条待办事项

 | 同上

 |
flow_activate

 | 流程被激活

 | 由系统管理员转交给您1条待办事项

 | 同上

 |
flow_sign_before

 | 前加签

 | 由「~$加签人」加签给您1条待办事项

 | 同上

 |
flow_sign_after

 | 后加签

 | 由「~$加签人」加签给您1条待办事项

 | 同上

 |
flow_sign_parallel

 | 添加审批人

 | 由「~$加签人」加签给您1条待办事项

 | 同上

 |
flow_sign_before_complete

 | 前加签处理完成

 | 前加签处理已完成，您有新的流程待办事项

 | 同上

 |
flow_batch_transfer

 | 多条流程数据被管理员调整负责人

 | 由系统管理员转交给您新的待办事项

 | 无

 |
flow_batch_forward

 | 多条流程提交

 | 有[~$count]条新的流程待办事项

 | 无

 |
flow_batch_cc

 | 多条流程抄送

 | 有[~$count]条新的流程处理结果抄送给您

 | 无

 |
flow_urge

 | 流程催办

 | 有一条流程急需处理

 | 无

 |
4.5.3 新旧流程消息推送时变化

1）新旧流程消息推送时to的变化

旧版to：会集合在同一条推送里，见下方代码中的 to 部分，无论节点多少人，就只推送一次。
{
    "data": {
      "content": "",
      "entry_name": "旧版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "张三",
          "username": "zhangsan"
        },
        {
          "name": "李四",
          "username": "lisi"
        },
        {
          "name": "王五",
          "username": "wangwu"
        }
      ],
      "url": "https://www.jiandaoyun.com/dashboard/app/642e37f2374e1b0007f537b2/form/642e37f5fe736900073a99e5/data/642e3855dd27960007cf9514?actionType=flow_forward&flowId=1&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:11:18.102Z"
}

新版to：会拆分为多条推送，有几个负责人就推送几条，如下该节点有三个负责人，则推送三次，to 里面始终只有一个人。
{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "张三",
          "username": "zhangsan"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}

{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "李四",
          "username": "lisi"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}

{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "王五",
          "username": "wangwu"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}

1）新旧流程消息推送时url的变化

旧版地址：https://www.jiandaoyun.com/dashboard/app/6331609e3c17350008d45fdb/form/633160a368ae71000a94676a/data/64054250c68b1e0008b822a7?actionType=flow_forward&flowId=1&memberType=0&guestCorpId=
新版地址：https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=64100d6e2ac023000782ec79&taskId=641b2fdec3ddb00007aa36a8&actionType=flow_forward&flowId=1&memberType=0&guestCorpId=&appId=6331609e3c17350008d45fdb&formId=633160a368ae71000a94676a&dataId=64054250c68b1e0008b822a7
新版地址相较旧版地址差别如下所示：

数据 id 以 url 参数形式放在 url 中，参数名 instanceId 和 dataId 均等于数据 id；
应用 id 和表单 id 以 url 参数形式放在 url 中，参数名为 appId 和 formId；
新增了 taskId（任务 id，同一个节点多个负责人每个人的 taskId 不同）。
4.6 仪表盘定时提醒

4.6.1 配置方式

进入仪表盘的「仪表盘设计」，点击设置「定时提醒」，设置好提醒内容后，在提醒方式处勾选「推送至我的服务器」：

4.6.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “dash_schedule_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源仪表盘名称

 |
data.notify_text

 | string

 | 提醒文字，默认为“已到提醒时间，请及时处理”，可在提醒设置中自定义

 |
data.url

 | string

 | 仪表盘访问内链，需授权才可访问

 |
send_time

 | string

 | 推送时间

 |
4.6.3 推送数据样例

{
	op: "dash_schedule_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "物料盘点",
		notify_text: "2019年度物料盘点的时间到了",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}

4.7 仪表盘预警提醒

4.7.1 配置方式

进入统计表的编辑页面，在「功能配置 >> 数据预警」处添加预警，设置好预警内容后，在提醒方式处勾选「推送至我的服务器」：

4.7.2 推送内容

字段

 | 类型

 | 说明

 |
op

 | string

 | “dash_alert_message”，固定值

 |
data

 | json

 | 推送内容

 |
data.to

 | json[]

 | 被提醒人列表

 |
data.entry_name

 | string

 | 推送来源仪表盘名称

 |
data.notify_text

 | string

 | 使用预警名称作为提醒文字

 |
data.content

 | string

 | 详细内容，预警来源：{应用名称}>{仪表盘名称}>{组件名称}

 |
data.url

 | string

 | 仪表盘内链，需仪表盘授权才可访问

 |
send_time

 | string

 | 推送时间

 |
4.7.3 推送数据样例

{
	op: "dash_alert_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "库存统计",
		notify_text: "库存警告",
		content: "预警来源：库存应用>华南区盘点>库存剩余量",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}


---

## 管理数据推送

- 官方文档：https://hc.jiandaoyun.com/open/25086

1. 简介

1.1 功能简介

管理数据推送指的是，对设置完成的数据推送事件进行启用/关闭、编辑、删除等操作。

1.2 使用场景

适用于多系统对接过程中，大量使用数据推送事件的企业。

1.3 预期效果

以删除「推送到 FineReport 服务器」事件为例，效果如下所示：

2. 管理步骤

数据推送有「当前表单管理」和「应用内所有表单管理」两个入口，本章节以「当前表单管理」为例进行详细的管理步骤讲解。所有表单管理中，除入口不同，其余方法相同。

2.1 管理入口

1）管理当前表单数据推送

当表单内有多个数据推送，且只查看管理当前表单内的数据推送时，可在「扩展功能 >> 数据推送」处进行管理。

2）管理所有表单数据推送

当应用内有多个数据推送，且要查看管理应用内所有数据推送时，可在「应用后台 >> 数据推送」处进行管理。

2.2 启用/关闭数据推送

数据推送设置完成后，可在「数据推送」页面中，点击推送事件右侧的开关，即可启用/关闭数据推送事件。

2.3 查看推送日志

数据推送完成后，点击数据推送事件右侧的「推送日志」，即可查看推送详情。支持查看以下数据推送详情：

推送失败日志
推送成功日志
全部日志

注：仅保留 6 个月的推送日志。

2.4 编辑数据推送

点击推送事件右侧的「编辑」按钮，即可进入到数据推送编辑页面，重新设置数据推送。

2.5 删除数据推送

若确认推送事件无用吼，点击「删除」按钮，即可删除对应的推送事件。
