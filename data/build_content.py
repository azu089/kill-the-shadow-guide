# -*- coding: utf-8 -*-
"""KTS site.json 重建：5 语言 (en/zh-CN/zh-TW/ja/ko) + 新页面 + 内容增强."""
import json, re, copy
from pathlib import Path
import opencc
import sys
sys.path.insert(0, str(Path(__file__).parent))
import ko_content as KO

ROOT = Path(__file__).parent
# 始终从已提交的原始站点数据重建（幂等）；site.json 是输出文件
BASE = ROOT / "site.base.json"
d = json.loads(BASE.read_text() if BASE.exists() else (ROOT / "site.json").read_text())
cc = opencc.OpenCC("s2t")

# ---------- 1) page meta: icon + case file id ----------
ICON = {
  "how-to-play":"how-to-play","walkthrough":"walkthrough","choices":"choices","endings":"endings",
  "cases":"cases","characters":"characters","investigation":"investigation","achievements":"achievements",
  "controls":"controls","system-requirements":"system-requirements","steam-deck":"steam-deck",
  "tips-and-tricks":"tips-and-tricks","faq":"faq","update-log":"update-log",
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
}
zh_cn.update(zh_cn_extra)
for k, v in EN_SITE.items():
    zh_cn.setdefault(k, v)
zh_tw = {k: cc.convert(str(v)) for k, v in zh_cn.items()}

