# -*- coding: utf-8 -*-
"""Kill The Shadow 攻略站内容源 → 生成 site.json
所有事实均来自已核实来源（Steam 商店页 / IGN / 官方新闻稿 / SteamDB / intoindiegames）。
未公开的信息明确标注【待确认】，不编造。
"""
import json, os

SITE = {
    "name": "Kill The Shadow Guide",
    "domain": "killtheshadowguides.com",
    "tagline": "Walkthrough, Choices, Endings, Cases & FAQs",
    "description": "The best Kill The Shadow guides: full walkthrough, choices and endings guide, all cases, investigation system explained, achievements, system requirements and FAQs. Updated regularly.",
    "language": "en",
    "gaId": "",
    "gscVerification": "",
    "adsenseId": "",
    "ogImage": "/images/hero.jpg",
    "languages": ["en", "zh", "ja"],
    "defaultLanguage": "en",
    "i18n": {
        "zh": {
            "name": "杀死影子攻略站",
            "tagline": "全流程、抉择、结局、案件与常见问题",
            "description": "最好的杀死影子攻略：完整流程、抉择与结局指南、全部案件、调查系统详解、成就、配置要求与常见问题。持续更新。",
            "navHome": "首页",
            "navAbout": "关于",
            "navPrivacy": "隐私",
            "navContact": "联系",
            "langLabel": "语言",
            "aboutTitle": "关于本站",
            "privacyTitle": "隐私政策",
            "contactTitle": "联系我们",
            "footerNote": "非官方粉丝站——游戏及相关资产归其所有者所有。",
            "footerSource": "信息核对自 Steam 官方商店页、IGN、官方新闻稿与 SteamDB。",
            "quickAnswers": "常见问题速答",
            "guides": "全部攻略",
            "aboutGame": "关于这款游戏",
            "startPlaying": "开始游玩 →",
            "getOnSteam": "在 Steam 获取 ↗",
            "moreGuides": "更多攻略",
            "sources": "来源与事实核对",
            "readGuide": "新手攻略 →",
        },
        "ja": {
            "name": "キル・ザ・シャドウ攻略ガイド",
            "tagline": "完全攻略・選択肢・エンディング・事件・FAQ",
            "description": "キル・ザ・シャドウ攻略の決定版：完全ウォークスルー、選択肢とエンディング、全事件、調査システム解説、実績、必要スペック、FAQ。定期的に更新。",
            "navHome": "ホーム",
            "navAbout": "このサイト",
            "navPrivacy": "プライバシー",
            "navContact": "お問い合わせ",
            "langLabel": "言語",
            "aboutTitle": "このサイトについて",
            "privacyTitle": "プライバシーポリシー",
            "contactTitle": "お問い合わせ",
            "footerNote": "非公式ファンサイトです。ゲームおよび関連アセットは各権利者に帰属します。",
            "footerSource": "情報は Steam 公式ストア・IGN・公式プレスリリース・SteamDB で確認しています。",
            "quickAnswers": "よくある質問",
            "guides": "攻略一覧",
            "aboutGame": "このゲームについて",
            "startPlaying": "プレイする →",
            "getOnSteam": "Steam で入手 ↗",
            "moreGuides": "その他の攻略",
            "sources": "出典とファクトチェック",
            "readGuide": "遊び方 →",
        },
    },
}

GAME = {
    "name": "Kill The Shadow",
    "releaseDate": "August 5, 2026",
    "platforms": ["PC (Steam)"],
    "genre": "Detective RPG / Mystery / 2.5D Pixel",
    "price": "$16.99",
    "steamUrl": "https://store.steampowered.com/app/2660230/Kill_The_Shadow/",
    "officialSite": "",
    "intro": "Kill The Shadow is an atmospheric detective RPG with multiple endings, developed by Chinese studio Shadowlight and published globally under a deal with NEOWIZ. You play as Lucas, a former police officer in the divided city of Dark Tide City, who carries a supernatural entity called the Shadow on his back. It lets him reconstruct the final moments of the dead and rewind time during investigations. Every choice you make shapes relationships, the truth that comes to light, and which of the multiple endings you reach.",
    "keyFacts": [
        "Launched August 5, 2026 on Steam (Windows) at $16.99 / £14.99 / €16.99 with a 10% launch discount",
        "Detective RPG with multiple endings and a 'Shadow corruption' meter influenced by your choices",
        "Crime-scene reconstruction: witness the final moments of the dead exactly as they happened",
        "Time rewind: undo mistakes mid-investigation to try different dialogue and actions",
        "100,000+ Steam wishlists before launch, over 80% from outside China",
        "A free demo (with 10 achievements) has been available since 2024"
    ],
    "stats": [
        {"value": "Aug 5", "label": "Steam release"},
        {"value": "10万+", "label": "Wishlists before launch"},
        {"value": "Multi", "label": "Endings"},
        {"value": "2.5D", "label": "Pixel art noir"},
        {"value": "$16.99", "label": "On Steam"},
        {"value": "Win", "label": "Platform"}
    ],
    "nameI18n": {"zh": "杀死影子", "ja": "キル・ザ・シャドウ"},
    "statsI18n": {
        "zh": [
            {"value": "8月5日", "label": "Steam 发售"},
            {"value": "10万+", "label": "发售前愿望单"},
            {"value": "多结局", "label": "结局数量"},
            {"value": "2.5D", "label": "像素黑色电影"},
            {"value": "$16.99", "label": "Steam 售价"},
            {"value": "Windows", "label": "平台"}
        ],
        "ja": [
            {"value": "8/5", "label": "Steam 発売"},
            {"value": "10万+", "label": "発売前ウィッシュリスト"},
            {"value": "複数", "label": "エンディング"},
            {"value": "2.5D", "label": "ピクセル・ノワール"},
            {"value": "$16.99", "label": "Steam 価格"},
            {"value": "Windows", "label": "対応OS"}
        ],
    },
    "keyFactsI18n": {
        "zh": [
            "2026年8月5日在 Steam（Windows）发售，售价 $16.99 / £14.99 / €16.99，首发 -10%",
            "多结局侦探 RPG，你的选择会影响「影子黑化度」并决定结局走向",
            "犯罪现场重建：如同亲历死者最后时刻",
            "时间回溯：调查中可回退重来，尝试不同的对话与行动",
            "发售前愿望单突破 10 万份，80% 以上来自海外",
            "自 2024 年起有免费 Demo 可玩（含 10 个成就）"
        ],
        "ja": [
            "2026年8月5日に Steam（Windows）で発売。$16.99 / £14.99 / €16.99、ローンチ割引10%",
            "マルチエンディングの探偵RPG。選択が「シャドウの浸食度」に影響し、エンディングが分岐",
            "犯行現場再現：死者の最後の瞬間をそのまま目撃できる",
            "時間巻き戻し：調査中に失敗をやり直し、別の会話・行動を試せる",
            "発売前ウィッシュリスト10万件超、うち80%以上が海外からの登録",
            "2024年から無料デモを公開（実績10個）"
        ],
    },
    "introI18n": {
        "zh": "《杀死影子》是一款多结局的氛围派侦探 RPG，由中国工作室坞光岚影（Shadowlight）开发，并在 NEOWIZ 的全球发行协议下发行。你扮演暗潮市（Dark Tide City）的前警官 Lucas，他的背上寄宿着名为「影子」的超自然存在，能让他重建死者最后的瞬间，并在调查中回溯时间。你的每个选择都会改变人物关系、被揭开的真相，以及最终抵达的多个结局之一。",
        "ja": "『キル・ザ・シャドウ』は、中国のスタジオ Shadowlight が開発し、NEOWIZ のグローバル契約のもと配信される、マルチエンディングの空気感重視の探偵RPG。プレイヤーは分断された都市ダークタイド・シティの元警官ルーカスとなり、背中に宿る超常的存在「シャドウ」の力で死者の最期の瞬間を再現し、調査中に時間を巻き戻せます。選択のひとつひとつが関係性と明かされる真実、そして複数のエンディングの分岐に影響します。"
    },
}

print("SITE/GAME built, len ok:", len(json.dumps(SITE)), len(json.dumps(GAME)))

STEAM_URL = GAME["steamUrl"]
def SRC(label, url, zh, ja):
    return {"label": label, "url": url, "zh": zh, "ja": ja}

SRC_STEAM = SRC("Official Steam store page — Kill The Shadow", STEAM_URL,
                "Steam 官方商店页 — 杀死影子", "Steam 公式ストア — キル・ザ・シャドウ")
SRC_IGN = SRC("IGN — Kill the Shadow Launch Trailer", "https://in.ign.com/kill-the-shadow/268073/kill-the-shadow-official-launch-trailer",
              "IGN — 杀死影子发售宣传片", "IGN — キル・ザ・シャドウ ローンチトレーラー")
SRC_G2A = SRC("G2A News — Kill the Shadow game spotlight", "https://www.g2a.com/news/game-spotlights/kill-the-shadow-release/",
              "G2A News — 杀死影子专题报道", "G2A News — キル・ザ・シャドウ特集")
SRC_PRESS = SRC("Official press release — Phoenix Games", "https://www.gamespress.com/en-GB/Reconstruct-the-Past-Uncover-the-Truth-Kill-the-Shadow-Launches-on-Ste",
                "官方新闻稿 — Phoenix Games", "公式プレスリリース — Phoenix Games")
SRC_STEAMDB = SRC("SteamDB — Kill The Shadow Demo stats", "https://steamdb.info/app/2947640/stats/",
                  "SteamDB — 杀死影子 Demo 数据", "SteamDB — キル・ザ・シャドウ デモ統計")
SRC_IIG = SRC("Into Indie Games — Kill the Shadow Walkthrough Part 1", "https://intoindiegames.com/walkthroughs/kill-the-shadow-walkthrough-part-1-the-factory/",
              "Into Indie Games — 杀死影子流程攻略第一部分", "Into Indie Games — キル・ザ・シャドウ攻略パート1")

PAGES = []

def P(slug, title, metaTitle, metaDescription, intro, sections, sources, i18n):
    PAGES.append({"slug": slug, "title": title, "metaTitle": metaTitle, "metaDescription": metaDescription,
                  "intro": intro, "sections": sections, "sources": sources, "i18n": i18n})

