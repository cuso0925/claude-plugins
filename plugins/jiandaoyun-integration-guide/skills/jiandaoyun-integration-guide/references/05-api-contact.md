# 通讯录 / 角色 / 企业互联接口

> 来源：简道云官方文档（hc.jiandaoyun.com），提取日期 2026-09-10。以下为原文摘录，参数细节以官方页面为准。


---

## 通讯录接口

- 官方文档：https://hc.jiandaoyun.com/open/11493

1. 开发准备

开发前，请仔细阅读 开发指南。

2. 实体结构

2.1 部门实体结构（department）

属性

 | 类型

 | 含义

 | 备注

 |
dept_no

 | Number

 | 部门编号，企业内唯一

 | 不同企业之间可能存在重复

 |
name

 | String

 | 部门名称

 |

 |
parent_no

 | Number

 | 父部门编号

 | 在企业互联接口中(外部部门)不存在

 |
type

 | Number

 | 部门类型

 | 0: 常规部
2: 企业互联外部部门
 |
status

 | Number

 | 部门状态

 | 1: 使用中的部门
-1: 集成模式下同步后删除的部门
 |
integrate_id

 | String

 | 集成模式同步部门关联 ID

 | 仅在集成模式下返回，且在企业互联接口(外部部门)不返回

 |
seq

 | number

 | 部门排序

 | 部门在父部门内的序号，从小到大排列

 |
2.2 成员实体结构（user）

属性

 | 类型

 | 含义

 | 备注

 |
username

 | String

 | 成员编号，企业内唯一

 | 不同企业之间可能存在重复

 |
name

 | String

 | 昵称

 |

 |
departments

 | Number[]

 | 成员所在部门编号列表

 |

 |
type

 | Number

 | 成员类型

 | 0: 常规成员
2: 企业互联外部对接人
 |
status

 | Number

 | 成员状态

 | 0: 未确认的成员
1: 已加入
 |
integrate_id

 | String

 | 集成模式同步成员关联 ID

 | 仅在集成模式下返回，且在企业互联接口(外部对接人)不返回

 |
2.3 角色实体结构 (role)

属性

 | 类型

 | 含义

 | 备注

 |
role_no

 | Number

 | 角色编号，企业内唯一

 | 不同企业之间可能存在重复

 |
group_no

 | Number

 | 角色组编号，企业内唯一

 | 不同企业之间可能存在重复

 |
name

 | String

 | 角色名称

 |

 |
type

 | Number

 | 角色类型

 | 0: 常规角色
2: 企业互联外部角色
 |
status

 | Number

 | 角色状态

 | 1:使用中

 |
integrate_id

 | String

 | 集成模式同步成员关联 ID

 | 仅在集成模式下返回，且在企业互联接口(外部对接人)不返回

 |
2.4 角色组实体结构 (role_group)

属性

 | 类型

 | 含义

 | 备注

 |
group_no

 | Number

 | 角色组编号, 企业内唯一

 | 不同企业之间可能存在重复

 |
name

 | String

 | 角色组名称

 |

 |
type

 | Number

 | 角色组类型

 | 0: 常规角色组
2: 企业互联外部角色组
 |
status

 | Number

 | 角色组状态

 | 1: 使用中

 |
integrate_id

 | String

 | 集成模式同步角色组关联 ID

 | 仅在集成模式下(飞书除外)，同步的角色组返回

 |
3. 版本说明

当前接口不同版本的主要区别:

接口类型

 | v1

 | v2

 | v4

 | v5

 |
成员

 | 使用 _id 作为 id

 | 使用 username 作为 id

 | 返回值新增字段 type、status、integrate_id

 | 在 v4 的基础上，接口请求频率提升。

 |
部门

 | 使用 _id 作为id

 | 使用 dept_no 作为 id

 | 返回值新增字段 type、status、integrate_id

 | 在 v4 的基础上，接口请求频率提升。

 |
角色

 | 无

 | 角色使用 role_no

角色组使用 group_no

包含 integrate_id、type 字段

 | 返回值新增字段 status

 | 在 v4 的基础上，接口请求频率提升。

 |
企业互联

 | 无

 | 无

 | 成员使用 username

部门使用 dept_no

包含 type、status 字段

 | 在 v4 的基础上，接口请求频率提升。

 |
4. 注意事项

1）每个通讯录都是一棵部门树，且根部门的部门编号都是 1。

2）对公共模式模式和集成模式支持的程度不同，会在每个接口上备注。

3）由于企业微信/钉钉与简道云通讯录的当前部门规则一致，因此 integrate_id 与 dept_no 的值暂时保持一致；而飞书平台的部门 ID 是由字符串组成，因此与简道云通讯录的部门 dept_no 不一致。integrate_id 与 dept_no 的含义不同，后续更新中不保证使用相同的值，使用时须加以区分。

本章内容：

成员接口
部门接口
角色接口
角色组接口
企业互联接口


---

## 成员接口

- 官方文档：https://hc.jiandaoyun.com/open/11504

1. 简介

成员接口是可以对通讯录成员进行查询、添加、修改等一系列操作的接口。

开发前，请仔细阅读 开发指南（内含错误码对照表）。

2. 接口列表

成员接口主要包括以下接口：

接口名称

 | 释义

 |
获取成员信息接口

 | 根据 username 获取指定成员的名称和部门编号。支持公共模式和集成模式。

 |
添加成员接口

 | 在指定部门下添加一位成员，该成员用户自动激活（可直接通过单点登录进行访问，并且会占用1个用户数），但是没有手机、邮箱和密码等个人注册信息。仅支持公共模式。

 |
修改成员接口

 | 修改指定成员的信息，比如部门、昵称。仅支持公共模式。

 |
删除成员接口

 | 从通讯录中删除指定成员编号的用户。仅支持公共模式。

 |
批量删除成员接口

 | 对成员进行批量删除。（仅支持公共模式）

 |
