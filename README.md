# cuso0925-plugins

个人 Claude 插件市场。

## 插件

| 插件 | 说明 |
|------|------|
| `jiandaoyun-integration-guide` | 简道云对接配置指南（开放 API、Webhook、SSO、前端事件、自建插件、MCP） |

## 安装

在 Claude Code 中：

```
/plugin marketplace add cuso0925/claude-plugins
/plugin install jiandaoyun-integration-guide@cuso0925-plugins
```

## 来源与版权

`jiandaoyun-integration-guide` 技能内容来自 SkillHub：
<https://skillhub.cn/skills/@org-nznpea4p/jiandaoyun-integration-guide>（v1.0.0，作者：南京致和），
此处仅做插件格式封装，内容版权归原作者所有。

`scripts/jdy_api.py` 需要设置环境变量 `JDY_API_KEY` 才能调用简道云 API，请勿把密钥提交到仓库。
