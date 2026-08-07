# -*- coding: utf-8 -*-
"""KTS site.json 重建：5 语言 (en/zh-CN/zh-TW/ja/ko) + 新页面 + 内容增强."""
import json, re, copy
from pathlib import Path
import opencc
import sys
sys.path.insert(0, str(Path(__file__).parent))
import ko_content as KO
import walkthrough_v2 as WT
import content_v2 as C2

ROOT = Path(__file__).parent
# 始终从已提交的原始站点数据重建（幂等）；site.json 是输出文件
BASE = ROOT / "site.base.json"
d = json.loads(BASE.read_text() if BASE.exists() else (ROOT / "site.json").read_text())
cc = opencc.OpenCC("s2tw")

# ---------- 1) page meta: icon + case file id ----------
ICON = {
  "how-to-play":"how-to-play","walkthrough":"walkthrough","choices":"choices","endings":"endings",
  "cases":"cases","characters":"characters","investigation":"investigation","achievements":"achievements",
  "controls":"controls","system-requirements":"system-requirements","steam-deck":"steam-deck",
  "tips-and-tricks":"tips-and-tricks","faq":"faq","update-log":"update-log",
  "where-to-buy":"where-to-buy","how-long-to-beat":"how-long-to-beat",
}
FID = {slug: "F-" + str(i+1).zfill(2) for i, slug in enumerate(ICON)}
for p in d["pages"]:
    p["meta"] = {"icon": ICON.get(p["slug"],"faq"), "id": FID.get(p["slug"],"F-00")}

# ---------- 1b) idempotent: remove existing characters pages ----------
d["pages"] = [p for p in d["pages"] if p.get("slug") != "characters"]

# ---------- 1c) heroImage per page ----------
HERO = {
  "how-to-play":"/images/how-to-play.jpg","walkthrough":"/images/walkthrough.jpg",
  "cases":"/images/cases.jpg","characters":"/images/characters.jpg",
  "investigation":"/images/investigation.jpg","endings":"/images/endings.jpg",
  "tips-and-tricks":"/images/tips-and-tricks.jpg",
  "achievements":"/images/achievements.jpg","controls":"/images/controls.jpg",
  "faq":"/images/faq.jpg","update-log":"/images/update-log.jpg",
  "choices":"/images/choices.jpg","system-requirements":"/images/system-requirements.jpg",
  "steam-deck":"/images/steam-deck.jpg",
}
for pg in d["pages"]:
    if pg["slug"] in HERO:
        pg["heroImage"] = HERO[pg["slug"]]
        for lang in ("zh-CN","zh-TW","ja","ko"):
            tr = pg.get("i18n", {}).get(lang)
            if tr: tr["heroImage"] = HERO[pg["slug"]]

# ---------- 2) languages ----------
d["site"]["languages"] = ["en","zh-CN","zh-TW","ja","ko"]
d["site"]["defaultLanguage"] = "en"

# ---------- 3) site i18n: rename zh -> zh-CN, add zh-TW (OpenCC), ko ----------
site_i18n = d["site"]["i18n"]
zh_cn = site_i18n.pop("zh", {})
zh_tw = {k: cc.convert(str(v)) for k, v in zh_cn.items()}
# fill missing keys with en fallback then convert
def _fill(obj, en_key):
    if en_key not in obj:
        obj[en_key] = EN_SITE.get(en_key, "")
EN_SITE = {
  "name": d["site"]["name"], "tagline": d["site"]["tagline"], "description": d["site"]["description"],
  "navHome":"Home","navGuides":"Guides","navCases":"Case Board","navCharacters":"Characters",
  "navAbout":"About","navPrivacy":"Privacy","navContact":"Contact","langLabel":"Language",
  "aboutTitle":"About this site","privacyTitle":"Privacy Policy","contactTitle":"Contact",
  "footerNote":"Unofficial fan site — game and related assets belong to their respective owners.",
  "footerSource":"Information checked against the official Steam store page, the publisher and media reports.",
  "quickAnswers":"Quick answers","guides":"All guides","aboutGame":"About the game",
  "startPlaying":"Get it on Steam","getOnSteam":"Get it on Steam ↗","readGuide":"Read the guide →",
  "moreGuides":"More guides","sources":"Sources & fact-checking","caseFile":"CASE FILE",
  "evidence":"EVIDENCE","sealed":"SEALED","latest":"Latest guides","updated":"Contents","explore":"Explore the investigation",
}
# zh-CN extra keys (translate)
zh_cn_extra = {
  "navCases":"案件板","navCharacters":"角色档案","caseFile":"案件卷宗","evidence":"证据",
  "sealed":"已封存","latest":"最新攻略","updated":"目录","explore":"深入调查暗潮市的离奇案件",
  "startPlaying":"在 Steam 获取 →","getOnSteam":"在 Steam 获取 ↗",
}
zh_cn.update(zh_cn_extra)
for k, v in EN_SITE.items():
    zh_cn.setdefault(k, v)
zh_tw = {k: cc.convert(str(v)) for k, v in zh_cn.items()}

ja = site_i18n.pop("ja", {})
ja_extra = {
  "navCases":"事件ボード","navCharacters":"キャラクター","caseFile":"事件ファイル","evidence":"証拠",
  "sealed":"封印済み","latest":"最新ガイド","updated":"目次","explore":"暗潮市の事件を調査しよう",
  "startPlaying":"Steam で入手 →","getOnSteam":"Steam で入手 ↗",
}
ja.update(ja_extra)
for k, v in EN_SITE.items():
    ja.setdefault(k, v)

d["site"]["i18n"] = {"en": dict(EN_SITE), "zh-CN": zh_cn, "zh-TW": zh_tw, "ja": ja, "ko": dict(KO.SITE)}

# ---------- 4) game i18n ----------
g = d["game"]
def _tr(dst, key, zhv, jav, kov, env):
    dst[key] = {"en": env, "zh-CN": zhv, "zh-TW": cc.convert(str(zhv)), "ja": jav, "ko": kov}