增量导入成员接口

 | 本接口以企业内的 username（用户编号）为主键，更新创建企业成员。（仅支持公共模式）

 |


---

## 获取成员信息接口

- 官方文档：https://hc.jiandaoyun.com/open/18509

1. 简介

1.1 接口简介

根据 username 获取指定成员的名称和部门编号。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

参数 username 放入body，接口路由修改为 POST corp/user/get

 |
2. 接口调用

该接口可以根据 username 获取指定成员的名称和部门编号。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/user/get

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 必需

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 成员编号

 |
请求示例：

{
    "username": "jiandaoyun"
}

响应内容：

参数

 | 含义

 |
user

 | 成员信息，同单个成员的返回数据结构

 |
响应示例：

{
  "user": {
    "username": "jiandaoyun",
    "name": "小云",
    "departments": [1,3],
    "type": 0,
    "status": 1,
    "integrate_id": "jiandaoyun"
  }
}


---

## 添加成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18510

1. 简介

1.1 接口简介

在指定部门下添加一位成员，该成员用户自动激活（可直接通过单点登录进行访问，并且会占用1个用户数），但是没有手机、邮箱和密码等个人注册信息。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/user/create

 |
2. 接口调用

在指定部门下添加一位成员，该成员用户自动激活（可直接通过单点登录进行访问，并且会占用1个用户数），但是没有手机、邮箱和密码等个人注册信息。仅支持公共模式。

请求地址： https://api.jiandaoyun.com/api/v5/corp/user/create

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
name

 | 是

 | String

 | 昵称

 |
departments

 | 否

 | Number[]

 | 用户所属部门列表

 |
username

 | 否

 | String

 | 成员编号（成员编号仅支持字母、数字和下划线）

 |
请求示例：

{
    "username": "jiandaoyun",
    "name": "小云",
    "departments": [1, 3]
}

响应内容：

参数

 | 类型

 | 说明

 |
user

 | Json

 | 新添加的该成员信息，同 单个成员的返回数据结构

 |
响应示例：

{
  "user": {
    "username": "jiandaoyun",
    "name": "小云",
    "departments": [1,3],
    "type": 0,
    "status": 1
  }
}


---

## 修改成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18511

1. 简介

1.1 接口简介

修改指定成员的信息，比如部门、昵称。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 username 放入body，接口路由修改为 POST corp/user/update

 |
2. 接口调用

修改指定成员的信息，比如部门、昵称。仅支持公共模式。

注：成员编号不允许修改。

请求地址：https://api.jiandaoyun.com/api/v5/corp/user/update

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 成员编号

 |
name

 | 否

 | String

 | 昵称

 |
departments

 | 否

 | Number[]

 | 用户所属部门列表

 |
请求示例：

{
    "username": "jiandaoyun",
     "name": "小云",
    "departments": [4]
}

响应内容：

参数

 | 类型

 | 说明

 |
user

 | Json

 | 修改后的该成员信息，同 单个成员的返回数据结构。

 |
响应示例：

{
  "user": {
    "username": "jiandaoyun",
    "name": "小云",
    "departments": [1,3],
    "type": 0,
    "status": 1
  }
}


---

## 删除成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18512

1. 简介

1.1 接口简介

从通讯录中删除指定成员编号的用户。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

参数 username 放入body，接口路由修改为 POST corp/user/delete

 |
2. 接口调用

从通讯录中删除指定成员编号的用户。仅支持公共模式。

请求地址： https://api.jiandaoyun.com/api/v5/corp/user/delete

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 必需

 | 类型

 | 说明

 |
username

 | 是

 | String

 | 成员编号

 |

请求示例：

{
    "username": "jiandaoyun"
}

响应参数：

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

注：删除成员即将在职成员转离职，并不是彻底删除。转离职成员的成员可以在 离职成员管理 页面进行管理。


---

## 批量删除成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18513

1. 简介

1.1 接口简介

对成员进行批量删除。（仅支持公共模式）

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

接口路由修改为 POST corp/user/batch_delete

 |
2. 接口调用

对成员进行批量删除。（仅支持公共模式）

请求地址：https://api.jiandaoyun.com/api/v5/corp/user/batch_delete

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
usernames

 | 是

 | Array

 | 成员编号列表

 |
请求示例：

