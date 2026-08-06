# Kill The Shadow · 差异化改造方案（v2，2026-08-06）

> 目标：彻底脱离 Meccha 模板观感，打造侦探 noir 专属视觉 + 按搜索区域扩语言 + 流量向内容结构。
> 对标调研：Gamepressure(Disco Elysium)、intoindiegames(KTS hub)、GameRant、Fandom 风格指南。

## 1. 视觉语言「案件卷宗 Case File Noir」（全新建模，不复用 Meccha 主题）
- **概念**：整站 = 一册侦探案件卷宗。页面元素带「证据标签/红章/编号」，读者即调查员。
- **配色**（vs Meccha 深蓝+绿/珊瑚渐变 → 完全更换）：
  - 背景碳黑 `#0c0e12` / 面板深灰 `#14171d`
  - 主强调 **血红 `#e63946`**（犯罪现场）+ **警用琥珀 `#f2a900`**（证据标签/编号）
  - 辅助蓝灰 `#4cc9f0`（时间回溯/超自然元素）、纸张白 `#e8e6e1`、褪色黄 `#f5e6c8`（旧档案纸）
- **字体**：标题 **Archivo/Chakra Petch（警示牌感）**；正文 Inter；**证据标签/编号用等宽 IBM Plex Mono**（case/evidence 编号、时间戳）
- **标志性元素**（CSS/SVG 组件，区别于任何通用模板）：
  - 证据标签（黄色 tape 标签 + 编号 E-01/02…）
  - 案件板（case board）：线索卡片 + 红色虚线连线 + 图钉，首页 hero 视觉
  - 「SEALED / 已封存」红章；胶片颗粒/扫描线质感；断头台分割线
  - 侦探工具 SVG 图标组：放大镜/手铐/证据袋/打字机/怀表(时间回溯)/左轮/档案夹/指纹
- **布局**：
  - 首页：案件板 hero（线索卡片+连线）→ 案件档案卡网格（每案一张"档案卡"）→ 关键证据/FAQ
  - 内页：左「卷宗目录」+ 右内容；内容块用「证据框/证词块」样式；walkthrough 用时间线式（章节→目标→关键抉择→后果）

## 2. 语言：按游戏搜索区域扩到 5 种（依据 Steam 官方支持语言）
- **en / zh-CN / zh-TW / ja / ko**（Steam 商店页官方语言列表：英/简中/繁中/日/韩）
- hreflang 用 zh-CN / zh-TW（不再用笼统 zh）；路径 /zh-CN/ /zh-TW/ /ja/ /ko/
- 繁体+韩语为新增内容（content.py 补 i18n），简体沿用现有 zh 内容

## 3. 内容结构增强（流量向）
- 新增「案件板」页：案件总览 + 线索 + 人物关系（侦探游戏核心流量词：all cases / all suspects）
- 新增「角色档案」页：Lucas / Lynn DaHandt / Officer May / The Shadow
- walkthrough 拆多章（Part 1 警察局 / Part 2 工厂…随进度扩充）；选择树表格（选项→影响→结果）
- 每页配 Seedream noir 插图（警察局/工厂/暗潮市夜景/现场/时间回溯），不再只有一张 hero

## 4. 执行顺序（本方案确认后执行）
A. generate.js + style.css 全新建模（案件卷宗主题 + 图标组 + 布局）
B. content.py 扩 zh-TW/ko 双语 → 重新生成
C. 新增案件板/角色页 + 每页配图（Seedream 批量）
D. CDP 全维度审计（布局/响应式/SEO/三语纯净）→ 修复 → 部署
E. GSC/GA4（用户交互）

## 5. 流量判断
- 差异化视觉 → 跳出率低、停留长（Google 用行为信号）
- 5 语言覆盖 Steam 官方语言区 = 搜索区域全覆盖（韩语区是 NEOWIZ 主场）
- 案件板/角色档案 = 侦探游戏高搜索长尾（cases/suspects/characters）
- 深度 walkthrough 碾压 intoindiegames 的浅层 Part 1