g["nameI18n"] = {"en":"Kill The Shadow","zh-CN":"杀死影子","zh-TW":cc.convert("杀死影子"),"ja":"キル・ザ・シャドウ","ko":"킬 더 섀도우"}
g["introI18n"] = {
  "en": g["intro"],
  "zh-CN": "《杀死影子》是一款氛围浓厚的侦探RPG，由中国工作室坞光岚影（Shadowlight）开发，凤凰游戏（Phoenix Game）发行。你扮演分裂城市暗潮市的前警官 Lucas，背上寄宿着名为「影子」的超自然存在，它能让你重现死者最后的时刻，并在调查中倒转时间。你的每一个选择都会塑造人物关系、被揭开的真相，以及你最终抵达的多种结局之一。",
  "zh-TW": cc.convert("《殺死影子》是一款氛圍濃厚的偵探RPG，由中國工作室塢光嵐影（Shadowlight）開發，鳳凰遊戲（Phoenix Game）發行。你扮演分裂城市暗潮市的前警官 Lucas，背上寄宿著名為「影子」的超自然存在，它能讓你重現死者最後的時刻，並在調查中倒轉時間。你的每一個選擇都會塑造人物關係、被揭開的真相，以及你最終抵達的多種結局之一。"),
  "ja": "『キル・ザ・シャドウ』は、中国のスタジオ Shadowlight（塢光嵐影）が開発し、Phoenix Game が発売した、雰囲気のある刑事RPGです。分断された都市ダークタイドシティで、元警官ルーカスとしてプレイ。背中に宿る超常存在「シャドウ」は、死者の最後の瞬間を再現し、調査中に時間を巻き戻すことを可能にします。すべての選択が、人間関係・明らかになる真実・たどり着く複数のエンディングを形作ります。",
  "ko": KO.GAME["introI18n"],
}
g["statsI18n"] = {
  "en": g["stats"],
  "zh-CN": [{"value":"8月5日","label":"Steam 发售"},{"value":"10万+","label":"发售前愿望单"},{"value":"多结局","label":"结局数量"},{"value":"2.5D","label":"像素 noir"},{"value":"$16.99","label":"Steam 售价"},{"value":"Win","label":"平台"}],
  "zh-TW": [{"value":"8月5日","label":"Steam 發售"},{"value":"10萬+","label":"發售前願望單"},{"value":"多結局","label":"結局數量"},{"value":"2.5D","label":"像素 noir"},{"value":"$16.99","label":"Steam 售價"},{"value":"Win","label":"平台"}],
  "ja": [{"value":"8月5日","label":"Steam 発売"},{"value":"10万+","label":"発売前ウィッシュリスト"},{"value":"複数","label":"エンディング"},{"value":"2.5D","label":"ピクセルノワール"},{"value":"$16.99","label":"Steam 価格"},{"value":"Win","label":"プラットフォーム"}],
  "ko": KO.GAME["statsI18n"],
}
g["keyFactsI18n"] = {
  "en": g["keyFacts"],
  "zh-CN": [
    "2026年8月5日在 Steam（Windows）发售，$16.99 / £14.99 / €16.99，首发两周 10% 折扣",
    "多结局侦探RPG — 含「影子黑化度」系统",
    "重现死者最后时刻 + 调查中时间回溯的独特调查系统",
    "以半开放城市「暗潮市」为舞台的多案件结构",
  ],
  "zh-TW": [cc.convert(x) for x in [
    "2026年8月5日在 Steam（Windows）發售，$16.99 / £14.99 / €16.99，首發兩週 10% 折扣",
    "多結局偵探RPG — 含「影子黑化度」系統",
    "重現死者最後時刻 + 調查中時間回溯的獨特調查系統",
    "以半開放城市「暗潮市」為舞台的多案件結構",
  ]],
  "ja": [
    "2026年8月5日に Steam（Windows）で発売、$16.99 / £14.99 / €16.99、発売2週間は10%オフ",
    "複数エンディングの刑事RPG —「シャドウ汚染度」システム搭載",
    "死者の最後の瞬間を再現し、調査中に時間を巻き戻す独自の調査システム",
    "半オープン都市「ダークタイドシティ」を舞台にした複数事件構造",
  ],
  "ko": KO.GAME["keyFactsI18n"],
}

# ---------- 5) pages: rename zh -> zh-CN, add zh-TW, merge ko ----------
def _tr_sections(sections_en, sections_zh, sections_ja, sections_ko):
    """merge: return per-lang section list aligned to en structure."""
    out = {"en": sections_en, "zh-CN": sections_zh or sections_en, "ja": sections_ja or sections_en}
    out["zh-TW"] = json.loads(cc.convert(json.dumps(out["zh-CN"], ensure_ascii=False)))
    out["ko"] = sections_ko or sections_en
    return out

