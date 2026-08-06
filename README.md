# Kill The Shadow Guide

非官方 Kill The Shadow（杀死影子）攻略站。数据驱动：`data/site.json` → `node scripts/generate.js` → `public/`（en/zh/ja 三语，13 页）。

- 域名：killtheshadowguides.com（Spaceship，2026-08-06 注册）
- 部署：Cloudflare Pages（build: node scripts/generate.js → public）
- 内容原则：每页 1-2 可靠来源，禁止编造；未核实内容明确标注

## 本地
```bash
node scripts/generate.js   # 生成 public/
node scripts/dev-server.js # 本地预览 http://127.0.0.1:8899（支持 clean URL）
```

## 内容维护
- 改 `data/content.py`（内容源，含三语）→ `python3 data/content.py` 重新生成 site.json → `node scripts/generate.js`
- 或直接编辑 `data/site.json`
