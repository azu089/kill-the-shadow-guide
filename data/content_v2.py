# -*- coding: utf-8 -*-
"""内容深化：基于知识库已验证机制（来源见 docs/kill-the-shadow-research.md）。"""

def S(t, heading, body=None, items=None, rows=None, cols=None, tag=None):
    d={"type":t,"heading":heading}
    if body: d["body"]=body
    if items is not None: d["items"]=items
    if rows is not None: d["rows"]=rows
    if cols is not None: d["columns"]=cols
    if tag: d["tag"]=tag
    return d

# ===== how-to-play 深化 =====
HTP2_EN = [
  S("table", "Ability Growth: Strength, Spirit, Charm", "Confirmed by the official store description — you choose how Lucas grows, and the path you invest in changes which case approaches feel reliable.", rows=[
    ["Strength (力量)","Physical options: violence, intimidation, punching through deadlocks","Unlocks brute-force routes; raises the Shadow corruption meter faster on dark choices"],
    ["Spirit (精神)","The Shadow's power: stronger death-reconstruction, better time-rewind","Deepens the investigation pillar; the core of the reconstruction fantasy"],
    ["Charm (魅力)","Dialogue and persuasion: bribery, lies, charisma checks","Opens non-violent paths and relationship-friendly outcomes"],
  ], cols=["Stat","What it unlocks","How it shapes play"]),
  S("list","Case Approaches in Practice","The store description says cases can be solved with eloquence, intelligence, time rewind — or even violence. In practice:",[
    "Eloquence: charm and bribery let you walk into rooms others cannot",
    "Intelligence: chain the clues and let contradictions convict the guilty",
    "Time rewind + reconstruction: replay the death until the scene confesses",
    "Violence: fast and brutal, but it moves the corruption meter and burns relationships",
  ]),
]
HTP2_ZH = [
  S("table", "能力成长：力量 / 精神 / 魅力", "官方商店页确认——你选择 Lucas 如何成长，投入的路线决定哪些案件途径更可靠。", rows=[
    ["力量","物理选项：暴力、威慑、用拳头打破僵局","解锁强攻路线；黑暗选择会更快推高影子黑化度"],
    ["精神","影子的力量：更强的死亡重建、更好的时间回溯","加深调查支柱；是重建玩法幻想的核心"],
    ["魅力","对话与说服：贿赂、谎言、魅力检定","打开非暴力路线与关系友好的结局"],
  ], cols=["属性","解锁什么","如何塑造游玩"]),
  S("list","案件途径的实际运用","商店页描述：案件可以用口才、智慧、时间回溯——甚至暴力解决。实际中：",[
    "口才：魅力与贿赂让你走进别人进不去的房间",
    "智慧：串联线索，让矛盾为有罪者定罪",
    "时间回溯 + 重建：反复回放死亡，直到现场「坦白」",
    "暴力：快速而粗暴，但会推高黑化度、烧毁关系",
  ]),
]
HTP2_JA = [
  S("table", "能力成長：筋力 / 精神 / 魅力", "公式ストアで確認——ルーカスの成長を選び、投資した道によって頼れる事件の進め方が変わります。", rows=[
    ["筋力","物理的な選択肢：暴力、威嚇、拳で膠着を破る","強硬ルートを解放；暗い選択で汚染度が上がりやすい"],
    ["精神","シャドウの力：より強い死亡再現、より良い時間巻き戻し","調査の柱を深める；再現体験の中核"],
    ["魅力","対話と説得：賄賂、嘘、カリスマ判定","非暴力ルートと関係良好な結末を開く"],
  ], cols=["ステータス","解放されるもの","プレイへの影響"]),
  S("list","事件の進め方・実践","ストアの説明では、事件は口才・知性・時間巻き戻し、あるいは暴力で解決できます。実際には：",[
    "口才：魅力と賄賂で、他の人が入れない部屋へ入れる",
    "知性：手がかりを繋ぎ、矛盾に有罪者を告発させる",
    "時間巻き戻し＋再現：死を何度も再生し、現場に「自白」させる",
    "暴力：速くて粗いが、汚染度が上がり関係を損なう",
  ]),
]
HTP2_KO = [
  S("table", "능력 성장: 힘 / 정신 / 매력", "공식 스토어 설명으로 확인 — 루카스가 어떻게 성장할지 선택하며, 투자한 길에 따라 믿을 수 있는 사건 진행 방식이 달라집니다.", rows=[
    ["힘","물리적 선택지: 폭력, 협박, 주먹으로 교착 돌파","강경 루트 해금; 어두운 선택 시 오염도가 더 빨리 오름"],
    ["정신","섀도우의 힘: 더 강한 죽음 재구성, 더 나은 시간 되감기","수사 기둥을 깊게 함; 재구성 경험의 핵심"],
    ["매력","대화와 설득: 뇌물, 거짓말, 카리스마 판정","비폭력 루트와 관계 친화적 결말을 엶"],
  ], cols=["스탯","해금되는 것","플레이에 미치는 영향"]),
  S("list","사건 접근법 실전","스토어 설명: 사건은 말솜씨·지혜·시간 되감기, 심지어 폭력으로 해결할 수 있습니다. 실제로는:",[
    "말솜씨: 매력과 뇌물로 남이 못 들어가는 방에 들어갑니다",
    "지혜: 단서를 엮고 모순이 유죄자를 고발하게 만듭니다",
    "시간 되감기 + 재구성: 죽음을 반복 재생해 현장이 '자백'하게 합니다",
    "폭력: 빠르고 거칠지만 오염도를 올리고 관계를 태웁니다",
  ]),
]