ja = site_i18n.pop("ja", {})
ja_extra = {
  "navCases":"事件ボード","navCharacters":"キャラクター","caseFile":"事件ファイル","evidence":"証拠",
  "sealed":"封印済み","latest":"最新ガイド","updated":"目次","explore":"暗潮市の事件を調査しよう",
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
  "zh-CN": "《杀死影子》是一款氛围浓厚的侦探RPG，由中国工作室坞光岚影（Shadowlight）开发，并在 NEOWIZ 的全球发行协议下发行。你扮演分裂城市暗潮市的前警官 Lucas，背上寄宿着名为「影子」的超自然存在，它能让你重现死者最后的时刻，并在调查中倒转时间。你的每一个选择都会塑造人物关系、被揭开的真相，以及你最终抵达的多种结局之一。",
  "zh-TW": cc.convert("《殺死影子》是一款氛圍濃厚的偵探RPG，由中國工作室塢光嵐影（Shadowlight）開發，並在 NEOWIZ 的全球發行協議下發行。你扮演分裂城市暗潮市的前警官 Lucas，背上寄宿著名為「影子」的超自然存在，它能讓你重現死者最後的時刻，並在調查中倒轉時間。你的每一個選擇都會塑造人物關係、被揭開的真相，以及你最終抵達的多種結局之一。"),
  "ja": "『キル・ザ・シャドウ』は、中国のスタジオ Shadowlight（塢光嵐影）が開発し、NEOWIZ のグローバルパブリッシング契約のもと発売された、雰囲気のある刑事RPGです。分断された都市ダークタイドシティで、元警官ルーカスとしてプレイ。背中に宿る超常存在「シャドウ」は、死者の最後の瞬間を再現し、調査中に時間を巻き戻すことを可能にします。すべての選択が、人間関係・明らかになる真実・たどり着く複数のエンディングを形作ります。",
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
  "title":"Kill The Shadow Characters: Character Files",
  "metaTitle":"Kill The Shadow Characters Guide: All Characters (2026)",
  "metaDescription":"The confirmed characters in Kill The Shadow: Lucas, Lynn DaHandt, Officer May and the Shadow. Their roles, relationships and meaning in the story.",
  "intro":"The confirmed character files in Kill The Shadow so far, based on launch coverage and our Chapter 1 playthrough. Updated as more is verified.",
  "sections":[
    {"type":"table","heading":"Character Overview","body":"The main characters verified in Chapter 1.","columns":["Character","Role","Notes"],"rows":[
      ["Lucas","Protagonist · former officer","A former police officer carrying the Shadow. Can reconstruct the final moments of the dead."],
      ["Lynn DaHandt","Mysterious sender","Sent the letter written on a medical gauge in the opening."],
      ["Officer May","Police station contact","Greets Lucas on his return and sets the tone of the Chapter 1 opening."],
      ["The Shadow","Supernatural entity","Lucas's partner. Source of time rewind and crime-scene reconstruction."],
    ]},
    {"type":"list","heading":"Lucas","body":"What is confirmed about the protagonist.","items":[
      "A former police officer in Dark Tide City",
      "Uses the Shadow's power to reconstruct the final moments of the dead",
      "Your choices decide his relationships and moral stance across the story",
    ]},
    {"type":"list","heading":"The Shadow","body":"Partner and source of power.","items":[
      "Reconstructs the final moments of the dead 'exactly as they happened'",
      "Lets you rewind time during investigations to retry failed moments",
      "Darker choices raise the corruption meter and change how the story unfolds",
    ]},
    {"type":"list","heading":"Officer May & Lynn DaHandt","body":"The people you meet in Chapter 1.","items":[
      "Officer May is the first person to greet Lucas at the station",
      "Lynn DaHandt is the sender of the opening letter — the start of the medical documents thread",
      "Their relationships continue to connect in later cases",
    ]},
  ],
}
CHAR_ZH = {
  "title":"杀死影子角色：人物档案",
  "metaTitle":"杀死影子角色指南：全部角色（2026）",
  "metaDescription":"《杀死影子》已确认的角色：Lucas、Lynn DaHandt、警官 May 与影子。他们在故事中的角色、关系与意义。",
  "intro":"根据发售报道与第一章通关记录，整理目前确认的《杀死影子》人物档案。随着更多内容得到验证会持续更新。",
  "sections":[
    {"type":"table","heading":"角色总览","body":"第一章中确认的主要角色。","columns":["角色","身份","备注"],"rows":[
      ["Lucas","主角 · 前警官","背着影子的前警官。能够重现死者最后的时刻。"],
      ["Lynn DaHandt","神秘寄信人","在开场寄出写在医疗计量器上的信。"],
      ["警官 May","警察局联系人","迎接 Lucas 回归，奠定第一章开场的基调。"],
      ["影子","超自然存在","Lucas 的搭档。时间回溯与现场重建的力量来源。"],
    ]},
    {"type":"list","heading":"Lucas","body":"关于主角已确认的信息。","items":[
      "暗潮市的前警官",
      "借助影子的力量重现死者最后的时刻",
      "你的选择决定他在故事中的关系与道德立场",
    ]},
    {"type":"list","heading":"影子","body":"搭档与力量来源。","items":[
      "「如实」重现死者最后的时刻",
      "调查中可回溯时间，重试失败的关键时刻",
      "越黑暗的选择越推高黑化度，改变故事走向",
    ]},
    {"type":"list","heading":"警官 May 与 Lynn DaHandt","body":"第一章中遇到的人物。","items":[
      "警官 May 是在警察局迎接 Lucas 的第一人",
      "Lynn DaHandt 是开场信的寄信人——医疗文档线索的开端",
      "他们的关系在之后的案件中持续串联",
    ]},
  ],
}
CHAR_JA = {
  "title":"キル・ザ・シャドウ キャラクター：人物ファイル",
  "metaTitle":"キル・ザ・シャドウ キャラクターガイド：全キャラクター（2026）",
  "metaDescription":"『キル・ザ・シャドウ』で確認されたキャラクター：ルーカス、リン・ダハント、メイ巡査、シャドウ。その役割と物語上の意味。",
  "intro":"発売報道と第1章プレイをもとに、確認済みのキャラクターファイルをまとめました。確認でき次第更新します。",
  "sections":[
    {"type":"table","heading":"キャラクター概要","body":"第1章で確認された主要人物。","columns":["人物","役割","備考"],"rows":[
      ["ルーカス","主人公・元警官","シャドウを背負う元警官。死者の最後の瞬間を再現できる。"],
      ["リン・ダハント","謎の差出人","オープニングで医療ゲージに書かれた手紙を送った人物。"],
      ["メイ巡査","警察署の窓口","ルーカスの復帰を迎え、第1章オープニングの空気を作る。"],
      ["シャドウ","超常存在","ルーカスのパートナー。時間巻き戻しと現場再現の源。"],
    ]},
    {"type":"list","heading":"ルーカス","body":"主人公について確認済みの情報。","items":[
      "ダークタイドシティの元警官",
      "シャドウの力で死者の最後の瞬間を再現する",
      "選択が関係と道徳的立場を決める",
    ]},
    {"type":"list","heading":"シャドウ","body":"パートナーであり力の源。","items":[
      "死者の最後の瞬間を「そのまま」再現する",
      "調査中に時間を巻き戻し、失敗した瞬間をやり直せる",
      "暗い選択は汚染度を上げ、物語の展開を変える",
    ]},
    {"type":"list","heading":"メイ巡査とリン・ダハント","body":"第1章で出会う人物たち。","items":[
      "メイ巡査は警察署で最初にルーカスを迎える人物",
      "リン・ダハントはオープニングの手紙の差出人",
      "彼らの関係は以後の事件にもつながる",
    ]},
  ],
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
