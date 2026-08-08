# -*- coding: utf-8 -*-
"""KTS achievements 进度追踪器 section 数据。

事实源：data/achievements.json（2026-08-08 取自 Steam Community 官方成就页，
成就名/描述为 Steam 官方本地化，五语齐全；百分比 = 全玩家解锁占比）。
本模块只做「组装 + 界面文案」，不新增任何游戏事实。
"""
import json
from pathlib import Path
import opencc

ROOT = Path(__file__).parent
_cc = opencc.OpenCC("s2tw")
DATA = json.loads((ROOT / "achievements.json").read_text())

LANGS = ["en", "zh-CN", "zh-TW", "ja", "ko"]

# 界面文案（渐进增强控件的标签；不是游戏内容）
UI = {
    "en": {
        "heading": "Full Achievement List (41)",
        "body": ("All 41 achievements from the full game, straight from Steam's official list. "
                 "The percentage is the share of all players who unlocked each one. Rarity tiers: "
                 "Common = 50%+ of players, Uncommon = 10\u201349.9%, Rare = under 10%. "
                 "Tick achievements to track your progress \u2014 it saves in your browser."),
        "search": "Search achievements\u2026", "all": "All", "common": "Common",
        "uncommon": "Uncommon", "rare": "Rare", "hidden": "Hidden",
        "count": "{n} of {t} shown", "done": "{n}/{t} done ({p}%)", "reset": "Reset progress",
        "empty": "No achievements match.", "hiddenTag": "HIDDEN",
        "hiddenDesc": "Hidden \u2014 its description is revealed when you unlock it.",
        "nameCol": "Achievement", "descCol": "Description", "playersCol": "Players", "iconCol": "Icon",
    },
    "zh-CN": {
        "heading": "正式版完整成就列表（41 个）",
        "body": ("正式版全部 41 个成就，直接取自 Steam 官方列表。百分比表示已解锁该成就的玩家占比。"
                 "稀有度分级：常见 = 50% 以上玩家，少见 = 10\u201349.9%，稀有 = 低于 10%。"
                 "勾选成就即可记录进度——保存在你的浏览器中。"),
        "search": "搜索成就\u2026", "all": "全部", "common": "常见", "uncommon": "少见",
        "rare": "稀有", "hidden": "隐藏", "count": "显示 {n} / {t} 个", "done": "已完成 {n}/{t}（{p}%）",
        "reset": "重置进度", "empty": "没有匹配的成就。", "hiddenTag": "隐藏",
        "hiddenDesc": "隐藏成就——解锁后才会显示描述。",
        "nameCol": "成就", "descCol": "描述", "playersCol": "玩家占比", "iconCol": "图标",
    },
    "zh-TW": {
        "heading": "正式版完整成就列表（41 個）",
        "body": ("正式版全部 41 個成就，直接取自 Steam 官方列表。百分比表示已解鎖該成就的玩家佔比。"
                 "稀有度分級：常見 = 50% 以上玩家，少見 = 10\u201349.9%，稀有 = 低於 10%。"
                 "勾選成就即可記錄進度——儲存在你的瀏覽器中。"),
        "search": "搜尋成就\u2026", "all": "全部", "common": "常見", "uncommon": "少見",
        "rare": "稀有", "hidden": "隱藏", "count": "顯示 {n} / {t} 個", "done": "已完成 {n}/{t}（{p}%）",
        "reset": "重設進度", "empty": "沒有符合的成就。", "hiddenTag": "隱藏",
        "hiddenDesc": "隱藏成就——解鎖後才會顯示描述。",
        "nameCol": "成就", "descCol": "描述", "playersCol": "玩家佔比", "iconCol": "圖示",
    },
    "ja": {
        "heading": "製品版 実績一覧（41個）",
        "body": ("製品版の実績は全部で41個。Steam公式リストから直接取得しています。"
                 "パーセントは全プレイヤーのうち解除した人の割合。レア度：コモン＝50%以上、"
                 "アンコモン＝10〜49.9%、レア＝10%未満。実績にチェックを付けて進捗を記録できます（ブラウザに保存）。"),
        "search": "実績を検索\u2026", "all": "すべて", "common": "コモン", "uncommon": "アンコモン",
        "rare": "レア", "hidden": "非表示", "count": "{n} / {t} 件を表示", "done": "達成 {n}/{t}（{p}%）",
        "reset": "リセット", "empty": "一致する実績がありません。", "hiddenTag": "非表示",
        "hiddenDesc": "非表示実績——解除すると説明が表示されます。",
        "nameCol": "実績", "descCol": "説明", "playersCol": "プレイヤー", "iconCol": "アイコン",
    },
    "ko": {
        "heading": "정식판 전체 업적 목록 (41개)",
        "body": ("정식판 업적 41개 전체를 Steam 공식 목록에서 직접 가져왔습니다. "
                 "퍼센트는 전체 플레이어 중 달성한 비율입니다. 희귀도: 흔함 = 50% 이상, "
                 "보통 = 10\u201349.9%, 희귀 = 10% 미만. 업적을 체크해 진행 상황을 기록하세요 (브라우저에 저장)."),
        "search": "업적 검색\u2026", "all": "전체", "common": "흔함", "uncommon": "보통",
        "rare": "희귀", "hidden": "숨김", "count": "{n} / {t}개 표시", "done": "달성 {n}/{t} ({p}%)",
        "reset": "초기화", "empty": "일치하는 업적이 없습니다.", "hiddenTag": "숨김",
        "hiddenDesc": "숨겨진 업적 — 달성하면 설명이 공개됩니다.",
        "nameCol": "업적", "descCol": "설명", "playersCol": "플레이어", "iconCol": "아이콘",
    },
}


def _section(lang):
    ui = UI[lang]
    rows = []
    for a in DATA["achievements"]:
        t = a[lang]
        # zh-TW 用官方繁体，但统一过一遍 OpenCC s2tw，保证字形与全站 zh-TW 约定一致（如 祕→秘）
        if lang == "zh-TW":
            t = {"name": _cc.convert(t["name"]), "desc": _cc.convert(t["desc"])}
        rows.append({
            "i": a["i"], "name": t["name"], "desc": t["desc"],
            "pct": a["pct"], "tier": a["tier"], "hidden": a["hidden"], "icon": a["icon"],
        })
    return {"type": "achieve", "heading": ui["heading"], "body": ui["body"],
            "ui": ui, "achievements": rows}


ACH_SECTIONS = {lang: _section(lang) for lang in LANGS}