# characters page (en/zh/ja base) — ko from KO.PAGES
CHAR_EN = {
 "title": "Kill The Shadow Characters: Character Files",
 "metaTitle": "Kill The Shadow Characters Guide: All Characters (2026)",
 "metaDescription": "Confirmed Kill The Shadow characters from Chapter 1: Lucas, the Shadow, Lynn DaHandt, Officer May, Uncle Smith, Captain Theo, the Flints, Rafe and Teddy.",
 "intro": "The confirmed character files in Kill The Shadow, based on launch coverage and our Chapter 1 playthrough. The roster below covers everyone verified in the opening and the factory case — updated as more is confirmed.",
 "sections": [
  {
   "type": "table",
   "heading": "Character Overview",
   "body": "Everyone verified in Chapter 1 — from the opening letter to the factory floor.",
   "columns": [
    "Character",
    "Role",
    "Notes"
   ],
   "rows": [
    [
     "Lucas",
     "Protagonist · former officer",
     "Former police officer carrying the Shadow; reconstructs the final moments of the dead"
    ],
    [
     "The Shadow",
     "Supernatural entity",
     "Lucas's partner; source of time rewind and crime-scene reconstruction"
    ],
    [
     "Lynn DaHandt",
     "Mysterious sender",
     "Sent the letter written on a medical gauge in the opening"
    ],
    [
     "Officer May",
     "Police station contact",
     "Greets Lucas on his return and sets the tone of the opening"
    ],
    [
     "Uncle Smith",
     "Senior officer",
     "Mysteriously disappears during the police station prologue"
    ],
    [
     "Captain Theo",
     "Factory supervisor",
     "Chapter 1 key figure; reconstructing his objects ties into the ten-year mystery"
    ],
    [
     "Axel Flint",
     "Factory worker",
     "Half of the Flint argument under the bridge; can be punched in a skill check"
    ],
    [
     "Griff Flint",
     "Factory worker",
     "The other half; buys Lucas a drink for two clue points"
    ],
    [
     "The Old Machinist",
     "Factory elder",
     "Trades the book 'Machinist's Basics' for a relief meal"
    ],
    [
     "Rafe",
     "Child in the factory case",
     "His father's secret drives a Chapter 1 subplot"
    ],
    [
     "Teddy",
     "The dead dog",
     "The case that breaks the factory open"
    ]
   ]
  },
  {
   "type": "list",
   "heading": "Lucas",
   "body": "What is confirmed about the protagonist.",
   "items": [
    "A former police officer in Dark Tide City",
    "Uses the Shadow's power to reconstruct the final moments of the dead",
    "Your choices decide his relationships and moral stance across the story"
   ]
  },
  {
   "type": "list",
   "heading": "The Shadow",
   "body": "Partner and source of power.",
   "items": [
    "Reconstructs the final moments of the dead 'exactly as they happened'",
    "Lets you rewind time during investigations to retry failed moments",
    "Darker choices raise the corruption meter and change how the story unfolds"
   ]
  },
  {
   "type": "list",
   "heading": "Officer May, Lynn DaHandt & Uncle Smith",
   "body": "The people of the police station prologue.",
   "items": [
    "Officer May is the first person to greet Lucas at the station",
    "Lynn DaHandt is the sender of the opening letter — the start of the medical documents thread",
    "Uncle Smith is the senior officer who mysteriously disappears when the station catches fire",
    "Their threads continue to connect in later cases"
   ]
  },
  {
   "type": "list",
   "heading": "Captain Theo & the Factory",
   "body": "The man who runs the factory floor.",
   "items": [
    "The factory supervisor who assembles the crew after Teddy's death",
    "His objects, when reconstructed, connect the case to the city's ten-year-old mystery",
    "He is the anchor of the Chapter 1 main case"
   ]
  },
  {
   "type": "list",
   "heading": "Axel & Griff Flint",
   "body": "The argument under the bridge.",
   "items": [
    "Axel and Griff argue beneath the overpass before the case breaks",
    "A skill check lets Lucas punch Axel — a choice with consequences",
    "Griff buys Lucas a drink, earning two investigation clue points",
    "Both are caught up in the Teddy case that follows"
   ]
  },
  {
   "type": "list",
   "heading": "The Old Machinist, Rafe & Teddy",
   "body": "The supporting cast of the factory.",
   "items": [
    "The Old Machinist trades the book 'Machinist's Basics' for a relief meal at the pawnshop",
    "Rafe's family thread — his mother's request, the Anti-Blockade Protest and calming Rafe down — is a full Chapter 1 subplot",
    "Teddy, the dead dog, is the incident that opens the factory case"
   ]
  },
  {
   "type": "note",
   "heading": "How the Cast Connects",
   "body": "The medical gauge from the opening letter recurs across investigations. People from one case reappear in later ones, with relationships that persist. The mysterious event that fractured Dark Tide City ten years ago is the thread connecting everything — and the Shadow's corruption meter shapes how Lucas's story ends."
  }
 ]
}

