# Kill The Shadow Guide (v2 · Case File Noir)

非官方 Kill The Shadow（杀死影子）攻略站，侦探 noir「案件卷宗」主题。

- 域名：killtheshadowguides.com（Spaceship，2026-08-06 注册）
- 部署：Cloudflare Pages `kill-the-shadow-guide`（build: `node scripts/generate.js` → public）
- **5 语言**：en / zh-CN / zh-TW / ja / ko（按 Steam 官方语言区；hreflang 用 zh-CN/zh-TW）
- **14 页面**：13 原页 + 新增 characters（角色档案）；walkthrough 含时间线+关键抉择表，investigation 含证据块，cases 含嫌疑人表
- **视觉**：案件卷宗 Case File Noir（碳黑+血红+琥珀、证据标签、案件板 hero、SEALED 红章、侦探工具 SVG、Archivo+IBM Plex Mono）
- **配图**：Seedream 生成 7 张 noir 2.5D 像素插图（hero + 6 页面），全部 16:9 三档 srcset

## 构建与内容维护
```bash
python3 data/build_content.py   # 从 data/site.base.json 重建 site.json（幂等，5 语言 + 新页面）
node scripts/generate.js        # 生成 public/
node scripts/dev-server.js      # 本地预览 http://127.0.0.1:8899
```
- 韩语内容在 `data/ko_content.py`；简体→繁体用 OpenCC 自动转；英文为基准内容（site.base.json）
- 新增/修改页面后：`python3 data/build_content.py && node scripts/generate.js` → 按 `work/` 审计 → commit+push

## 线上验证
- `python3 -c "import requests;s=requests.Session();s.trust_env=False;print(s.get('https://killtheshadowguides.com/').status_code)"`
- GSC/GA4 状态见 `docs/` 或项目 README。
