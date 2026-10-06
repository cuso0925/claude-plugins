# 单点登录集成

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 单点登录

- 官方文档：https://hc.jiandaoyun.com/open/11433

1. 简介

1.1 功能简介

简道云单点登录功能可将简道云集成至其他系统/产品（例如私有化企业微信、微信公众号、APP等），打通登录系统、消息通知及通讯录体系。

1.2 使用场景

如公司在使用简道云的同时还使用了帆软的报表工具，但是帆软报表跟简道云并不是一套用户体系，那么可以通过单点登录功能，使员工使用帆软的账号密码在简道云中轻松完成登录。便于企业成员在多个系统平台之间的切换，提高企业管理效率。

1.3 预期效果

1）网页/系统集成

登录用户自己的系统后，即可通过单点登录协议进入简道云对应成员的账号。以通过阿里云云盾认证后，登录简道云为例，效果如下所示：

2）微信服务号集成

公共模式账户可以通过 微信服务号集成功能 将简道云集成到自己企业的微信服务号中，集成模式账户同样可以使用单点登录实现这一效果。

1.4 版本说明

1）本功能为付费高级功能，需简道云企业版及以上版本可用（试用版可进行试用），您可升级简道云版本来使用该功能，版本升级可点击：商务咨询。

2）若您需要体验使用该功能，可点击右侧表单提交试用申请：申请试用 - 单点登录。

2. 设置步骤

2.1 设置入口

在「账户中心 >> 企业管理 >> 企业设置 >> 企业安全」处，打开单点登录后面的开关，并点击「设置」按钮即可进入单点登录设置页面。

2.2 配置内容

简道云中支持 3 种配置方式，不同的配置方式对应不同的配置内容。如下表所示：

配置方式

 | 配置内容

 |
SAML 2.0

 | SAML 2.0 Endpoint (HTTP)
IdP 公钥
SAML 加密算法
Issuer URL
SLO Endpoint (HTTP)
 |
自定义接口

 | IdP 登录接口
认证密钥
认证加密算法
Issuer URL
IdP 登出接口
 |
CAS

 | IdP 登录接口
 |

2.3 效果演示

效果参见本文【1.3 预期效果】。

3. 开发能力

1）单点登录文档中包含以下几部分的内容：

开发文档
客户案例
您可以通过阅读以上几部分内容，来了解学习和实现简道云的单点登录功能。

2）简道云中的单点登录功能，需要企业成员有一定的开发能力。您可以根据自身的开发能力，来选择不同的方式实现单点登录配置：

若您拥有开发能力，可以点击 申请试用 - 单点登录 并参照 开发文档 进行对接；
若您没有开发能力，可以选择 提交定制开发需求 由简道云实施工程师为您开发。
4. 代码示例

下面给出不同编程语言对应的代码 Demo，您可通过修改Demo来完成自定义接口的配置：

Golang ：示例工程
Java ：示例工程
Node.js：示例工程
PHP ：示例工程
Python：示例工程
注： java 代码处，若 username 值以 0 开头，在 yaml 配置文件中需要添加单引号。


---

## 开发文档

- 官方文档：https://hc.jiandaoyun.com/open/11468

1. 简介

单点登录，即 Single Sign On，简称为 SSO。SSO是在多个应用系统中，用户只需要登录一次就可以访问所有相互信任的应用系统，是目前比较流行的企业业务整合的解决方案之一。

2. 开发步骤

2.1 开发预备

2.1.1 预备知识

在开始开发之前，您需要了解以下预备知识：

1）什么是单点登录？

单点登录指用户在认证中心登录后，即同时登录到所有与此认证中心关联的所有服务中。如您只需登录 Google 即可以已登录用户的身份访问 Youtube 和 Gmail。

2）单点登录流程中的 IdP 和 SP 是什么？

IdP 是 Identity Provider 的缩写，指认证中心，在认证过程中 IdP 持有用户信息，并与用户建立会话。
SP 是 Service Provider 的缩写，指服务提供者，当用户访问 SP 提供的服务时，如果 SP 无法识别用户，会请求 IdP 对用户进行认证。
3）什么是 SAML？

SAML 是一种单点登录实现协议，这是一个传统协议，并集成在很多现有的系统中，如 Windows AD 和 Apereo CAS。

4）什么是 JWT？

JWT 是一种数据交换格式，本质是一个 Encode 后的 JSON，其中包含了用户自定义的消息，以及一些辅助验证字段，如签名，过期时间。

2.1.2 工作原理

SAML（安全断言标记语言）是一种 XML 开放标准，SAML 2.0 、CAS 和自定义接口都基于这种协议。SAML 用于在服务提供者和身份提供者之间交换身份验证信息。

服务提供者：SP，Service Provider，这里指简道云；
身份提供者：IdP，Identity Provider，这里指企业内部或第三方的身份验证系统。
用户通过 IDP 发起登录时，将使用 IDP 进行身份验证，验证通过后跳转至简道云。如果 IDP 身份未得到验证，你的用户将被导航至 IDP 的登录界面先进行登录验证，通过后跳转至简道云。

2.1.3 配置流程

简道云在单点登录过程中扮演 SP 身份。在管理员启用单点登录功能后，当一个未登录的成员访问简道云时，简道云会将此请求重定向至管理员配置的 IDP 地址。此时如果成员登录过 IDP，则 IDP 只需读取会话中的用户信息并将其通过配置的方式返回给简道云，简道云即可识别此成员并提供后续服务。流程大致如下：

2.2 申请试用

1）本功能为付费高级功能，需简道云企业版及以上版本可用。若您需要体验使用该功能，可点击右侧表单提交试用申请：申请试用 - 单点登录。

2）若您在使用中遇到问题，也可 联系我们 进行咨询。