# ===== investigation 深化 =====
INV2_EN = [
  S("evidence","The Three Pillars in Practice","How observation, reconstruction and deduction actually combine in a case, from verified coverage.",[
    ["P-1","Observation: read every document and scan every micro-scene — details are deliberately enlarged for you to search"],
    ["P-2","Reconstruction: trigger the death-flashback on the right object to see what really happened"],
    ["P-3","Deduction: link the contradictions into a chain — the chain, not the feeling, convicts"],
  ]),
  S("list","Micro-Scenes & Free Camera","Reviews highlight how the game presents evidence: the scene is broken into enlarged micro-scenes you can rotate and inspect freely, with no hand-holding.",[
    "Scan each enlarged detail for interactables before moving on",
    "Rotate the camera — clues are placed in depth, not on a flat surface",
    "Interact with everything: a document, a gauge, a half-hidden object",
    "The game avoids arrows and guides — curiosity is the intended tool",
  ]),
  S("steps","Building a Deduction Chain","The mechanic reviewers describe as the heart of the game: you do not get answers, you assemble them.",[
    "Collect facts from documents, witnesses and reconstruction",
    "Find where two facts contradict each other",
    "Link contradictions into a logical chain toward one conclusion",
    "Present the chain at the right moment — or rewind and try a different reading",
  ]),
]
INV2_ZH = [
  S("evidence","三支柱的实际运用","根据已核实的报道，观察、重建与推理在案件中如何真正结合。",[
    ["P-1","观察：阅读每一份文档、扫描每一个微场景——细节被刻意放大供你搜索"],
    ["P-2","重建：在正确的物品上触发死亡回溯，看清真正发生了什么"],
    ["P-3","推理：把矛盾串联成一条逻辑链——定罪的是链条，不是感觉"],
  ]),
  S("list","微场景与自由视角","评测强调游戏呈现证据的方式：场景被拆成可自由旋转、放大检查的微场景，没有任何引导。",[
    "继续前先扫描每个放大的细节，寻找可交互物",
    "旋转视角——线索在纵深里，不在平面上",
    "与一切交互：文档、计量器、半隐藏的物体",
    "游戏不用箭头和引导——好奇心就是设计好的工具",
  ]),
  S("steps","构建推理链","评测所描述的玩法核心：你得不到答案，你组装答案。",[
    "从文档、证人、重建中收集事实",
    "找出两个事实互相矛盾之处",
    "把矛盾串联成指向一个结论的逻辑链",
    "在正确的时机呈现链条——或回溯，尝试另一种解读",
  ]),
]
INV2_JA = [
  S("evidence","三本柱の実践","検証済みの報道によれば、観察・再現・推理は実際の事件でこう組み合わさります。",[
    ["P-1","観察：すべての文書を読み、すべてのミニシーンを調べる——細部は意図的に拡大されている"],
    ["P-2","再現：正しい物体で死亡フラッシュバックを発動し、実際に起きたことを見る"],
    ["P-3","推理：矛盾を論理の連鎖に繋ぐ——有罪にするのは感覚ではなく連鎖"],
  ]),
  S("list","ミニシーンと自由視点","レビューが強調する証拠の提示方法：シーンは拡大されたミニシーンに分解され、自由に回転・検査でき、手引きはありません。",[
    "進む前に、拡大された細部をすべてスキャンする",
    "視点を回す——手がかりは平面ではなく奥行きに置かれている",
    "すべてとインタラクトする：書類、ゲージ、半ば隠れた物体",
    "矢印もガイドもない——好奇心こそ意図されたツール",
  ]),
  S("steps","推理の連鎖を組む","レビューが「本作の核心」と評する仕組み：答えは与えられず、組み立てるものです。",[
    "文書・目撃者・再現から事実を集める",
    "二つの事実が矛盾する箇所を見つける",
    "矛盾を一つの結論へ向かう論理の連鎖に繋ぐ",
    "正しいタイミングで連鎖を提示する——あるいは巻き戻して別の読み方を試す",
  ]),
]
INV2_KO = [
  S("evidence","세 기둥의 실제 운용","검증된 보도에 따르면, 관찰·재구성·추리는 사건에서 이렇게 결합합니다.",[
    ["P-1","관찰: 모든 문서를 읽고 모든 마이크로 씬을 조사하세요 — 세부는 의도적으로 확대되어 있습니다"],
    ["P-2","재구성: 올바른 물건에서 죽음 플래시백을 발동해 실제로 일어난 일을 보세요"],
    ["P-3","추리: 모순을 논리 사슬로 연결하세요 — 유죄를 만드는 것은 감정이 아니라 사슬입니다"],
  ]),
  S("list","마이크로 씬과 자유 시점","리뷰가 강조하는 증거 제시 방식: 장면은 확대된 마이크로 씬으로 분해되며 자유롭게 회전·검사할 수 있고 안내가 없습니다.",[
    "넘어가기 전에 확대된 세부를 모두 스캔하세요",
    "시점을 회전하세요 — 단서는 평면이 아니라 깊이에 있습니다",
    "모든 것과 상호작용하세요: 문서, 게이지, 반쯤 숨은 물체",
    "화살표도 가이드도 없습니다 — 호기심이 의도된 도구입니다",
  ]),
  S("steps","추리 사슬 만들기","리뷰가 '이 게임의 핵심'이라 부르는 방식: 답을 주지 않고, 답을 조립하게 합니다.",[
    "문서·목격자·재구성에서 사실을 모으세요",
    "두 사실이 서로 모순되는 지점을 찾으세요",
    "모순을 하나의 결론으로 향하는 논리 사슬로 연결하세요",
    "올바른 순간에 사슬을 제시하세요 — 또는 되감아 다른 해석을 시도하세요",
  ]),
]

