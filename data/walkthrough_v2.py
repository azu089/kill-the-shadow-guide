# -*- coding: utf-8 -*-
"""Kill The Shadow 第一章深度流程（按已核实结构重写，来源：intoindiegames walkthrough + Steam 官方）。
内容用自己的话重写，不复制原文；结构（序章→老机械师→泰迪之死→父亲的秘密→西奥队长→收尾）已核实。
"""

def S(t, heading, body=None, items=None, rows=None, cols=None, tag=None):
    d={"type":t,"heading":heading}
    if body: d["body"]=body
    if items is not None: d["items"]=items
    if rows is not None: d["rows"]=rows
    if cols is not None: d["columns"]=cols
    if tag: d["tag"]=tag
    return d

EN = [
  S("steps","Part 1 — Prologue: The Police Station","The game opens outside the station. This first sequence teaches the core loop: talk, search, read, then act.",[
    "Enter the police station and talk to Officer May at the front desk — she tells you about a letter and about Uncle Smith being out on a case",
    "Head into the lounge and find Uncle Smith watching TV in the dark; switch on the lights and he disappears",
    "Try the Mailroom door on the left — it is locked for now",
    "Return to May and she asks you to check Officer Smith's desk: take the Key from a drawer, plus a Liquor Token and a collectable Document under the desk",
    "Unlock the Mailroom and inspect the clipboard on the desk to find the Mysterious Letter",
    "May calls you back — speak with Officer Smith and open the letter: it is from Lynn DaHandt, asking you to go to the Factory and look for a band called The Gentle Rogues",
    "The station suddenly catches fire — grab the front-door Key from the Mailroom desk, pick up the Police Dispatch Record in the lounge, and leave through the front door",
  ]),
  S("steps","Part 2 — The Overpass & The Old Machinist","You wake up near the Factory. The chapter's real investigation begins on the streets below.",[
    "Wake up on an overpass and look down — a commotion: a dog named Teddy has died",
    "Captain Theo, the Factory supervisor, tells you to fetch Axel Flint and join the meeting",
    "Talk to the Old Machinist — trade your Relief Meal for the book Fundamentals for the Machinist (waiting at the Pawnshop)",
    "Drop to the streets and head right; under the overpass you find Axel Flint arguing with Griff Flint",
    "Tell Axel that Captain Theo is looking for him",
    "A skill check comes up — smack Axel or talk him down; each choice changes how the scene plays out",
    "Griff Flint offers to share a drink with you, and you gain 2 Clues for your Deduction",
  ]),
  S("steps","Part 3 — Teddy's Death: Interrogating the People","The Factory case is built on the testimony around Teddy's death. Talk before you act.",[
    "Talk to everyone at the scene before deciding anything",
    "Let Captain Theo lay out the meeting and what he expects from you",
    "Ask witnesses what they actually saw — and what they only assumed",
    "Note who has a history with Teddy or a reason to hide something",
    "Use rewind to ask the same person different questions and compare answers",
  ]),
  S("list","Part 4 — Teddy's Death: Following the Clues","The testimonies do not add up. Find where.",[
    "Cross-reference what each witness said about the same moment",
    "Look for the contradiction — the bread and butter of every KTS case",
    "Check the physical scene: positions, the scribblings on the screen, anything out of place",
    "The clue chain points to who was really responsible, not who everyone blames",
  ]),
  S("steps","Part 5 — Teddy's Death: Resolving the Incident","Present what you found and choose how to act on it.",[
    "Bring your conclusion back to Captain Theo",
    "Decide between justice and protection for the person responsible",
    "The choice shapes your standing with the Factory workers and moves the corruption meter",
    "Save before committing — the consequences carry into later chapters",
  ]),
  S("steps","Part 6 — Father's Secret: Rafe's Mom's Request & The Protest","A personal thread opens next to the main case.",[
    "Rafe's mom asks for your help with a private matter",
    "An Anti-Blockade Protest is brewing in the streets — talk to the people involved",
    "Decide how you engage: support the protest, calm it down, or step aside",
    "Watch how your choice reflects on Rafe and the family secret at the center of this arc",
  ]),
  S("list","Part 7 — Father's Secret: Cooling Rafe Down","Rafe is ready to escalate. How you cool him down decides what you learn.",[
    "Reason with him directly — show him what you know about his father",
    "Involve Captain Theo to keep the situation from boiling over",
    "Or use force, if you are willing to pay the relationship cost",
    "Each path changes Rafe's arc and what the Factory reveals about the past",
  ]),
  S("list","Part 8 — Captain Theo's Memories","The Shadow's reconstruction shines on the people of the Factory too.",[
    "Use reconstruction on objects tied to Theo to see what happened, not what is claimed",
    "Revisit earlier scenes after the meeting — new details appear once you know more",
    "Theo's memories connect the Factory incident to the larger mystery of Dark Tide City",
  ]),
  S("steps","Part 9 — Wrapping Up Loose Ends","Before you move to the South, close every open thread.",[
    "Return to areas you visited early once you have new information — dialogue can change",
    "Talk to each named character one final time",
    "Collect any documents you skipped the first time through",
    "Save before the chapter-end decision; the choice ripples into the next chapter",
  ]),
]