2.3 配置方式

简道云中支持 3 种单点登录的配置方式：

配置方式

 | 说明

 | 优缺点

 | 适用对象

 |
SAML2.0

 | 安全断言标记语言，使用统一的身份提供服务（IDP）验证用户身份，然后将认证后的安全断言和用户信息返回给简道云，简道云将用户与简道云内账号系统关联

 | 优点：通用协议，若已集成了相关功能则可以直接配置复用，也可以使用如 OneLogin 这样的认证服务提供者。
缺点：如果没有集成相关功能，用户需要自行开发对接层，开发难度较高。
 | 适用于认证系统中已经集成了相关功能，或背景知识较强的用户

 |
自定义接口

 | 简化的 SAML 协议，企业客户可在现有 SSO 接口基础上进行修改，按照简道云的要求调用服务和返回参数，并将认证后的用户信息返回给简道云，完成账号关联。

 | 优点：易于理解，开发简单。
缺点：这是简道云的自有协议，用户需要自行开发对接层。
 | 适用于自己开发相关接口与简道云对接的用户。

 |
CAS

 | 允许用户访问多个应用程序，同时仅向中央CAS 服务器应用程序提供一次凭据（如用户名和密码）。

 | 优点: 通用协议, 并且有开源的 IdP 实现如 Apereo CAS 和 Cloak。
缺点: 如果没有集成相关功能，用户需要自行开发对接层，开发难度中等。
 | 适用于认证系统中已经集成了相关功能的用户

 |
3. 代码示例

若您需要通过自定义接口来实现单点登录，您可通过修改以下Demo 代码示例来完成自定义接口的配置：

Golang ：示例工程
Java ：示例工程
Node.js：示例工程
PHP ：示例工程
Python：示例工程


---

## SAML2.0配置

- 官方文档：https://hc.jiandaoyun.com/open/11398

1 功能简介

SAML2.0：安全断言标记语言，使用统一的身份提供服务（IDP）验证用户身份，然后将认证后的安全断言和用户信息返回给简道云，简道云将用户与简道云内账号系统关联。

登录页的设置方式参考文档：「自定义登录页」

2 使用现有系统的 SAML 功能

如果用户使用的系统中集成了 SAML 功能，用户可以自行查阅相关资料进行配置。下面以 OneLogin 的配置过程举例：

2.1 身份认证服务配置

首先选择支持SAML 认证协议的身份认证服务商，以下以OneLogin 为例介绍：

1） 以管理员身份登录企业的 OneLogin 账号，进入 Administration；

2） 进入 Company Apps ，点击ADD APP。搜索SAML，并选择 SAML Test Connector （IdP w/attr）；

3）进入应用Info页面设置名称及图标；4）进入应用SSO 页面，即可获得 SAML 2.0 Endpoint (HTTP) 、Issuer URL、 SLO Endpoint (HTTP) 以及 View Details 内的 X.509 Certificate 等信息；

2.2 简道云内的单点登录配置

以下在简道云内进行操作：

1）账户中心>>企业管理>>企业信息>>单点登录>>开启/ 配置；

2）将 OneLogin 内获得的 SSO 相关信息写入，即可获得「认证返回地址」；

SAML 2.0 Endpoint (HTTP)：简道云发送 SAML 时请求的地址（必填）
IdP 公钥：身份提供商用于签名的公钥证书（必填）
SAML 加密算法：SHA-1、SHA-256、SHA-512（必填）
Issuer 地址：使用身份提供商的应用标识（必填）
SLO Endpoint (HTTP)：若填写此项，用户从简道云登出后，会同时登出该 Idp 下所有 SAML 应用（选填）
3）将「认证返回地址」写入 OneLogin 的ACS (Consumer) URL和ACS (Consumer) URL Validator，即可完成配置

2.3 成员帐号配置

进入 USERS 的点击 「NEW USER」，添加新的成员；然后从ALL USERS里找到这个用户，将他添加到需要单点登录的应用里;在更多操作里为此成员设置登录密码。（成员在首次登录的时候需要输入OneLogin 中的登录密码）

2.4 配置username

在OneLogin 里找到之前创建的这个应用，然后添加参数username。

2.5 SSO 登录

登录页的设置参考文档「自定义登录页」 完成以上操作后，相关成员就可以在移动端或 Web 端通过 SSO 的方式直接登录简道云。

在登录之前需要先设置好企业账号URL，成员通过企业账号URL进行单点登录；
首次登录需要输入认证服务商（如OneLogin ）中的用户名和密码。本文以OneLogin为例介绍单点登录配置方式，其他支持 SAML认证协议的身份认证服务商皆可同理配置单点登录。
3 自行开发对接层

SAML 是一个标准协议，因此开发人员在动手开发前，必须对此协议有一定的了解，此处给出官方文档以供参考。

用户给出的 IdP 必须能够返回符合标准的 SAMLResponse，其 IdP 的 EntityId 必须与管理员在简道云配置的 Issuer 一致，并在 Attribute 段包含一个名为 username 的属性，其值对应成员在简道云内的编号。此外，IdP 必须返回 RelayState。

开发人员可以参考：

Node.js ： >>示例工程。


---

## 同阿里云IDaaS对接实例（SAML2.0）

- 官方文档：https://hc.jiandaoyun.com/open/12234

1.简介

1.1 案例简介

通过阿里云提供的应用身份服务（IDaaS），实现简道云的单点登录业务。

1.2 使用场景

在企业管理当中，企业同时拥有 OA 管理系统和简道云平台，通过单点登录，可以实现登录 OA 管理系统后，免登录进入简道云中，便于多个系统平台之间的切换，提高企业管理效率。

1.3 预期效果