CHAR_ZH = {
 "title": "杀死影子角色：人物档案",
 "metaTitle": "杀死影子角色指南：全部角色（2026）",
 "metaDescription": "《杀死影子》第一章已确认的角色：Lucas、影子、Lynn DaHandt、梅警官、史密斯叔叔、西奥队长、弗林特父子、老机械师、拉夫与泰迪。",
 "intro": "根据发售报道与第一章通关记录，整理目前确认的《杀死影子》人物档案。以下阵容覆盖开场与工厂案中核实到的每一位角色——随着更多内容得到验证会持续更新。",
 "sections": [
  {
   "type": "table",
   "heading": "角色总览",
   "body": "第一章中核实到的全部角色——从开场信件到工厂车间。",
   "columns": [
    "角色",
    "身份",
    "备注"
   ],
   "rows": [
    [
     "Lucas",
     "主角 · 前警官",
     "背着影子的前警官；能重现死者最后的时刻"
    ],
    [
     "影子",
     "超自然存在",
     "Lucas 的搭档；时间回溯与现场重建的力量来源"
    ],
    [
     "Lynn DaHandt",
     "神秘寄信人",
     "在开场寄出写在医疗计量器上的信"
    ],
    [
     "梅警官",
     "警察局联系人",
     "迎接 Lucas 回归，奠定开场基调"
    ],
    [
     "史密斯叔叔",
     "资深警官",
     "在警察局序章中神秘消失"
    ],
    [
     "西奥队长",
     "工厂主管",
     "第一章关键人物；重建他的物品会把案件与十年谜团相连"
    ],
    [
     "阿克塞尔·弗林特",
     "工厂工人",
     "天桥下弗林特争吵的一方；技能检定中可以被揍"
    ],
    [
     "格里夫·弗林特",
     "工厂工人",
     "争吵的另一方；请 Lucas 喝酒换来 2 条推理线索"
    ],
    [
     "老机械师",
     "工厂长者",
     "用《机械师基础》一书换救济餐"
    ],
    [
     "拉夫",
     "工厂案中的孩子",
     "父亲的秘密驱动第一章的一条完整支线"
    ],
    [
     "泰迪",
     "死去的狗",
     "打开工厂案的事件起点"
    ]
   ]
  },
  {
   "type": "list",
   "heading": "Lucas",
   "body": "关于主角已确认的信息。",
   "items": [
    "暗潮市的前警官",
    "借助影子的力量重现死者最后的时刻",
    "你的选择决定他在故事中的关系与道德立场"
   ]
  },
  {
   "type": "list",
   "heading": "影子",
   "body": "搭档与力量来源。",
   "items": [
    "「如实」重现死者最后的时刻",
    "调查中可回溯时间，重试失败的关键时刻",
    "越黑暗的选择越推高黑化度，改变故事走向"
   ]
  },
  {
   "type": "list",
   "heading": "梅警官、Lynn DaHandt 与史密斯叔叔",
   "body": "警察局序章中的人物。",
   "items": [
    "梅警官是在警察局迎接 Lucas 的第一人",
    "Lynn DaHandt 是开场信的寄信人——医疗文档线索的开端",
    "史密斯叔叔是警局起火时神秘消失的资深警官",
    "他们的线索在之后的案件中持续串联"
   ]
  },
  {
   "type": "list",
   "heading": "西奥队长与工厂",
   "body": "掌管工厂车间的人。",
   "items": [
    "泰迪之死后召集工厂众人的主管",
    "重建他的物品，会把案件与城市十年谜团相连",
    "他是第一章主案件的锚点"
   ]
  },
  {
   "type": "list",
   "heading": "阿克塞尔与格里夫·弗林特",
   "body": "天桥下的争吵。",
   "items": [
    "阿克塞尔与格里夫在案发前于天桥下争吵",
    "技能检定允许 Lucas 揍阿克塞尔——一个有后果的选择",
    "格里夫请 Lucas 喝酒，换来 2 条推理线索",
    "两人都被卷入随后的泰迪案"
   ]
  },
  {
   "type": "list",
   "heading": "老机械师、拉夫与泰迪",
   "body": "工厂的配角阵容。",
   "items": [
    "老机械师在当铺用《机械师基础》一书换救济餐",
    "拉夫的家庭线——母亲的请求、反封锁抗议与安抚拉夫——是第一章的一条完整支线",
    "死去的泰迪是打开工厂案的事件起点"
   ]
  },
  {
   "type": "note",
   "heading": "角色如何相连",
   "body": "开场信里的医疗计量器在多个调查中反复出现。一个案件里的人物会出现在后续案件中，关系持续存在。十年前撕裂暗潮市的神秘事件是贯穿一切的线索——而影子的黑化度决定 Lucas 的故事如何收尾。"
  }
 ]
}

CHAR_JA = {
 "title": "キル・ザ・シャドウ キャラクター：人物ファイル",
 "metaTitle": "キル・ザ・シャドウ キャラクターガイド：全キャラクター（2026）",
 "metaDescription": "『キル・ザ・シャドウ』第1章の確認済みキャラクター：ルーカス、シャドウ、リン、メイ巡査、テオ船長、フリント父子ほか。",
 "intro": "発売報道と第1章プレイをもとに、確認済みのキャラクターファイルをまとめました。オープニングと工場事件で確認できた全員を網羅しており、確認でき次第更新します。",
 "sections": [
  {
   "type": "table",
   "heading": "キャラクター概要",
   "body": "第1章で確認された全員——オープニングの手紙から工場の現場まで。",
   "columns": [
    "人物",
    "役割",
    "備考"
   ],
   "rows": [
    [
     "ルーカス",
     "主人公・元警官",
     "シャドウを背負う元警官。死者の最後の瞬間を再現できる"
    ],
    [
     "シャドウ",
     "超常存在",
     "ルーカスのパートナー。時間巻き戻しと現場再現の源"
    ],
    [
     "リン・ダハント",
     "謎の差出人",
     "オープニングで医療ゲージに書かれた手紙を送った人物"
    ],
    [
     "メイ巡査",
     "警察署の窓口",
     "ルーカスの復帰を迎え、オープニングの空気を作る"
    ],
    [
     "スミスおじさん",
     "先任警官",
     "警察署の序章で謎の失踪"
    ],
    [
     "テオ船長",
     "工場の監督",
     "第1章の要。彼の品物の再現が事件を10年前の謎へとつなぐ"
    ],
    [
     "アクセル・フリント",
     "工場労働者",
     "高架下のフリント喧嘩の片割れ。スキルチェックで殴れる"
    ],
    [
     "グリフ・フリント",
     "工場労働者",
     "もう片割れ。ルーカスに酒を振る舞い推理ポイント2つ"
    ],
    [
     "老機械工",
     "工場の古老",
     "『機械士の基礎』の本を救済食と交換"
    ],
    [
     "レイフ",
     "工場事件の子供",
     "父の秘密が第1章のサブプロットを動かす"
    ],
    [
     "テディ",
     "死んだ犬",
     "工場事件を開くきっかけ"
    ]
   ]
  },
  {
   "type": "list",
   "heading": "ルーカス",
   "body": "主人公について確認済みの情報。",
   "items": [
    "ダークタイドシティの元警官",
    "シャドウの力で死者の最後の瞬間を再現する",
    "選択が関係と道徳的立場を決める"
   ]
  },
  {
   "type": "list",
   "heading": "シャドウ",
   "body": "パートナーであり力の源。",
   "items": [
    "死者の最後の瞬間を「そのまま」再現する",
    "調査中に時間を巻き戻し、失敗した瞬間をやり直せる",
    "暗い選択は汚染度を上げ、物語の展開を変える"
   ]
  },
  {
   "type": "list",
   "heading": "メイ巡査、リン・ダハント、スミスおじさん",
   "body": "警察署序章の人々。",
   "items": [
    "メイ巡査は警察署で最初にルーカスを迎える人物",
    "リン・ダハントはオープニングの手紙の差出人——医療書類の始まり",
    "スミスおじさんは署が炎上する中で謎の失踪を遂げる先任警官",
    "彼らの糸は以後の事件にもつながる"
   ]
  },
  {
   "type": "list",
   "heading": "テオ船長と工場",
   "body": "工場の現場を仕切る男。",
   "items": [
    "テディの死後に作業員を集める監督",
    "彼の品物の再現が事件を10年前の謎へとつなぐ",
    "第1章メイン事件の要"
   ]
  },
  {
   "type": "list",
   "heading": "アクセルとグリフ・フリント",
   "body": "高架下の喧嘩。",
   "items": [
    "アクセルとグリフは事件前に高架下で喧嘩",
    "スキルチェックでルーカスがアクセルを殴れる——結果を伴う選択",
    "グリフは酒を振る舞い、推理ポイント2つを稼ぐ",
    "二人とも続くテディ事件に巻き込まれる"
   ]
  },
  {
   "type": "list",
   "heading": "老機械工、レイフ、テディ",
   "body": "工場の脇役たち。",
   "items": [
    "老機械工は質屋で『機械士の基礎』を救済食と交換",
    "レイフの家族の物語——母の依頼、封鎖反対デモ、レイフを落ち着かせる——は第1章の完全なサブプロット",
    "死んだテディは工場事件を開くきっかけ"
   ]
  },
  {
   "type": "note",
   "heading": "キャストのつながり",
   "body": "冒頭の手紙の医療ゲージは複数の調査に登場。ある事件の人物が後の事件にも現れ、関係は継続。10年前にダークタイドシティを分断した謎の出来事がすべてをつなぐ——そしてシャドウの汚染度がルーカスの物語の結末を形作ります。"
  }
 ]
}