{
    "usernames": ["tester", "developer"]
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

注：删除成员即将在职成员转离职，并不是彻底删除。转离职成员的成员可以在 离职成员管理 页面进行管理。


---

## 增量导入成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18514

1. 简介

1.1 接口简介

本接口以企业内的 username（成员编号）为主键，更新创建企业成员。（仅支持公共模式）

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 username 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

接口路由修改为 POST corp/user/import

 |
2. 接口调用

本接口以企业内的 username（成员编号）为主键，更新创建企业成员。（仅支持公共模式）

请求地址：https://api.jiandaoyun.com/api/v5/corp/user/import

请求频率：10 次/秒

请求方式：POST

注意事项：

成员编号在企业内唯一，仅支持由字母、数字、下划线组成；
成员昵称最长为 80 个字符；
所有成员必须在部门下，如果导入成员不存在部门，则会移动到根部门下；
通过该接口导入的成员会自动激活，且没有邮箱、密码、手机号等信息，可以配合 单点登录 功能实现企业用户登录；
如果导入数据存在，但是现有企业通讯录中不存在该成员，则新建成员；
如果导入数据存在，且现有企业通讯录中存在该成员，则更新成员信息；
该接口不会执行删除成员操作；
该接口每次调用允许导入的成员数为 20000；
该接口调用执行期间，将无法同时调用其他对通讯录的修改、删除、新增接口。
请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
users

 | 是

 | Json[]

 | 成员列表

 |
users[].username

 | 是

 | String

 | 成员编号

 |
users[].name

 | 是

 | String

 | 昵称

 |
users[].departments

 | 是

 | Number[]

 | 所在部门编号列表

 |
请求示例：

{
    "users": [{
        "username": "coding_master",
        "name": "小简",
        "departments": [1, 3]
    }]
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

## 部门接口

- 官方文档：https://hc.jiandaoyun.com/open/11505

1. 简介

部门接口是可以对通讯录部门组织进行新增、删除、修改、查询等一系列操作的接口。

开发之前，请仔细阅读 开发指南（内含错误码对照表）。

2. 接口列表

部门接口主要包括以下接口：

接口名称

 | 释义

 |
（递归）获取部门成员接口

 | 能够（递归）获取指定部门 id 下的所有成员。支持公共模式和集成模式。

 |
（递归）获取部门列表接口

 | 能够（递归）获取指定部门 id 的所有子部门。支持公共模式和集成模式。

 |
创建部门接口

 | 创建一个新部门。仅支持公共模式。

 |
修改部门接口

 | 修改指定部门的部门信息。仅支持公共模式。

 |
删除部门接口

 | 将指定部门从通组织架构接中移除。仅支持公共模式。

 |
获取集成模式部门编号接口

 | 本接口可以通过第三方平台的通讯录部门的 ID 获取其对应的简道云通讯录部门编号。仅支持集成模式。

 |
全量导入部门接口

 | 本接口以 dept_no（部门编号）为主键，全量覆盖企业内的通讯录部门树。仅支持公共模式。

 |


---

## （递归）获取部门成员接口

- 官方文档：https://hc.jiandaoyun.com/open/18515

1. 简介

1.1 接口简介

能够（递归）获取指定部门编号下的所有成员。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 10 次每秒；

参数 dept_no 放入 body，接口路由修改为 POST corp/department/user/list

 |
2. 接口调用

能够（递归）获取指定部门 id 下的所有成员。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/department/user/list

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
dept_no

 | Number

 | 是

 | 部门编号

 |
has_child

 | Boolean

 | 否

 | 是否递归获取所有成员。默认为 false，即只获取当前部门下的成员，而不获取其子部门的成员。

 |
请求示例：

{
   "dept_no":1,
  "has_child": true
}

响应内容：

参数

 | 含义

 |
users

 | 当前指定部门下的成员列表

 |
单个成员的返回数据结构：

参数

 | 含义

 | 备注

 |
name

 | 昵称

 | name 可以重复，重名成员的name相同

 |
username

 | 成员编号

 | username 在企业内是唯一的，不同企业之间可能存在重复

 |
departments

 | 用户所属的部门编号列表

 |

 |
type

 | 部门类型

 | 0: 常规部门
2: 企业互联外部部门
 |
status

 | 部门状态

 | 1: 使用中的部门
-1: 集成模式下同步后删除的部门
 |
integrate_id

 | 集成模式同步部门关联 ID

 | 仅在集成模式下返回，且在企业互联接口(外部对接人)不返回

 |
响应示例：

{
  "users": [
    {
      "username": "aubrey",
      "name": "aubrey",
      "departments": [1],
      "type": 0,
      "status": 1
    }
  ]
}


---

## （递归）获取部门列表接口

- 官方文档：https://hc.jiandaoyun.com/open/18516

1. 简介

1.1 接口简介

能够（递归）获取指定部门 id 的所有子部门。支持公共模式和集成模式。

1.2 接口版本

接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 10 次每秒；

参数 dept_no 放入 body，接口路由修改为 POST corp/department/list

 |
v6

 | 2022.08.01

 | 部门实体结构 中，新增响应参数 seq，支持对部门进行排序

 |
2. 接口调用

能够（递归）获取指定部门编号的所有子部门。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v6/corp/department/list

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
dept_no

 | 是

 | Number

 | 部门编号

 |
has_child

 | 否

 | Boolean

 | 是否递归获取所有子部门。默认为 false，即只获取一级子部门。

 |
请求示例：

递归获取当前企业的根部门下所有部门列表。 注：数字 1 为根部门编号。

{
  "dept_no": 1,
  "has_child": true
}

响应内容：

参数

 | 类型

 | 说明

 |
departments

 | Array

 | 当前指定部门下的子部门列表，值结构同 部门实体结构

 |
响应示例：

{
  "departments": [
    {
      "dept_no": 3,
      "name": "销售部",
      "parent_no": 1,
      "type": 0,
      "status": 1
    },
    {
      "dept_no": 33,
      "name": "华东区销售小组",
      "parent_no": 3,
      "type": 0,
      "status": 1,
      "seq": 2
    }
  ]
}


---

## 创建部门接口

- 官方文档：https://hc.jiandaoyun.com/open/18517

1. 简介

1.1 接口简介

创建一个新部门。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 20 次每秒；

接口路由修改为 POST corp/department/create

 |
v6

 | 2023.08.01

 | 新增响应参数 seq，支持对部门进行排序

 |
2. 接口调用

创建一个新部门。仅支持公共模式。

请求地址：https://api.jiandaoyun.com/api/v6/corp/department/create

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
name

 | 是

 | String

 | 部门名称（最多不超过 50 个字符）

 |
parent_no

 | 否

 | Number

 | 父部门编号，不传默认为根部门

 |
dept_no

 | 否

 | Number

 | 部门编号，不传自动生成（上限 9007199254740991）

 |
请求示例：

{
    "name": "研发部门",
    "parent_no": 1,
    "dept_no": 2
}

响应内容：

参数

 | 类型

 | 说明

 |
department

 | Json

 | 创建的部门信息。同 部门实体结构

 |
dept_no

 | Number

 | 部门编号

 |
name

 | String

 | 部门名称

 |
parent_no

 | Number

 | 父部门编号

 |
type

 | Number

 | 部门类型

 |
status

 | Number

 | 部门状态

 |
integrate_id

 | String

 | 集成模式同步部门关联 ID，仅在集成模式下返回，且在企业互联接口(外部对接人)不返回

 |
seq

 | number

 | 部门排序

 |
响应示例：

{
  "department": {
    "dept_no": 2,
    "name": "研发部门",
    "parent_no": 1,
    "type": 0,
    "status": 1
    "seq": 1
  }
}


---

## 修改部门接口

- 官方文档：https://hc.jiandaoyun.com/open/18518

1. 简介

1.1 接口简介

修改指定部门的部门信息。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 20 次每秒；

参数 dept_no 放入 body，接口路由修改为 POST corp/department/update

 |
v6

 | 2023.08.01

 | 新增请求参数和响应参数seq，支持进行部门排序。

 |
2. 接口调用

修改指定部门的部门信息。仅支持公共模式。

请求地址：https://api.jiandaoyun.com/api/v6/corp/department/update

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
name

 | 否

 | String

 | 部门名称

 |
parent_no

 | 否

 | Integer

 | 上级部门编号

 |
dept_no

 | 是

 | Number

 | 部门编号

 |
seq

 | 否

 | number

 | 部门排序

 |
注：请求参数中的 name 、 parent_no 和 seq 至少填写一个。

请求示例：

{
    "dept_no": 3,
    "name": "测试部门",
    "parent_no": 1,
    "seq": 1
}

响应内容：

参数

 | 类型

 | 说明

 |
department

 | Json

 | 创建的部门信息

 |
department.dept_no

 | Number

 | 部门编号

 |
department.name

 | String

 | 部门名称

 |
department.parent_no

 | Number

 | 父部门编号

 |
type

 | Number

 | 部门类型

 |
status

 | Number

 | 部门状态

 |
integrate_id

 | String

 | 集成模式同步部门关联 ID，仅在集成模式下返回，且在企业互联接口(外部对接人)不返回

 |
seq

 | number

 | 部门排序

 |
响应示例：

{
  "department": {
    "dept_no": 3,
    "name": "测试部门",
    "parent_no": 2,
    "type": 0,
    "status": 1
    "seq": 1
  }
}


---

## 删除部门接口

- 官方文档：https://hc.jiandaoyun.com/open/18519

1. 简介

1.1 接口简介

将指定部门从通组织架构接中移除。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 20 次每秒；

参数 dept_no 放入 body，接口路由修改为 POST corp/department/delete

 |
2. 接口调用

将指定部门从通组织架构接中移除。仅支持公共模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/department/delete

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
dept_no

 | Number

 | 是

 | 部门编号

 |
请求示例：

{
    "dept_no": 1
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

## 获取集成模式部门编号接口

- 官方文档：https://hc.jiandaoyun.com/open/18520

1. 简介

1.1 接口简介

本接口可以通过第三方平台的通讯录部门的 ID 获取其对应的简道云通讯录部门编号。仅支持集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 30 次每秒；

接口路由修改为 POST corp/department/dept_no/get

 |
v6

 | 2022.08.01

 | 部门实体结构 中，新增响应参数 seq，支持对部门进行排序。

 |
2. 接口调用

在集成模式下，企业通讯录的部门是同步自第三方平台通讯录的，因此简道云通讯录的部门与第三方平台的通讯录部门之间存在着一一对应的关系。

本接口可以通过第三方平台的通讯录部门的 ID 获取其对应的简道云通讯录部门编号。仅支持集成模式。

请求地址：https://api.jiandaoyun.com/api/v6/corp/department/dept_no/get

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
integrate_id

 | 是

 | String

 | 第三方平台通讯录的部门 ID，如钉钉/企业微信/飞书的通讯录部门 ID。

 |
请求示例：

{
     "integrate_id": "1005"
}

响应内容：

参数

 | 类型

 | 说明

 |
department

 | json

 | 返回部门编号。同 部门实体结构。

 |
响应示例：

{
  "department": {
    "dept_no": 1005,
    "name": "产品部门",
    "parent_no": 2,
    "type": 0,
    "status": 1,
    "integrate_id": "1005"
    "seq": 1
  }
}

注：由于企业微信/钉钉与简道云通讯录的当前部门规则一致，因此 integrate_id 与 dept_no 的值是保持一致的，并不一定需要使用此接口；而飞书平台的部门 ID 是由字符串组成，因此与简道云通讯录的部门 ID 不一致，需要使用此接口。


---

## 全量导入部门接口

- 官方文档：https://hc.jiandaoyun.com/open/18521

1. 简介

1.1 接口简介

本接口以 dept_no（部门编号）为主键，全量覆盖企业内的通讯录部门树。仅支持公共模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v1

 | 2018.12.4

 | 使用 _id 作为 id

 |
v2

 | 2019.6.21

 | 使用 dept_no 作为 id

 |
v4

 | 2022.6.30

 | 返回值新增字段 type、status、integrate_id

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次每秒提升至 10 次每秒；

接口路由修改为 POST corp/department/import

 |
2. 接口调用

本接口以 dept_no（部门编号）为主键，全量覆盖企业内的通讯录部门树。仅支持公共模式。

接口地址：https://api.jiandaoyun.com/api/v5/corp/department/import

请求频率：10 次/秒

请求方式：POST

注意事项：

1）部门编号为数字类型且唯一。

2）除了根部门以外所有部门的父部门必须存在。如果新导入列表中不存在根部门, 则会自动插入根部门, 且部门名称为企业名称。

3）同级部门名称不能有重复。

4）部门层级不能超过 16 级。

5）如果导入数据存在，且现有企业通讯录中也存在，则更新该部门的信息。

6）如果导入数据存在，而现有企业通讯录中不存在，则新建该部门。

7）如果导入数据不存在，但现有企业通讯录中存在，则继续判断该部门下是否存在子部门和成员，如果都没有则自动删除该部门，否则将子部门和成员转移到根部门下继续保留。

8）该接口允许导入的部门数上限为 100000。

9）该接口调用执行期间，将无法同时调用其他对通讯录的修改、删除、新增接口。

请求参数：

参数

 | 是否必需

 | 类型

 | 说明

 |
departments

 | 是

 | Array

 | 部门列表

 |
departments[].dept_no

 | 是

 | Number

 | 部门编号（上限 9007199254740991）

 |
departments[].name

 | 是

 | String

 | 部门名称

 |
departments[].parent_no

 | 否

 | Number

 | 父部门编号，不传默认为根部门下

 |
请求示例：

{
    "departments": [{
        "dept_no": 11,
        "name": "研发部门",
        "parent_no": 1
    }, {
     "dept_no": 12,
     "name": "测试部门",
     "parent_no": 1
    }]
}

注：在使用批量导入部门的 API 接口时，在传入新部门的同时，还需要写入新部门的根部门，以保证部门树结构的完整性。

例如，想在 SSO_dept 这个部门下插入一个新的子部门，如果只传新部门的话，会报错父部门不存在。

此时需要把 SSO_dept 部门也传一下，即使该部门已经存在了，但为了树结构的完整性以及新部门的准确插入，需要再次写入。

最终效果如下：

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

## 获取部门主管列表接口

- 官方文档：https://hc.jiandaoyun.com/open/25948

1. 简介

1.1 接口简介

获取指定部门下的主管成员列表

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v6

 | 2026.06.12

 | 原始接口

 |
2. 接口调用

获取指定部门下的主管成员列表。

请求地址：https://api.jiandaoyun.com /api/v6/corp/department/manager/get

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
dept_no

 | number

 | 是

 | 部门编号

 |
请求示例：

{
  "dept_no": 1
}

响应内容：

参数

 | 类型

 | 说明

 |
dept_managers

 | array

 | 部门主管成员列表

 |
成员对象字段

字段

 | 类型

 | 说明

 |
username

 | string

 | 成员用户名

 |
name

 | string

 | 成员昵称

 |
departments

 | number[]

 | 所属部门编号列表

 |
type

 | number

 | 成员类型：

0：常规成员
2：企业互联外部对接人
注：部门主管只能是内部成员，所以该接口中返回值仅会为 0。

 |
status

 | number

 | 成员状态

0：未确认的成员
1：已加入
 |
integrate_id

 | string

 | 第三方平台集成 ID（仅集成模式企业返回）

 |
响应示例：

{
  "dept_managers": [
    {
      "username": "zhangsan",
      "name": "张三",
      "departments": [1, 2],
      "type": 0,
      "status": 1
    }
  ]
}


---

## 设置部门主管接口

- 官方文档：https://hc.jiandaoyun.com/open/25949

1. 简介

1.1 接口简介

设置指定部门的主管成员，以全量覆盖方式更新。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v6

 | 2026.06.12

 | 原始接口

 |
2. 接口调用

设置指定部门的主管成员，以全量覆盖方式更新。

请求地址：https://api.jiandaoyun.com/api/v6/corp/department/manager/update

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 必填

 | 说明

 |
dept_no

 | number

 | 是

 | 部门编号

 |
managers

 | string[]

 | 是

 | 主管成员用户名列表，传入空数组 [] 可清空所有主管

 |

请求示例：

{
  "dept_no": 1,
  "managers": ["zhangsan", "lisi"]
}

响应内容：

参数

 | 类型

 | 说明

 |
dept_managers

 | array

 | 部门主管成员列表

 |
成员对象字段：

字段

 | 类型

 | 说明

 |
username

 | string

 | 成员用户名

 |
name

 | string

 | 成员昵称

 |
departments

 | number[]

 | 所属部门编号列表

 |
type

 | number

 | 成员类型：

0：常规成员
2：企业互联外部对接人
注：部门主管只能是内部成员，所以该接口中返回值仅会为 0。

 |
status

 | number

 | 成员状态

0：未确认的成员
1：已加入
 |
integrate_id

 | string

 | 第三方平台集成 ID（仅集成模式企业返回）

 |
响应示例：

{
  "dept_managers": [
    {
      "username": "zhangsan",
      "name": "张三",
      "departments": [1, 2],
      "type": 0,
      "status": 1
    },
    {
      "username": "lisi",
      "name": "李四",
      "departments": [1],
      "type": 0,
      "status": 1
    }
  ]
}


---

## 角色接口

- 官方文档：https://hc.jiandaoyun.com/open/14136

1. 简介

角色接口是可以对 通讯录 中的角色进行新增、删除、修改、查询等一系列操作的接口。

开发前，请仔细阅读 开发指南（内含错误码对照表）。

2. 接口列表

角色接口主要包括以下接口：

接口名称

 | 释义

 |
列出角色接口

 | 将角色列出来。支持公共模式和集成模式。

 |
创建一个自建角色

 | 只能创建内部自建角色。支持公共模式和集成模式。

 |
更新一个自建角色

 | 对自建角色进行更新。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

 |
删除一个自建角色

 | 对某个自建角色进行删除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

 |
列出角色下的成员

 | 列出角色下的所有成员信息。支持公共模式和集成模式。

 |
为自建角色批量添加成员

 | 为自建的角色批量添加成员。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

 |
为自建角色批量移除成员

 | 将成员从角色中批量移除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作。

 |


---

## 列出角色接口

- 官方文档：https://hc.jiandaoyun.com/open/18522

1. 简介

1.1 接口简介

将角色列出来。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/role/list

 |
2. 接口调用

将角色列出来。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
skip

 | Number

 | 否

 | 偏移量

 |
limit

 | Number

 | 否

 | limit，不传递时默认值为 1

 |
has_internal

 | Boolean

 | 否

 | 是否包含自建角色默认为 true

 |
has_sync

 | Boolean

 | 否

 | 是否包含集成角色默认为 true

 |
请求示例：

{
    "skip": 0,
    "limit": 3,
    "has_internal": true,
    "has_sync": true
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号

 |
group_no

 | Number

 | 否

 | 角色组编号

 |
name

 | String

 | 是

 | 角色名称

 |
type

 | Number

 | 是

 | 角色类型，若为 0 则表示为常规角色

 |
status

 | Number

 | 是

 | 成员状态：

0: 未确认的成员
1: 已加入
 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
响应示例：

{
    "roles": [
        {
            "role_no": 3,
            "group_no": 2547,
            "name": "设计中心",
            "type": 0,
            "status": 1
        },
        {
            "role_no": 2551,
            "group_no": 2550,
            "name": "销售总监",
            "type": 0,
           "status": 1
        },
        {
            "role_no": 2552,
            "group_no": 2550,
            "name": "销售主管",
            "type": 0,
           "status": 1
        }
    ]
}


---

## 创建一个自建角色

- 官方文档：https://hc.jiandaoyun.com/open/18523

1. 简介

1.1 接口简介

只能创建内部自建角色。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role/create

 |
2. 接口调用

只能创建内部自建角色。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/create

请求频率：20 次/秒

请求方式：POST

请求参数

参数

 | 类型

 | 是否必需

 | 说明

 |
name

 | String

 | 是

 | 角色名称

 |
group_no

 | Number

 | 是

 | 角色组编号

 |
请求示例：

{
    "group_no": 2547,
    "name": "研发中心"
}

响应内容：

参数

 | 类型

 | 是否必须

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号

 |
group_no

 | Number

 | 否

 | 角色组编号

 |
name

 | String

 | 是

 | 角色名称

 |
type

 | Number

 | 是

 | 角色类型：

0 ：常规角色
2 ：外部角色
 |
status

 | Number

 | 是

 | 成员状态：

0: 未确认的成员
1: 已加入
 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
响应示例：

{
  "role": {
    "role_no": 2558,
    "group_no": 2547,
    "name": "研发中心",
    "type": 0,
    "status": 1
  }
}


---

## 更新一个自建角色

- 官方文档：https://hc.jiandaoyun.com/open/18524

1. 简介

1.1 接口简介

对自建角色进行更新。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role/update

 |
2. 接口调用

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/update

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号

 |
group_no

 | Number

 | 是

 | 角色组编号

 |
name

 | String

 | 否

 | 角色名称

 |
请求示例：

{
    "role_no": 2558,
    "group_no": 2547,
    "name": "研发部门"
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号

 |
group_no

 | Number

 | 否

 | 角色组编号

 |
name

 | String

 | 是

 | 角色名称

 |
type

 | Number

 | 是

 | 角色类型：

0 ：常规角色
2 ：外部角色
 |
status

 | Number

 | 是

 | 成员状态：

0: 未确认的成员
1: 已加入
 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
返回示例：

{
  "role": {
    "role_no": 2558,
    "group_no": 2547,
    "name": "研发部门",
    "type": 0,
    "status": 1
  }
}


---

## 删除一个自建角色

- 官方文档：https://hc.jiandaoyun.com/open/18525

1. 简介

1.1 接口简介

对某个自建角色进行删除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role/delete

 |
2. 接口调用

对某个自建角色进行删除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/delete

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号

 |
请求示例：

{
    "role_no": 2558
}

响应内容：

状态码：200。


---

## 列出角色下的成员

- 官方文档：https://hc.jiandaoyun.com/open/18526

1. 简介

1.1 接口简介

列出角色下的所有成员信息。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/role/user/list

 |
2023.10.11

 | 1）新增请求参数：

是否包含分管部门信息：has_manage_range
2）新增响应参数：

角色分管部门编号：departments_range ；
是否包含子部门：has_child。
 |
2. 接口调用

列出角色下的所有成员信息。支持公共模式和集成模式。

注：只会返回邀请中和已激活的成员。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/user/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 位置

 | 是否必需

 | 说明

 |
skip

 | Number

 | 否

 | 分页偏移

 |
limit

 | Number

 | 否

 | 分页大小，最大值为 10000。

 |
role_no

 | Number

 | 是

 | 角色编号

 |
has_manage_range

 | Boolean

 | 否

 | 是否包含分管部门信息，默认值为 false。

 |
请求示例：

{
    "skip": 0,
    "limit": 3,
    "role_no": 72,
    "has_manage_range": True
}

响应内容：

参数

 | 类型

 | 是否必须

 | 说明

 |
username

 | String

 | 是

 | 成员的编号，企业内唯一

 |
name

 | String

 | 是

 | 成员昵称

 |
departments

 | Number[]

 | 是

 | 成员所在部门编号列表

 |
type

 | Number

 | 是

 | 成员类型：

0: 常规成员
2: 企业互联外部对接人
 |
status

 | Number

 | 是

 | 成员状态：

0: 未确认的成员
1: 已加入
 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
departments_range

 | Number[]

 | 否

 | 角色分管部门编号

注：只有配置了分管部门的成员才会显示此参数。

 |
has_child

 | Boolean

 | 否

 | 是否包含子部门

注：只有配置了分管部门的成员才会显示此参数。

 |
返回示例：

{
    "users": [
  {
    "username": "jdy-xulalikdbj82",
    "name": "frank",
    "departments": [212],
    "type": 0,
    "status": 1,
    "deptarments_range": [378,1157],
    "has_child": true
  },
  {
    "username": "R-E9rRNbwL",
    "name": "成员删除1",
    "departments": [338,226],
    "type": 0,
    "status": 1,
    "deptarments_range": [1157],
    "has_child": false
  },
  {
    "username": "UPDATE",
    "name": "testadmin",
    "departments": [1],
    "type": 0,
    "status": 1
  }
   ]
}


---

## 为自建角色批量添加成员

- 官方文档：https://hc.jiandaoyun.com/open/18527

1. 简介

1.1 接口简介

为自建的角色批量添加成员。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

接口路由修改为 POST corp/role/add_members

 |
2. 接口调用

为自建的角色批量添加成员。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作，不支持对第三方同步过来的角色操作。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/add_members

请求频率：10 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必须

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号，示例：3

 |
usernames

 | String[]

 | 是

 | 员工工号

 |
请求示例：

{
    "role_no": 3,
    "usernames": [
         "fr0005",
         "fr008"
    ]
}

响应内容：

参数

 | 类型

 | 是否必须

 | 说明

 |
status

 | String

 | 否

 | 返回请求结果

 |
返回示例：

{
    "status": "success"
}


---

## 为自建角色批量移除成员

- 官方文档：https://hc.jiandaoyun.com/open/18528

1. 简介

1.1 接口简介

将成员从角色中批量移除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id、type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；

接口路由修改为 POST corp/role/remove_members

 |
2. 接口调用

将成员从角色中批量移除。支持公共模式和集成模式， 但集成模式下只支持对自建角色的操作。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role/remove_members

请求频率：10 次/秒

请求方式：POST

请求参数:

参数

 | 类型

 | 是否必须

 | 说明

 |
role_no

 | Number

 | 是

 | 角色编号，示例：3

 |
usernames

 | String[]

 | 是

 | 员工工号

 |
请求示例：

{
    "role_no": 3,
    "usernames": [
        "fr0005",
        "fr008"
    ]
}

响应内容：

参数

 | 类型

 | 是否必须

 | 说明

 |
status

 | String

 | 否

 | 返回请求结果

 |
返回示例：

{
    "status": "success"
}


---

## 角色组接口

- 官方文档：https://hc.jiandaoyun.com/open/14915

1. 简介

角色组接口是可以对 通讯录 中的角色组进行新增、删除、更新、列出等一系列操作的接口。

开发前，请仔细阅读 开发指南（内含错误码对照表）。

2. 接口列表

角色组接口主要包括以下接口：

接口名称

 | 释义

 |
列出自建角色组

 | 将角色组全部拉取出来。支持公共模式和集成模式。

 |
创建自建角色组

 | 通过接口新建角色组。支持公共模式和集成模式。

 |
更新自建角色组

 | 更新创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

 |
删除自建角色组

 | 删除创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

 |


---

## 列出自建角色组

- 官方文档：https://hc.jiandaoyun.com/open/18529

1. 简介

1.1 接口简介

将角色组全部拉取出来。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id, type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/role_group/list

 |
2. 接口调用

将角色组全部拉取出来。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role_group/list

请求频率：30 次/秒

请求方式：POST

请求参数:

参数

 | 类型

 | 是否必需

 | 说明

 |
skip

 | Integer

 | 否

 | 偏移量

 |
limit

 | Integer

 | 否

 | limit

 |
has_internal

 | Boolean

 | 否

 | 是否包含自建角色组

默认为 true

 |
has_sync

 | Boolean

 | 否

 | 是否包含集成角色组

默认为 true

 |
请求示例：

{
    "skip": 0,
    "limit": 3,
    "has_internal": ture,
    "has_sync": ture
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
group_no

 | Number

 | 是

 | 角色组编号

 |
name

 | String

 | 是

 | 角色组名称

 |
type

 | Number

 | 是

 | 角色组类型

0: 常规角色组
2: 企业互联外部角色组
 |
status

 | Number

 | 是

 | 1: 使用中

 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
返回示例：

{
    "role_groups": [
        {
            "group_no": 2547,
            "name": "默认",
            "type": 0
            "status": 1
        },
        {
            "group_no": 2550,
            "name": "CRM角色组",
            "type": 0
            "status": 1
        },
        {
            "group_no": 2556,
            "name": "营销中心",
            "type": 0
            "status": 1
        }
    ]
}


---

## 创建自建角色组

- 官方文档：https://hc.jiandaoyun.com/open/18530

1. 简介

1.1 接口简介

通过接口新建角色组。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id, type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role_group/create

 |
2. 接口调用

通过接口新建角色组。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role_group/create

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
name

 | String

 | 是

 | 角色组名称

 |
请求示例：

{
    "name": "研发中心"
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
group_no

 | Number

 | 是

 | 角色组编号

 |
name

 | String

 | 是

 | 角色组名称

 |
type

 | Number

 | 是

 | 角色组类型

0: 常规角色组
2: 企业互联外部角色组
 |
status

 | Number

 | 是

 | 1: 使用中

 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
响应示例：

{
  "role_group": {
    "group_no": 2559,
    "name": "研发中心",
    "type": 0,
    "status": 1
  }
}


---

## 更新自建角色组

- 官方文档：https://hc.jiandaoyun.com/open/18531

1. 简介

1.1 接口简介

更新创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id, type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role_group/update

 |
2. 接口调用

更新创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role_group/update

请求频率：20 次/秒

请求方式：POST

请求参数

参数

 | 类型

 | 是否必须

 | 说明

 |
role_group_no

 | Integer

 | 是

 | 角色组编号

 |
name

 | String

 | 是

 | 角色组名称

 |
请求示例：

{
    "role_group_no": 2559,
    "name": "研发部门"
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
group_no

 | Number

 | 是

 | 角色组编号

 |
name

 | String

 | 是

 | 角色组名称

 |
type

 | Number

 | 是

 | 角色组类型

0: 常规角色组
2: 企业互联外部角色组
 |
status

 | Number

 | 是

 | 1: 使用中

 |
integrate_id

 | String

 | 否

 | 集成模式同步角色关联 ID，仅在集成模式下返回

 |
响应示例：

{
  "role_group": {
    "group_no": 2559,
    "name": "研发部门",
    "type": 0,
    "status": 1
  }
}


---

## 删除自建角色组

- 官方文档：https://hc.jiandaoyun.com/open/18532

1. 简介

1.1 接口简介

删除创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v2

 | 2022.4.8

 | 初始版本：

角色使用 role_no
角色组使用 group_no
包含 integrate_id, type 字段
 |
v4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；

接口路由修改为 POST corp/role_group/delete

 |
2. 接口调用

删除创建好的角色组信息。支持公共模式和集成模式，但集成模式下只支持对自建角色操作，不支持对第三方同步的角色操作。

请求地址：https://api.jiandaoyun.com/api/v5/corp/role_group/delete

请求频率：20 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必须

 | 说明

 |
role_group_no

 | Number

 | 是

 | 角色组编号

 |
请求示例：

{
    "role_group_no": 2561
}

响应内容：

参数

 | 类型

 | 是否必须

 | 说明

 |
status

 | String

 | 否

 | 返回请求结果

 |
响应示例：

{
    "status": "success"
}


---

## 企业互联接口

- 官方文档：https://hc.jiandaoyun.com/open/14201

1. 简介

企业互联接口支持对通讯录中 互联组织 中的企业及对接人进行列出，获取我连接的企业对接人的详细信息。

1）开发前，请仔细阅读 开发指南（内含错误码对照表）。

2）接口文档中的「我连接的企业」 =客体企业=外部部门。

2. 接口列表

企业互联接口主要包括以下接口：

接口名称

 | 释义

 |
列出我连接的企业

 | 能够获取所有 外部部门 的列表。支持公共模式和集成模式。

 |
列出我连接的企业的对接人

 | 能够获取 外部对接人 的列表部列出来。支持公共模式和集成模式。

 |
获取我连接的企业对接人的详细信息

 | 获取某个 对接人 的详细资料。

 |


---

## 列出我连接的企业

- 官方文档：https://hc.jiandaoyun.com/open/18533

1. 简介

1.1 接口简介

能够获取所有 外部部门 的列表。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v4

 | 2022.4.21

 | 初始版本：

成员使用 username
部门使用 dept_no
包含 type 字段
 |
V4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/guest/department/list

 |
2. 接口调用

能够获取所有 外部部门 的列表。支持公共模式和集成模式。

注：只返回已加入的, 不返回未加入和已解除的。

请求地址：https://api.jiandaoyun.com/api/v5/corp/guest/department/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必须

 | 说明

 |
dept_no

 | integer

 | 否

 | 部门编号，不填则返回所有外部部门

 |

请求示例：

{
    "dept_no": 1012
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
dept_list

 | Array

 | 是

 | 部门内容数组

 |
name

 | String

 | 是

 | 部门名称

 |
dept_no

 | Integer

 | 是

 | 部门编号

 |
type

 | Number

 | 是

 | 部门类型

0: 常规部
2: 企业互联外部部门
 |
status

 | Number

 | 是

 | 部门状态：

1: 使用中的部门
-1: 集成模式下同步后删除的部门
 |
integrate_id

 | String

 | 否

 | 集成模式同步部门关联 ID

 |

响应示例：

{
    "dept_list": [
        {
         "name": "帆软软件有限公司"
         "dept_no": 1012
         "type": 2
          "status": 1
        }
    ]
}


---

## 列出我连接的企业的对接人

- 官方文档：https://hc.jiandaoyun.com/open/18534

1. 简介

1.1 接口简介

能够获取 外部对接人 的列表部列出来。支持公共模式和集成模式。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v4

 | 2022.4.21

 | 初始版本：

成员使用 username
部门使用 dept_no
包含 type 字段
 |
V4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/guest/member_list

 |

2. 接口调用

能够获取 外部对接人 的列表部列出来。支持公共模式和集成模式。

请求地址：https://api.jiandaoyun.com/api/v5/corp/guest/user/list

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
dept_no

 | Integer

 | 否

 | 部门编号，不填则返回全部

 |

请求示例：

{
    "dept_no":19
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
member_list

 | Array

 | 是

 | 企业对接人内容数组

 |
name

 | string

 | 是

 | 昵称

 |
username

 | String

 | 是

 | 成员编号

 |
departments

 | Array[integer]

 | 是

 | 部门编号

 |
type

 | Number

 | 是

 | 部门类型

0: 常规部
2: 企业互联外部部门
 |
status

 | Number

 | 是

 | 部门状态：

1: 使用中的部门
-1: 集成模式下同步后删除的部门
 |
integrate_id

 | String

 | 否

 | 集成模式同步部门关联 ID

 |

响应示例：

{
  "member_list": [
    {
      "name": "Purl",
      "username": "R-ww9a61c11fc226842f-#admin",
      "departments": [
        19
      ],
      "type": 2,
      "status": 1
    }
  ]
}


---

## 获取我连接的企业对接人的详细信息

- 官方文档：https://hc.jiandaoyun.com/open/18535

1. 简介

1.1 接口简介

获取某个 对接人 的详细信息。

1.2 接口版本

接口版本

 | 更新时间

 | 版本说明

 |
v4

 | 2022.4.21

 | 初始版本：

成员使用 username
部门使用 dept_no
包含 type 字段
 |
V4

 | 2022.6.30

 | 返回值新增字段 status

 |
v5

 | 2022.10.28

 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；

接口路由修改为 POST corp/guest/user/get

 |
2. 接口调用

获取某个 对接人 的信息详细信息。

请求地址：https://api.jiandaoyun.com/api/v5/corp/guest/user/get

请求频率：30 次/秒

请求方式：POST

请求参数：

参数

 | 类型

 | 是否必需

 | 说明

 |
username

 | String

 | 是

 | 成员编号

 |

请求示例：

{
    "username": "R-611e10175402f70006bcdc2c-jdy-e4703i1mde61"
}

响应内容：

参数

 | 类型

 | 是否必需

 | 说明

 |
name

 | String

 | 是

 | 昵称

 |
username

 | String

 | 是

 | 成员编号

 |
departments

 | Array[integer]

 | 是

 | 部门编号

 |
type

 | Number

 | 是

 | 部门类型

0: 常规部
2: 企业互联外部部门
 |
status

 | Number

 | 是

 | 部门状态：

1: 使用中的部门
-1: 集成模式下同步后删除的部门
 |
integrate_id

 | String

 | 否

 | 集成模式同步部门关联 ID

 |

响应示例：

{
  "member": {
    "name": "peach",
    "username": "R-611e10175402f70006bcdc2c-jdy-e4703i1mde61",
    "departments": [
      62
    ],
    "type": 2,
    "status": 1
  }
}