访问简道云企业URL时，点击单点登录，通过阿里云云盾认证后，成功登录到了简道云中。

2.设置步骤

2.1 在阿里云IDaaS中创建SAML应用

2.1.1 创建实例

1）登录到 阿里云管理后台（无阿里云账号的需要先注册），搜索并进入应用身份管理（IDaaS）中，选择 EIAM云身份服务。

2）在 EIAM云身份服务中，点击「免费创建实例」，输入实例名称并勾选协议后点击「创建」。

2.1.2 添加SAML应用

1）在创建的示例中，点击「实例名称」或者「访问控制台」进入云身份服务管理后台。

示例：点击「实例名称」进入云身份服务管理后台。

2）在云身份服务中，选择应用，在应用页面点击「添加应用」。

3）在「添加应用>>标准协议>> SAML 2.0」处，点击「添加应用」，输入应用名称后，点击「立即添加」。

2.1.3 查看应用配置信息

应用添加成功后，显示如下页面，在「SAML应用>>登录访问>>单点登录>>应用配置信息」处，查看以下信息：

IdP 唯一标识（IdP Entity ID）
IdP SSO地址（IdP Sign-in URL）
公钥证书

注：需要根据应用配置信息去配置简道云中的单点登录，故先不关闭此页面。

2.2 在简道云中配置单点登录

2.2.1 开启单点登录

1）新开一个浏览器页面，登录 简道云账号，进入「企业管理 >> 管理工具 >> 企业设置」页面中。

2）在「企业安全 >> 单点登录」处，打开单点登录的开关，并点击「配置」按钮。

2.2.2 配置单点登录

单点登录配置项如下所示，部分配置信息需复制阿里云 SAML应用中的应用配置信息。

单点登录配置方式：SAML 2.0
SAML 2.0 Endpoint（HTTP）：复制阿里云「SAML 应用 >> 应用配置信息 >> IdP SSO 地址（IdP Sign-in URL）」处的内容
IdP公钥：复制阿里云「SAML 应用 >> 应用配置信息 >> 公钥证书（Certificate）」处的内容
SAML 加密算法：任意选择
Issuer URL：复制阿里云「SAML 应用 >> 应用配置信息 >> IdP 唯一标识（IdP Entity Id）」处的内容
SLO Endpoint (HTTP)：保持默认即可
配置完成后点击「保存」。

2.2.3 生成单点登录信息

完成单点登录配置后，会生成如下对应信息：

注：需要根据生成的信息去完成阿里云SAML应用中的配置，故先不关闭此页面。

2.3 在阿里云中修改SAML应用

2.3.1 配置阿里云中单点登录

返回到阿里云 SAML应用配置页面，按照如下所示进行配置，部分配置内容需要复制简道云中单点登录信息。

单点登录地址（ACS URL）：复制简道云中的认证返回地址
应用唯一标识（SP Entity ID）：复制简道云中的认证返回地址
应用账户（Name ID）：选择应用账户/应用账户
断言属性（Attribute Statements）：修改 key 值为 username；修改 value 值为 appUser.username
其余配置项：保持默认即可
配置完成后点击「保存」。

点击「显示高级配置」，修改断言属性中 key 的值为 username，修改 value 的值为 appUser.username。

2.3.2 开启接口

在「SAML应用>>通用配置」处，开启接口访问。

2.3.3 创建账户

在「云身份服务>>账户」页面，点击创建账户，输入账户名、密码等信息，点击「确定」。

2.3.4 添加应用账户

1）进入简道云「通讯录」中，查看并保存需要进行单点登录的「成员编号」。

2）进入阿里云的「云身份服务>>应用>>单点登录>>应用账户」中，点击「添加应用账户」。

3）选择步骤 2.3.3 中创建的账户，在输入框中输入需要进行单点登录的成员编号，点击「保存」。

2.3.5 添加授权

在「SAML应用>>登录访问>>授权」处，点击「添加授权」，选择步骤 2.3.3 中创建的账户，点击「保存授权」。

2.4 关闭二次认证（可选）

此步骤为可选步骤：

若希望成员在使用账户名、密码登录时，还需要进行手机号、邮箱的二次认证，则无需进行此步骤；

若不需要成员进行手机号、邮箱的验证，则需要进行此步骤，关闭二次认证。

在「云身份服务>>登录>>二次认证」中，关闭「二次认证配置」按钮，点击「确认禁用」并输入验证码后，点击「确定」即可禁用。

2.5 效果演示

效果演示参见本文【1.3 预期效果】


---

## 同Keycloak对接实例（SAML2.0）

- 官方文档：https://hc.jiandaoyun.com/open/16090

1. 简介

1.1 案例简介

通过配置 Keycloak 的相关实例，实现简道云的单点登录业务。

1.2 使用场景

当企业同时拥有多套管理系统和简道云平台，通过单点登录的方式，可以实现登录相关管理系统后，免登录进入简道云中，便于多个系统平台之间的切换，提高企业管理效率。

1.3 预期效果

访问简道云企业 URL时，点击单点登录，通过输入 Keycloak 中设置的用户名及密码后，成功登录到了简道云中。

2. 设置步骤

2.1 在Keycloak中创建相关实例

2.1.1 登录到Keycloak控制台

打开Keycloak，点击左侧「Administration Console」，输入账号密码后（无账号的需要先注册），登录到 Keycloak 控制台中。

2.1.2 新增realm实例

1）在 Keycloak 控制台中，点击 Master 右侧的下拉箭头，在弹出的面板中点击「Add realm」，并修改 realm 的名字为 Test，修改完成后点击「Create」。如下所示：

2）realm 实例创建完成后，在「 realm 实例 >> Keys 」处，选择 Type 类型为「RSA」的算法，点击该算法最右侧的「Certificate」，在弹出的面板中，复制并保存对应的秘钥。