# enrich existing pages: add new sections (en/zh/ja base + ko merge)
WALKTHROUGH_EXTRA_EN = [
  {"type":"timeline","tag":"FLOW","heading":"Chapter 1 at a Glance","body":"The route from opening to factory in one timeline.","items":[
    ["00:00","Outside the station — read the letter from Lynn DaHandt"],
    ["00:15","Enter the station — talk to Officer May and the squad"],
    ["01:10","Head to the Factory district"],
    ["01:30","Inspect the scene before reconstructing"],
    ["02:00","Reconstruct the victim's final moments"],
    ["02:30","Compare reconstruction with the staged scene — find the tell"],
  ]},
  {"type":"table","tag":"CHOICES","heading":"Key Choices in Chapter 1","body":"The decisions that matter most in the opening and factory sections, based on our playthrough.","columns":["Decision","Effect","Tip"],"rows":[
    ["How you answer May's questions","Shapes your relationship with the station","Be honest about the Shadow — or not; both are viable"],
    ["Share or hide the letter","Changes who trusts you early","Keeping it secret opens a private investigation path"],
    ["Use violence vs persuasion at the scene","Affects witnesses and the corruption meter","Try both with rewind to see consequences"],
  ]},
]
WALKTHROUGH_EXTRA_ZH = [
  {"type":"timeline","tag":"流程","heading":"第一章速览","body":"从开场到工厂的完整路线，一条时间线看完。","items":[
    ["00:00","警察局外——阅读 Lynn DaHandt 的来信"],
    ["00:15","进入警察局——与警官 May 和同僚交谈"],
    ["01:10","前往工厂区"],
    ["01:30","重建前先检查现场"],
    ["02:00","重建受害者的最后时刻"],
    ["02:30","对比重建与被伪造的现场——找到破绽"],
  ]},
  {"type":"table","tag":"抉择","heading":"第一章关键抉择","body":"根据我们的通关记录，开场与工厂部分最重要的选择。","columns":["抉择","影响","建议"],"rows":[
    ["如何回应 May 的问题","塑造你与警察局的关系","可以坦诚谈影子，也可以保留——两者都可行"],
    ["分享或隐瞒信件","决定早期谁信任你","保密可开启一条私下调查的路线"],
    ["在现场用暴力还是说服","影响目击者与黑化度","用回溯两种都试，看看后果"],
  ]},
]
WALKTHROUGH_EXTRA_JA = [
  {"type":"timeline","tag":"フロー","heading":"第1章の流れ","body":"オープニングから工場までのルートを1本のタイムラインで。","items":[
    ["00:00","警察署の外——リン・ダハントからの手紙を読む"],
    ["00:15","警察署へ——メイ巡査と同僚に話す"],
    ["01:10","工場地区へ向かう"],
    ["01:30","再現の前に現場を調べる"],
    ["02:00","被害者の最後の瞬間を再現する"],
    ["02:30","再現と偽装現場を比較——破綻を見つける"],
  ]},
  {"type":"table","tag":"選択","heading":"第1章の重要選択","body":"プレイ記録に基づく、オープニングと工場パートで最も重要な選択。","columns":["選択","影響","アドバイス"],"rows":[
    ["メイの質問への答え方","警察署との関係を形作る","シャドウについて正直に話すか、黙るか——どちらも成立"],
    ["手紙を共有するか隠すか","初期に誰が信頼するかが変わる","隠すと非公開の調査ルートが開く"],
    ["現場で暴力か説得か","目撃者と汚染度に影響","巻き戻しで両方を試して結果を確認"],
  ]},
]
WALKTHROUGH_EXTRA_KO = [
  {"type":"timeline","tag":"흐름","heading":"1장 한눈에 보기","body":"오프닝부터 공장까지의 루트를 하나의 타임라인으로.","items":[
    ["00:00","경찰서 밖 — 린 다한트의 편지 읽기"],
    ["00:15","경찰서 진입 — 메이 경관과 대화"],
    ["01:10","공장 지구로 이동"],
    ["01:30","재구성 전에 현장 확인"],
    ["02:00","피해자의 마지막 순간 재구성"],
    ["02:30","재구성과 조작된 현장 비교 — 실마리 찾기"],
  ]},
  {"type":"table","tag":"선택","heading":"1장의 핵심 선택","body":"플레이 기록 기준, 오프닝과 공장 파트에서 가장 중요한 선택.","columns":["결정","효과","팁"],"rows":[
    ["메이의 질문에 답하는 방식","경찰서와의 관계 형성","섀도우에 대해 솔직히 말하거나 말거나 — 둘 다 유효"],
    ["편지 공유 또는 숨김","초반 신뢰도 변화","숨기면 개인 조사 루트가 열림"],
    ["현장에서 폭력 vs 설득","목격자와 오염도에 영향","되감기로 둘 다 시도해 결과 확인"],
  ]},
]