ZH = [
  S("steps","第一部分 · 序章：警察局","游戏从警察局外开始。这一小段教你核心循环：交谈、搜查、阅读，然后行动。",[
    "进入警察局，与前台警官 May 交谈——她会告诉你关于一封信的事，以及 Uncle Smith 正在外面办案",
    "走进休息室，发现 Uncle Smith 在黑暗中看电视；打开灯后他消失了",
    "试试左边的邮件室门——目前是锁着的",
    "回到 May 那里，她让你检查 Smith 警官的办公桌：从抽屉里拿到钥匙，桌下还有一枚酒馆代币和一份可收集文档",
    "打开邮件室，检查桌上的剪贴板，找到神秘信件",
    "May 叫你回去——与 Smith 警官对话并打开信：寄信人是 Lynn DaHandt，请你前往工厂寻找一支叫「温柔无赖（The Gentle Rogues）」的乐队",
    "警察局突然起火——回到邮件室拿前门钥匙，在休息室拾取一份警局调度记录，然后从前门离开",
  ]),
  S("steps","第二部分 · 天桥与老机械师","你在工厂附近醒来。本章真正的调查从下方的街道开始。",[
    "在天桥上醒来，往下看——一片骚动：一只叫泰迪（Teddy）的狗死了",
    "工厂主管西奥队长（Captain Theo）让你去找 Axel Flint 并参加集会",
    "与老机械师交谈——用你的救济餐换一本《机械师基础》（放在当铺里）",
    "下到街道往右走；在天桥下发现 Axel Flint 正在和 Griff Flint 争吵",
    "告诉 Axel，西奥队长在找他",
    "出现技能检定——揍 Axel 或说服他，你的选择会改变接下来的场景",
    "Griff Flint 邀请你喝一杯，你获得 2 条推理线索",
  ]),
  S("steps","第三部分 · 泰迪之死：审讯众人","工厂案建立在泰迪之死相关证词之上。先交谈，再行动。",[
    "在做出任何决定前，先和现场所有人交谈",
    "让西奥队长说明集会的安排和他对你的期望",
    "问目击者他们真正看到了什么——以及哪些只是猜测",
    "留意谁与泰迪有过节，或谁有理由隐瞒什么",
    "用回溯对同一个人问不同的问题，比较答案",
  ]),
  S("list","第四部分 · 泰迪之死：追查线索","证词对不上。找到对不上的地方。",[
    "交叉比对每个目击者对同一时刻的描述",
    "寻找矛盾——这是每个 KTS 案件的核心",
    "检查物理现场：位置、屏幕上的涂鸦、任何不对劲的细节",
    "线索链指向真正该负责的人，而不是众人指责的那个人",
  ]),
  S("steps","第五部分 · 泰迪之死：解决事件","呈上你的结论，并选择如何行动。",[
    "把你的结论带回给西奥队长",
    "在正义与保护之间，为真正负责的人做出选择",
    "这个选择会影响你在工厂工人中的声望，并推动黑化度",
    "在作出承诺前保存——后果会延续到后面的章节",
  ]),
  S("steps","第六部分 · 父亲的秘密：Rafe 母亲的请求与抗议","主线之外，一条个人线索展开了。",[
    "Rafe 的母亲请你帮忙处理一件私事",
    "街头的反封锁抗议正在酝酿——与参与者交谈",
    "决定你的态度：支持抗议、平息它，或置身事外",
    "观察你的选择如何影响 Rafe，以及这段故事核心的家庭秘密",
  ]),
  S("list","第七部分 · 父亲的秘密：安抚 Rafe","Rafe 准备把事情闹大。你如何安抚他，决定你能了解到什么。",[
    "直接与他讲道理——告诉他你对他父亲的了解",
    "请西奥队长介入，避免局面失控",
    "或者使用武力，如果你愿意付出关系的代价",
    "每条路线都会改变 Rafe 的剧情线，以及工厂揭示的过去",
  ]),
  S("list","第八部分 · 西奥队长的记忆","影子的重建同样照亮工厂里的人。",[
    "对与西奥相关的物品使用重建，看清真正发生了什么，而不是别人声称的",
    "集会结束后重访之前的场景——知道得更多后，新细节会出现",
    "西奥的记忆把工厂事件与暗潮市的更大谜团连接起来",
  ]),
  S("steps","第九部分 · 收尾","在前往南方之前，把每一条线索都收干净。",[
    "拿到新信息后，回到早期去过的区域——对话可能会改变",
    "和每个有名有姓的角色最后谈一次",
    "补上第一次漏掉的文档",
    "在章节结尾的决定前保存；这个选择会影响下一章",
  ]),
]