注：请务必复制并保存秘钥，便于后面步骤的配置与使用。

2.1.3 新增client实例

1）切换左侧导航栏至「Clients」，点击页面右侧的「Create」按钮，创建新的 Client 实例：

在「Client ID」处 ，设置 ID 名称，如设置其为 SSO；
在「Clients Protocol」处，选择类型为「saml」。
全部设置完成后点击「Save」按钮进行保存。

2）在「SSO >> Settings」处，确认打开「Enabled」、「Include AuthnStatement」、「Sign Docunments」这 3 部分的开关。

3）同时，对其他配置项进行如下所示操作：

Signature Algorithm：下拉框内选择「RSA_SHA256」；
SAML Signature Key Name：下拉框内选择「KEY_ID」；
Canonicalization Method：下拉框内选择「EXCLUSIVE」；
Name ID Format：下拉框内选择「username」；
IDP Initiated SSO URL Name：根据企业需求，设置名称，如设置其名称为 jdy。
其他配置项保持默认即可。

4）以上配置项确认设置完成后，复制并保存 SSO URL 地址，复制完成后点击「Save」进行保存。如下所示：

注：请务必复制并保存 URL 地址，便于后面步骤的配置与使用。

2.1.4 新增mapper配置

1）在「SSO >> Mappers」处，点击右侧「Create」按钮，新增 mapper 配置。

2）对于新增的 mapper ，进行如下所示的配置：

Name：设置其名称为「username」；
Mapper Type：下拉框内选择「User Property」；
Property：设置其为「username」；
SAML Attribute Name：设置其为「username」；
SAML Attribute NameFormat：下拉框内选择为「Basic」。
设置完成后，点击「Save」按钮，保存以上设置。

注：该步骤中，各项配置须与图示保持一致，不可随意更改。

2.1.5 新增用户

1）切换左侧导航栏至「Users」处，点击右侧「Add user」按钮，并在新增用户面板上，设置 Username。设置完成后点击「Save」进行保存。

注：

1）确保新增用户的 username，在简道云系统中存在相同 username 的成员。

2）Keycloak 中仅能识别小写字母，其他如大写字母、符号等无法识别；故确保用户的 username 是由小写字母组成的。

2）在「新增的用户名 >> Credentials」处，设置用户密码，如下所示：

2.2 在简道云中配置单点登录

2.2.1 开启单点登录

1）新开一个浏览器页面，登录 简道云账号，进入「企业管理 >> 管理工具 >> 企业设置」页面中。

2）在「企业安全 >> 单点登录」处，打开单点登录的开关，并点击「配置」按钮。

2.2.2 配置单点登录

单点登录配置项如下所示，部分配置信息需复制 Keycloak 中 Client 实例的配置信息。

单点登录配置方式：SAML 2.0
SAML 2.0 Endpoint（HTTP）：复制 Keycloak 中「Clients >> SSO >> Settings >> IDP Initiated SSO URL Name 」处的内容，即本文【2.1.3 新增client实例】中的 SSO URL 地址。
IdP公钥：复制 Keycloak 中「 Realm Settings >> Keys >> Certificate 」处的内容，即本文【2.1.2 新增realm实例】中要求复制的秘钥内容。
SAML 加密算法：下拉框中选择「SHA-256 」。
Issuer URL：复制 Keycloak 中「Clients >> SSO >> Settings >> IDP Initiated SSO URL Name 」处的内容，即本文【2.1.3 新增client实例】中的 SSO URL 地址，并去掉 test 之后的地址后缀。
SLO Endpoint (HTTP)：保持默认即可。

2.2.3 生成单点登录信息

完成单点登录配置后，会生成如下单点登录相关信息，复制并保存「认证返回地址」。

注：需要根据生成的信息去完成 Keycloak 中的相关配置，故可以暂时不关闭此页面。

2.3 在Keycloak中回调URL

返回到「Keycloak >> Clients >> SSO >> Settings 」配置页面，按照如下所示进行配置，配置内容需要复制简道云中单点登录信息。

Valid Redirect URls：复制简道云中的认证返回地址；
Master SAML Processing URL：复制简道云中的认证返回地址。
配置完成后点击「Save」进行保存。

2.4 效果演示

效果演示参见本文【1.3 预期效果】。

3. 注意事项

在「Clients >> SSO >> Mappers」设置中，若 Mappers username 是由域账户自动生成的，此时在新增的 Users 处，添加新的 Attributes 并设置其值为企业微信 ID，设置完成后也可进行单点登录。


---

## 自定义接口配置

- 官方文档：https://hc.jiandaoyun.com/open/11434

1. 功能简介

SAML 2 是一个标准的 SSO 协议， 并受 Windows AD 支持, 因此在 SSO 领域有着广泛的应用，但其要求开发者具有一定的背景知识(建议阅读官方文档)，对接成本较高， 因此我们补充实现了自定义接口。

自定义接口是简化的 SAML 协议，企业客户可在现有 SSO 接口基础上进行修改，按照简道云的要求调用服务和返回参数，并将认证后的用户信息返回给简道云，完成账号关联。

2. 设置步骤

2.1 设置入口

1）登录 简道云账号，进入「企业管理 >> 管理工具 >> 企业设置」页面中。

2）在「企业安全 >> 单点登录」处，打开单点登录的开关，并点击「配置」按钮。

2.2 选择配置方式

进入配置单点登录详情页中，选择单点登录配置方式为「自定义接口」。如下所示：

2.3 设置Idp登录接口

Idp 登录接口，指的是通过开发人员部署所需的基础内容，允许用户登录系统的接口。通常用于需要验证用户身份并且允许用户访问系统的场景当中。详情可参见文档：Idp 配置说明。