INVESTIGATION_EXTRA_EN = [
  {"type":"evidence","tag":"KEY EVIDENCE","heading":"Evidence That Cracked Chapter 1","body":"The evidence types that mattered most, pulled from our playthrough notes.","items":[
    ["E-01","The medical gauge from the opening letter — cross-reference it with every medical document"],
    ["E-02","Access records: who could reach the factory floor at the time of death"],
    ["E-03","Body position vs reconstruction — staged scenes rarely survive comparison"],
    ["E-04","The unspoken detail: an object in the scene no witness mentioned"],
  ]},
]
INVESTIGATION_EXTRA_ZH = [
  {"type":"evidence","tag":"关键证据","heading":"破解第一章的证据","body":"根据我们的通关笔记，最重要的证据类型。","items":[
    ["E-01","开场信中的医疗计量器——与每一份医疗文档交叉比对"],
    ["E-02","出入记录：死亡发生时谁有权进入工厂车间"],
    ["E-03","尸体位置与重建的对比——伪装的现场经不起对照"],
    ["E-04","无人提及的细节：现场某件所有目击者都没提到的物品"],
  ]},
]
INVESTIGATION_EXTRA_JA = [
  {"type":"evidence","tag":"重要証拠","heading":"第1章を解いた証拠","body":"プレイノートから抽出した、最も重要だった証拠の種類。","items":[
    ["E-01","オープニングの手紙の医療ゲージ——すべての医療文書と照合"],
    ["E-02","出入記録：死亡時に工場フロアへ入れた人物"],
    ["E-03","遺体の位置と再現の比較——偽装現場は比較に耐えない"],
    ["E-04","誰も言及しなかった物——現場にあった語られぬ物体"],
  ]},
]
INVESTIGATION_EXTRA_KO = [
  {"type":"evidence","tag":"핵심 증거","heading":"1장을 풀어낸 증거","body":"플레이 노트에서 추출한 가장 중요한 증거 유형.","items":[
    ["E-01","오프닝 편지의 의료 게이지 — 모든 의료 문서와 교차 확인"],
    ["E-02","출입 기록: 사망 당시 공장 내부에 접근할 수 있었던 사람"],
    ["E-03","시신 위치 vs 재구성 — 조작된 현장은 비교를 견디지 못함"],
    ["E-04","아무도 언급하지 않은 물체 — 현장에 있던 말해지지 않은 세부"],
  ]},
]

CASES_EXTRA_EN = [
  {"type":"table","tag":"SUSPECTS","heading":"Persons of Interest","body":"Who we are watching in Chapter 1 — confirmed from coverage and our playthrough.","columns":["Person","Relation","Why They Matter"],"rows":[
    ["Lynn DaHandt","Sender of the opening letter","Their connection to the victim is the thread behind the factory case"],
    ["Officer May","Station contact","Gatekeeper to the station's trust and information"],
    ["The Factory Foreman","Factory district","Had access and authority over the crime scene"],
    ["Unknown (staging)","Unidentified","The staged scene suggests a second party — motive still unknown"],
  ]},
]
CASES_EXTRA_ZH = [
  {"type":"table","tag":"嫌疑人","heading":"重点关注人物","body":"第一章中我们正在关注的人物——根据报道与通关记录确认。","columns":["人物","关系","为何重要"],"rows":[
    ["Lynn DaHandt","开场信寄信人","与受害者的关联是工厂案背后的线索"],
    ["警官 May","警察局联系人","掌握警察局的信任与信息"],
    ["工厂领班","工厂区","对案发现场拥有出入权与管辖权"],
    ["未知人物（伪装的现场）","身份不明","被伪造的现场暗示有第二方——动机仍未知"],
  ]},
]
CASES_EXTRA_JA = [
  {"type":"table","tag":"容疑者","heading":"注目人物","body":"第1章で注目している人物——報道とプレイ記録で確認。","columns":["人物","関係","重要な理由"],"rows":[
    ["リン・ダハント","オープニングの手紙の差出人","被害者とのつながりが工場事件の糸"],
    ["メイ巡査","警察署の窓口","警察署の信頼と情報への鍵"],
    ["工場の現場監督","工場地区","犯行現場への出入りと権限を持つ"],
    ["不明（偽装）","身元不明","偽装された現場は第二の人物を示唆——動機は未判明"],
  ]},
]
CASES_EXTRA_KO = [
  {"type":"table","tag":"용의자","heading":"관심 인물","body":"1장에서 주시하는 인물 — 보도와 플레이 기록으로 확인.","columns":["인물","관계","중요한 이유"],"rows":[
    ["린 다한트","오프닝 편지 발신자","피해자와의 연결이 공장 사건의 실마리"],
    ["메이 경관","경찰서 접점","경찰서의 신뢰와 정보의 관문"],
    ["공장 현장 감독","공장 지구","현장에 대한 접근 권한과 통제권 보유"],
    ["미상 (조작된 현장)","신원 불명","조작된 현장은 제2의 인물을 암시 — 동기 미상"],
  ]},
]