# ===== choices 深化 =====
CHO2_EN = [
  S("table", "What Choices Change, Layer by Layer", "The publisher's description names three things choices change — here is how each layer shows up in play.", rows=[
    ["Relationship layer","How you treat each character now","They remember. A worker you punched will not open the same doors; a friend you protected returns the favor"],
    ["Truth layer","Which facts come to light","Some paths reveal a confession; others bury a more dangerous truth — official: 'protecting someone can leave a more dangerous truth buried'"],
    ["Ending layer","Where the story lands","Multiple endings branch from decisions made across the whole story, not just the final chapter"],
  ], cols=["Layer","What changes","In practice"]),
]
CHO2_ZH = [
  S("table", "选择改变什么：分层解析", "官方描述指出选择改变三件事——这是每一层在实际游玩中的体现。", rows=[
    ["关系层","你现在如何对待每个角色","他们记得。你揍过的工人不会为你开同一扇门；你保护过的朋友会在你需要时回报"],
    ["真相层","哪些事实浮出水面","有些路线揭发一份供词；另一些把更危险的真相埋起来——官方：「保护某人可能让更危险的真相被埋藏」"],
    ["结局层","故事落在哪里","多结局由贯穿整个故事的选择分叉，而不仅仅是最后一章"],
  ], cols=["层级","改变什么","实际表现"]),
]
CHO2_JA = [
  S("table", "選択が変えるもの：層別の整理", "公式説明は選択が変える3つの要素を挙げます——各層が実際のプレイでどう現れるか。", rows=[
    ["関係層","今、各キャラクターをどう扱うか","彼らは覚えています。殴った労働者は同じ扉を開けない。守った友人は恩を返す"],
    ["真実層","どの事実が明らかになるか","ある道は自白を暴き、別の道はより危険な真実を埋める——公式：「守ることはより危険な真実を埋めることになるかもしれない」"],
    ["結末層","物語がどこに着地するか","複数エンディングは最終章だけでなく、物語全体の選択から分岐する"],
  ], cols=["層","変わるもの","実際の様子"]),
]
CHO2_KO = [
  S("table", "선택이 바꾸는 것: 층위별 정리", "퍼블리셔 설명은 선택이 바꾸는 세 가지를 말합니다 — 각 층위가 실제 플레이에서 어떻게 나타나는지.", rows=[
    ["관계 층위","지금 각 캐릭터를 대하는 방식","그들은 기억합니다. 때린 노동자는 같은 문을 열어주지 않고, 지킨 친구는 보답합니다"],
    ["진실 층위","어떤 사실이 드러나는지","어떤 길은 자백을 드러내고, 다른 길은 더 위험한 진실을 묻습니다 — 공식: '누군가를 보호하면 더 위험한 진실이 묻힐 수 있다'"],
    ["엔딩 층위","이야기가 어디에 도달하는지","멀티 엔딩은 마지막 챕터뿐 아니라 스토리 전체의 선택에서 분기합니다"],
  ], cols=["층위","바뀌는 것","실제 양상"]),
]