JA = [
  S("steps","パート1 · 序章：警察署","ゲームは警察署の外から始まります。この導入で「話す・調べる・読む・行動する」の基本ループを学びます。",[
    "警察署に入り、受付のメイ巡査と話す——一通の手紙と、スミス署長が事件で外出中だと教えられる",
    "ラウンジに入るとスミス署長が暗闇でテレビを見ている——電気を付けると彼は消える",
    "左の郵便室のドアを試す——今は鍵がかかっている",
    "メイのところに戻ると、スミス署長の机を調べるよう頼まれる：引き出しから鍵を、机の下から酒場トークンと収集可能な書類を入手",
    "郵便室を開け、机のクリップボードを調べて「謎の手紙」を見つける",
    "メイに呼び戻され、スミス署長と話して手紙を開く：差出人はリン・ダハント。工場へ行き「ザ・ジェントルローグス」というバンドを探してほしいと頼まれる",
    "警察署が突然炎上——郵便室で正面玄関の鍵を取り、ラウンジで警察配備記録を拾い、正面玄関から脱出する",
  ]),
  S("steps","パート2 · 高架橋と老機械工","工場の近くで目覚めます。本章の本格的な調査は下の街で始まります。",[
    "高架橋で目覚め、下を見る——騒ぎが起きている：テディという犬が死んでいる",
    "工場の監督、テオ船長がアクセル・フリントを呼んで集会に参加するよう命じる",
    "老機械工と話し、配給食と交換で『機械工の基礎』（質屋にある）を手に入れる",
    "通りに降りて右へ——高架橋の下でアクセル・フリントがグリフ・フリントと口論している",
    "アクセルにテオ船長が探していると伝える",
    "スキルチェック発生——アクセルを殴るか説得するか。選択で展開が変わる",
    "グリフ・フリントが一杯おごると言い、推理用の手がかりを2つ獲得",
  ]),
  S("steps","パート3 · テディの死：人々への尋問","工場の事件はテディの死をめぐる証言が鍵です。行動より先に話を聞きましょう。",[
    "何かを決める前に、現場の全員と話す",
    "テオ船長に集会の趣旨と期待を聞く",
    "目撃者に「実際に見たもの」を聞く——思い込みと区別する",
    "テディと因縁のある人物、何かを隠したがっている人物に注目",
    "巻き戻しで同じ相手に違う質問をし、答えを比べる",
  ]),
  S("list","パート4 · テディの死：手がかりを追う","証言は一致しません。どこが食い違うのかを見つけます。",[
    "同じ瞬間について各目撃者の証言を突き合わせる",
    "矛盾を探す——KTS の事件の核心はここ",
    "物理的な現場を確認：位置、画面の落書き、不自然な点",
    "手がかりの連鎖は、皆が疑う人物ではなく本当の責任者を指す",
  ]),
  S("steps","パート5 · テディの死：事件の解決","結論を提出し、どう動くかを選びます。",[
    "結論をテオ船長に持ち帰る",
    "責任者への「正義」か「保護」かを選ぶ",
    "この選択は工場労働者との関係に影響し、汚染度を動かす",
    "決断前にセーブ——結果は後の章まで続く",
  ]),
  S("steps","パート6 · 父の秘密：レイフの母の依頼と抗議","本筋に並行して、個人の物語が開きます。",[
    "レイフの母が私事の手助けを求める",
    "街で封鎖反対デモが起きつつある——関わった人々と話す",
    "デモに加勢するか、鎮めるか、距離を置くかを決める",
    "その選択がレイフと、この物語の中心にある家族の秘密にどう映るかを見る",
  ]),
  S("list","パート7 · 父の秘密：レイフを落ち着かせる","レイフは事を大きくしようとしています。どう鎮めるかで得られる情報が変わります。",[
    "直接説得する——彼の父親について知っていることを伝える",
    "テオ船長を巻き込んで事態を収める",
    "関係の代償を払う覚悟があれば、力に訴える",
    "どの道もレイフの物語と、工場が明かす過去を変える",
  ]),
  S("list","パート8 · テオ船長の記憶","シャドウの再現は工場の人々にも光を当てます。",[
    "テオに関係する物体に再現を使い、「主張」ではなく「実際」を見る",
    "集会後に以前の場面を再訪——知ることが増えると新たな細部が見える",
    "テオの記憶は工場の事件をダークタイドシティの大きな謎へと結びつける",
  ]),
  S("steps","パート9 · 未解決の糸を結ぶ","南へ移る前に、すべての糸を回収します。",[
    "新しい情報を得たら早期のエリアに戻る——会話が変わることもある",
    "名前のあるキャラクター全員と最後にもう一度話す",
    "最初に取り逃がした書類を回収する",
    "章末の決断の前にセーブ——選択は次章へと続く",
  ]),
]