在简道云的单点登录中，您可以根据企业自身的服务器配置，设置登录接口：

2.4 生成认证密钥

认证密钥指的是信息的发送方和接收方，需要通过一个密钥去加密和解密数据。在自定义接口当中，用户可以自定义设置认证密钥，也可以点击「生成密钥」按钮，直接生成一串认证密钥。如下所示：

注：认证密钥需要与代码中的 SECRET 保持一致。

2.5 选择认证加密算法

简道云的单点登录中，支持以下 3 种加密算法，您可以根据自己的需求来选择合适的加密算法，从而完成单点登录配置：

HS256
HS384
HS512

2.6 设置Issuer URL

Issuer URL 用于验证请求内容与服务后台是否能够匹配成功，若匹配成功则可以进行解析，否则将请求失败。您可自定义 Issuer URL 的内容。如设置为： Issuer.test。

注：若设置了 Issuer URL，则 Issuer URL 中的内容需要与代码中的 Issuer 保持一致。

2.7 设置登出接口

Idp 登出接口，是指当企业成员访问了简道云的单点登出地址时，简道云不仅会登出当前成员，同时还会将成员重定向至 Idp 并携带登出请求参数。

注：

1）IdP 可以销毁与此成员的会话以实现单点登出的效果。

2）单点登出请求参数格式与认证请求参数一致, 并额外包含 jti 或 nameId 参数, 但不包含 state 字段, 在 Token 中的 type 为常量「slo_req」。

3. 代码示例

绝大多数编程语言都有较为良好的 JWT  算法实现, 第三方库列表可在这个页面中查找，下面给出以 Python 代码和 Golang 代码 实现 IdP 配置 的简单示例:

3.1 Golang Demo

package main

import (
   "fmt"
   "github.com/dgrijalva/jwt-go"
   "log"
   "net/http"
   "time"
)

const (
   acs      = "https://www.jiandaoyun.com/sso/custom/5cd91fe50e42834f41b7c6ef/acs"
   issuer   = "com.example"
   username = "angelmsger"
   secret   = "jdy"
)

func ValidBody(body jwt.MapClaims) bool {
   return body["iss"] == "com.jiandaoyun" && body["aud"] == issuer && body["type"] == "sso_req"
}

func ValidToken(query string) bool {
   token, err := jwt.Parse(query, func(token *jwt.Token) (interface{}, error) {
      if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
         return nil, fmt.Errorf("Unexpected Signing Method: %v ", token.Header["alg"])
      }
      return []byte(secret), nil
   })
   if err != nil {
      return false
   }
   claims, ok := token.Claims.(jwt.MapClaims)
   return ok && token.Valid && ValidBody(claims)
}

func GetTokenByUsername(username string) (string, error) {
   now := time.Now()
   token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
      "type":     "sso_res",
      "username": username,
      "iss":      issuer,
      "aud":      "com.jiandaoyun",
      "nbf":      now.Unix(),
      "iat":      now.Unix(),
      "exp":      now.Add(1 * time.Minute).Unix(),
   })
   return token.SignedString([]byte(secret))
}

func BuildResponseUri(token string, state string) string {
   target := acs + "?response=" + token
   if state != "" {
      target += "&state=" + state
   }
     return target
}

func handler(w http.ResponseWriter, r *http.Request) {
   query := r.URL.Query()
   reqToken := query.Get("request")
   if ok := ValidToken(reqToken); ok {
      if resToken, err := GetTokenByUsername(username); err == nil {
         target := BuildResponseUri(resToken, query.Get("state"))
         http.Redirect(w, r, target, http.StatusSeeOther)
      }
      w.WriteHeader(404)
   }
   w.WriteHeader(404)
}

func main() {
   http.HandleFunc("/sso", handler)
   log.Fatal(http.ListenAndServe(":8080", nil))
}

3.2 Pyhton Demo

from datetime import datetime, timedelta
from flask import Flask, abort, redirect, request
import jwt

from jwt import InvalidTokenError

class Const:
    ACS = 'https://www.jiandaoyun.com/sso/custom/5cd91fe50e42834f41b7c6ef/acs'
    SECRET = 'jdy'
    ISSUER = 'com.example'
    USERNAME = 'angelmsger'

app = Flask(__name__)

 def valid_token(query):
    try:
        token = jwt.decode(
            query, Const.SECRET,
            audience=Const.ISSUER,
            issuer='com.jiandaoyun'
        )
        return token.get('type') == 'sso_req'
    except InvalidTokenError:
        return False

def get_token_from_username(username):
    now = datetime.utcnow()
    return jwt.encode({
        "type": "sso_res",
        'username': username,
        'iss': Const.ISSUER,
        "aud": "com.jiandaoyun",
        "nbf": now,
        "iat": now,
        "exp": now + timedelta(seconds=60),
    }, Const.SECRET, algorithm='HS256').decode('utf-8')

@app.route('/sso', methods=['GET'])
def handler():
    query = request.args.get('request', default='')
    state = request.args.get('state')
    if valid_token(query):
        token = get_token_from_username(Const.USERNAME)
        stateQuery = "" if not state else f"&state={state}"
        return redirect(f'{Const.ACS}?response={token}{stateQuery}')
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(port=8080)

3.3 其它Demo

下面给出其它编程语言对应的代码 Demo，您可通过修改Demo来完成自定义接口的配置：

Golang ：示例工程
Java ：示例工程
Node.js：示例工程
PHP ：示例工程
Python：示例工程
4. 单点登录方式

企业成员进行单点登录时，可以通过「企业 URL 」和「 iss 地址」两种方式访问企业，两种方式详情如下：

4.1 通过「企业 URL」登录