# ===== tips 深化 =====
TIPS2_EN = [
  S("list","Advanced Detective Habits","Beyond the basics — the habits that separate a first playthrough from a complete one.",[
    "Scan every micro-scene with the camera fully rotated before you leave — clues hide in depth",
    "Cross-examine witnesses against each other, not just against evidence",
    "Keep a two-column note: what people say vs what reconstruction shows",
    "Spend stat points deliberately: Strength, Spirit and Charm open different routes",
    "Use rewind as information-gathering, not a reset — the game remembers what you learned",
    "Before the chapter-end choice, revisit everyone with new information — dialogue updates",
  ]),
]
TIPS2_ZH = [
  S("list","进阶侦探习惯","超越基础——把「第一遍通关」和「完整通关」区分开的习惯。",[
    "离开前把每个微场景的视角完全旋转扫描一遍——线索藏在纵深里",
    "让目击者之间互相质证，而不仅仅是和证据对照",
    "记两栏笔记：人们说了什么 vs 重建显示了什么",
    "有意识地分配属性点：力量、精神、魅力打开不同的路线",
    "把回溯当作收集信息而非重置——游戏记得你学到的东西",
    "章节结尾的选择前，带着新信息重访每个人——对话会更新",
  ]),
]
TIPS2_JA = [
  S("list","上級探偵の習慣","基本を超えた——初見プレイと完全攻略を分ける習慣。",[
    "離れる前に、各ミニシーンの視点を完全に回してスキャンする——手がかりは奥行きに隠れている",
    "目撃者同士を突き合わせる——証拠とだけ比べない",
    "2列のメモを取る：人が言ったこと vs 再現が示したこと",
    "ステータスを意図的に振る：筋力・精神・魅力で別ルートが開く",
    "巻き戻しをリセットではなく情報収集として使う——ゲームは学んだことを覚えている",
    "章末の選択前に、新しい情報を持って全員を再訪する——会話が更新される",
  ]),
]
TIPS2_KO = [
  S("list","고급 형사 습관","기본을 넘어서 — 첫 플레이와 완전 플레이를 가르는 습관.",[
    "떠나기 전에 각 마이크로 씬의 시점을 완전히 회전해 스캔하세요 — 단서는 깊이에 숨어 있습니다",
    "목격자들을 서로 대질시키세요 — 증거와만 비교하지 마세요",
    "두 칸 메모를 쓰세요: 사람들이 말한 것 vs 재구성이 보여준 것",
    "스탯을 의도적으로 투자하세요: 힘·정신·매력이 다른 루트를 엽니다",
    "되감기를 리셋이 아닌 정보 수집으로 쓰세요 — 게임은 배운 것을 기억합니다",
    "챕터 끝 선택 전에 새 정보를 가지고 모두를 다시 방문하세요 — 대화가 갱신됩니다",
  ]),
]