KO = [
  S("steps","파트 1 — 프롤로그: 경찰서","게임은 경찰서 밖에서 시작합니다. 이 도입부에서 '말하기·조사하기·읽기·행동하기'의 핵심 루프를 배웁니다.",[
    "경찰서에 들어가 접수대의 메이 경관과 대화 — 편지에 대한 이야기와 스미스 서장이 사건으로 외출 중이라는 말을 듣습니다",
    "라운지로 가면 스미스 서장이 어둠 속에서 TV를 보고 있습니다 — 불을 켜면 그는 사라집니다",
    "왼쪽 우편실 문을 시도 — 지금은 잠겨 있습니다",
    "메이에게 돌아가면 스미스 서장의 책상을 조사하라고 합니다: 서랍에서 열쇠를, 책상 아래에서 술집 토큰과 수집용 문서를 얻습니다",
    "우편실을 열고 책상의 클립보드를 조사해 '수수께끼의 편지'를 찾습니다",
    "메이가 다시 부르면 스미스 서장과 대화하고 편지를 엽니다: 발신자는 린 다한트. 공장으로 가서 '젠틀 로그스'라는 밴드를 찾아달라는 내용입니다",
    "경찰서가 갑자기 불에 타기 시작합니다 — 우편실에서 정문 열쇠를 챙기고, 라운지에서 경찰 배치 기록을 주운 뒤 정문으로 탈출합니다",
  ]),
  S("steps","파트 2 — 고가도로와 늙은 기계공","공장 근처에서 깨어납니다. 이번 장의 진짜 수사는 아래 거리에서 시작됩니다.",[
    "고가도로에서 깨어나 아래를 내려다봅니다 — 소란이 일어나고 있습니다: 테디라는 개가 죽었습니다",
    "공장 감독인 테오 선장이 액셀 플린트를 데려와 회의에 참석하라고 합니다",
    "늙은 기계공과 대화 — 배급 식사를 내주고 '기계공의 기초' 책(전당포에 있음)을 받습니다",
    "거리로 내려가 오른쪽으로 — 고가도로 아래에서 액셀 플린트가 그리프 플린트와 다투고 있습니다",
    "액셀에게 테오 선장이 찾고 있다고 전합니다",
    "스킬 체크가 나옵니다 — 액셀을 때리거나 설득하세요. 선택에 따라 장면이 달라집니다",
    "그리프 플린트가 한잔 하자고 하며, 추리용 단서 2개를 얻습니다",
  ]),
  S("steps","파트 3 — 테디의 죽음: 사람들 심문","공장 사건은 테디의 죽음에 관한 증언이 핵심입니다. 행동보다 대화를 먼저 하세요.",[
    "무엇이든 결정하기 전에 현장의 모두와 대화하세요",
    "테오 선장에게 회의의 취지와 기대를 들으세요",
    "목격자들에게 실제로 본 것을 물어보세요 — 추측과 구분해서",
    "테디와 악연이 있거나 무언가를 숨기려는 사람을 주목하세요",
    "되감기로 같은 상대에게 다른 질문을 하고 답을 비교하세요",
  ]),
  S("list","파트 4 — 테디의 죽음: 단서 추적","증언은 맞지 않습니다. 어디가 어긋나는지 찾으세요.",[
    "같은 순간에 대한 각 목격자의 증언을 교차 비교하세요",
    "모순을 찾으세요 — 모든 KTS 사건의 핵심입니다",
    "물리적 현장을 확인하세요: 위치, 화면의 낙서, 어색한 부분",
    "단서의 사슬은 모두가 의심하는 사람이 아니라 진짜 책임자를 가리킵니다",
  ]),
  S("steps","파트 5 — 테디의 죽음: 사건 해결","결론을 제출하고 어떻게 행동할지 선택하세요.",[
    "결론을 테오 선장에게 가져가세요",
    "책임자에게 '정의'를 실현할지 '보호'할지 선택하세요",
    "이 선택은 공장 노동자들과의 관계를 만들고 오염도를 움직입니다",
    "결정 전에 저장하세요 — 결과는 이후 챕터까지 이어집니다",
  ]),
  S("steps","파트 6 — 아버지의 비밀: 레이프 엄마의 부탁과 시위","본편과 나란히 개인적인 이야기가 펼쳐집니다.",[
    "레이프의 엄마가 사적인 일을 도와달라고 합니다",
    "거리에서 봉쇄 반대 시위가 일어나고 있습니다 — 관련자들과 대화하세요",
    "시위를 지지할지, 진정시킬지, 거리를 둘지 결정하세요",
    "그 선택이 레이프와, 이 이야기 중심에 있는 가족의 비밀에 어떻게 비치는지 지켜보세요",
  ]),
  S("list","파트 7 — 아버지의 비밀: 레이프 진정시키기","레이프는 일을 키우려 합니다. 어떻게 진정시키느냐에 따라 알게 되는 것이 달라집니다.",[
    "직접 설득하세요 — 그의 아버지에 대해 아는 것을 보여주세요",
    "테오 선장을 개입시켜 상황이 과열되는 것을 막으세요",
    "관계의 대가를 감당할 수 있다면 힘을 쓰세요",
    "모든 길은 레이프의 서사와 공장이 드러내는 과거를 바꿉니다",
  ]),
  S("list","파트 8 — 테오 선장의 기억","섀도우의 재구성은 공장 사람들에게도 빛을 비춥니다.",[
    "테오와 관련된 물건에 재구성을 사용해 '주장'이 아닌 '실제'를 보세요",
    "회의 후 이전 장면을 다시 방문하세요 — 더 알게 되면 새로운 세부가 보입니다",
    "테오의 기억은 공장 사건을 다크 타이드 시티의 더 큰 미스터리로 연결합니다",
  ]),
  S("steps","파트 9 — 마무리: 묶이지 않은 실타래","남쪽으로 이동하기 전에 모든 실타래를 정리하세요.",[
    "새 정보를 얻으면 초반에 갔던 지역으로 돌아가세요 — 대화가 바뀔 수 있습니다",
    "이름이 있는 캐릭터 전원과 마지막으로 한 번 더 대화하세요",
    "처음에 놓친 문서를 챙기세요",
    "챕터 끝 결정 전에 저장하세요 — 선택은 다음 챕터로 이어집니다",
  ]),
]