企业 URL 地址指的是在「企业信息 >> 基础信息 >> 企业账号 URL」处，企业根据自身需求设置的 URL 地址。成员通过企业 URL 进行登录时，会先跳转至单点登录的页面，点击「登录」后即可进入企业。

4.2 通过「iss 地址」登录

iss 地址指的是在「企业设置 >> 企业安全 >> 单点登录 >> 认证地址返回」处，将认证返回地址复制后，修改 acs 后缀为 iss。如下所示：

https://www.jiandaoyun.com/sso/custom/XXXXXXXX/acs  //原认证返回地址
https://www.jiandaoyun.com/sso/custom/XXXXXXXX/iss //修改后的 iss 地址

企业成员通过 iss 地址进行登录时，不会跳转至单点登录的页面，可以直接进入企业。


---

## Idp配置说明

- 官方文档：https://hc.jiandaoyun.com/open/18257

1. 简介

1.1 功能简介

自定义接口的整体配置与 SAML 2 类似， 只是支持的加密算法与密钥的形式存在差异，在 SAML 中我们支持 SHA 系列算法，而自定义接口中我们支持 HMAC-SHA  系列算法。在 SAML 中我们要求用户填写包含公钥的基于 X.509 格式的证书，而在自定义接口中需要填写的是一个普通的密钥字符串，长度最大为 128。

1.2 Idp作用

基于配置的 IdP 信息，客户可以通过开发自己的 IdP 来与简道云对接，从而实现单点登录。那么用户 IdP 的作用如下所示：

接收由用户浏览器发起的认证请求（该请求基于简道云后端生成的重定向链接）；
基于其在简道云的配置与简道云的开发文档中提到的规范, 验证请求的合法性；
从 Session 中获取当前成员的相关信息, 封装及签发 Token；
将 Token 作为参数, 将用户重定向回简道云。

2. 配置说明

2.1 参数

IdP 服务与简道云间的 Token 传递基于 JWT 标准。JWT 标准可以参考如下所示 2 篇文档：

Introduction to JSON Web Tokens；
阮一峰老师的 JSON Web Token 入门教程。
在配置来自简道云的认证请求或者返回简道云的认证断言时，参数格式如下所示：

配置步骤

 | 参数名

 | 说明

 |
由用户浏览器发起的认证请求

 | request

 | 认证请求 Token，详见【2.2.1 认证请求】

 |
state

 | 状态值, 此值需要原封不动的返回简道云, 简道云通过此值来避免恶意的断言请求

 |
返回简道云的认证断言

 | response

 | 认证断言Token，详见【2.2.2 认证断言】

 |
state

 | 状态值，来自认证请求

 |
redirect_uri

 | 重定向地址，可选项，需要进行 URL 编码

 |
2.2 签名内容

2.2.1 认证请求

1）认证请求是指，由用户浏览器发起的认证请求，IdP 需要根据您的安全级别自行验证。

参数名

 | 说明

 |
iss

 | 常量值 “com.jiandaoyun”, 意指此请求由简道云发起

 |
aud

 | 可选, 管理员在简道云配置的 Issuer

 |
iat

 | 签名签发时间(通常 JWT 第三方库会包含此验证, 无需手动实现验证逻辑)

 |
exp

 | 签名失效时间(通常 JWT 第三方库会包含此验证, 无需手动实现验证逻辑)

 |
type

 | 常量值 “sso_req”, 意指此为一个单点登录认证请求

 |
注：开发环境可以跳过 Idp 验证。

2）您实际收到的请求原文及其对应解码后的格式，如下所示:

2.2.2 认证断言

1）简道云要求 IdP 在确认用户身份并将其重定向回简道云时，携带的 response 参数解码后对应的内容如下:

参数名

 | 说明

 |
aud

 | 常量值 “com.jiandaoyun”, 意指此断言的接收方为简道云

 |
exp

 | 签名失效时间

 |
iat

 | 签名签发时间

 |
iss

 | 可选, 管理员在简道云配置的 Issuer

 |
nbf

 | 可选, 签名生效时间

 |
type

 | 常量值 “sso_res”, 意指此为一个单点登录认证断言

 |
username

 | 成员工号, 此值应当与一个已经在简道云通讯录中激活的成员工号一致

 |
redirect_uri

 | 重定向地址, 可选, 无需进行 URL 编码, 若该参数存在, 将覆盖 URL 中的同名参数.

 |
2）您实际发送的断言原文及其对应解码后的格式，如下所示:


---

## 基于Python代码的单点登录

- 官方文档：https://hc.jiandaoyun.com/open/18258

1. 简介

1.1 案例简介

本案例通过 Python 代码配置自定义接口，实现简道云的单点登录业务。

1.2 使用场景

企业拥有自己的企业微信、中台等账号时，需要通过单点登录实现企业成员登录简道云的效果，则可以通过自定义接口实现。

1.3 预期效果

以本地登录为例，成员访问简道云企业 URL 时，点击单点登录后即可自动登录至简道云工作台中，退出登录后进入官网页面。效果如下所示：

2. 设置步骤

2.1 Python的安装及配置

2.1.1 Python安装

登录 Python 官网，根据企业需求选择合适的Python版本，点击「下载使用」进行下载，如下所示：

2.1.2 安装依赖包

1）Python 安装完成后，下载对应的依赖包：依赖包下载链接。如下所示：

2）在电脑中同时按住 windows+R，输入 cmd 后，进入命令行后，输入执行命令进行安装。执行命令如下所示：

pip install -r D:\requirements.txt

注：

1）该示例在 windows 环境中进行。

2）输入执行命令时，需根据 txt 文件位置在执行命令中补充完整文件的绝对路径。

2.1.3 下载demo

您可以根据企业自身需求，自己开发编写出对应的 Python 代码。简道云也为您提供了对应的 Python demo 示例供您参考：Python 代码示例工程。