TIPS_EXTRA_EN = [
  {"type":"note","tag":"FIELD NOTE","heading":"Detective's Field Notes","body":"A running note from our playthrough: when you rewind time, the game remembers what you learned. Treat rewind as information gathering, not a reset button — the game rewards you for trying every path before committing."},
]
TIPS_EXTRA_ZH = [
  {"type":"note","tag":"现场笔记","heading":"侦探现场笔记","body":"通关记录里的一条持续笔记：当你回溯时间时，游戏会记住你学到的东西。把回溯当作收集信息，而不是重置按钮——游戏鼓励你在做出承诺前尝试每条路径。"},
]
TIPS_EXTRA_JA = [
  {"type":"note","tag":"現場ノート","heading":"探偵の現場ノート","body":"プレイ記録からのメモ：時間を巻き戻しても、学んだことは記憶に残ります。巻き戻しをリセットではなく情報収集と捉えましょう——ゲームは決断前にすべての道を試すことを評価します。"},
]
TIPS_EXTRA_KO = [
  {"type":"note","tag":"현장 메모","heading":"형사의 현장 노트","body":"플레이 기록에서 남긴 메모: 시간을 되감아도 배운 것은 기억에 남습니다. 되감기를 리셋 버튼이 아닌 정보 수집으로 여기세요 — 게임은 결정 전에 모든 길을 시도하는 것을 보상합니다."},
]

EXTRAS = {
  "walkthrough": (WALKTHROUGH_EXTRA_EN, WALKTHROUGH_EXTRA_ZH, WALKTHROUGH_EXTRA_JA, WALKTHROUGH_EXTRA_KO),
  "investigation": (INVESTIGATION_EXTRA_EN, INVESTIGATION_EXTRA_ZH, INVESTIGATION_EXTRA_JA, INVESTIGATION_EXTRA_KO),
  "cases": (CASES_EXTRA_EN, CASES_EXTRA_ZH, CASES_EXTRA_JA, CASES_EXTRA_KO),
  "tips-and-tricks": (TIPS_EXTRA_EN, TIPS_EXTRA_ZH, TIPS_EXTRA_JA, TIPS_EXTRA_KO),
}

# characters page (new)
char_en = dict(CHAR_EN); char_en["slug"]="characters"; char_en["sources"]=[
  {"label":"Official Steam store page — Kill The Shadow","url":"https://store.steampowered.com/app/2660230/Kill_The_Shadow/"},
  {"label":"Into Indie Games — Kill the Shadow Walkthrough Part 1","url":"https://intoindiegames.com/walkthroughs/kill-the-shadow-walkthrough-part-1-the-factory/"},
]
char_en["i18n"] = {}
char_en["i18n"]["zh-CN"] = dict(CHAR_ZH)
char_en["i18n"]["zh-TW"] = json.loads(cc.convert(json.dumps(CHAR_ZH, ensure_ascii=False)))
char_en["i18n"]["ja"] = dict(CHAR_JA)
char_en["i18n"]["ko"] = dict(KO.PAGES["characters"])
char_en["meta"] = {"icon":"characters","id":"F-14"}
d["pages"].append(char_en)