WALKTHROUGH = {
  "sections": { "en": EN, "zh-CN": ZH, "zh-TW": None, "ja": JA, "ko": KO },
}

# ===== how-to-play 首 15 分钟（已验证） =====
HTP_EN = [S("steps","The First 15 Minutes (Verified)","The opening is short and scripted. Here is exactly what happens, from our verified playthrough notes.",[
    "Start outside the police station and walk inside to the front desk",
    "Talk to Officer May — she mentions a letter and that Uncle Smith is out on a case",
    "Find Uncle Smith in the lounge; switch on the lights and he vanishes",
    "Check Officer Smith's desk: Key in a drawer, Liquor Token and a Document underneath",
    "Open the Mailroom, inspect the clipboard, and find the Mysterious Letter",
    "Read the letter: Lynn DaHandt asks you to find a band called The Gentle Rogues at the Factory",
    "The station catches fire — grab the front-door Key and escape through the entrance",
  ])]
HTP_ZH = [S("steps","前 15 分钟（已验证）","开场很短且有脚本。以下是根据我们已验证的通关笔记整理的完整过程。",[
    "在警察局外开始，走进去到前台",
    "与警官 May 交谈——她提到一封信，并说 Uncle Smith 正在外面办案",
    "在休息室找到 Uncle Smith；打开灯后他消失了",
    "检查 Smith 警官的办公桌：抽屉里有钥匙，桌下有酒馆代币和一份文档",
    "打开邮件室，检查剪贴板，找到神秘信件",
    "读信：Lynn DaHandt 请你去工厂寻找一支叫「温柔无赖」的乐队",
    "警察局起火——拿上前门钥匙，从入口逃走",
  ])]