2.2 在简道云中配置单点登录

本文自定义接口中的相关配置，是以本地登录进行演示。企业可根据自身的服务器配置对应的登录信息，服务器信息配置完成后，即可实现企业内成员登录的效果。

2.2.1 开启单点登录

1）登录 简道云账号，进入「账户中心 >> 管理后台」页面中。

2）在「管理工具 >> 企业设置 >> 企业安全」处，打开单点登录的开关，并点击「配置」按钮。

2.2.2 配置单点登录

单点登录配置项如下所示：

单点登录配置方式：自定义接口
Idp登录接口：http://127.0.0.1:8080/sso
认证密钥：可点击「生成密钥」按钮，生成对应的密钥。
认证加密算法：下拉框内选择 HS256
Issuer URL：自定义设置对应内容，如：Issuer.test
IdP 登出接口：自定义设置对应登出接口地址，如：https://www.jiandaoyun.com
配置完成后点击「保存」。

注：

1）除了系统自动生成密钥外，您也可以自定义密钥内容，保证自定义接口配置与 Python demo中的密钥一致即可。

2）认证加密算法支持 HS256、HS384、HS512，Python demo 中默认为 HS256。

2.2.3 生成单点登录信息

完成单点登录配置后，会生成如下对应信息：

注：需要根据生成的信息去修改代码中的相关内容，故可以暂时不关闭此页面。

2.3 修改并运行demo

根据【2.1.3 下载demo】中的内容，下载好 Python 代码后，通过软件 Pycharm 打开 demo，并按照以下步骤修改demo 中的内容。

2.3.1 修改ACS信息

将【2.2.3 生成单点登录信息】中的「认证返回地址」，复制在代码中的 ACS 处。如下所示：

2.3.2 修改SECRET和ISSUER

1）根据【2.2.2 配置单点登录】中的信息，对代码进行如下所示的修改：

将「认证密钥」复制在代码中的 SECRET 处；
将「Issuer URL」中的内容复制在代码中的 ISSUER 处。

2）若简道云的自定义接口处，未配置 Issuer URL相关内容，则代码中对应的 ISSUER 留空，并且注释掉 audience和 iss 这两行代码。如下所示：

2.3.3 配置成员账号

1）进入「简道云 >> 通讯录 >> 内部组织」页面中，点击需要配置单点登录成员的姓名，在成员信息详情页中，查看并复制成员编号。

2）将查看到的成员编号，复制到代码中的 USERNAME 处。如下所示：

2.3.4 修改algorithm内容

根据【2.2.2 配置单点登录】中的信息，将「认证加密算法」复制在代码中的 algorithm 处。如下所示：

2.3.5 配置登录重定向

登录后自动重定向参数，即登录后跳转到指定地址。如设置成员通过单点登录后，直接跳转至定价页面，则修改redirect_uri 为：https://www.jiandaoyun.com/index/price/。

2.3.6 运行代码

代码全部修改完后，在代码页面点击鼠标右键，选择「Run 'sso_pydemo'」后运行代码。

2.4 效果演示

效果参见本文【1.3 预期效果】。


---

## CAS接口配置

- 官方文档：https://hc.jiandaoyun.com/open/18405

1. 简介

1.1 功能简介

CAS，即中央身份验证服务，是网络的单点登录/单点登录协议。它允许用户访问多个应用程序，同时仅向中央CAS 服务器应用程序提供一次凭据（如用户名和密码）。

1.2 使用场景

适用于员工需要访问多个内部系统的场景当中，那么通过单点登录，员工只需登录一次，即可访问所有相关系统，提高工作效率，简化工作流程，减少登录的复杂性。

如学生和教职员工可能需要访问学校门户、学生信息系统、在线课程等多个系统；
医疗管理系统中，医生和医护人员可能需要访问患者记录、医疗历史、预约系统等。
1.3 预期效果

以通过帆软通行证单点登录至简道云为例，效果如下所示：

2. 设置步骤

2.1 设置入口

1）登录 简道云账号，进入「企业管理 >> 管理工具 >> 企业设置」页面中。

2）在「企业安全 >> 单点登录」处，打开单点登录的开关，并点击「配置」按钮。

2.2 选择配置方式

进入配置单点登录详情页中，选择单点登录配置方式为「CAS」。如下所示：

2.3 设置Idp登录接口

Idp 登录接口，指的是通过开发人员部署所需的基础内容，允许用户登录系统的接口。通常用于需要验证用户身份并且允许用户访问系统的场景当中。详情可参见文档：Idp 配置说明。

在简道云的单点登录中，您可以根据企业自身的服务器配置，设置登录接口：

2.4 成员编号设置

在「通讯录 >> 内部组织」处，点击需要通过单点登录的成员信息，进入成员信息编辑界面，修改成员编号，从而保证成员所需要登录的各个平台中的成员编号相同。如下所示：

注：简道云中的成员编号仅能修改一次，请确认成员编号无误后再进行修改。

2.5 效果演示

效果参见本文【1.3 预期效果】。

3. 注意事项

简道云目前支持 V2、V3 版本的 CAS 协议。

---

## 简道云 CAS 单点登录配置调整说明

- 官方文档：https://hc.jiandaoyun.com/doc/27308

尊敬的简道云用户：

简道云将在 11.9.0 版本中进行品牌和架构升级，届时平台登录服务将统一迁移至 portal.finecloud.com。

如果您的企业当前使用 CAS 单点登录，请企业管理员在 11.9.0 版本更新后（2026年9月14日晚）及时完成相关配置调整。若未及时完成，可能导致企业成员无法通过单点登录访问简道云。简道云账号密码等其他登录方式是否可用，以企业当前登录设置为准。

