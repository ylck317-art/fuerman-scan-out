# OPC 工作台（飞书驱动）

飞书多维表 = 管理后台；本服务拉表并展示网页。

## 本地

```bash
export FEISHU_APP_ID=cli_aa6aa3fddbb81c1e
export FEISHU_APP_SECRET=***   # 勿提交
export FEISHU_BITABLE_APP_TOKEN=KvnVbzkAWab2sQsaqTQcn3csnwc
uvicorn server:app --host 0.0.0.0 --port 8000
```

## 小 a 增删功能

在飞书表「导航菜单」新增一行（启用=是）→ 网页点刷新或等约 10 分钟自动同步后出现新导航；删行或启用=否则消失。

## 环境变量（Render）

- FEISHU_APP_ID
- FEISHU_APP_SECRET
- FEISHU_BITABLE_APP_TOKEN