HTP_JA = [S("steps","最初の15分（検証済み）","オープニングは短く、スクリプトに従って進みます。検証済みのプレイ記録をもとに、正確な流れを紹介します。",[
    "警察署の外から始まり、中へ入って受付へ",
    "メイ巡査と話す——一通の手紙と、スミス署長が事件で外出中だと聞く",
    "ラウンジでスミス署長を見つけ、電気を付けると彼は消える",
    "スミス署長の机を調べる：引き出しに鍵、下に酒場トークンと書類",
    "郵便室を開け、クリップボードを調べ、「謎の手紙」を見つける",
    "手紙を読む：リン・ダハントが工場で「ザ・ジェントルローグス」を探すよう依頼",
    "警察署が炎上——正面玄関の鍵を取り、入口から脱出",
  ])]
HTP_KO = [S("steps","첫 15분 (검증됨)","오프닝은 짧고 정해진 흐름입니다. 검증된 플레이 기록을 바탕으로 정확한 진행을 소개합니다.",[
    "경찰서 밖에서 시작해 안으로 들어가 접수대로 갑니다",
    "메이 경관과 대화 — 편지 이야기와 스미스 서장이 사건으로 외출 중이라는 말을 듣습니다",
    "라운지에서 스미스 서장을 찾아 불을 켜면 그는 사라집니다",
    "스미스 서장의 책상을 조사: 서랍에 열쇠, 아래에 술집 토큰과 문서",
    "우편실을 열고 클립보드를 조사해 '수수께끼의 편지'를 찾습니다",
    "편지를 읽습니다: 린 다한트가 공장에서 '젠틀 로그스' 밴드를 찾아달라고 합니다",
    "경찰서가 불탑니다 — 정문 열쇠를 챙기고 입구로 탈출합니다",
  ])]

# ===== cases 第一章案件拆解（已验证） =====
CASES_EN = [S("table", "Chapter 1 Case Breakdown", "The verified beats of Chapter 1, mapped to the case board.", rows=[
    ["The Letter","Police Station","A medical-gauge letter from Lynn DaHandt; the station burns after you read it","Prologue"],
    ["Teddy's Death","Factory district","A dog's death becomes the case that breaks the Factory open — interrogate, follow the clues, resolve","Part 3-5"],
    ["Father's Secret","Factory & streets","Rafe's family thread: his mother's request, the Anti-Blockade Protest, cooling Rafe down","Part 6-7"],
    ["Captain Theo's Memories","Factory","Reconstruction on Theo's objects connects the incident to the city's ten-year-old mystery","Part 8"],
    ["Loose Ends","Dark Tide City","Return to earlier areas, close every thread, save before the chapter-end choice","Part 9"],
  ], cols=["Beat","Location","Key Element","Stage"])]