本次调整为简道云多产品平台登录服务的最终架构形态。完成配置后，短期内无需再次修改相关域名。如您在调整过程中遇到问题，请通过客服提交反馈，我们将协助处理。

尊敬的简道云用户：

简道云将在 11.9.0 版本中进行品牌和架构升级，届时平台登录服务将统一迁移至 portal.finecloud.com。

如果您的企业当前使用 CAS 单点登录，请企业管理员在 11.9.0 版本更新后（2026年9月14日晚）及时完成相关配置调整。若未及时完成，可能导致企业成员无法通过单点登录访问简道云。简道云账号密码等其他登录方式是否可用，以企业当前登录设置为准。

本次调整为简道云多产品平台登录服务的最终架构形态。完成本次配置后，短期内无需再次修改相关登录域名。

1. 需要调整的内容

如果您的企业使用开源 CAS 框架，并通过 serviceId 限制允许接入 CAS 的服务地址，需要同步修改对应的 serviceId。根据当前配置方式，通常分为以下两种情况。

情况一：serviceId 仅限制域名

如果当前 serviceId 仅限制到简道云相关域名，例如：

"serviceId": "^https?://www\.jiandaoyun.com.*"

原始配置通常类似下图：

请将原域名修改为新的平台域名：

"serviceId": "^https?://portal\.finecloud\.com.*"

即将原 jiandaoyun.com 替换为 portal.finecloud.com。

情况二：serviceId 限制到具体 URL

如果当前 serviceId 中除域名外，还包含 /sso/cas/... 等具体路径，例如：

"serviceId": "^https?://www\.jiandaoyun.com/sso/cas/66500473530c8e182de72154.*"

原始配置通常类似下图：

此类配置需要先获取您企业的租户 ID，再修改为新的完整 CAS 地址：

"serviceId": "^https?://portal\.finecloud\.com/portal/tenant/{tenantId}/sso/cas.*"

其中 {tenantId} 请替换为您企业实际的租户 ID。

例如：

"serviceId": "^https?://portal\.finecloud\.com/portal/tenant/589815XXXXXXX9b51db/sso/cas.*"

请勿直接使用示例中的租户 ID。

2. 如何判断自己是否需要修改 serviceId

如果您不确定企业是否使用了上述配置，可联系负责 CAS 服务的 IT 管理员检查 {service-name}.json 或对应的 CAS Service Registry 配置：

如果 serviceId 仅配置到原简道云域名，请按照“情况一”修改；
如果 serviceId 配置到了具体 /sso/cas/... 地址，请按照“情况二”修改；
如果未通过 serviceId 对简道云服务地址进行限制，则无需进行这一项额外修改。
3. 操作时间

请在 2026年9月14日晚 11.9.0 版本更新完成后进行配置调整。

修改完成后，请使用企业成员账号重新发起一次 CAS 单点登录，确认可以正常进入简道云。

本次调整仅影响简道云在线 SaaS 环境，简道云独享版暂不受影响。

如您在配置过程中遇到问题，请通过简道云客服提交反馈，我们将协助处理。

简道云团队

2026年9月8日

---

## 简道云 SAML 单点登录配置调整说明

- 官方文档：https://hc.jiandaoyun.com/doc/27309

尊敬的简道云用户：

简道云将在 11.9.0 版本中进行品牌和架构升级，届时平台登录服务将统一迁移至 portal.finecloud.com。

如果您的企业当前使用 SAML 单点登录对接 Microsoft Entra ID，请企业管理员在 11.9.0 版本更新后（2026年9月14日晚）及时完成相关配置调整。若未及时完成，可能导致企业成员无法通过单点登录访问简道云。简道云账号密码等其他登录方式是否可用，以企业当前登录设置为准。

本次调整为简道云多产品平台登录服务的最终架构形态。完成配置后，短期内无需再次修改相关域名。如您在调整过程中遇到问题，请通过客服提交反馈，我们将协助处理。

1. 配置调整说明

请进入 Microsoft Entra 管理中心，找到简道云对应的企业应用，进入「单一登录 > SAML > 基本 SAML 配置」，修改以下两个地址：

标识符（实体 ID）
回复 URL（断言使用者服务 URL）
本次仅需将地址中的原域名 www.jiandaoyun.com 替换为 portal.finecloud.com，企业租户 ID 及后续路径保持不变。

修改前

标识符（实体 ID）：https://www.jiandaoyun.com/portal/tenant/{tenantId}/sso/saml/iss

回复 URL（断言使用者服务 URL）：https://www.jiandaoyun.com/portal/tenant/{tenantId}/sso/saml/acs

修改后

标识符（实体 ID）：https://portal.finecloud.com/portal/tenant/{tenantId}/sso/saml/iss

回复 URL（断言使用者服务 URL）：https://portal.finecloud.com/portal/tenant/{tenantId}/sso/saml/acs

其中，{tenantId} 为您企业原配置中的租户 ID，无需重新查询或修改。

2. 完成配置并验证

完成上述修改后，请保存配置，并使用企业成员账号进行一次 SAML 单点登录测试，确认能够正常访问简道云。

本次仅涉及“标识符（实体 ID）”和“回复 URL（断言使用者服务 URL）”两项配置，登录 URL、中继状态、注销 URL 等其他配置无需修改。

3. 操作时间

请在 2026年9月14日晚 11.9.0 版本更新完成后进行配置调整。

修改完成后，请使用企业成员账号重新发起一次 SAML单点登录，确认可以正常进入简道云。

本次调整仅影响简道云在线 SaaS 环境，简道云独享版暂不受影响。

如您在配置过程中遇到问题，请通过简道云客服提交反馈，我们将协助处理。感谢您的理解与配合。

简道云团队

2026年9月8日