# rename zh -> zh-CN on existing pages, add zh-TW, merge ko, enrich
for p in d["pages"]:
    if p["slug"] == "characters": continue
    i18n = p.get("i18n", {})
    zh = i18n.pop("zh", i18n.pop("zh-CN", {}))
    ja = i18n.pop("ja", {})
    ko = KO.PAGES.get(p["slug"])
    # source label translations
    src_zh = {}
    src_ja = {}
    for s in p.get("sources", []):
        src_zh[s["label"]] = s.get("zh", s["label"])
        src_ja[s["label"]] = s.get("ja", s["label"])
    # walkthrough: use deep verified structure (walkthrough_v2) as base
    if p["slug"] == "walkthrough":
        zh_wt = {"title":"杀死影子全流程：第一章 · 工厂（深度攻略）","metaTitle":"杀死影子全流程：第一章 · 工厂（2026）","metaDescription":"杀死影子第一章深度攻略：序章警察局、老机械师、泰迪之死、父亲的秘密、西奥队长记忆与收尾，含全部关键抉择。","intro":"这份第一章攻略覆盖从警察局序章到工厂区收尾的完整流程，基于已核实的结构（intoindiegames 流程 + 官方资料）用自己的话重写。因为选择会改变结果，你的流程可能略有不同——把它当作地图而非唯一答案。","sections":list(WT.WALKTHROUGH["sections"]["zh-CN"])}
        ja_wt = {"title":"キル・ザ・シャドウ 攻略：第1章 ファクトリー（完全版）","metaTitle":"キル・ザ・シャドウ 攻略：第1章 ファクトリー（2026）","metaDescription":"キル・ザ・シャドウ第1章の完全攻略：警察署の序章、老機械工、テディの死、父の秘密、テオ船長の記憶と締めくくり、重要選択も網羅。","intro":"この第1章攻略は、警察署の序章から工場地区の締めくくりまでの完全な流れをカバーします。検証済みの構成（intoindiegames の攻略と公式資料）に基づき、独自の文章で書き直しました。選択によって結果は変わります。","sections":list(WT.WALKTHROUGH["sections"]["ja"])}
        ko_wt = {"title":"킬 더 섀도우 워크스루: 1장 — 공장 (심층)","metaTitle":"킬 더 섀도우 워크스루: 1장 — 공장 (2026)","metaDescription":"킬 더 섀도우 1장 심층 공략: 경찰서 프롤로그, 늙은 기계공, 테디의 죽음, 아버지의 비밀, 테오 선장의 기억과 마무리, 핵심 선택까지.","intro":"이 1장 공략은 경찰서 프롤로그부터 공장 지구 마무리까지의 전체 흐름을 다룹니다. 검증된 구조(intoindiegames 워크스루 + 공식 자료)를 바탕으로 자체 문장으로 다시 썼습니다. 선택에 따라 결과가 달라질 수 있습니다.","sections":list(WT.WALKTHROUGH["sections"]["ko"])}
        en_wt = {"title":"Kill The Shadow Walkthrough: Chapter 1 — The Factory (Full Guide)","metaTitle":"Kill The Shadow Walkthrough: Chapter 1 — The Factory (2026)","metaDescription":"Full Kill The Shadow Chapter 1 walkthrough: police station prologue, the Old Machinist, Teddy's death, Father's Secret and Captain Theo's memories.","intro":"This Chapter 1 walkthrough covers the full route from the police station prologue to the Factory's closing beats. It is rewritten in our own words from a verified structure (intoindiegames' walkthrough and official material). Because choices change outcomes, treat it as a map, not the only path.","sections":list(WT.WALKTHROUGH["sections"]["en"])}
        zh = dict(zh_wt); ja = dict(ja_wt); ko_wt = dict(ko_wt)
        ko = ko_wt
        p["sections"] = list(en_wt["sections"])
        p["title"] = en_wt["title"]; p["metaTitle"] = en_wt["metaTitle"]; p["metaDescription"] = en_wt["metaDescription"]; p["intro"] = en_wt["intro"]

    # how-to-play: append verified first-15-minutes section
    if p["slug"] == "how-to-play":
        p["sections"] = p["sections"] + list(WT.HTP_EN)
        zh = dict(zh); zh["sections"] = list(zh.get("sections", [])) + list(WT.HTP_ZH)
        ja = dict(ja); ja["sections"] = list(ja.get("sections", [])) + list(WT.HTP_JA)
        if ko is not None:
            ko = dict(ko); ko["sections"] = list(ko.get("sections", [])) + list(WT.HTP_KO)
    # cases: append verified chapter breakdown
    if p["slug"] == "cases":
        p["sections"] = p["sections"] + list(WT.CASES_EN)
        zh = dict(zh); zh["sections"] = list(zh.get("sections", [])) + list(WT.CASES_ZH)
        ja = dict(ja); ja["sections"] = list(ja.get("sections", [])) + list(WT.CASES_JA)
        if ko is not None:
            ko = dict(ko); ko["sections"] = list(ko.get("sections", [])) + list(WT.CASES_KO)
    # faq: append verified Q&A
    if p["slug"] == "faq":
        zh = dict(zh); ja = dict(ja)
        for lang, add in [("en", WT.FAQ_ADD_EN), ("zh", WT.FAQ_ADD_ZH), ("ja", WT.FAQ_ADD_JA)]:
            pass
        # en
        faq_sec = next((sec for sec in p["sections"] if sec.get("type")=="faq"), None)
        if faq_sec: faq_sec["items"] = faq_sec.get("items", []) + list(WT.FAQ_ADD_EN)
        for tr, add in [(zh, WT.FAQ_ADD_ZH), (ja, WT.FAQ_ADD_JA)]:
            tsec = next((sec for sec in tr.get("sections", []) if sec.get("type")=="faq"), None)
            if tsec: tsec["items"] = tsec.get("items", []) + list(add)
        if ko is not None:
            ko = dict(ko)
            ksec = next((sec for sec in ko.get("sections", []) if sec.get("type")=="faq"), None)
            if ksec: ksec["items"] = ksec.get("items", []) + list(WT.FAQ_ADD_KO)

    # content_v2 deepening: how-to-play / investigation / choices / tips
    V2MAP = {
      "how-to-play": ("HTP2_EN","HTP2_ZH","HTP2_JA","HTP2_KO"),
      "investigation": ("INV2_EN","INV2_ZH","INV2_JA","INV2_KO"),
      "choices": ("CHO2_EN","CHO2_ZH","CHO2_JA","CHO2_KO"),
      "tips-and-tricks": ("TIPS2_EN","TIPS2_ZH","TIPS2_JA","TIPS2_KO"),
    }
    if p["slug"] in V2MAP:
        e, z, j, k = V2MAP[p["slug"]]
        p["sections"] = p["sections"] + list(getattr(C2, e))
        zh = dict(zh); zh["sections"] = list(zh.get("sections", [])) + list(getattr(C2, z))
        ja = dict(ja); ja["sections"] = list(ja.get("sections", [])) + list(getattr(C2, j))
        if ko is not None:
            ko = dict(ko); ko["sections"] = list(ko.get("sections", [])) + list(getattr(C2, k))

    # enrich: append extra sections to en/zh/ja/ko
    if p["slug"] in EXTRAS:
        e_en, e_zh, e_ja, e_ko = EXTRAS[p["slug"]]
        p["sections"] = p["sections"] + e_en
        zh = dict(zh); zh["sections"] = list(zh.get("sections", p["sections"])) + e_zh
        ja = dict(ja); ja["sections"] = list(ja.get("sections", p["sections"])) + e_ja
        if ko is not None:
            ko = dict(ko); ko["sections"] = list(ko.get("sections", [])) + e_ko
    zh_cn = dict(zh)
    zh_tw = json.loads(cc.convert(json.dumps(zh_cn, ensure_ascii=False)))
    new_i18n = {}
    if zh_cn: new_i18n["zh-CN"] = zh_cn
    if zh_tw: new_i18n["zh-TW"] = zh_tw
    if ja: new_i18n["ja"] = ja
    if ko: new_i18n["ko"] = ko
    p["i18n"] = new_i18n
    # source label i18n for zh/ja/ko
    for s in p.get("sources", []):
        s["labels"] = {}
        for lang, label in [("zh-CN", src_zh.get(s["label"], s["label"])), ("ja", src_ja.get(s["label"], s["label"])), ("ko", KO.SOURCES_LABELS.get(s["label"], s["label"]))]:
            s["labels"][lang] = label

# write
(ROOT / "site.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
print("✓ site.json rebuilt:", len(d["pages"]), "pages x", len(d["site"]["languages"]), "langs")
for p in d["pages"]:
    langs = ["en"] + list(p.get("i18n", {}).keys())
    print("  ", p["slug"], "->", langs)