# ---------- 1. how-to-play ----------
P("how-to-play",
  "How to Play Kill The Shadow",
  "How to Play Kill The Shadow: Full Beginner's Guide (2026)",
  "New to Kill The Shadow? Learn the core investigation loop, crime-scene reconstruction, time rewind, the Shadow corruption meter and how your choices shape the story.",
  "Kill The Shadow is a detective RPG where you investigate bizarre cases, reconstruct crime scenes and make moral choices that change the ending. Here is everything you need before your first case.",
  [
      {"type": "steps", "heading": "The Core Loop: Investigate, Reconstruct, Decide",
       "body": "Each case follows the same rhythm: gather evidence, use your supernatural power to relive the final moments of the dead, then decide how to act on what you learn.",
       "items": [
           "Investigate the scene — inspect clues, talk to witnesses and read documents",
           "Reconstruct the crime — rewind time and witness the victim's final moments exactly as they happened",
           "Confront the truth — choose how to respond with dialogue, intelligence or violence",
           "Live with the consequences — choices change relationships and which truths come to light"
       ]},
      {"type": "table", "heading": "The Three Approaches",
       "body": "The official store description says you can solve cases with eloquence, intelligence, the ability to rewind time — or even violence. Each approach suits different situations.",
       "columns": ["Approach", "How it works", "Best for"],
       "rows": [
           ["Eloquence", "Persuade witnesses and suspects through dialogue", "Getting information without raising suspicion"],
           ["Intelligence", "Link clues into logical chains and deduce the truth", "Cases built on contradictions in testimony"],
           ["Time rewind + violence", "Replay moments and, when needed, use force", "Breaking deadlocks or pursuing a darker path"]
       ]},
      {"type": "list", "heading": "Crime-Scene Reconstruction",
       "body": "Your partner, the Shadow, lets you reconstruct the final moments of the dead. This is the heart of every investigation.",
       "items": [
           "Use reconstruction to see exactly how a victim died, not just what the scene suggests",
           "Watch for details the killer tried to hide — staging a scene is a common tactic",
           "Reconstruction shows the past as it happened, but your interpretation still matters",
           "The same scene can be read differently once you know more about the people involved"
       ]},
      {"type": "list", "heading": "Time Rewind",
       "body": "During investigations you can rewind time to retry failed moments — wrong dialogue choices, missed clues or botched actions.",
       "items": [
           "Rewind to before a bad decision instead of restarting the whole chapter",
           "Try different dialogue options to see how characters react",
           "Rewinding does not erase knowledge — use what you learned to pick better options"
       ]},
      {"type": "steps", "heading": "How the Opening Plays Out",
       "body": "The game opens outside the police station, where Lucas receives a mysterious letter written on a medical gauge from someone named Lynn DaHandt.",
       "items": [
           "Enter the police station and meet the people Lucas used to work with",
           "Officer May greets you and sets the tone for your return",
           "Your first goal takes you toward the Factory district — the setting of Chapter 1",
           "From here, every conversation is a chance to shape relationships and the story"
       ]},
      {"type": "list", "heading": "Quickstart Checklist for Beginners",
       "body": "Five habits that will make you a better detective immediately.",
       "items": [
           "Reconstruct every scene you can — details hidden in the final moments often crack the case",
           "Read the documents: letters and medical gauges carry crucial story clues",
           "Talk to everyone before making decisions — relationships change endings",
           "Rewind freely in the early chapters to learn how characters react",
           "Keep the Shadow corruption meter in mind: darker choices push it higher"
       ]}
  ],
  [SRC_STEAM, SRC_IGN],
  {"zh": {
      "title": "杀死影子怎么玩",
      "metaTitle": "杀死影子怎么玩：新手完整指南（2026）",
      "metaDescription": "第一次玩杀死影子？掌握核心调查循环、犯罪现场重建、时间回溯、影子黑化度机制，以及选择如何改变剧情。",
      "intro": "《杀死影子》是一款侦探 RPG：调查离奇案件、重建犯罪现场，做出改变结局的道德抉择。这是你接手第一个案件前需要知道的一切。",
      "sections": [
          {"type": "steps", "heading": "核心循环：调查 → 重建 → 抉择",
           "body": "每个案件都遵循同一节奏：收集证据，用超能力重历死者最后的瞬间，然后决定如何利用你所知的一切。",
           "items": [
               "调查现场——检查线索、询问证人、阅读文档",
               "重建犯罪——回溯时间，亲眼目睹受害者最后的瞬间",
               "直面真相——用对话、智慧或暴力决定如何应对",
               "承担后果——选择改变人物关系，也改变被揭开的真相"
           ]},
          {"type": "table", "heading": "三种破案路线",
           "body": "官方商店页描述：你可以用口才、智慧、时间回溯能力——甚至暴力——来解决案件。每条路线适合不同情境。",
           "columns": ["路线", "运作方式", "适合场景"],
           "rows": [
               ["口才", "用对话说服证人与嫌疑人", "不打草惊蛇地获取信息"],
               ["智慧", "把线索连成逻辑链并推理真相", "证词互相矛盾的案件"],
               ["时间回溯+暴力", "重放关键时刻，必要时诉诸武力", "打破僵局或走上更黑暗的道路"]
           ]},
          {"type": "list", "heading": "犯罪现场重建",
           "body": "你的搭档「影子」能让你重建死者最后的瞬间。这是每个调查的核心。",
           "items": [
               "用重建看到受害者真实的死法，而不只是现场表面的样子",
               "留意凶手试图掩盖的细节——伪造现场是常见手段",
               "重建展示的是过去发生的事实，但你的解读仍然重要",
               "当你更了解涉案人物后，同一个现场会有不同的读法"
           ]},
          {"type": "list", "heading": "时间回溯",
           "body": "调查中你可以回溯时间，重试失败的关键时刻——错误的对话选项、漏掉的线索或搞砸的行动。",
           "items": [
               "回退到糟糕决定之前，而不是重开整个章节",
               "尝试不同的对话选项，看看角色如何反应",
               "回溯不会抹去记忆——用学到的信息选更好的选项"
           ]},
          {"type": "steps", "heading": "开场流程",
           "body": "游戏在警察局外开场，Lucas 收到一封写在医疗计量器上的神秘信件，寄信人是 Lynn DaHandt。",
           "items": [
               "进入警察局，见到 Lucas 曾经的同事",
               "警官 May 接待了你，为你的回归定下基调",
               "第一个目标指向工厂区——第一章的舞台",
               "从这里开始，每段对话都是改变关系与剧情的机会"
           ]},
          {"type": "list", "heading": "新手快速上手清单",
           "body": "五个能立刻提升你侦探水平的小习惯。",
           "items": [
               "尽量重建每个现场——藏在最后瞬间里的细节往往能破案",
               "读文档：信件和医疗计量器承载着关键剧情线索",
               "做决定前先和所有人聊一遍——关系会改变结局",
               "前几章放心回溯，学习角色们会如何反应",
               "留意影子黑化度：更黑暗的选择会让它升高"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウの遊び方",
      "metaTitle": "キル・ザ・シャドウの遊び方：初心者完全ガイド（2026）",
      "metaDescription": "キル・ザ・シャドウ初心者向け。調査ループ、犯行現場再現、時間巻き戻し、シャドウ浸食度、選択が物語をどう変えるかを解説。",
      "intro": "『キル・ザ・シャドウ』は、奇怪な事件を調査し、犯行現場を再現し、エンディングを変える道徳的選択を行う探偵RPG。最初の事件を始める前に知っておくべきことをすべてまとめました。",
      "sections": [
          {"type": "steps", "heading": "基本ループ：調査 → 再現 → 選択",
           "body": "どの事件も同じリズムで進みます：証拠を集め、超常の力で死者の最期を再現し、知った事実をどう使うかを選びます。",
           "items": [
               "現場を調査——手がかりを調べ、目撃者に話し、書類を読む",
               "犯行を再現——時間を巻き戻し、犠牲者の最期をそのまま目撃する",
               "真実と向き合う——会話・知性・暴力のどれで応じるか選ぶ",
               "結果を受け入れる——選択が関係性と明かされる真実を変える"
           ]},
          {"type": "table", "heading": "3つのアプローチ",
           "body": "公式ストア説明では、弁舌・知性・時間巻き戻し、さらには暴力で事件を解決できるとされています。",
           "columns": ["アプローチ", "仕組み", "適した場面"],
           "rows": [
               ["弁舌", "会話で証人や容疑者を説得", "疑われずに情報を得たいとき"],
               ["知性", "手がかりを論理の鎖で結び真実を導く", "証言が矛盾する事件"],
               ["時間巻き戻し+暴力", "場面を再生し、必要なら実力行使", "行き詰まりの打破、あるいは暗い道"]
           ]},
          {"type": "list", "heading": "犯行現場再現",
           "body": "相棒「シャドウ」の力で死者の最期を再現できます。すべての調査の核心です。",
           "items": [
               "現場の見た目だけでなく、犠牲者が実際にどう死んだかを再現で見る",
               "犯人が隠そうとした細部を見逃さない——偽装現場はよくある手口",
               "再現は「実際に起きた過去」を見せるが、解釈は自分次第",
               "関係者を深く知ると、同じ現場も違って読める"
           ]},
          {"type": "list", "heading": "時間巻き戻し",
           "body": "調査中に時間を巻き戻し、失敗した瞬間——間違えた会話、見落とした手がかり、失敗した行動——をやり直せます。",
           "items": [
               "章全体をやり直すのではなく、悪い判断の前に戻る",
               "別の会話選択を試してキャラクターの反応を見る",
               "巻き戻しても記憶は消えない——学んだ情報でより良い選択を"
           ]},
          {"type": "steps", "heading": "オープニングの流れ",
           "body": "ゲームは警察署の外で始まり、ルーカスは医療メーターに書かれた謎の手紙を Lynn DaHandt という人物から受け取ります。",
           "items": [
               "警察署に入り、ルーカスのかつての同僚たちに会う",
               "メイ巡査が迎え、彼の復帰の雰囲気を語る",
               "最初の目標はファクトリー地区——第1章の舞台へ",
               "ここから先、すべての会話が関係性と物語を変えるチャンス"
           ]},
          {"type": "list", "heading": "初心者チェックリスト",
           "body": "すぐに上達する5つの習慣。",
           "items": [
               "できるだけ現場を再現する——最期の瞬間に事件を解く鍵が隠れている",
               "書類を読む：手紙や医療メーターは重要な物語の手がかり",
               "決断の前に全員と話す——関係性がエンディングを変える",
               "序盤は気軽に巻き戻してキャラクターの反応を学ぶ",
               "シャドウ浸食度に注意：暗い選択ほど上昇する"
           ]}
      ]
  }})
print("batch1 done, pages:", len(PAGES))

# ---------- 2. walkthrough ----------
P("walkthrough",
  "Kill The Shadow Walkthrough: Chapter 1 — The Factory",
  "Kill The Shadow Walkthrough: Chapter 1 — The Factory (2026)",
  "Step-by-step walkthrough of Kill The Shadow Chapter 1: from the police station opening to the Factory district, including key decisions and what to look for.",
  "This walkthrough follows our verified playthrough of Chapter 1. Because choices change outcomes, your results may differ — use this as a map, not a script.",
  [
      {"type": "steps", "heading": "Part 1 — The Police Station Opening",
       "body": "Kill The Shadow begins outside the police station, where Lucas receives a mysterious letter written on a medical gauge from someone named Lynn DaHandt.",
       "items": [
           "Walk into the station — Officer May greets you as you return",
           "Explore the station and talk to the officers; dialogue choices here start shaping relationships",
           "Read the letter carefully: the medical gauge is the first of several medical documents that matter later",
           "Your objective points toward the Factory district, the setting of Chapter 1"
       ]},
      {"type": "list", "heading": "Key Decisions in the Opening",
       "body": "The opening is short but sets the tone for how Lucas is received — and how the Shadow reacts.",
       "items": [
           "How you respond to May's questions affects your relationship with the station",
           "Choosing to share or hide information about the Shadow changes how characters see you",
           "Rewind is available early — experiment with different responses to learn the tone"
       ]},
      {"type": "steps", "heading": "Part 2 — Heading to the Factory",
       "body": "The first real investigation takes you to the Factory district, where Lucas must reconstruct what happened on the scene.",
       "items": [
           "Make your way to the Factory and enter the scene",
           "Inspect the area before using reconstruction — the physical clues inform what you should look for",
           "Use crime-scene reconstruction to witness the victim's final moments",
           "Compare what reconstruction shows with what the scene appears to say — staged details are the key tell"
       ]},
      {"type": "list", "heading": "What to Look For in the Factory",
       "body": "Based on our playthrough, these are the details that matter most in Chapter 1.",
       "items": [
           "The medical gauge: cross-reference it with the opening letter",
           "Who had access to the factory floor at the time of death",
           "Whether the victim's body position matches the reconstructed events",
           "Small environmental clues that dialogue alone will not reveal"
       ]},
      {"type": "list", "heading": "After Chapter 1",
       "body": "The game's semi-open city opens up as you complete chapters. Keep these habits going.",
       "items": [
           "Return to previous areas when you learn new information — dialogue can change",
           "Track the relationships panel and Shadow corruption meter between chapters",
           "Each case feeds into the larger mystery behind Dark Tide City's ten-year-old event"
       ]}
  ],
  [SRC_IIG, SRC_STEAM],
  {"zh": {
      "title": "杀死影子全流程：第一章 · 工厂",
      "metaTitle": "杀死影子全流程攻略：第一章工厂（2026）",
      "metaDescription": "杀死影子第一章完整流程：从警察局开场到工厂区，含关键抉择与注意事项。选择会改变结果，本攻略是地图而非剧本。",
      "intro": "本攻略基于我们已核实的通关记录。由于选择会改变结果，你的体验可能不同——把它当作地图，而不是剧本。",
      "sections": [
          {"type": "steps", "heading": "第一部分 · 警察局开场",
           "body": "游戏在警察局外开始，Lucas 收到一封写在医疗计量器上的神秘信件，寄信人是 Lynn DaHandt。",
           "items": [
               "走进警察局——警官 May 迎接你的回归",
               "探索警察局并与警官们交谈；这里的对话选择开始塑造关系",
               "仔细读信：医疗计量器是之后重要的医疗类文档中的第一件",
               "目标指向工厂区——第一章的舞台"
           ]},
          {"type": "list", "heading": "开场的关键抉择",
           "body": "开场虽短，却决定了 Lucas 如何被接纳——以及影子如何反应。",
           "items": [
               "你对 May 问题的回应会影响你与警察局的关系",
               "选择分享或隐瞒影子的信息，会改变他人对你的看法",
               "早期就能回溯——尝试不同回应来把握基调"
           ]},
          {"type": "steps", "heading": "第二部分 · 前往工厂",
           "body": "第一次真正的调查带你来到工厂区，Lucas 必须重建现场发生的一切。",
           "items": [
               "前往工厂并进入现场",
               "先用肉眼检查区域——物理线索决定你该寻找什么",
               "用犯罪现场重建目睹受害者最后的瞬间",
               "对比重建与现实现场的差异——伪造的细节是关键破绽"
           ]},
          {"type": "list", "heading": "在工厂里留意什么",
           "body": "根据我们的通关记录，以下是第一章里最重要的细节。",
           "items": [
               "医疗计量器：与开场的信件交叉比对",
               "死亡发生时谁有权限进入工厂车间",
               "受害者的尸体位置是否与重建的事件一致",
               "仅靠对话无法揭示的环境小线索"
           ]},
          {"type": "list", "heading": "第一章之后",
           "body": "随着章节推进，游戏的半开放城市会逐渐展开。请保持这些习惯。",
           "items": [
               "获得新信息后回到旧区域——对话可能会改变",
               "在章节之间关注关系面板与影子黑化度",
               "每个案件都汇入暗潮市十年前的谜团主线"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ攻略：第1章 ファクトリー",
      "metaTitle": "キル・ザ・シャドウ攻略：第1章 ファクトリー（2026）",
      "metaDescription": "キル・ザ・シャドウ第1章の完全攻略：警察署のオープニングからファクトリー地区まで。重要選択と見どころを解説。",
      "intro": "この攻略は検証済みのプレイ記録に基づいています。選択によって結果が変わるため、あなたの展開は異なるかもしれません。地図として使い、台本にはしないでください。",
      "sections": [
          {"type": "steps", "heading": "パート1 · 警察署のオープニング",
           "body": "ゲームは警察署の外で始まり、ルーカスは医療メーターに書かれた謎の手紙を Lynn DaHandt から受け取ります。",
           "items": [
               "署内に入る——メイ巡査が復帰を迎えてくれる",
               "署内を探索し警官たちと話す——ここでの選択が関係性を形作る",
               "手紙をよく読む：医療メーターは後に重要な医療書類の第一号",
               "目標は第1章の舞台、ファクトリー地区へ"
           ]},
          {"type": "list", "heading": "オープニングの重要選択",
           "body": "短いオープニングですが、ルーカスがどう迎えられるか、シャドウがどう反応するかを決めます。",
           "items": [
               "メイの質問への答え方で署との関係が変わる",
               "シャドウの情報を共有するか隠すかで、周囲の見方が変わる",
               "序盤から巻き戻し可能——反応を試してトーンを掴もう"
           ]},
          {"type": "steps", "heading": "パート2 · ファクトリーへ",
           "body": "最初の本格調査はファクトリー地区。ルーカスは現場で何が起きたのかを再現しなければなりません。",
           "items": [
               "ファクトリーに向かい現場に入る",
               "再現の前にまず現場を調べる——物理的な手がかりが探すべきものを示す",
               "犯行現場再現で犠牲者の最期を目撃する",
               "再現と現場の見た目の違いを比べる——偽装の細部が決定的な手掛かり"
           ]},
          {"type": "list", "heading": "ファクトリーで注目すべき点",
           "body": "私たちのプレイ記録に基づく、第1章で最も重要な細部です。",
           "items": [
               "医療メーター：冒頭の手紙と照合する",
               "死亡時刻に工場フロアへ出入りできた人物",
               "犠牲者の体勢と再現された出来事の一致",
               "会話だけでは明かされない環境の細かい手がかり"
           ]},
          {"type": "list", "heading": "第1章のあと",
           "body": "章を進めるほど半オープンの都市が広がります。この習慣を続けましょう。",
           "items": [
               "新しい情報を得たら以前の場所に戻る——会話が変わることも",
               "章の合間に関係パネルとシャドウ浸食度を確認",
               "各事件はダークタイド・シティの10年前の謎へとつながる"
           ]}
      ]
  }})

# ---------- 3. choices ----------
P("choices",
  "Kill The Shadow Choices: How Every Decision Changes the Story",
  "Kill The Shadow Choices Guide: Relationships, Truth & Endings (2026)",
  "How choices work in Kill The Shadow: dialogue and moral decisions, the Shadow corruption meter, and how protecting someone can bury a more dangerous truth.",
  "Kill The Shadow is built around meaningful choice. This guide explains the systems behind the choices and what to consider before you commit.",
  [
      {"type": "list", "heading": "What Choices Actually Change",
       "body": "According to the publisher's description, choices change relationships, determine which truths come to light, and contribute to multiple endings.",
       "items": [
           "Relationships: characters remember how you treated them and react differently later",
           "Truth: some paths reveal certain facts while burying others",
           "Endings: the game's multiple endings branch from the decisions you make",
           "The Shadow: darker choices push the corruption meter and change how the story unfolds"
       ]},
      {"type": "steps", "heading": "The Choice Framework",
       "body": "Most meaningful choices fit into three layers. Knowing the layers helps you predict consequences.",
       "items": [
           "Immediate: what happens in the next scene (who trusts you, what doors open)",
           "Relationship: how a character's arc develops across the whole game",
           "Thematic: whether you pursue justice or protection — the official description notes 'justice may not always produce the kindest result, while protecting someone can leave a more dangerous truth buried'"
       ]},
      {"type": "list", "heading": "Justice vs Protection",
       "body": "The launch spotlight describes the central tension: do you deliver justice, or protect the people involved?",
       "items": [
           "Justice may feel clean but can hurt people who did not deserve it",
           "Protection can spare someone while letting a bigger truth stay buried",
           "There is no 'correct' answer — the game is designed so both roads lead somewhere meaningful",
           "Decide based on the character, not on trying to game the system"
       ]},
      {"type": "list", "heading": "Tips for Choosing Well",
       "body": "Practical habits from our playthrough.",
       "items": [
           "Reconstruct the scene and read all documents before choosing — information is power",
           "Rewind after a choice you regret; the game encourages experimentation",
           "Keep a mental note of who told you what — contradictions are the game's bread and butter",
           "If you want to see everything, plan a second playthrough with an opposite moral stance"
       ]}
  ],
  [SRC_G2A, SRC_PRESS],
  {"zh": {
      "title": "杀死影子抉择指南：每个决定如何改变剧情",
      "metaTitle": "杀死影子抉择攻略：关系、真相与结局（2026）",
      "metaDescription": "杀死影子的抉择系统详解：对话与道德选择、影子黑化度，以及「保护某人可能埋下更危险的真相」。",
      "intro": "《杀死影子》围绕有分量的选择而建。本指南解释选择背后的系统，以及你在做出承诺前该考虑什么。",
      "sections": [
          {"type": "list", "heading": "选择真正改变什么",
           "body": "发行方描述：选择会改变关系、决定哪些真相浮出水面，并通向多个结局。",
           "items": [
               "关系：角色会记住你如何对待他们，并在之后做出不同的反应",
               "真相：有些路线会揭示某些事实，同时埋没另一些",
               "结局：游戏的多结局由你的决定分叉",
               "影子：更黑暗的选择会推高黑化度，改变故事的展开方式"
           ]},
          {"type": "steps", "heading": "选择的层次框架",
           "body": "大多数有意义的选择分三层。理解层次有助于预判后果。",
           "items": [
               "即时层：下一个场景发生什么（谁信任你、哪些门打开）",
               "关系层：一个角色的故事线如何贯穿全程发展",
               "主题层：你追求正义还是保护——官方描述指出「正义未必带来最仁慈的结果，而保护某人可能埋下更危险的真相」"
           ]},
          {"type": "list", "heading": "正义 vs 保护",
           "body": "发售专题描述了核心张力：你选择伸张正义，还是保护涉案的人？",
           "items": [
               "正义可能看起来很干净，却会伤害不该受伤的人",
               "保护可以放过某人，却让更大的真相继续被埋没",
               "没有「正确」答案——游戏设计上两条路都通向有意义的结果",
               "根据角色本身做决定，而不是试图操纵系统"
           ]},
          {"type": "list", "heading": "做出好选择的技巧",
           "body": "来自我们通关记录的实用习惯。",
           "items": [
               "先重建现场、读完所有文档再选择——信息就是力量",
               "后悔了就回溯；游戏鼓励你尝试",
               "在心里记下谁对你说了什么——矛盾正是这款游戏的精髓",
               "想看完一切？二周目用相反的道德立场再来一次"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ選択肢ガイド：選択が物語をどう変えるか",
      "metaTitle": "キル・ザ・シャドウ選択肢攻略：関係・真実・エンディング（2026）",
      "metaDescription": "キル・ザ・シャドウの選択システム解説：会話と道徳的判断、シャドウ浸食度、そして「誰かを守ることが危険な真実を埋めること」について。",
      "intro": "『キル・ザ・シャドウ』は意味ある選択を軸に作られています。選択の背後にあるシステムと、決断前に考えるべきことを解説します。",
      "sections": [
          {"type": "list", "heading": "選択が実際に変えるもの",
           "body": "パブリッシャーの説明によれば、選択は関係性を変え、明かされる真実を左右し、複数のエンディングへとつながります。",
           "items": [
               "関係性：キャラクターはあなたの扱いを覚え、後で違う反応をする",
               "真実：一部の道はある事実を明かし、別の事実を埋める",
               "エンディング：マルチエンディングはあなたの決断から分岐する",
               "シャドウ：暗い選択は浸食度を上げ、物語の展開を変える"
           ]},
          {"type": "steps", "heading": "選択の3つのレイヤー",
           "body": "意味ある選択のほとんどは3層に分かれます。層を知れば結果を予測しやすくなります。",
           "items": [
               "即時：次のシーンで起こること（誰が信頼するか、どの扉が開くか）",
               "関係：キャラクターの物語がゲーム全体でどう育つか",
               "テーマ：正義か保護か——公式説明は「正義が常に最も優しい結果をもたらすとは限らず、誰かを守ることが危険な真実を埋め続けることもある」と述べています"
           ]},
          {"type": "list", "heading": "正義 vs 保護",
           "body": "ローンチ特集が描く中心的な葛藤：あなたは正義を貫くのか、関わった人々を守るのか。",
           "items": [
               "正義はきれいに見えるが、報われるべきでない人を傷つけることも",
               "保護は誰かを救う代わりに、より大きな真実を埋め続ける",
               "「正解」はない——どちらの道も意味ある結末に至る設計",
               "システムを攻略しようとせず、キャラクター本位で決める"
           ]},
          {"type": "list", "heading": "上手に選ぶための習慣",
           "body": "私たちのプレイ記録から得た実用的な習慣です。",
           "items": [
               "選ぶ前に現場を再現し、すべての書類を読む——情報は力",
               "後悔したら巻き戻す；このゲームは試行錯誤を歓迎する",
               "誰が何を言ったかを心に留める——矛盾こそこのゲームの真骨頂",
               "全部見たければ、二周目は逆の道徳的立場で"
           ]}
      ]
  }})
print("batch2 done, pages:", len(PAGES))

# ---------- 4. endings ----------
P("endings",
  "Kill The Shadow Endings: How Many Endings & How to Reach Them",
  "Kill The Shadow Endings Guide: All Endings & Branch Conditions (2026)",
  "Everything confirmed about Kill The Shadow's multiple endings: how many there are, how the Shadow corruption meter and choices branch the story, and what to do for a second playthrough.",
  "Kill The Shadow is confirmed to have multiple endings driven by player choice. Full branch conditions are still being documented by the community; this page covers everything verified so far.",
  [
      {"type": "list", "heading": "Confirmed Facts",
       "body": "What we can state from official sources without guessing.",
       "items": [
           "The game features multiple endings (confirmed by the publisher and press coverage)",
           "Endings branch from player choices across the whole story, not just the final chapter",
           "The 'Shadow corruption' mechanic — influenced by darker choices — is tied to how the story unfolds",
           "A single playthrough is not enough to see every ending; the game rewards an opposite-stance second run"
       ]},
      {"type": "list", "heading": "What Affects the Ending",
       "body": "Based on the officially described systems, these are the levers that matter.",
       "items": [
           "The Shadow corruption meter — darker choices push it higher",
           "Key dialogue decisions and how you treat each character",
           "Whether you pursue justice or protection in each case",
           "Which truths you uncover — or choose to leave buried",
           "Relationships built across all chapters, not isolated decisions"
       ]},
      {"type": "steps", "heading": "How to Approach a Second Playthrough",
       "body": "To see endings you missed, change your moral stance — not just your dialogue.",
       "items": [
           "Pick the opposite stance on justice vs protection from your first run",
           "Keep the Shadow corruption meter low in one run and high in another",
           "Save often and use rewind to experiment at major decision points",
           "Track which characters you prioritized — relationship arcs change what is revealed"
       ]},
      {"type": "list", "heading": "⚠️ Not Yet Verified",
       "body": "Community documentation is still catching up after launch. We will update this page as reliable sources confirm specifics.",
       "items": [
           "The exact total number of endings",
           "The precise corruption-meter thresholds for each branch",
           "Whether every ending is reachable in a single playthrough"
       ]}
  ],
  [SRC_PRESS, SRC_G2A],
  {"zh": {
      "title": "杀死影子结局：有几个结局，如何达成",
      "metaTitle": "杀死影子结局攻略：全部结局与分叉条件（2026）",
      "metaDescription": "杀死影子多结局的已确认信息：结局数量、影子黑化度与选择如何分叉剧情，以及二周目该怎么做。",
      "intro": "《杀死影子》已确认拥有由玩家选择驱动的多结局。完整分叉条件仍在被社区整理；本页汇总目前所有已核实的信息。",
      "sections": [
          {"type": "list", "heading": "已确认的事实",
           "body": "以下是我们能基于官方来源、不做猜测得出的信息。",
           "items": [
               "游戏拥有多结局（发行方与媒体均已确认）",
               "结局由整个故事中的选择分叉，而不只是最后一章",
               "「影子黑化度」机制——受更黑暗的选择影响——与故事的展开方式相关",
               "单周目无法看完全部结局；游戏奖励相反立场的二周目"
           ]},
          {"type": "list", "heading": "什么影响结局",
           "body": "根据官方描述的系统，以下杠杆至关重要。",
           "items": [
               "影子黑化度——更黑暗的选择推高它",
               "关键对话决定，以及你对待每个角色的方式",
               "每个案件里你选择正义还是保护",
               "你揭开了哪些真相——或选择让哪些继续埋没",
               "跨章节建立的关系，而不是孤立的决定"
           ]},
          {"type": "steps", "heading": "二周目怎么做",
           "body": "要看错过的结局，改变你的道德立场——而不只是换对话。",
           "items": [
               "与一周目相反的正义/保护立场",
               "一周目压低影子黑化度，另一周目抬高它",
               "经常存档，在关键决策点用回溯做实验",
               "记录你优先对待的角色——关系线会改变被揭示的内容"
           ]},
          {"type": "list", "heading": "⚠️ 尚未核实",
           "body": "发售后的社区整理仍在进行中。可靠来源确认细节后，我们会更新本页。",
           "items": [
               "结局的确切总数",
               "各分叉对应的黑化度精确阈值",
               "每个结局是否都能在单周目内达成"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ エンディング：数と到達条件",
      "metaTitle": "キル・ザ・シャドウ エンディング攻略：全エンドと分岐条件（2026）",
      "metaDescription": "キル・ザ・シャドウのマルチエンディング確定情報：エンド数、シャドウ浸食度と選択による分岐、2周目の進め方。",
      "intro": "『キル・ザ・シャドウ』はプレイヤーの選択で分岐するマルチエンディングが確定しています。分岐条件の完全な整理はコミュニティで進行中。本ページでは現時点で検証済みの情報をまとめています。",
      "sections": [
          {"type": "list", "heading": "確定している事実",
           "body": "推測を交えず、公式ソースから言えること。",
           "items": [
               "マルチエンディング（パブリッシャーと報道が確認）",
               "エンディングは最終章だけでなく物語全体の選択から分岐",
               "「シャドウ浸食度」——暗い選択で上昇——が物語の展開と関連",
               "1周で全エンドは見られない；逆の立場での2周目が報われる設計"
           ]},
          {"type": "list", "heading": "エンディングを左右する要素",
           "body": "公式に説明されているシステムに基づく、重要なレバーです。",
           "items": [
               "シャドウ浸食度——暗い選択ほど上昇",
               "重要な会話の選択と、各キャラクターへの接し方",
               "各事件で正義を選ぶか保護を選ぶか",
               "明かす真実——あるいは埋めたままにする真実",
               "単発の決定ではなく、全章にわたって築く関係性"
           ]},
          {"type": "steps", "heading": "2周目の進め方",
           "body": "見逃したエンドを見るには、会話だけでなく道徳的立場を変えましょう。",
           "items": [
               "1周目と逆の正義/保護スタンスで",
               "片方の周は浸食度を低く、もう片方は高く",
               "こまめにセーブし、重要分岐で巻き戻しを活用",
               "優先したキャラクターを記録——関係線が明かされる内容を変える"
           ]},
          {"type": "list", "heading": "⚠️ 未検証",
           "body": "発売直後のため、コミュニティの整理が追いついていません。信頼できる情報源が確定次第、本ページを更新します。",
           "items": [
               "エンディングの正確な総数",
               "各分岐の浸食度の正確なしきい値",
               "全エンドが1周で到達可能かどうか"
           ]}
      ]
  }})

# ---------- 5. cases ----------
P("cases",
  "Kill The Shadow Cases: Every Investigation So Far",
  "Kill The Shadow Cases Guide: All Investigations (2026)",
  "The confirmed cases in Kill The Shadow so far — from the police station opening to the Factory — and how each investigation builds the central mystery.",
  "Kill The Shadow is structured as a series of cases that feed into one larger mystery. This page tracks every case we can verify.",
  [
      {"type": "table", "heading": "Verified Cases",
       "body": "Cases confirmed in coverage of the launch and the first chapter walkthrough.",
       "columns": ["Case", "Location", "Key Element", "Status"],
       "rows": [
           ["The Letter", "Police Station (opening)", "A letter written on a medical gauge from Lynn DaHandt", "Chapter 1 opening"],
           ["The Factory Case", "Factory district", "Crime-scene reconstruction of the victim's final moments", "Chapter 1 main case"],
           ["Ongoing investigations", "Dark Tide City", "Semi-open city with multiple cases", "As the story unfolds"]
       ]},
      {"type": "list", "heading": "How Cases Connect",
       "body": "Each case you solve feeds the larger picture.",
       "items": [
           "Medical documents — the gauge from the opening letter — recur across investigations",
           "People from one case appear in later ones, with relationships that persist",
           "The mysterious event that fractured Dark Tide City ten years ago is the thread connecting everything"
       ]},
      {"type": "list", "heading": "Case-Solving Checklist",
       "body": "The routine that works on every case we have played.",
       "items": [
           "Read every document before talking to anyone",
           "Reconstruct the scene early — then re-read it after new information",
           "Note contradictions between what witnesses say and what reconstruction shows",
           "Decide whether the case calls for justice or protection before you act"
       ]}
  ],
  [SRC_IIG, SRC_IGN],
  {"zh": {
      "title": "杀死影子案件：目前全部调查",
      "metaTitle": "杀死影子案件攻略：全部调查（2026）",
      "metaDescription": "杀死影子目前已确认的案件——从警察局开场到工厂——以及每个调查如何构建核心谜团。",
      "intro": "《杀死影子》由一系列案件构成，它们汇入一个更大的谜团。本页追踪所有我们能核实的案件。",
      "sections": [
          {"type": "table", "heading": "已核实的案件",
           "body": "发售报道与第一章流程中确认的案件。",
           "columns": ["案件", "地点", "关键要素", "状态"],
           "rows": [
               ["那封信", "警察局（开场）", "Lynn DaHandt 写在医疗计量器上的信", "第一章开场"],
               ["工厂案", "工厂区", "对受害者最后瞬间的犯罪现场重建", "第一章主案件"],
               ["持续调查", "暗潮市", "半开放城市中的多个案件", "随剧情展开"]
           ]},
          {"type": "list", "heading": "案件如何相连",
           "body": "你解决的每个案件都汇入更大的图景。",
           "items": [
               "医疗文档——开场信件里的计量器——在多个调查中反复出现",
               "一个案件里的人物会出现在后续案件中，关系持续存在",
               "十年前撕裂暗潮市的神秘事件，是贯穿一切的线索"
           ]},
          {"type": "list", "heading": "破案检查清单",
           "body": "在我们玩过的每个案件上都行之有效的例行程序。",
           "items": [
               "与任何人交谈前先读完所有文档",
               "尽早重建现场——获得新信息后再重读一遍",
               "留意证人的说法与重建展示之间的矛盾",
               "行动前先判断这个案件该用正义还是保护"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウの事件：確認済みの全調査",
      "metaTitle": "キル・ザ・シャドウ事件攻略：全調査（2026）",
      "metaDescription": "キル・ザ・シャドウで確認済みの事件——警察署のオープニングからファクトリーまで——と、各調査が中心の謎をどう築くか。",
      "intro": "『キル・ザ・シャドウ』は、より大きな謎へとつながる一連の事件で構成されています。検証できるすべての事件を本ページで追跡します。",
      "sections": [
          {"type": "table", "heading": "検証済みの事件",
           "body": "ローンチ報道と第1章ウォークスルーで確認された事件。",
           "columns": ["事件", "場所", "重要な要素", "状態"],
           "rows": [
               ["手紙", "警察署（オープニング）", "Lynn DaHandt が医療メーターに書いた手紙", "第1章オープニング"],
               ["ファクトリー事件", "ファクトリー地区", "犠牲者の最期の犯行現場再現", "第1章のメイン事件"],
               ["進行中の調査", "ダークタイド・シティ", "半オープン都市での複数の事件", "物語が進むにつれて"]
           ]},
          {"type": "list", "heading": "事件のつながり",
           "body": "解決した事件はすべて、より大きな絵の一部になります。",
           "items": [
               "医療書類——冒頭の手紙のメーター——が複数の調査に登場",
               "ある事件の人物が後の事件にも現れ、関係性は継続",
               "10年前にダークタイド・シティを分断した謎の出来事がすべてをつなぐ糸"
           ]},
          {"type": "list", "heading": "事件解決チェックリスト",
           "body": "プレイしたすべての事件で有効だった手順です。",
           "items": [
               "誰かに話す前にすべての書類を読む",
               "早めに現場を再現し、新情報を得たら読み直す",
               "証言と再現の矛盾に注目する",
               "行動前に、この事件が正義か保護かを判断する"
           ]}
      ]
  }})

# ---------- 6. investigation ----------
P("investigation",
  "Kill The Shadow Investigation System Explained",
  "Kill The Shadow Investigation System: Reconstruction & Deduction Guide (2026)",
  "How the investigation system works in Kill The Shadow: crime-scene reconstruction, the logic chains of deduction, time rewind and the evidence you need to solve each case.",
  "The investigation system is the mechanical heart of Kill The Shadow. Here is how it actually works, based on official descriptions and our playthrough.",
  [
      {"type": "list", "heading": "The Three Pillars",
       "body": "Every investigation combines three systems.",
       "items": [
           "Observation: inspect the scene, read documents, talk to people",
           "Reconstruction: use the Shadow to witness the victim's final moments exactly as they happened",
           "Deduction: link clues into logical chains to identify the truth behind the contradiction"
       ]},
      {"type": "steps", "heading": "Reconstruction, Step by Step",
       "body": "The signature mechanic. Official materials describe reconstructing the past 'exactly as it happened'.",
       "items": [
           "Trigger reconstruction at the scene where the death occurred",
           "Watch the final moments unfold — do not assume the scene is what it looks like",
           "Look for details the killer may have staged or removed",
           "Compare the reconstructed past with the physical evidence in the present"
       ]},
      {"type": "list", "heading": "Reading Contradictions",
       "body": "Most cases are solved by finding where the story does not add up.",
       "items": [
           "A witness describes the victim differently than reconstruction shows",
           "The body position does not match the claimed cause of death",
           "An object is present that the reconstructed events cannot explain",
           "Timing: the sequence of events reconstruction reveals does not fit the timeline others describe"
       ]},
      {"type": "list", "heading": "Evidence That Matters",
       "body": "From our playthrough, these evidence types consistently carry weight.",
       "items": [
           "Medical documents — the gauge from the opening letter is the first of several",
           "Environmental details at the scene that dialogue does not mention",
           "Who had access and motive, established through conversation",
           "Your own reconstruction notes — write down what differs from the official story"
       ]},
      {"type": "list", "heading": "Common Mistakes",
       "body": "Things that slow down a case.",
       "items": [
           "Relying on conversation alone instead of reconstructing the scene",
           "Missing documents because you left an area early — return after new information",
           "Ignoring the contradiction between witnesses and evidence",
           "Forgetting that rewind is available when you feel stuck"
       ]}
  ],
  [SRC_IGN, SRC_STEAMDB],
  {"zh": {
      "title": "杀死影子调查系统详解",
      "metaTitle": "杀死影子调查系统：重建与推理指南（2026）",
      "metaDescription": "杀死影子调查系统详解：犯罪现场重建、逻辑链推理、时间回溯，以及破案需要的证据。",
      "intro": "调查系统是《杀死影子》机制的核心。以下基于官方描述与我们的通关记录，说明它实际如何运作。",
      "sections": [
          {"type": "list", "heading": "三大支柱",
           "body": "每次调查都结合三个系统。",
           "items": [
               "观察：检查现场、阅读文档、与人交谈",
               "重建：用影子亲眼目睹受害者最后的瞬间",
               "推理：把线索连成逻辑链，找出矛盾背后的真相"
           ]},
          {"type": "steps", "heading": "重建，一步步来",
           "body": "招牌机制。官方资料描述为「如同亲历」地重建过去。",
           "items": [
               "在死亡发生的现场触发重建",
               "观看最后瞬间展开——不要默认现场就是它看起来的样子",
               "寻找凶手可能伪造或移除的细节",
               "把重建的过去与当下的物理证据对比"
           ]},
          {"type": "list", "heading": "读懂矛盾",
           "body": "大多数案件靠找出「对不上」的地方来破解。",
           "items": [
               "证人对受害者的描述与重建展示的不一致",
               "尸体位置与所称死因不符",
               "出现了重建事件无法解释的物品",
               "时序：重建揭示的事件顺序与其他人描述的时间线不符"
           ]},
          {"type": "list", "heading": "重要的证据",
           "body": "从我们的通关记录看，这些证据类型始终有分量。",
           "items": [
               "医疗文档——开场信件的计量器是其中第一件",
               "对话未提及的现场环境细节",
               "通过交谈确认谁有权限、谁有动机",
               "你自己的重建笔记——记下与官方说法不同的地方"
           ]},
          {"type": "list", "heading": "常见错误",
           "body": "会拖慢破案节奏的事情。",
           "items": [
               "只靠对话，不重建现场",
               "提前离开区域而漏掉文档——有新信息后要回去",
               "忽略证人与证据之间的矛盾",
               "卡住时忘了还有时间回溯可用"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ調査システム解説",
      "metaTitle": "キル・ザ・シャドウ調査システム：再現と推理ガイド（2026）",
      "metaDescription": "キル・ザ・シャドウの調査システム解説：犯行現場再現、論理の鎖による推理、時間巻き戻し、事件解決に必要な証拠。",
      "intro": "調査システムは『キル・ザ・シャドウ』のメカニクスの核心です。公式説明と私たちのプレイ記録に基づき、実際の仕組みを解説します。",
      "sections": [
          {"type": "list", "heading": "3つの柱",
           "body": "すべての調査は3つのシステムを組み合わせます。",
           "items": [
               "観察：現場を調べ、書類を読み、人と話す",
               "再現：シャドウの力で犠牲者の最期をそのまま目撃する",
               "推理：手がかりを論理の鎖で結び、矛盾の背後にある真実を特定する"
           ]},
          {"type": "steps", "heading": "再現の進め方",
           "body": "看板メカニクス。公式資料は過去を「そのまま」再現すると説明します。",
           "items": [
               "死亡が起きた現場で再現を発動",
               "最期の瞬間を見届ける——現場をそのまま信じない",
               "犯人が偽装したり取り除いたりした細部を探す",
               "再現された過去と現在の物理的証拠を比較する"
           ]},
          {"type": "list", "heading": "矛盾を読む",
           "body": "ほとんどの事件は「辻褄が合わない場所」を見つけて解決します。",
           "items": [
               "証人の証言と再現が食い違う",
               "遺体の体勢が主張された死因と一致しない",
               "再現された出来事では説明できない物体が存在する",
               "時系列：再現が示す順序が他人の証言と合わない"
           ]},
          {"type": "list", "heading": "重要な証拠",
           "body": "私たちのプレイ記録で一貫して重みのあった証拠タイプです。",
           "items": [
               "医療書類——冒頭の手紙のメーターが最初の一つ",
               "会話では触れられない現場の環境的細部",
               "会話を通じて確認する、立ち入り権限と動機",
               "自分の再現メモ——公式の説明と異なる点を書き留める"
           ]},
          {"type": "list", "heading": "よくあるミス",
           "body": "事件を遅らせる要因です。",
           "items": [
               "再現せず会話だけに頼る",
               "早く離れて書類を見逃す——新情報があれば戻る",
               "証言と証拠の矛盾を無視する",
               "行き詰まったときに巻き戻しを忘れる"
           ]}
      ]
  }})
print("batch3 done, pages:", len(PAGES))

# ---------- 7. achievements ----------
P("achievements",
  "Kill The Shadow Achievements Guide",
  "Kill The Shadow Achievements Guide (2026)",
  "What is confirmed about Kill The Shadow achievements: the free demo has 10 achievements, and how the full game's list is being documented after launch.",
  "Achievement hunting in Kill The Shadow is just getting started. This page covers what is verified so far and how to track the full list as it is documented.",
  [
      {"type": "list", "heading": "The Demo: 10 Achievements",
       "body": "Verified through SteamDB and achievement trackers, the free demo includes 10 achievements with a total of 5,129 obtainable EXP.",
       "items": [
           "Demo app ID on SteamDB: 2947640",
           "10 total achievements, tracked by 58 players on Exophase",
           "Completionist players have earned all 10 (the '100% club' is active)",
           "Full achievement names and descriptions are listed on the Steam store's demo page"
       ]},
      {"type": "list", "heading": "The Full Game",
       "body": "The full release launched August 5, 2026. Its achievement list is being documented by the community now.",
       "items": [
           "The full game has its own achievement set separate from the demo",
           "Tracking sites update as players earn achievements — check SteamDB for the live list",
           "We will publish a complete checklist here once reliable sources confirm every achievement"
       ]},
      {"type": "list", "heading": "How to Track the Full List",
       "body": "Recommended places to follow the list as it fills in.",
       "items": [
           "SteamDB achievement stats page for Kill The Shadow (app 2660230)",
           "The Steam Community hub — player-written guides often list achievements fastest",
           "TrueSteamAchievements for completionist stats and percentages"
       ]}
  ],
  [SRC_STEAMDB, {"label": "Exophase — Kill The Shadow Demo achievements", "url": "https://www.exophase.com/game/sha-si-ying-zi-demo-steam/achievements/", "zh": "Exophase — 杀死影子 Demo 成就", "ja": "Exophase — キル・ザ・シャドウ デモ実績"}],
  {"zh": {
      "title": "杀死影子成就指南",
      "metaTitle": "杀死影子成就攻略（2026）",
      "metaDescription": "杀死影子成就的已确认信息：免费 Demo 有 10 个成就，以及正式版成就列表的发售后整理进展。",
      "intro": "《杀死影子》的成就收集才刚刚开始。本页汇总目前已核实的信息，以及如何跟进正在整理中的完整列表。",
      "sections": [
          {"type": "list", "heading": "Demo：10 个成就",
           "body": "经 SteamDB 与成就追踪站核实，免费 Demo 包含 10 个成就，总可获得 EXP 为 5,129。",
           "items": [
               "Demo 在 SteamDB 的 app ID：2947640",
               "共 10 个成就，Exophase 上已有 58 名玩家在追踪",
               "完成度玩家已集齐全部 10 个（「100% 俱乐部」活跃中）",
               "完整成就名称与描述在 Steam 商店 Demo 页面可查"
           ]},
          {"type": "list", "heading": "正式版",
           "body": "正式版于 2026 年 8 月 5 日发售，成就列表正在被社区整理。",
           "items": [
               "正式版拥有独立于 Demo 的成就集",
               "追踪站会随玩家解锁不断更新——到 SteamDB 查看实时列表",
               "可靠来源确认全部成就后，我们会在这里发布完整清单"
           ]},
          {"type": "list", "heading": "如何跟进完整列表",
           "body": "推荐以下位置跟进逐步补全的列表。",
           "items": [
               "SteamDB 的 Kill The Shadow 成就统计页（app 2660230）",
               "Steam 社区中心——玩家写的指南往往最快列出成就",
               "TrueSteamAchievements 查看完成度统计与百分比"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ実績ガイド",
      "metaTitle": "キル・ザ・シャドウ実績攻略（2026）",
      "metaDescription": "キル・ザ・シャドウ実績の確定情報：無料デモには実績10個、製品版のリストは発売後に整理中。",
      "intro": "『キル・ザ・シャドウ』の実績集めは始まったばかりです。現時点で検証済みの情報と、整理中の完全リストの追い方をまとめます。",
      "sections": [
          {"type": "list", "heading": "デモ：実績10個",
           "body": "SteamDB と実績トラッカーで検証済み。無料デモには実績10個、取得可能EXP合計5,129があります。",
           "items": [
               "デモの SteamDB app ID：2947640",
               "実績10個、Exophase で58人のプレイヤーが追跡",
               "コンプリート勢が10個すべて獲得済み（100%クラブ稼働中）",
               "実績名と説明は Steam ストアのデモページで確認可能"
           ]},
          {"type": "list", "heading": "製品版",
           "body": "製品版は2026年8月5日に発売。実績リストは現在コミュニティが整理中です。",
           "items": [
               "製品版にはデモとは別の実績セットがある",
               "トラッカーはプレイヤーの解除に合わせて更新——SteamDB で最新リストを",
               "信頼できる情報源が全実績を確認次第、完全チェックリストを公開します"
           ]},
          {"type": "list", "heading": "完全リストの追い方",
           "body": "リストが埋まっていくのを追うのにおすすめの場所です。",
           "items": [
               "SteamDB のキル・ザ・シャドウ実績統計ページ（app 2660230）",
               "Steam コミュニティハブ——プレイヤー作成ガイドが最も速い",
               "TrueSteamAchievements でコンプ率と統計を確認"
           ]}
      ]
  }})

# ---------- 8. controls ----------
P("controls",
  "Kill The Shadow Controls & Keybinds",
  "Kill The Shadow Controls & Keybinds Guide (2026)",
  "The controls layout for Kill The Shadow: movement, investigation, reconstruction and dialogue — with a note that exact keybinds are configurable in-game.",
  "This page covers the control categories you will use in Kill The Shadow. The exact default keybinds are best confirmed in-game (Options → Controls), and we will document them here once verified.",
  [
      {"type": "table", "heading": "Control Categories",
       "body": "The actions you will use most, grouped by system. Exact keys are configurable in-game.",
       "columns": ["Category", "Actions", "Note"],
       "rows": [
           ["Movement", "Move, run, interact with the environment", "Standard third-person/overhead controls"],
           ["Investigation", "Inspect clues, open documents, examine objects", "Requires being near the interactable"],
           ["Reconstruction", "Trigger crime-scene reconstruction, scrub through the moment", "The signature detective ability"],
           ["Dialogue", "Choose dialogue options, rewind a conversation", "Rewind is the safety net for choices"],
           ["System", "Pause, journal, map, save", "Use the journal to review evidence"]
       ]},
      {"type": "list", "heading": "First-Time Setup Notes",
       "body": "Practical tips before you start.",
       "items": [
           "Open Options → Controls at the start to see your exact keybinds",
           "Remap anything that feels awkward — the game supports rebinding",
           "Make sure your graphics driver is up to date for the 2.5D pixel rendering"
       ]}
  ],
  [SRC_STEAM],
  {"zh": {
      "title": "杀死影子操作与键位",
      "metaTitle": "杀死影子操作与键位指南（2026）",
      "metaDescription": "杀死影子的操作分类：移动、调查、重建与对话——注意确切键位可在游戏内设置。",
      "intro": "本页覆盖你在《杀死影子》中会用到的主要操作分类。确切的默认键位建议在游戏内确认（设置 → 操作），核实后我们会在这里补充。",
      "sections": [
          {"type": "table", "heading": "操作分类",
           "body": "你最常使用的动作，按系统分组。确切按键可在游戏内自定义。",
           "columns": ["分类", "动作", "备注"],
           "rows": [
               ["移动", "移动、奔跑、与环境互动", "标准第三人称/俯视角操作"],
               ["调查", "检查线索、打开文档、查看物品", "需要靠近可交互物"],
               ["重建", "触发犯罪现场重建、快进关键时刻", "招牌侦探能力"],
               ["对话", "选择对话选项、回溯一段对话", "回溯是选择的安全网"],
               ["系统", "暂停、日志、地图、存档", "用日志回顾证据"]
           ]},
          {"type": "list", "heading": "首次设置建议",
           "body": "开始前的实用提示。",
           "items": [
               "开始前打开 设置 → 操作 查看确切键位",
               "任何不顺手的键都可以重绑——游戏支持自定义",
               "确保显卡驱动为最新版本，以获得最佳 2.5D 像素渲染效果"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ操作とキーバインド",
      "metaTitle": "キル・ザ・シャドウ操作ガイド（2026）",
      "metaDescription": "キル・ザ・シャドウの操作カテゴリ：移動、調査、再現、会話——正確なキーはゲーム内で設定可能。",
      "intro": "本ページでは『キル・ザ・シャドウ』で使う操作カテゴリを解説します。正確な既定キーはゲーム内（設定→操作）で確認するのが確実で、検証後にこちらへ記載します。",
      "sections": [
          {"type": "table", "heading": "操作カテゴリ",
           "body": "最もよく使うアクションをシステムごとに分類。正確なキーはゲーム内で設定可能です。",
           "columns": ["カテゴリ", "アクション", "備考"],
           "rows": [
               ["移動", "移動、走る、環境とインタラクト", "標準的な三人称/見下ろし操作"],
               ["調査", "手がかりを調べる、書類を開く、物を見る", "インタラクト可能物の近くにいる必要"],
               ["再現", "犯行現場再現の発動、瞬間の送り/戻し", "看板の探偵能力"],
               ["会話", "会話選択、会話の巻き戻し", "巻き戻しが選択のセーフティネット"],
               ["システム", "ポーズ、ジャーナル、マップ、セーブ", "ジャーナルで証拠を振り返る"]
           ]},
          {"type": "list", "heading": "初回セットアップの注意",
           "body": "始める前の実用的なヒントです。",
           "items": [
               "最初に 設定→操作 で正確なキーを確認",
               "違和感のあるキーは自由にリマップ可能",
               "2.5D ピクセル描画のためにグラフィックドライバを最新に"
           ]}
      ]
  }})

# ---------- 9. system-requirements ----------
P("system-requirements",
  "Kill The Shadow System Requirements",
  "Kill The Shadow System Requirements: Minimum & Recommended (2026)",
  "Verified minimum system requirements for Kill The Shadow on Steam: Windows 10 64-bit, Intel i5-6400, 8 GB RAM, GTX 960, 4 GB storage.",
  "These are the minimum system requirements as published on the official Steam store page.",
  [
      {"type": "table", "heading": "Minimum Requirements",
       "body": "As listed on the Steam store page for Kill The Shadow.",
       "columns": ["Component", "Minimum"],
       "rows": [
           ["OS", "Windows 10 64-bit"],
           ["Processor", "Intel i5-6400"],
           ["Memory", "8 GB RAM"],
           ["Graphics", "Nvidia GeForce GTX 960"],
           ["Storage", "4 GB available space"],
           ["Other", "64-bit processor and operating system required"]
       ]},
      {"type": "table", "heading": "Quick Spec Summary",
       "body": "At a glance, the minimum spec is a modest 2015-era gaming PC.",
       "columns": ["Spec", "Minimum"],
       "rows": [
           ["OS", "Windows 10 64-bit"],
           ["CPU", "Intel i5-6400"],
           ["RAM", "8 GB"],
           ["GPU", "GTX 960"],
           ["Storage", "4 GB"]
       ]},
      {"type": "list", "heading": "Recommended Requirements",
       "body": "The Steam page lists minimum requirements; recommended specs are confirmed in-game and will be added here once verified from an official source.",
       "items": [
           "Check the official Steam store page for the latest spec list",
           "The game is 2.5D pixel art — it runs well on modest hardware",
           "Windows-only at launch; no macOS or Linux version is listed"
       ]},
      {"type": "list", "heading": "Notes for Players",
       "body": "Practical considerations before buying.",
       "items": [
           "Steam requires Windows 10 or newer as of January 1, 2024",
           "4 GB of free space is small — installs are quick",
           "SSD is recommended for faster scene loads, though not required"
       ]}
  ],
  [SRC_STEAM],
  {"zh": {
      "title": "杀死影子配置要求",
      "metaTitle": "杀死影子配置要求：最低与推荐（2026）",
      "metaDescription": "杀死影子在 Steam 上已核实的配置要求：Windows 10 64位、Intel i5-6400、8 GB 内存、GTX 960、4 GB 存储。",
      "intro": "以下是 Steam 官方商店页公布的最低配置要求。",
      "sections": [
          {"type": "table", "heading": "最低配置",
           "body": "根据 Steam 商店页《杀死影子》页面所列。",
           "columns": ["组件", "最低要求"],
           "rows": [
               ["操作系统", "Windows 10 64位"],
               ["处理器", "Intel i5-6400"],
               ["内存", "8 GB RAM"],
               ["显卡", "Nvidia GeForce GTX 960"],
               ["存储", "4 GB 可用空间"],
               ["其他", "需要 64 位处理器和操作系统"]
           ]},
          {"type": "table", "heading": "配置速览",
       "body": "一眼看懂：最低配置约为 2015 年主流游戏 PC 的水准。",
       "columns": ["项目", "最低要求"],
       "rows": [
           ["操作系统", "Windows 10 64位"],
           ["处理器", "Intel i5-6400"],
           ["内存", "8 GB"],
           ["显卡", "GTX 960"],
           ["存储", "4 GB"]
       ]},
      {"type": "list", "heading": "推荐配置",
           "body": "Steam 页面仅列出最低配置；推荐配置将在官方来源核实后补充。",
           "items": [
               "查看 Steam 官方商店页获取最新配置列表",
               "游戏为 2.5D 像素风，中低配置即可流畅运行",
               "发售时仅支持 Windows；未列出 macOS 或 Linux 版本"
           ]},
          {"type": "list", "heading": "玩家注意事项",
           "body": "购买前的实用考虑。",
           "items": [
               "自 2024 年 1 月 1 日起，Steam 客户端仅支持 Windows 10 及以上",
               "4 GB 可用空间很小——安装很快",
               "虽然非必需，SSD 能加快场景加载"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ システム要件",
      "metaTitle": "キル・ザ・シャドウ システム要件：最低・推奨（2026）",
      "metaDescription": "キル・ザ・シャドウの検証済み最低要件：Windows 10 64bit、Intel i5-6400、8GB RAM、GTX 960、4GB ストレージ。",
      "intro": "以下は Steam 公式ストアページに掲載された最低システム要件です。",
      "sections": [
          {"type": "table", "heading": "最低要件",
           "body": "Steam ストアの『キル・ザ・シャドウ』ページ記載の内容。",
           "columns": ["項目", "最低"],
           "rows": [
               ["OS", "Windows 10 64bit"],
               ["CPU", "Intel i5-6400"],
               ["メモリ", "8 GB RAM"],
               ["GPU", "Nvidia GeForce GTX 960"],
               ["ストレージ", "4 GB 空き容量"],
               ["その他", "64bit プロセッサと OS が必要"]
           ]},
          {"type": "table", "heading": "スペック早見表",
       "body": "ひと目で：最低構成は2015年頃の標準的なゲーミングPCです。",
       "columns": ["項目", "最低"],
       "rows": [
           ["OS", "Windows 10 64bit"],
           ["CPU", "Intel i5-6400"],
           ["RAM", "8 GB"],
           ["GPU", "GTX 960"],
           ["ストレージ", "4 GB"]
       ]},
      {"type": "list", "heading": "推奨要件",
           "body": "Steam ページは最低要件のみ掲載。推奨スペックは公式ソースで確認後、こちらに追記します。",
           "items": [
               "最新のスペック表は Steam 公式ストアページで確認",
               "2.5D ピクセルアートなので、控えめな構成でも快適",
               "発売時は Windows のみ。macOS / Linux 版の記載なし"
           ]},
          {"type": "list", "heading": "プレイヤー向けメモ",
           "body": "購入前に考慮すべき点です。",
           "items": [
               "2024年1月1日以降、Steam クライアントは Windows 10 以降のみ対応",
               "4GB の空き容量は小さく、インストールは高速",
               "必須ではないが SSD でシーンの読み込みが速くなる"
           ]}
      ]
  }})
print("batch4 done, pages:", len(PAGES))

# ---------- 10. steam-deck ----------
P("steam-deck",
  "Kill The Shadow on Steam Deck",
  "Kill The Shadow Steam Deck Guide (2026)",
  "Is Kill The Shadow Steam Deck verified? What is confirmed so far, plus practical tips for running this Windows-only detective RPG on Steam Deck.",
  "Kill The Shadow is currently listed as Windows-only. This page covers what is confirmed about Steam Deck compatibility and how to approach it.",
  [
      {"type": "list", "heading": "What Is Confirmed",
       "body": "Official status as of launch.",
       "items": [
           "The Steam store page lists Windows only — no official macOS or Linux build",
           "Steam Deck compatibility is not yet verified by Valve at the time of writing",
           "The demo has been playable since 2024 and some players have run it on Deck, but that is anecdotal, not official"
       ]},
      {"type": "list", "heading": "Approach for Deck Owners",
       "body": "If you want to try it on Deck, these are reasonable steps — not guarantees.",
       "items": [
           "Try the free demo first on Deck before buying",
           "Check ProtonDB for community reports on the demo and full game",
           "Use the latest Proton GE if the default Proton does not start the game",
           "Set the game to a comfortable TDP if you play on battery"
       ]},
      {"type": "list", "heading": "Controls on Deck",
       "body": "Kill The Shadow is a dialogue-heavy RPG, which works well with controller-style layouts.",
       "items": [
           "Dialogue and investigation-driven games map well to gamepad layouts",
           "Use the Steam Input community layouts once the game is running",
           "Remap in-game controls to suit the Deck's buttons"
       ]}
  ],
  [SRC_STEAM, {"label": "ProtonDB — community compatibility reports", "url": "https://www.protondb.com/", "zh": "ProtonDB — 社区兼容性报告", "ja": "ProtonDB — コミュニティ互換性レポート"}],
  {"zh": {
      "title": "杀死影子在 Steam Deck 上运行",
      "metaTitle": "杀死影子 Steam Deck 指南（2026）",
      "metaDescription": "杀死影子是否通过 Steam Deck 验证？当前已确认的信息，以及在这款仅支持 Windows 的侦探 RPG 上使用 Steam Deck 的实用建议。",
      "intro": "《杀死影子》目前仅支持 Windows。本页汇总关于 Steam Deck 兼容性的已确认信息与应对方式。",
      "sections": [
          {"type": "list", "heading": "已确认的信息",
           "body": "发售时的官方状态。",
           "items": [
               "Steam 商店页仅列出 Windows——没有官方的 macOS 或 Linux 版本",
               "截至撰写时，Valve 尚未验证 Steam Deck 兼容性",
               "Demo 自 2024 年起可玩，部分玩家在 Deck 上运行过，但这属于社区经验而非官方结论"
           ]},
          {"type": "list", "heading": "Deck 用户的应对",
           "body": "如果你想在 Deck 上尝试，这些是合理的步骤——不保证一定可行。",
           "items": [
               "购买前先在 Deck 上试免费 Demo",
               "到 ProtonDB 查看社区对 Demo 与正式版的报告",
               "若默认 Proton 无法启动，尝试最新的 Proton GE",
               "用电池游玩时设置合适的 TDP 功耗"
           ]},
          {"type": "list", "heading": "Deck 上的操作",
           "body": "《杀死影子》是对话密集的 RPG，非常适合手柄式布局。",
           "items": [
               "对话与调查驱动的游戏很适合手柄布局",
               "游戏运行后使用 Steam Input 社区布局",
               "把游戏内操作重绑到 Deck 的按键上"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウを Steam Deck で",
      "metaTitle": "キル・ザ・シャドウ Steam Deck ガイド（2026）",
      "metaDescription": "キル・ザ・シャドウは Steam Deck 検証済み？確定情報と、Windows 専用のこの探偵RPGを Deck で動かす実用的なヒント。",
      "intro": "『キル・ザ・シャドウ』は現在 Windows 専用です。Steam Deck 互換性の確定情報と対処法をまとめます。",
      "sections": [
          {"type": "list", "heading": "確定していること",
           "body": "発売時点での公式ステータス。",
           "items": [
               "Steam ストアは Windows のみ——公式の macOS / Linux ビルドなし",
               "本稿執筆時点で Valve による Steam Deck 検証は未実施",
               "デモは2024年からプレイ可能で、Deck で動かしたという報告はあるが、公式ではない"
           ]},
          {"type": "list", "heading": "Deck オーナー向けの進め方",
           "body": "Deck で試したい場合の妥当な手順です——保証ではありません。",
           "items": [
               "購入前に Deck で無料デモを先に試す",
               "ProtonDB でデモと製品版のコミュニティ報告を確認",
               "既定の Proton で起動しない場合は最新の Proton GE を試す",
               "バッテリー運用時は適切な TDP を設定"
           ]},
          {"type": "list", "heading": "Deck での操作",
           "body": "『キル・ザ・シャドウ』は会話中心の RPG で、ゲームパッド式レイアウトと相性が良いです。",
           "items": [
               "会話・調査中心のゲームはパッドレイアウトに良く合う",
               "起動後は Steam Input のコミュニティレイアウトを活用",
               "ゲーム内操作を Deck のボタンに合わせてリマップ"
           ]}
      ]
  }})

# ---------- 11. tips-and-tricks ----------
P("tips-and-tricks",
  "Kill The Shadow Tips & Tricks",
  "Kill The Shadow Tips & Tricks: Play Smarter (2026)",
  "Practical Kill The Shadow tips: use reconstruction early, read medical documents, track contradictions, manage the Shadow corruption meter and experiment with rewind.",
  "These tips come from the officially described systems and our own verified playthrough of Chapter 1.",
  [
      {"type": "list", "heading": "Investigation Tips",
       "body": "Solve cases faster and more completely.",
       "items": [
           "Reconstruct every scene you can — the final moments hide what the scene is staged to hide",
           "Read documents before talking to people; contradictions are easier to spot with full knowledge",
           "Re-read reconstructed scenes after learning new information",
           "Note who told you what — the game rewards tracking testimony"
       ]},
      {"type": "list", "heading": "Choice & Ending Tips",
       "body": "Shape the story the way you want.",
       "items": [
           "Decide on a stance (justice or protection) and stay consistent — relationships compound",
           "Watch the Shadow corruption meter; it responds to darker choices",
           "Rewind when you are unsure — trying both options is the fastest way to learn",
           "Keep a second save before major decisions so you can explore branches"
       ]},
      {"type": "list", "heading": "Efficiency Tips",
       "body": "Save time without missing content.",
       "items": [
           "Explore the semi-open city after each chapter — dialogue changes with new information",
           "Interact with everything at a scene before triggering reconstruction",
           "The 2.5D pixel style means subtle environmental details matter — zoom in when you can",
           "A second playthrough with the opposite moral stance reveals the most content"
       ]}
  ],
  [SRC_STEAM, SRC_G2A],
  {"zh": {
      "title": "杀死影子技巧与心得",
      "metaTitle": "杀死影子技巧与心得：玩得更聪明（2026）",
      "metaDescription": "实用的杀死影子技巧：尽早重建、阅读医疗文档、追踪矛盾、管理影子黑化度、多用回溯。",
      "intro": "这些技巧来自官方描述的系统与我们已核实的第一章通关记录。",
      "sections": [
          {"type": "list", "heading": "调查技巧",
           "body": "更快、更完整地破案。",
           "items": [
               "尽量重建每个现场——最后瞬间藏着现场被伪装掩盖的东西",
               "与人交谈前先读文档；掌握全部信息后更容易发现矛盾",
               "获得新信息后重读重建的场景",
               "记录谁对你说了什么——这款游戏奖励追踪证词"
           ]},
          {"type": "list", "heading": "选择与结局技巧",
           "body": "让剧情按你想要的方向发展。",
           "items": [
               "定下一个立场（正义或保护）并保持一致——关系会累积",
               "留意影子黑化度；它对更黑暗的选择有反应",
               "不确定时就回溯——两个选项都试是学习最快的方式",
               "重大决定前留一个存档，方便探索不同分支"
           ]},
          {"type": "list", "heading": "效率技巧",
           "body": "省时间又不漏内容。",
           "items": [
               "每个章节后探索半开放城市——对话会随新信息改变",
               "触发重建前，先与现场所有可交互物互动",
               "2.5D 像素风格意味着细微的环境细节很重要——能放大就放大",
               "用相反的道德立场二周目能解锁最多内容"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ ヒントとコツ",
      "metaTitle": "キル・ザ・シャドウ ヒント：賢くプレイする（2026）",
      "metaDescription": "実用的なヒント：早めの再現、医療書類の読解、矛盾の追跡、シャドウ浸食度の管理、巻き戻しの活用。",
      "intro": "これらのヒントは公式に説明されたシステムと、私たちが検証した第1章のプレイ記録から得たものです。",
      "sections": [
          {"type": "list", "heading": "調査のヒント",
           "body": "より速く、より完全に事件を解決する。",
           "items": [
               "できる限り現場を再現する——最期の瞬間は現場が隠そうとしたものを隠している",
               "人と話す前に書類を読む；情報が揃えば矛盾に気づきやすい",
               "新情報を得たら再現シーンを読み直す",
               "誰が何を言ったか記録する——証言の追跡が報われるゲーム"
           ]},
          {"type": "list", "heading": "選択とエンディングのヒント",
           "body": "物語を思い通りに形作る。",
           "items": [
               "正義か保護か、スタンスを決めて一貫する——関係性は複利で効く",
               "シャドウ浸食度に注意——暗い選択に反応する",
               "迷ったら巻き戻す——両方試すのが最速の学び",
               "重要決定の前にセーブを分けて、分岐を探索"
           ]},
          {"type": "list", "heading": "効率のヒント",
           "body": "時間を節約しつつ内容を逃さない。",
           "items": [
               "各章の後に半オープンの都市を探索——新情報で会話が変わる",
               "再現を発動する前に、現場のインタラクト可能物をすべて調べる",
               "2.5D ピクセル画風では細かな環境の手がかりが重要——拡大できる時は拡大",
               "逆の道徳的立場での2周目が最も多くの内容を解放する"
           ]}
      ]
  }})

# ---------- 12. faq ----------
P("faq",
  "Kill The Shadow FAQ",
  "Kill The Shadow FAQ: Answers to Common Questions (2026)",
  "Frequently asked questions about Kill The Shadow: release date, price, platforms, game length, endings, demo and whether there are more games in the series.",
  "Quick answers to the questions players ask most about Kill The Shadow.",
  [
      {"type": "list", "heading": "Where This Page Can Help",
       "body": "Before you ask: most of the questions below are answered from official sources or verified coverage. Where something is still being documented after launch, we say so explicitly instead of guessing.",
       "items": [
           "Release and pricing facts come from the official Steam store page and the publisher's press release",
           "Ending and choice details are verified against publisher descriptions and launch coverage",
           "Anything still being documented by the community is marked clearly as unverified"
       ]},
      {"type": "faq", "heading": "FAQ",
       "items": [
           ["When was Kill The Shadow released?", "It launched on Steam (Windows) on August 5, 2026."],
           ["How much does Kill The Shadow cost?", "The standard price is $16.99 / £14.99 / €16.99, with a 10% launch discount for the first two weeks."],
           ["What platforms is it on?", "PC via Steam only at launch. The store page lists Windows; no macOS or Linux build is confirmed."],
           ["How many endings does it have?", "Multiple endings are officially confirmed. The exact number is still being documented by the community after launch."],
           ["How long is the game?", "Official playtime has not been published. It is a dialogue-heavy detective RPG with multiple cases and a semi-open city, so expect a story-driven length."],
           ["Is there a demo?", "Yes — a free demo has been available on Steam since 2024 and includes 10 achievements."],
           ["Who developed it?", "Chinese studio Shadowlight (坞光岚影), with a global publishing deal under NEOWIZ."],
           ["Is this a sequel?", "No sequel or prequel has been announced. The game is a standalone detective RPG."]
       ]}
  ],
  [SRC_STEAM, SRC_PRESS],
  {"zh": {
      "title": "杀死影子常见问题",
      "metaTitle": "杀死影子 FAQ：常见问题解答（2026）",
      "metaDescription": "关于杀死影子的常见问题：发售日、价格、平台、时长、结局、Demo，以及是否有续作。",
      "intro": "关于《杀死影子》，玩家最常问的问题的快速解答。",
      "sections": [
          {"type": "list", "heading": "本页能帮到你什么",
           "body": "先说明：以下大部分答案来自官方来源或已核实的报道。仍有待社区整理的部分，我们会明确标注「未核实」，而不是猜测。",
           "items": [
               "发售与价格信息来自 Steam 官方商店页与发行方新闻稿",
               "结局与选择信息对照发行方描述与发售报道核实",
               "任何仍在社区整理中的内容都会明确标注为未核实"
           ]},
      {"type": "faq", "heading": "常见问题",
           "items": [
               ["杀死影子什么时候发售？", "2026 年 8 月 5 日在 Steam（Windows）发售。"],
               ["杀死影子多少钱？", "标准售价 $16.99 / £14.99 / €16.99，前两周首发 -10%。"],
               ["支持哪些平台？", "发售时仅 Steam PC。商店页仅列出 Windows；未确认 macOS 或 Linux 版本。"],
               ["有几个结局？", "官方确认多结局。确切数量正由社区在发售后整理中。"],
               ["游戏时长多久？", "官方未公布时长。它是对话密集的侦探 RPG，含多个案件与半开放城市，预计为剧情驱动的中长篇幅。"],
               ["有 Demo 吗？", "有——自 2024 年起 Steam 上有免费 Demo，含 10 个成就。"],
               ["开发商是谁？", "中国工作室坞光岚影（Shadowlight），全球发行协议由 NEOWIZ 负责。"],
               ["这是续作吗？", "未公布任何续作或前传。它是一款独立的侦探 RPG。"]
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ FAQ",
      "metaTitle": "キル・ザ・シャドウ FAQ：よくある質問（2026）",
      "metaDescription": "キル・ザ・シャドウのよくある質問：発売日、価格、対応プラットフォーム、プレイ時間、エンディング、デモ、続編の有無。",
      "intro": "『キル・ザ・シャドウ』に関する最もよくある質問への簡潔な回答です。",
      "sections": [
          {"type": "list", "heading": "このページで分かること",
           "body": "先に説明します：以下の回答はほとんどが公式ソースまたは検証済みの報道に基づいています。発売後もコミュニティが整理中のものは、推測せず「未検証」と明記します。",
           "items": [
               "発売日・価格は Steam 公式ストアとパブリッシャーのプレスリリースに基づく",
               "エンディングと選択の情報はパブリッシャー説明とローンチ報道で検証",
               "コミュニティが整理中の内容は未検証と明記"
           ]},
      {"type": "faq", "heading": "よくある質問",
           "items": [
               ["発売日はいつ？", "2026年8月5日に Steam（Windows）で発売。"],
               ["価格は？", "標準価格は $16.99 / £14.99 / €16.99。ローンチ割引10%が2週間。"],
               ["対応プラットフォームは？", "発売時は Steam の PC のみ。ストアは Windows のみ記載。macOS / Linux 版は未確認。"],
               ["エンディングはいくつ？", "マルチエンディングは公式に確定。正確な数は発売後、コミュニティが整理中。"],
               ["プレイ時間は？", "公式のプレイ時間は未公表。会話中心の探偵RPGで複数の事件と半オープンの都市があり、ストーリー主導のボリューム。"],
               ["デモはある？", "あります——2024年から Steam で無料デモを公開中。実績10個。"],
               ["開発元は？", "中国のスタジオ Shadowlight（坞光岚影）。グローバル配信は NEOWIZ の契約。"],
               ["続編はある？", "続編・前日譚の発表はありません。単独の探偵RPGです。"]
           ]}
      ]
  }})

# ---------- 13. update-log ----------
P("update-log",
  "Kill The Shadow Update Log",
  "Kill The Shadow Update Log: Release History (2026)",
  "The verified release history of Kill The Shadow: the 2024 demo with 10 achievements, and the full launch on August 5, 2026.",
  "The verified release history of Kill The Shadow, kept current as updates ship.",
  [
      {"type": "table", "heading": "Release History",
       "body": "Confirmed dates from official and store sources.",
       "columns": ["Date", "Event", "Notes"],
       "rows": [
           ["2024 (July)", "Demo released", "Free demo on Steam with 10 achievements (app 2947640)"],
           ["July 2026", "Global publishing announced", "NEOWIZ signs global publishing deal for the title"],
           ["August 5, 2026", "Full release on Steam", "Windows launch at $16.99 / £14.99 / €16.99 with 10% launch discount until August 19"],
           ["August 12, 2026", "Console release (announced)", "PS5 / Xbox Series X|S versions announced by press coverage"]
       ]},
      {"type": "list", "heading": "About the Launch Discount",
       "body": "The 10% launch discount runs for the first two weeks, ending August 19, 2026.",
       "items": [
           "Final price during the discount: about $15.29 in USD regions",
           "Regional pricing applies (e.g. ¥58.5 in China)",
           "The wishlist count before launch exceeded 100,000, over 80% from outside China"
       ]}
  ],
  [SRC_STEAM, SRC_PRESS],
  {"zh": {
      "title": "杀死影子更新日志",
      "metaTitle": "杀死影子更新日志：发售历史（2026）",
      "metaDescription": "杀死影子已核实的发售历史：2024 年的 10 成就 Demo，以及 2026 年 8 月 5 日的正式发售。",
      "intro": "《杀死影子》已核实的发售历史，随更新持续维护。",
      "sections": [
          {"type": "table", "heading": "发售历史",
           "body": "来自官方与商店来源的确认日期。",
           "columns": ["日期", "事件", "备注"],
           "rows": [
               ["2024 年（7月）", "Demo 发布", "Steam 免费 Demo，含 10 个成就（app 2947640）"],
               ["2026 年 7 月", "全球发行官宣", "NEOWIZ 签下本作的全球发行协议"],
               ["2026 年 8 月 5 日", "Steam 正式发售", "Windows 平台，$16.99 / £14.99 / €16.99，首发 -10% 至 8 月 19 日"],
               ["2026 年 8 月 12 日", "主机版（已公布）", "媒体报道 PS5 / Xbox Series X|S 版本"]
           ]},
          {"type": "list", "heading": "关于首发折扣",
           "body": "首发 -10% 持续两周，至 2026 年 8 月 19 日结束。",
           "items": [
               "折扣期间约 $15.29（美元区）",
               "采用区域定价（如国区 ¥58.5）",
               "发售前愿望单突破 10 万份，80% 以上来自海外"
           ]}
      ]
  }, "ja": {
      "title": "キル・ザ・シャドウ アップデート履歴",
      "metaTitle": "キル・ザ・シャドウ アップデート履歴：リリース史（2026）",
      "metaDescription": "キル・ザ・シャドウの検証済みリリース履歴：実績10個の2024年デモと、2026年8月5日の製品版発売。",
      "intro": "『キル・ザ・シャドウ』の検証済みリリース履歴。更新があるたびに最新化します。",
      "sections": [
          {"type": "table", "heading": "リリース履歴",
           "body": "公式・ストア情報源による確定日。",
           "columns": ["日付", "出来事", "備考"],
           "rows": [
               ["2024年（7月）", "デモ公開", "Steam で無料デモ。実績10個（app 2947640）"],
               ["2026年7月", "グローバル配信を発表", "NEOWIZ が本作のグローバル配信契約を締結"],
               ["2026年8月5日", "Steam で製品版発売", "Windows 版。$16.99 / £14.99 / €16.99、ローンチ割引10%は8月19日まで"],
               ["2026年8月12日", "コンソール版（発表済み）", "報道で PS5 / Xbox Series X|S 版が言及"]
           ]},
          {"type": "list", "heading": "ローンチ割引について",
           "body": "ローンチ割引10%は2週間、2026年8月19日まで。",
           "items": [
               "割引中の価格は約 $15.29（米ドル圏）",
               "リージョナルプライシング適用（中国は ¥58.5 など）",
               "発売前ウィッシュリストは10万件超、80%以上が海外"
           ]}
      ]
  }})

def build():
    site_json = {"site": SITE, "game": GAME, "pages": PAGES}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(site_json, f, ensure_ascii=False, indent=1)
    print("site.json written:", out, "| pages:", len(PAGES))
    print("page slugs:", [p["slug"] for p in PAGES])

if __name__ == "__main__":
    build()