CASES_ZH = [S("table", "第一章案件拆解", "第一章已核实的节点，映射到案件板上。", rows=[
    ["信件","警察局","来自 Lynn DaHandt 的医疗计量器信件；读信后警察局起火","序章"],
    ["泰迪之死","工厂区","一只狗的死成为打开工厂的契机——审讯、追查线索、解决事件","第3-5部分"],
    ["父亲的秘密","工厂与街道","Rafe 的家庭线：母亲的请求、反封锁抗议、安抚 Rafe","第6-7部分"],
    ["西奥队长的记忆","工厂","对西奥物品的重建，把事件与城市十年谜团连接起来","第8部分"],
    ["收尾","暗潮市","回到早期区域，收清每条线索，在章节结尾选择前保存","第9部分"],
  ], cols=["节点","地点","关键元素","阶段"])]
CASES_JA = [S("table", "第1章の事件の内訳", "検証済みの第1章の節目を事件ボードに整理しました。", rows=[
    ["手紙","警察署","リン・ダハントからの医療ゲージの手紙；読むと警察署が炎上","序章"],
    ["テディの死","工場地区","犬の死が工場を切り開く事件に——尋問、手がかり追跡、解決","パート3-5"],
    ["父の秘密","工場と街","レイフの家族の物語：母の依頼、封鎖反対デモ、レイフを落ち着かせる","パート6-7"],
    ["テオ船長の記憶","工場","テオの物体への再現が、事件を10年前の謎へと結びつける","パート8"],
    ["締めくくり","ダークタイドシティ","初期エリアに戻り、すべての糸を回収し、章末の選択前にセーブ","パート9"],
  ], cols=["節目","場所","重要要素","段階"])]
CASES_KO = [S("table", "1장 사건 분해", "검증된 1장의 지점을 사건 보드에 정리했습니다.", rows=[
    ["편지","경찰서","린 다한트의 의료 게이지 편지; 읽으면 경찰서가 불탑니다","프롤로그"],
    ["테디의 죽음","공장 지구","개의 죽음이 공장을 열어젖히는 사건이 됩니다 — 심문, 단서 추적, 해결","파트 3-5"],
    ["아버지의 비밀","공장과 거리","레이프의 가족 이야기: 엄마의 부탁, 봉쇄 반대 시위, 레이프 진정시키기","파트 6-7"],
    ["테오 선장의 기억","공장","테오의 물건에 대한 재구성이 사건을 10년 전 미스터리로 연결합니다","파트 8"],
    ["마무리","다크 타이드 시티","초반 지역으로 돌아가 모든 실타래를 정리하고, 챕터 끝 선택 전에 저장","파트 9"],
  ], cols=["지점","위치","핵심 요소","단계"])]

# ===== faq 补充（已验证） =====
FAQ_ADD_EN = [["Is there a console version?","Yes — PS5 and Xbox Series X|S versions were announced by press coverage, with the console release set for August 12, 2026."],["How many achievements does the free demo have?","The free demo (app 2947640) includes 10 achievements, verified through SteamDB."]]
FAQ_ADD_ZH = [["有主机版吗？","有——PS5 和 Xbox Series X|S 版本已由媒体报道宣布，主机版定于 2026 年 8 月 12 日发售。"],["免费试玩版有多少成就？","免费试玩版（应用 2947640）包含 10 个成就，经 SteamDB 核实。"]]
FAQ_ADD_JA = [["コンソール版はありますか？","はい——PS5 / Xbox Series X|S 版が報道で発表され、コンソール版は2026年8月12日発売予定です。"],["無料デモの実績はいくつですか？","無料デモ（アプリ2947640）には実績10個が含まれます（SteamDBで確認）。"]]
FAQ_ADD_KO = [["콘솔 버전이 있나요?","네 — PS5 / Xbox Series X|S 버전이 언론 보도로 발표되었고, 콘솔 출시는 2026년 8월 12일 예정입니다."],["무료 데모 업적은 몇 개인가요?","무료 데모(앱 2947640)에는 업적 10개가 포함되어 있습니다(SteamDB로 확인)."]]
