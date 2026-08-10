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

# ===== 第二章 · 猪笼城寨（Part 10-25，来源：intoindiegames Part 2 + 玩家实测，用自己的话重写）=====
P2_EN = [
  S("steps","Part 10 — Arriving at the Wharf Marketplace","Chapter 2 opens in the Pig Cage Walled City. The Old City District has been abandoned, so everyone now lives around the Wharf.",[
    "Arrive at the busy Wharf of the Pig Cage Walled City — the Old City District is abandoned and everyone lives here now",
    "Explore the western side of the Wharf first; eavesdrop on people at the tables for flavor text and local lore",
    "Watch the Fisherman's Wharf Owner cook a meal for a customer — let the event play out, then talk to him",
    "Check the store with the vending machines past the Owner for consumables",
  ]),
  S("steps","Part 11 — Meeting Kiki & Max","Two siblings are waiting for someone shady, and their quest line unlocks a lot of the Wharf.",[
    "Cross the wooden bridge west of the shop and meet siblings Max and Kiki, who are waiting for a man in a Black Trenchcoat — agree to help them",
    "Continue over the bridge and eavesdrop: some people were stopped by the Reed Mansion butler despite holding Fair Tickets",
    "A guard blocks the stairs up to the Reed Mansion for now — come back later",
    "Head back and ask the man fishing at the Wharf about the man in the Black Trenchcoat; he says the kids were late but someone was indeed waiting — gain a Shadow Shard",
    "Ask the mahjong players: the man said he would try his luck at the Old County Office; they also recall a fight between the siblings and the Wharf Owner",
    "Ask the Wharf Owner about the kids — he says they loitered; suggest he checks his pocket and he finds his pack of cigarettes missing",
    "Inside the store, investigate near the vending machine: the poster can be moved, revealing a peephole in the wall",
    "Talk to the Shadow — you conclude Max and Kiki were peeping; you now have enough Shards to rewind the event",
    "Ask the siblings why they were following the man; they confess he seemed shady and they wanted back what was theirs; Max only took the cigarettes as revenge on the Owner, so you can trust them — the questline pauses here for now",
  ]),
  S("steps","Part 12 — Accepting Junior's Class Notes","A small errand that sets up the Priestess thread.",[
    "Return to your arrival point and check the northern area; find a child scolding another child named Dudly, saying he has a gift for Celestia",
    "Ask about the Priestess to learn more about Celestia",
    "Talk to Junior afterward — he convinces you to deliver the Class Notes to the Priestess",
  ]),
  S("steps","Part 13 — Finding Uncle Smith","The man you came north to find turns out to be right on the Wharf.",[
    "Head up the bridge past Junior's shop and find an old man fishing at the Wharf; he gives you a Fishing Rod — you can fish right away if you want",
    "Past the old man, a shirtless man (Chiffon) asks you to distract Junior so he can steal fruit; refusing improves your relationship with him",
    "The old man is Uncle Smith — the reunion is heartfelt, and over drinks he explains the city is volatile because of Master Reed's disappearance",
    "You get the option to rewind into a flashback — take it",
  ]),
  S("steps","Part 14 — Reed Village Flashback","Ten years back, as a rookie, you first met Officer Smith on a homicide case.",[
    "Rewind 10 years: you are a rookie cop sent to help with the Reed Village homicide case",
    "Talk to Officer Smith, then enter the temple and inspect the victim's body — the victim did not resist",
    "Inspect the broken table nearby: a fight broke out after the victim died",
    "Check the two rooms on each side of the idol to collect all four Shadow Shards",
    "Play the Reed Village Speculation, then speak with Officer Smith — Lucas senses something is off and gets worked up",
    "Back in the present, finish the dialogue with Uncle Smith; he heads for Reed Mansion but slips off the Wharf into the water",
    "A lady in a black dress helps him up — this is Mrs. Reed, wife of the late Master Reed; run through the introductions",
    "After they leave, Chiffon talks to you; tell him about Officer Smith to improve your relationship and start the Priestess's Curse storyline",
  ]),
  S("steps","Part 15 — Entering Reed Mansion","The mansion's butler is the first wall between you and the investigation.",[
    "Take the path left past the store; the Butler of Reed stops you even if you succeed the Skill Check",
    "Chiffon explains the easy way in: carry a fish and present it as an offering",
    "Buy a Sacrificial Fish from the Fisherman's Wharf Owner for 25 Money — earn it through part-time jobs or by searching trashcans",
    "Return to the butler; Chiffon is making a scene inside the mansion and then moves to the Opera Theater — side with Chiffon when asked",
    "Tell the butler you have come for Tribute; he lets you in but asks you to visit the Temple first",
  ]),
  S("steps","Part 16 — The Priestess Temple","A temple errand that doubles as your entrance ticket.",[
    "Go left to the front of the Temple; inspect a note on the desk and talk to the two people smoking nearby — they tell you to knock harder",
    "Bang on the Door to enter and talk to the Priestess at the Altar; place down the fish",
    "She asks you to move the offerings on the table; interact with every object to trigger a cutscene",
    "Check on the Priestess after the cutscene and mention the Class Notes",
    "She asks you to bring Junior to the Temple; agree and exit — the stairway near the temple is now usable",
    "Return to Junior's Boat, speak with him, escort him back to the Temple, and make a Pinky Promise to complete the questline",
    "Outside, pass the Skill Check to gain the Secret Hideout Clue; the butler arrives accusing Junior of theft — pay him to end the trouble",
  ]),
  S("steps","Part 17 — The Opera Theater","The theater holds the mansion's secrets — and a hidden compartment.",[
    "Head to the Opera Theater; speak to the Old Man Chiffon bumped into, then inspect the statue next to him — wipe off the dust if you have the brawn",
    "Inside, Chiffon is causing a scene as usual; he asks you to deliver a Fruit Basket to Mr. Collins, the restaurant owner on the second floor",
    "Take the stairs to the river and inspect the boat; move the fish away to find a secret compartment with Money and a Map — new Clue: The Secret Compartment",
    "A homeless person sits under the bridge nearby, but has no dialogue options yet",
    "Return to where you left the butler and take the elevator to the second floor; find Officer Smith speaking with Mrs. Reed",
    "Officer Smith shows you Master Reed's Suicide Note and explains the region's power dynamic; deliver the Fruit Basket without mentioning Chiffon's name",
  ]),
  S("steps","Part 18 — Finding the Man in Black Trenchcoat","Kiki and Max's man turns out to be closer than expected.",[
    "On the upper floor, take the bridge opposite the elevator west and follow the path past the Clinic",
    "At the end, a couple argues about rings near the Jewellery Store — they mention a homeless man who found a Gold Ring in a fish's belly",
    "Take the elevator down; the man in the trench coat stands right next to it — choose Sounds Familiar",
    "Before returning to the siblings, watch the event at the door: Lily arguing with Rochester's Butler",
    "Return to Kiki and Max and agree to take them to the man; watch what happens from a distance, then talk to Kiki on the railing near the Jewellery Store",
    "Max opens the Jewellery Store door",
  ]),
  S("steps","Part 19 — The Jewellery Store","The invoice inside ties Mrs. Reed to the day Master Reed vanished.",[
    "Inspect the Jewellery Display on the right, then open the front cabinet and read the Invoice inside — it shows Mrs. Reed making a large purchase on the day Master Reed disappeared",
    "Inspect the case on the other side of the store to find a second Shadow Shard, then rewind and play back the event",
    "When you exit the event, footsteps outside send Max and Kiki running",
    "Talk to the store owner and say you chased the thieves away",
  ]),
  S("steps","Part 20 — Delivering Max's Package","A rescue that earns you a favor — and a bigger favor down the line.",[
    "Go down the stairs and follow the path; find Max on the floor — he has been caught; save him and he gives you a package",
    "Find Kiki near where you shared a drink with Uncle Smith",
    "She offers to take you to Shipwreck Wharf if you can find three Boat Tickets",
    "Both siblings have roles to play later; for now, head back to Mrs. Reed",
  ]),
  S("steps","Part 21 — Interrogating Mrs. Reed","Her testimony has a loophole — find it with rewind.",[
    "Find Mrs. Reed on the mansion balcony overlooking the Opera Theater and talk to her",
    "She asks which Datura is your favorite — choose Red",
    "She explains the events of the day Master Reed disappeared; you can rewind the incident based on her testimony",
    "Ask her to repeat the incident; when she reaches the part about the Opera Stage, choose Wait",
    "Lucas finds a loophole and you get a new clue; let the conversation run its course",
  ]),
  S("list","Part 22 — Inquiring about the Curse","Two conversations that build the Priestess's Curse thread.",[
    "Talk to the Butler of Reed and ask about the curse — he asks for a favor in exchange",
    "Agree to hear him out: he wants you to check Mrs. Reed's house for signs she was unfaithful",
    "Talk to Chiffon in the Opera Theater about the curse; he suspects Master Reed was illiterate",
    "The questline pauses here for now",
  ]),
  S("steps","Part 23 — Inspecting Mrs. Reed's House","A locked door and a pickpocket partner.",[
    "Take the stairs at the back to reach Mrs. Reed's house; the door is locked",
    "Go back to Kiki and ask her to pick the lock; after you explain, she insists on tagging along",
    "Use the Lockpicking Tool to enter — Kiki closes the door behind you and you are both trapped inside",
  ]),
  S("steps","Part 24 — Mrs. Reed's Room: The Safe & the Land Deed","The room hides the chapter's biggest material clues.",[
    "Inside, the Study on the right is locked — you need a Key",
    "Search the cabinet in the living area: money and photographs; check the drawers for a note and read it",
    "In the bedroom, find the safe — the code is on the newspaper from the cabinet: January 1st, Year 355; enter 35511",
    "Take the Key and the note (a Land Deed), plus the Money",
    "Inspect the wardrobe thoroughly; talking with Kiki, you find a Torn Invoice",
    "On the makeup, choose Probably Not to cause a Worldline Shift and find a suspicious bottle",
    "The Fragment of Clothes gives you a clue for the Priestess's Curse storyline",
  ]),
  S("steps","Part 25 — The Study: The Forged Suicide Note","The chapter's climax: recreate the writing, and the forgery falls apart.",[
    "Use the Key to open the Study and talk with Kiki, then investigate the scene",
    "Inspect the thick layer of dust, then turn on the table lamp",
    "Investigate the table again — nothing; the Shadow intervenes and Lucas decides to reenact everything",
    "Follow the reenactment: turn on the desk lamp, wash the brush, dip it in ink, start writing",
    "Lucas notices it is too dark to write; move the desk lamp to the left and try writing again — now he notices the shadow",
    "Choose 'He moved the desk lamp!' and complete the clues: The Layout of the Desk, A Decorative Desk?, and Was Master Reed Left-handed?",
    "Lucas and Kiki realize Master Reed was illiterate and Mrs. Reed helped write the Suicide Note",
    "You find the major clue: The Forged Suicide Note; leave through the front door with the Key when you are ready",
  ]),
]

P2_ZH = [
  S("steps","第十部分 · 抵达码头集市","第二章在猪笼城寨展开。旧城区已经废弃，所有人都搬到码头一带生活。",[
    "抵达猪笼城寨繁忙的码头——旧城区已废弃，现在所有人都住在这里",
    "先探索码头西侧；偷听坐在桌边的人交谈，收集氛围文本和本地情报",
    "观看渔市老板（Fisherman's Wharf Owner）为顾客做饭——让事件自然发生，之后再与他交谈",
    "检查老板店铺旁带自动售货机的商店，补充消耗品",
  ]),
  S("steps","第十一部分 · 遇见 Kiki 与 Max","两个等着神秘人的兄妹，他们的任务线能解锁码头大量内容。",[
    "走过店铺西边的木桥，遇见兄妹 Max 和 Kiki——他们在等一个穿黑色风衣的男人；同意帮忙",
    "继续过桥偷听：有人手持「公正票」仍被 Reed 府邸的管家拦下",
    "通往 Reed 府邸的楼梯有守卫把守——暂时无法上去，之后再来",
    "回头问码头钓鱼的男人关于黑衣人的事——他说孩子们迟到了，但确实有人在等；获得一块影之碎片",
    "问麻将桌旁的人：黑衣人说过要去旧县政府碰碰运气；他们还提到兄妹俩与渔市老板打过一架",
    "问渔市老板关于两个孩子的事——他说他们在他店里闲逛；建议他检查口袋，他发现香烟不见了",
    "进店检查自动售货机附近：海报可以移开，露出墙上的偷窥孔",
    "与影子交谈——你得出结论：Max 和 Kiki 确实在偷看；现在碎片已够，可以回溯事件",
    "回头问兄妹为什么跟踪那个人；他们承认觉得他可疑，想拿回属于自己的东西；Max 只偷了香烟作为对老板的报复，因此可以信任他们——这条任务线暂时到此为止",
  ]),
  S("steps","第十二部分 · 接下 Junior 的课堂笔记","一个为女祭司线铺垫的小差事。",[
    "回到你抵达的地方，检查北侧；发现一个孩子在训斥另一个叫 Dudly 的孩子，说他有礼物要送给 Celestia",
    "问关于女祭司的事，了解 Celestia",
    "之后与 Junior 交谈——他说服你帮忙把课堂笔记送给女祭司",
  ]),
  S("steps","第十三部分 · 找到 Uncle Smith","你北上要找的人，其实就在码头。",[
    "走过 Junior 店铺旁的小桥，发现一位在码头钓鱼的老人；他送给你一根钓竿——想钓鱼的话现在就可以",
    "在老人后面，一个赤膊男人（Chiffon）请你去分散 Junior 的注意力，好让他偷水果；拒绝会提升你与他的关系",
    "这位老人就是 Uncle Smith——重逢令人动容；喝酒时他告诉你，因为 Master Reed 失踪，整座城都处于动荡之中",
    "你获得进入闪回的选项——选它",
  ]),
  S("steps","第十四部分 · 芦苇村闪回","十年前，你作为新警第一次见到 Smith 警官，正在查一桩凶杀案。",[
    "回溯十年：你是一名新警，被派去协助芦苇村的凶杀案调查",
    "与 Smith 警官交谈后，进入寺庙检查受害者遗体——受害者没有反抗",
    "检查附近摔坏的桌子：受害者死后才发生过打斗",
    "检查神像两侧的两个房间，集齐全部四块影之碎片",
    "进行「芦苇村推理」，然后与 Smith 警官交谈——Lucas 感觉哪里不对，情绪激动起来",
    "回到现在，与 Uncle Smith 把对话说完；他动身去 Reed 府邸，却从码头滑落掉进水里",
    "一位穿黑裙的女士扶起他——她是已故 Master Reed 的妻子 Mrs. Reed；完成互相介绍",
    "他们离开后，Chiffon 来找你搭话；告诉他关于 Smith 警官的事会提升关系，并开启「女祭司的诅咒」故事线",
  ]),
  S("steps","第十五部分 · 进入 Reed 府邸","府邸管家是挡在调查前的第一道墙。",[
    "走店铺左侧的小路；即使技能检定成功，Reed 的管家也会拦住你",
    "Chiffon 告诉你简单的办法：带一条鱼当作供品",
    "从渔市老板那里花 25 金币买一条献祭鱼——可以通过打零工或在垃圾桶里翻找来赚",
    "回到管家处；Chiffon 正在府邸里大闹一场，随后转到歌剧院——被问到时就站在 Chiffon 这边",
    "告诉管家你是来进贡的；他放你进去，但要求你先去寺庙",
  ]),
  S("steps","第十六部分 · 女祭司神庙","一趟神庙差事，也是你进府的入场券。",[
    "向左走到神庙前；检查桌上的便条，并和附近两个抽烟的人交谈——他们让你用力敲门",
    "选择「砸门」进入，与祭坛前的女祭司交谈；把鱼放下",
    "她请你移动桌上的供品；与每件物品互动，触发过场动画",
    "过场后问候女祭司是否安好，并提起课堂笔记",
    "她请你去把 Junior 带来神庙；答应后离开——神庙附近的楼梯现在可以用了",
    "回到 Junior 的小船，与他交谈，护送他回神庙，并拉钩许诺以完成这条任务线",
    "在外面通过技能检定，获得「秘密藏身处」线索；管家赶来指责 Junior 偷窃——花钱摆平此事",
  ]),
  S("steps","第十七部分 · 歌剧院","歌剧院藏着府邸的秘密——还有一个暗格。",[
    "前往歌剧院；先与 Chiffon 撞到的老人交谈，然后检查他旁边的雕像——力气够的话可以擦掉灰尘",
    "进入歌剧院，Chiffon 一如既往在大闹；他请你去给二楼的餐厅老板 Mr. Collins 送果篮",
    "从剧院走楼梯下到河边，检查小船；移开鱼，发现一个暗格，里面有金币和一张地图——新线索「秘密隔间」",
    "桥下有个流浪汉，但暂时没有对话选项",
    "回到管家所在处，乘电梯上二楼；看到 Smith 警官正在与 Mrs. Reed 交谈",
    "Smith 警官给你看 Master Reed 的遗书，并解释当地的权力格局；把果篮送到，别提 Chiffon 的名字",
  ]),
  S("steps","第十八部分 · 找到黑衣男人","Kiki 和 Max 要找的人，比想象中更近。",[
    "在二楼，走电梯对面的桥向西，沿路经过诊所",
    "走到路尽头：一对情侣在珠宝店附近为戒指争吵——他们提到有个流浪汉在鱼肚子里发现了一枚金戒指",
    "乘电梯下去；穿风衣的男人就站在电梯旁边——选择「听起来耳熟」",
    "在回到兄妹那里之前，先看门口的事件：Lily 正在和 Rochester 的管家争吵",
    "回到 Kiki 和 Max 身边，同意带他们去见那个人；从远处看着事情发生，然后和坐在珠宝店附近栏杆上的 Kiki 交谈",
    "Max 打开了珠宝店的门",
  ]),
  S("steps","第十九部分 · 珠宝店","店里的发票把 Mrs. Reed 与 Master Reed 失踪那天联系起来。",[
    "检查右侧的珠宝展示柜，打开前面的柜子，读里面的发票——显示 Mrs. Reed 在 Master Reed 失踪当天有大额消费",
    "检查店铺另一侧的柜子，找到第二块影之碎片，然后回溯并回放事件",
    "退出事件时听到外面有脚步声，Max 和 Kiki 跑开了",
    "出店与店主交谈，说你赶走了小偷",
  ]),
  S("steps","第二十部分 · 送 Max 的包裹","一次营救换来一个人情——以及后面更大的忙。",[
    "下楼梯沿路走，发现 Max 倒在地上——他被抓住了；选择救他，他会给你一个包裹",
    "在之前与 Uncle Smith 喝酒的地方附近找到 Kiki",
    "她说只要能找到三张船票，就带你去沉船码头",
    "兄妹俩以后都有用；现在先回去找 Mrs. Reed",
  ]),
  S("steps","第二十一部分 · 审讯 Mrs. Reed","她的证词有个漏洞——用回溯找出来。",[
    "在府邸俯瞰歌剧院的阳台上找到 Mrs. Reed，与她交谈",
    "她问你喜欢哪种曼陀罗——选择红色",
    "她讲述 Master Reed 失踪当天的事；你可以基于她的证词回溯事件",
    "请她重述事件；当她讲到歌剧院舞台那段时，选择「等等」",
    "Lucas 找到一个漏洞，你获得新线索；让对话自然结束",
  ]),
  S("list","第二十二部分 · 打听诅咒","两段对话，推动「女祭司的诅咒」线。",[
    "与 Reed 的管家交谈，问诅咒的事——他要你先帮他一个忙",
    "答应听他讲：他让你去 Mrs. Reed 的住处，看看她是否不忠",
    "在歌剧院与 Chiffon 谈诅咒；他怀疑 Master Reed 不识字",
    "这条任务线暂时到此为止",
  ]),
  S("steps","第二十三部分 · 搜查 Mrs. Reed 的住处","一扇锁着的门，和一个开锁搭档。",[
    "从后面走楼梯到 Mrs. Reed 的住处；门是锁着的",
    "回去找 Kiki，请她帮你撬锁；说明情况后，她坚持要一起去",
    "用开锁工具进入——Kiki 在你身后关上门，你们俩都被困在了里面",
  ]),
  S("steps","第二十四部分 · Mrs. Reed 的房间：保险箱与地契","房间里藏着本章最大的实物线索。",[
    "进入后，右侧的书房是锁着的——你需要一把钥匙",
    "搜查起居区的柜子：有金币和照片；检查抽屉，找到一张便条并阅读",
    "在卧室找到保险箱——密码在柜子里找到的报纸上：355 年 1 月 1 日；输入 35511",
    "拿走钥匙和便条（一张地契），以及金币",
    "彻底检查衣柜；与 Kiki 交谈时，你找到一张撕碎的发票",
    "关于化妆品，选择「大概不是」以触发世界线偏移，并发现一个可疑的瓶子",
    "衣服碎片给你一条「女祭司的诅咒」故事线的线索",
  ]),
  S("steps","第二十五部分 · 书房：伪造的遗书","本章高潮：重演书写过程，伪造随之崩解。",[
    "用钥匙打开书房，与 Kiki 交谈后开始调查现场",
    "检查厚厚的灰尘层，然后打开台灯",
    "再次检查桌子——什么都没有；影子介入，Lucas 决定把一切重演一遍",
    "按照重演操作：打开台灯、洗笔、蘸墨、开始写字",
    "Lucas 发现太暗没法写；把台灯移到左边，再试一次写字——这次他注意到了影子",
    "选择「他移动了台灯！」并完成线索：「书桌的布局」「一张装饰性的书桌？」「Master Reed 是左撇子吗？」",
    "Lucas 和 Kiki 意识到 Master Reed 不识字，遗书是 Mrs. Reed 帮忙写的",
    "你获得重大线索「伪造的遗书」；准备好后用钥匙从前门离开",
  ]),
]

P2_JA = [
  S("steps","パート10 — 埠頭マーケット到着","第2章は猪籠城で始まります。旧市街は放棄され、今は皆が埠頭周辺で暮らしています。",[
    "猪籠城の賑わう埠頭に到着 — 旧市街は放棄され、今は皆ここに住んでいます",
    "まず埠頭の西側を探索；テーブルの人々の会話を盗み聞きして、世界観や地元情報を集めましょう",
    "漁師の埠頭オーナーが客に料理を作る場面を見る — イベントを最後まで見てから話しかけましょう",
    "オーナーの先にある自動販売機の店で消耗品を補充",
  ]),
  S("steps","パート11 — キキとマックスに出会う","怪しい男を待つ兄妹。このクエストで埠頭の情報が大きく開けます。",[
    "店の西にある木の橋を渡り、兄妹のマックスとキキに出会う — 黒いトレンチコートの男を待っています。手助けを了承",
    "橋を渡り続けて盗み聞き：公正チケットを持っているのに Reed 邸の執事に止められた人々がいる",
    "Reed 邸へ続く階段は警備がいて通れない — 今は戻ろう",
    "引き返して埠頭で釣りをする男に黒いトレンチコートの男を尋ねる — 子供たちは遅れたが確かに誰かが待っていたと言う。シャドウシャードを入手",
    "麻雀台の客に尋ねる：男は旧郡役所で運試しすると言っていた。兄妹が埠頭オーナーと喧嘩した話も聞ける",
    "埠頭オーナーに子供たちのことを尋ねる — 彼らが店でたむろしていたと言う。ポケットを確認するよう提案すると、タバコの箱がなくなっている",
    "店内の自動販売機付近を調べる：ポスターを動かすと壁に覗き穴が見つかる",
    "シャドウと話す — キキとマックスが覗いていたと結論。シャードが揃い、イベントを巻き戻せる",
    "兄妹に何故尾行していたか尋ねる — 男が怪しいと思い、自分たちのものを取り戻したかったと告白。マックスはオーナーへの復讐でタバコしか盗んでいないので信用してよい。このクエストラインはここで一旦ストップ",
  ]),
  S("steps","パート12 — ジュニアの授業ノートを引き受ける","巫女編につながる小さな依頼。",[
    "到着地点に戻り北側を調べる — ドゥドリーという子を叱っている子供がいて、セレスティアに贈り物があると言う",
    "巫女について尋ねてセレスティアのことを知る",
    "その後ジュニアと話す — 授業ノートを巫女に届けるのを手伝ってほしいと頼まれる",
  ]),
  S("steps","パート13 — スミス署長を見つける","北へ来た目的の人物は、実はすぐ埠頭にいました。",[
    "ジュニアの店の先の橋を上がり、埠頭で釣りをする老人を見つける — 釣り竿をもらえます。すぐに釣りも可能",
    "老人の先で上半身裸の男（シフォン）がジュニアの注意をそらして果物を盗もうと頼む — 断ると関係が改善",
    "この老人こそスミス署長。心のこもった再会の後、酒を酌み交わしながら、マスター・リード失踪で街が不安定だと語る",
    "巻き戻してフラッシュバックに入る選択肢が出る — 選びましょう",
  ]),
  S("steps","パート14 — リード村のフラッシュバック","10年前、新人警官としてスミス署長と初めて会った殺人事件。",[
    "10年前へ巻き戻る：新人警官としてリード村の殺人事件捜査に派遣される",
    "スミス署長と話した後、寺院に入り被害者の遺体を調べる — 被害者は抵抗していない",
    "近くの壊れた机を調べる：被害者の死後に争いが起きている",
    "偶像の両側にある2つの部屋を調べて、シャドウシャードを4つ集める",
    "「リード村の推理」を実行し、スミス署長と話す — ルーカスは何かおかしいと感じ、興奮する",
    "現在に戻り、スミス署長との会話を最後まで — 彼は Reed 邸へ向かうが、埠頭から水に落ちてしまう",
    "黒いドレスの女性が彼を助け起こす — 故マスター・リードの妻、ミセス・リード。紹介の会話を進める",
    "2人が去った後、シフォンが話しかけてくる — スミス署長の話をすると関係が良くなり、「巫女の呪い」の物語が始まる",
  ]),
  S("steps","パート15 — Reed 邸に入る","邸の執事が調査への最初の壁。",[
    "店の左の道を行く — スキルチェックに成功しても執事に止められる",
    "シフォンが簡単な方法を教える：魚を担いで供物として捧げること",
    "漁師の埠頭オーナーから25マネーで犠牲の魚を買う — アルバイトやゴミ箱漁で稼げる",
    "執事のところに戻る — シフォンが邸内で騒ぎを起こし、その後オペラ劇場へ移動。聞かれたらシフォンの味方をする",
    "執事に「納品に来た」と伝える — 中に入れてくれるが、先に寺院へ行くよう言われる",
  ]),
  S("steps","パート16 — 巫女の寺院","寺院の用事が、邸に入る切符にもなります。",[
    "左へ行き寺院の正面へ — 机のメモを調べ、近くで煙草を吸う2人に話しかける — もっと強く叩くよう言われる",
    "「ドアを叩く」を選んで中へ入り、祭壇の巫女と話す — 魚を置く",
    "供物を動かすよう頼まれる — すべてのオブジェクトに触れてカットシーンを発生させる",
    "カットシーン後、巫女の無事を尋ね、授業ノートのことを話す",
    "ジュニアを寺院へ連れてくるよう頼まれる — 承諾して退出。寺院近くの階段が使えるようになる",
    "ジュニアのボートに戻って話し、寺院まで送り届け、「ゆびきりげんまん」でクエスト完了",
    "外でスキルチェックに成功し「秘密の隠れ家」の手がかりを入手 — 執事が来てジュニアを窃盗で非難。金を払って収める",
  ]),
  S("steps","パート17 — オペラ劇場","劇場は邸の秘密と、隠しコンパートメントを抱えています。",[
    "オペラ劇場へ向かう — シフォンがぶつかった老人に話し、隣の像を調べる — 力があれば埃を拭き取れる",
    "中へ入るとシフォンがまた騒いでいる — 2階のレストラン店主ミスター・コリンズへ果物かごを届けるよう頼まれる",
    "劇場から川へ下りる階段でボートを調べる — 魚をどけると秘密のコンパートメントがあり、マネーと地図を入手。新たな手がかり「秘密のコンパートメント」",
    "近くの橋の下にホームレスの人がいるが、まだ会話オプションなし",
    "執事のいた場所に戻り、エレベーターで2階へ — スミス署長がミセス・リードと話している",
    "スミス署長がマスター・リードの遺書を見せ、地域の権力構造を説明 — シフォンの名前を出さずに果物かごを届ける",
  ]),
  S("steps","パート18 — 黒いトレンチコートの男を探す","キキとマックスの相手は、思ったより近くにいます。",[
    "2階でエレベーター反対側の橋を西へ渡り、クリニックを通って道を進む",
    "道の突き当りで、宝飾店の近くで指輪を巡って言い争うカップル — ホームレスが魚の腹から金の指輪を見つけたと話している",
    "エレベーターで下りる — トレンチコートの男がすぐ隣に立っている。「聞き覚えがある」を選択",
    "兄妹のところへ戻る前に、扉でのイベントを見る：リリーがロチェスターの執事と言い争っている",
    "キキとマックスのところへ戻り、男のところへ連れて行くことを了承 — 遠くから出来事を見て、宝飾店近くの手すりに座るキキと話す",
    "マックスが宝飾店の扉を開ける",
  ]),
  S("steps","パート19 — 宝飾店","中の請求書が、ミセス・リードを失踪当日に結びつけます。",[
    "右側の宝飾品ディスプレイを調べ、前面のキャビネットを開けて中の請求書を読む — マスター・リード失踪当日にミセス・リードが高額購入している",
    "店の反対側のケースを調べて2つ目のシャドウシャードを入手し、巻き戻してイベントを再生",
    "イベントを抜けると足音がして、マックスとキキが走り去る",
    "店の外で店主と話し、泥棒を追い払ったと言う",
  ]),
  S("steps","パート20 — マックスの荷物を届ける","救出が恩義となり、後で大きな助けになります。",[
    "階段を下りて道を進む — マックスが床に倒れている。捕まっている。助けると荷物をくれる",
    "スミス署長と酒を飲んだ場所の近くでキキを見つける",
    "船チケットを3枚見つければ難破埠頭へ連れて行くと申し出る",
    "兄妹は後で活躍する — 今はミセス・リードのところへ戻ろう",
  ]),
  S("steps","パート21 — ミセス・リードへの尋問","彼女の証言には抜け穴がある — 巻き戻して見つけよう。",[
    "オペラ劇場を見下ろす邸のバルコニーでミセス・リードを見つけて話す",
    "好きなチョウセンアサガオを聞かれる — 赤を選ぶ",
    "マスター・リード失踪当日の出来事を語る — 彼女の証言に基づいてイベントを巻き戻せる",
    "事件をもう一度話してもらう — オペラ舞台の部分で「待って」を選択",
    "ルーカスが抜け穴を見つけ、新たな手がかりを得る — 会話を最後まで進める",
  ]),
  S("list","パート22 — 呪いについて尋ねる","「巫女の呪い」編を進める2つの会話。",[
    "Reed の執事に呪いについて尋ねる — 代わりに頼み事を聞いてほしいと言われる",
    "話を聞くことを承諾：ミセス・リードの家を調べて、不貞の証拠がないか確認してほしい",
    "オペラ劇場でシフォンに呪いの話をする — 彼はマスター・リードが文盲だったと疑っている",
    "このクエストラインはここで一旦ストップ",
  ]),
  S("steps","パート23 — ミセス・リードの家を調べる","鍵のかかった扉と、鍵開けの相棒。",[
    "裏の階段でミセス・リードの家へ — 扉は鍵がかかっている",
    "キキのところへ戻り鍵開けを頼む — 事情を話すと、彼女は一緒に行くと主張する",
    "鍵開けツールで中へ — キキが後ろで扉を閉め、2人とも閉じ込められる",
  ]),
  S("steps","パート24 — ミセス・リードの部屋：金庫と土地証書","この部屋に章最大の物的証拠が隠されています。",[
    "入ると右側の書斎は施錠されている — 鍵が必要",
    "リビングのキャビネットを調べる：マネーと写真。引き出しのメモを読む",
    "寝室で金庫を見つける — コードはキャビネットにあった新聞に載っている：355年1月1日。35511を入力",
    "鍵とメモ（土地証書）、そしてマネーを入手",
    "ワードローブを徹底的に調べる — キキと話すと、破れた請求書を見つける",
    "化粧品について「おそらく違う」を選ぶとワールドラインシフトが起き、怪しい瓶が見つかる",
    "衣服の切れ端から「巫女の呪い」編の手がかりを得る",
  ]),
  S("steps","パート25 — 書斎：偽造された遺書","章のクライマックス — 執筆を再現すると、偽造が崩れます。",[
    "鍵で書斎を開け、キキと話してから現場を調べる",
    "厚いほこりの層を調べ、テーブルランプを点ける",
    "もう一度机を調べる — 何もない。シャドウが介入し、ルーカスはすべてを再現することにする",
    "再現に従う：デスクランプを点け、筆を洗い、インクに浸し、書き始める",
    "ルーカスは暗すぎて書けないと気づく — デスクランプを左に動かし、もう一度書く — 今度は影に気づく",
    "「彼がデスクランプを動かした！」を選び、手がかりを完成させる：机のレイアウト、装飾的な机？、マスター・リードは左利きか？",
    "ルーカスとキキは、マスター・リードが文盲で、ミセス・リードが遺書を書くのを手伝ったと気づく",
    "重大な手がかり「偽造された遺書」を入手 — 準備ができたら鍵で正面玄関から出る",
  ]),
]

P2_KO = [
  S("steps","파트 10 — 부두 시장 도착","2장은 돼지우리 성곽 도시에서 시작합니다. 구시가지가 버려져 이제 모두 부두 근처에 삽니다.",[
    "돼지우리 성곽 도시의 북적이는 부두에 도착 — 구시가지는 버려졌고 지금은 모두 이곳에 삽니다",
    "먼저 부두 서쪽을 탐색하세요. 테이블 사람들의 대화를 엿들어 세계관과 지역 정보를 얻을 수 있습니다",
    "어부 부두 주인이 손님에게 요리를 만드는 모습을 보세요 — 이벤트를 끝까지 보고 나서 대화하세요",
    "주인 옆 자판기 가게에서 소모품을 챙기세요",
  ]),
  S("steps","파트 11 — 키키와 맥스 만나기","수상한 남자를 기다리는 남매. 이 퀘스트로 부두의 많은 내용이 열립니다.",[
    "가게 서쪽의 나무 다리를 건너 맥스와 키키 남매를 만납니다 — 검은 트렌치코트 남자를 기다리고 있습니다. 도와주겠다고 하세요",
    "다리를 건너며 엿듣기: 공정 티켓을 가졌는데도 리드 저택 집사에게 막힌 사람들이 있습니다",
    "리드 저택으로 가는 계단은 경비가 막고 있어 아직 못 갑니다 — 나중에 오세요",
    "돌아와 부두에서 낚시하는 남자에게 검은 트렌치코트 남자를 물어보세요 — 아이들이 늦었지만 분명 누군가 기다리고 있었다고 합니다. 섀도우 샤드를 얻습니다",
    "마작 테이블 사람들에게 물어보세요: 그 남자는 옛 군청에서 운을 시험해 보겠다고 했습니다. 남매가 부두 주인과 싸운 일도 들을 수 있습니다",
    "부두 주인에게 아이들에 대해 물어보세요 — 가게에서 어슬렁거렸다고 합니다. 주머니를 확인해 보라고 제안하면 담배가 사라져 있습니다",
    "가게 안 자판기 근처를 조사하세요 — 포스터를 옮기면 벽에 몰래 보는 구멍이 드러납니다",
    "섀도우와 대화 — 맥스와 키키가 몰래 보았다는 결론을 얻습니다. 샤드가 모여 이벤트를 되감을 수 있습니다",
    "남매에게 왜 따라다녔는지 물어보세요 — 남자가 수상해 보여 자기 것들을 되찾고 싶었다고 고백합니다. 맥스는 부두 주인에 대한 복수로 담배만 훔쳤으니 믿어도 됩니다 — 퀘스트라인은 여기서 일단 멈춥니다",
  ]),
  S("steps","파트 12 — 주니어의 수업 노트 받기","여사제 이야기를 준비하는 작은 심부름.",[
    "도착 지점으로 돌아가 북쪽을 확인하세요 — 두들리라는 아이를 꾸짖는 아이가 있고, 셀레스티아에게 줄 선물이 있다고 합니다",
    "여사제에 대해 물어 셀레스티아를 알아보세요",
    "그 후 주니어와 대화 — 수업 노트를 여사제에게 전해 달라고 설득합니다",
  ]),
  S("steps","파트 13 — 스미스 서장 찾기","북쪽으로 온 목적이었던 사람, 사실 부두에 있었습니다.",[
    "주니어 가게 옆 다리를 올라가 부두에서 낚시하는 노인을 찾으세요 — 낚싯대를 줍니다. 바로 낚시할 수 있습니다",
    "노인 너머에서 상의를 벗은 남자(시퐁)가 주니어의 주의를 돌려 과일을 훔치자고 부탁합니다 — 거절하면 관계가 좋아집니다",
    "이 노인이 스미스 서장입니다 — 감동적인 재회 후 술잔을 나누며, 마스터 리드의 실종으로 도시가 불안하다고 설명합니다",
    "회상으로 되감는 선택지가 나옵니다 — 선택하세요",
  ]),
  S("steps","파트 14 — 리드 마을 회상","10년 전, 신입 경찰로 스미스 서장을 처음 만난 살인 사건.",[
    "10년 전으로 되감기: 신입 경찰로 리드 마을 살인 사건 수사에 파견됩니다",
    "스미스 서장과 대화 후 사원에 들어가 피해자 시신을 조사하세요 — 피해자는 저항하지 않았습니다",
    "근처의 부서진 탁자를 조사하세요: 피해자가 죽은 뒤 싸움이 벌어졌습니다",
    "우상 양쪽의 두 방을 조사해 섀도우 샤드 4개를 모으세요",
    "'리드 마을 추리'를 실행하고 스미스 서장과 대화하세요 — 루카스는 뭔가 이상하다고 느끼며 흥분합니다",
    "현재로 돌아와 스미스 서장과 대화를 마치세요 — 그는 리드 저택으로 가다가 부두에서 물에 빠집니다",
    "검은 드레스의 여성이 그를 일으켜 세웁니다 — 고(故) 마스터 리드의 아내, 리드 부인입니다. 소개 대화를 진행하세요",
    "그들이 떠난 뒤 시퐁이 말을 겁니다 — 스미스 서장 이야기를 해 주면 관계가 좋아지고 '여사제의 저주' 스토리가 시작됩니다",
  ]),
  S("steps","파트 15 — 리드 저택 들어가기","저택 집사가 조사 앞의 첫 번째 벽입니다.",[
    "가게 왼쪽 길로 가세요 — 스킬 체크에 성공해도 리드 집사가 막습니다",
    "시퐁이 쉬운 방법을 알려줍니다: 물고기를 들고 제물로 바치는 것입니다",
    "어부 부두 주인에게서 25머니로 제물용 물고기를 사세요 — 아르바이트나 쓰레기통을 뒤져 돈을 모을 수 있습니다",
    "집사에게 돌아가세요 — 시퐁이 저택 안에서 소란을 피우다 오페라 극장으로 갑니다. 물어보면 시퐁 편을 들어주세요",
    "집사에게 공물을 바치러 왔다고 말하세요 — 들어가게 해 주지만 먼저 사원에 가라고 합니다",
  ]),
  S("steps","파트 16 — 여사제 사원","사원 심부름이 저택 입장권이 됩니다.",[
    "왼쪽으로 가 사원 앞에 도착 — 책상의 쪽지를 조사하고 근처에서 담배 피우는 두 사람과 대화하세요 — 더 세게 두드리라고 합니다",
    "'문을 두드린다'를 선택해 들어가 제단의 여사제와 대화하고 물고기를 내려놓으세요",
    "제단 위 제물을 옮기라고 합니다 — 모든 물건과 상호작용하면 컷신이 재생됩니다",
    "컷신 후 여사제의 안부를 묻고 수업 노트 이야기를 꺼내세요",
    "주니어를 사원으로 데려오라고 합니다 — 승낙하고 나가면 사원 근처 계단을 쓸 수 있습니다",
    "주니어의 배로 돌아가 대화하고, 그를 사원으로 데려간 뒤 새끼손가락 약속으로 퀘스트를 완료하세요",
    "밖에서 스킬 체크를 통과해 '비밀 은신처' 단서를 얻으세요 — 집사가 와서 주니어를 도둑으로 고발합니다. 돈을 주고 수습하세요",
  ]),
  S("steps","파트 17 — 오페라 극장","극장은 저택의 비밀과 숨은 칸을 품고 있습니다.",[
    "오페라 극장으로 가세요 — 시퐁이 부딪힌 노인에게 말을 걸고 옆의 동상을 조사하세요 — 힘이 있다면 먼지를 닦아낼 수 있습니다",
    "안으로 들어가면 시퐁이 또 소란을 피우고 있습니다 — 2층 식당 주인 콜린스 씨에게 과일 바구니를 배달해 달라고 합니다",
    "극장에서 강가로 내려가는 계단으로 배를 조사하세요 — 물고기를 치우면 숨은 칸이 나오고 돈과 지도를 얻습니다. 새 단서 '비밀 칸'",
    "근처 다리 아래에 노숙자가 있지만 아직 대화 옵션이 없습니다",
    "집사가 있던 곳으로 돌아가 엘리베이터로 2층에 오르세요 — 스미스 서장이 리드 부인과 이야기하고 있습니다",
    "스미스 서장이 마스터 리드의 유서를 보여주고 지역 권력 구조를 설명합니다 — 시퐁의 이름을 언급하지 않고 과일 바구니를 전하세요",
  ]),
  S("steps","파트 18 — 검은 트렌치코트 남자 찾기","키키와 맥스가 찾던 남자, 예상보다 가까이 있습니다.",[
    "2층에서 엘리베이터 맞은편 다리를 타고 서쪽으로, 진료소를 지나 길을 따라가세요",
    "길 끝에서 보석 가게 근처에서 반지를 두고 다투는 커플 — 노숙자가 물고기 배 속에서 금반지를 찾았다고 말합니다",
    "엘리베이터를 타고 내려가세요 — 트렌치코트 남자가 바로 옆에 서 있습니다. '익숙한 소리'를 선택하세요",
    "남매에게 돌아가기 전에 문 앞 이벤트를 보세요: 릴리가 로체스터 집사와 말다툼하고 있습니다",
    "키키와 맥스에게 돌아가 그 남자를 만나게 해 주겠다고 하세요 — 멀리서 상황을 지켜본 뒤 보석 가게 근처 난간에 앉은 키키와 대화하세요",
    "맥스가 보석 가게 문을 엽니다",
  ]),
  S("steps","파트 19 — 보석 가게","안의 청구서가 리드 부인을 실종 당일과 연결합니다.",[
    "오른쪽 보석 진열장을 조사하고, 앞 캐비닛을 열어 안의 청구서를 읽으세요 — 마스터 리드가 사라진 날 리드 부인이 큰 구매를 했음을 보여줍니다",
    "가게 반대편 케이스를 조사해 두 번째 섀도우 샤드를 찾고, 되감기로 이벤트를 재생하세요",
    "이벤트를 나오면 바깥에서 발소리가 들리고 맥스와 키키가 달아납니다",
    "가게 밖에서 주인과 대화하고 도둑을 쫓아냈다고 말하세요",
  ]),
  S("steps","파트 20 — 맥스의 소포 배달","구출이 호의가 되고, 나중에 더 큰 도움을 줍니다.",[
    "계단을 내려가 길을 따라가세요 — 맥스가 바닥에 쓰러져 있습니다. 붙잡혔습니다. 구해 주면 소포를 줍니다",
    "스미스 서장과 술을 나눈 곳 근처에서 키키를 찾으세요",
    "배 티켓 3장을 찾으면 난파선 부두로 데려가 주겠다고 합니다",
    "남매는 나중에 역할이 있습니다 — 지금은 리드 부인에게로 돌아가세요",
  ]),
  S("steps","파트 21 — 리드 부인 심문","그녀의 증언에는 허점이 있습니다 — 되감기로 찾아내세요.",[
    "오페라 극장이 내려다보이는 저택 발코니에서 리드 부인을 찾아 대화하세요",
    "어떤 다투라를 좋아하는지 묻습니다 — 빨간색을 선택하세요",
    "마스터 리드가 사라진 날의 일을 설명합니다 — 그녀의 증언을 바탕으로 사건을 되감을 수 있습니다",
    "사건을 다시 말해 달라고 하세요 — 오페라 무대 부분에서 '잠깐'을 선택하세요",
    "루카스가 허점을 찾아내고 새 단서를 얻습니다 — 대화를 끝까지 진행하세요",
  ]),
  S("list","파트 22 — 저주에 대해 묻기","'여사제의 저주' 이야기를 진행하는 두 대화.",[
    "리드 집사에게 저주에 대해 물어보세요 — 대신 부탁 하나를 들어달라고 합니다",
    "말을 들어주겠다고 하세요: 리드 부인의 집을 조사해 불륜 증거가 없는지 확인해 달라고 합니다",
    "오페라 극장에서 시퐁에게 저주 이야기를 하세요 — 그는 마스터 리드가 글을 몰랐다고 의심합니다",
    "퀘스트라인은 여기서 일단 멈춥니다",
  ]),
  S("steps","파트 23 — 리드 부인의 집 조사","잠긴 문과, 문따기 파트너.",[
    "뒤쪽 계단으로 리드 부인의 집에 가세요 — 문이 잠겨 있습니다",
    "키키에게 돌아가 문을 따 달라고 부탁하세요 — 상황을 설명하면 그녀가 따라가겠다고 우깁니다",
    "락픽 도구로 들어가세요 — 키키가 뒤에서 문을 닫아 둘 다 갇힙니다",
  ]),
  S("steps","파트 24 — 리드 부인의 방: 금고와 토지 증서","이 방에 장의 가장 큰 물질적 단서가 숨어 있습니다.",[
    "들어가면 오른쪽 서재가 잠겨 있습니다 — 열쇠가 필요합니다",
    "거실 캐비닛을 조사하세요: 돈과 사진이 있습니다. 서랍에서 쪽지를 찾아 읽으세요",
    "침실에서 금고를 찾으세요 — 비밀번호는 캐비닛에서 찾은 신문에 있습니다: 355년 1월 1일. 35511을 입력하세요",
    "열쇠와 쪽지(토지 증서), 그리고 돈을 챙기세요",
    "옷장을 철저히 조사하세요 — 키키와 대화하며 찢어진 청구서를 찾습니다",
    "화장품에 대해 '아마 아닐 거야'를 선택하면 월드라인 시프트가 일어나 수상한 병을 찾습니다",
    "옷 조각에서 '여사제의 저주' 이야기의 단서를 얻습니다",
  ]),
  S("steps","파트 25 — 서재: 위조된 유서","장의 클라이맥스 — 필기를 재현하면 위조가 무너집니다.",[
    "열쇠로 서재를 열고 키키와 대화한 뒤 현장을 조사하세요",
    "두꺼운 먼지 층을 조사한 뒤 테이블 램프를 켜세요",
    "탁자를 다시 조사하세요 — 아무것도 없습니다. 섀도우가 개입하고 루카스는 모든 것을 재연하기로 합니다",
    "재연을 따르세요: 책상 램프 켜기, 붓 씻기, 잉크에 담그기, 쓰기 시작",
    "루카스는 너무 어두워 쓸 수 없다는 것을 깨닫습니다 — 책상 램프를 왼쪽으로 옮기고 다시 써 보세요 — 이번에는 그림자를 발견합니다",
    "'그가 책상 램프를 옮겼어!'를 선택하고 단서를 완성하세요: 책상 배치, 장식용 책상?, 마스터 리드는 왼손잡이였나?",
    "루카스와 키키는 마스터 리드가 글을 몰랐고 리드 부인이 유서 쓰는 것을 도왔다는 것을 깨닫습니다",
    "중대한 단서 '위조된 유서'를 얻습니다 — 준비되면 열쇠로 정문을 나가세요",
  ]),
]

P2_TIMELINE_EN = {"type": "timeline", "tag": "FLOW", "heading": "Chapter 2 at a Glance", "body": "The route through the Pig Cage Walled City in one timeline.", "items": [["00:00", "Arrive at the Wharf — the Old City District is abandoned"], ["00:10", "Meet Kiki & Max; chase the man in the Black Trenchcoat thread"], ["00:25", "Find Uncle Smith, share drinks, rewind into the Reed Village flashback"], ["00:40", "Enter Reed Mansion with a Sacrificial Fish as tribute"], ["00:55", "Opera Theater — deliver the Fruit Basket, find the Secret Compartment"], ["01:10", "Interrogate Mrs. Reed and rewind her testimony for the loophole"], ["01:25", "Break into Mrs. Reed's house — safe code 35511, Land Deed, Torn Invoice"], ["01:40", "The Study — reenact the writing; the Suicide Note was forged"]]}

P2_TIMELINE_ZH = {"type": "timeline", "tag": "流程", "heading": "第二章速览", "body": "猪笼城寨的完整路线，一条时间线看完。", "items": [["00:00", "抵达码头——旧城区已废弃"], ["00:10", "遇见 Kiki 与 Max；追查黑衣男人线索"], ["00:25", "找到 Uncle Smith，喝酒后回溯芦苇村闪回"], ["00:40", "带着献祭鱼作为贡品进入 Reed 府邸"], ["00:55", "歌剧院——送果篮，发现秘密隔间"], ["01:10", "审讯 Mrs. Reed，回溯证词找漏洞"], ["01:25", "闯入 Mrs. Reed 住处——保险箱密码 35511、地契、撕碎的发票"], ["01:40", "书房——重演书写；遗书是伪造的"]]}

P2_TIMELINE_JA = {"type": "timeline", "tag": "フロー", "heading": "第2章の流れ", "body": "猪籠城のルートを1本のタイムラインで。", "items": [["00:00", "埠頭に到着 — 旧市街は放棄されている"], ["00:10", "キキとマックスに出会う — 黒いトレンチコートの男を追う"], ["00:25", "スミス署長を見つけ、酒を酌み交わし、リード村の回想へ巻き戻す"], ["00:40", "犠牲の魚を供物として Reed 邸に入る"], ["00:55", "オペラ劇場 — 果物かごを届け、秘密のコンパートメントを見つける"], ["01:10", "ミセス・リードを尋問し、証言を巻き戻して抜け穴を見つける"], ["01:25", "ミセス・リードの家に侵入 — 金庫コード35511、土地証書、破れた請求書"], ["01:40", "書斎 — 執筆を再現。遺書は偽造されていた"]]}

P2_TIMELINE_KO = {"type": "timeline", "tag": "흐름", "heading": "2장 한눈에 보기", "body": "돼지우리 성곽 도시의 루트를 하나의 타임라인으로.", "items": [["00:00", "부두 도착 — 구시가지는 버려져 있음"], ["00:10", "키키와 맥스 만남 — 검은 트렌치코트 남자 추적"], ["00:25", "스미스 서장을 찾아 술잔을 나누고 리드 마을 회상으로 되감기"], ["00:40", "제물용 물고기를 바치고 리드 저택 입장"], ["00:55", "오페라 극장 — 과일 바구니 배달, 비밀 칸 발견"], ["01:10", "리드 부인 심문 — 증언을 되감아 허점 발견"], ["01:25", "리드 부인의 집 침입 — 금고 코드 35511, 토지 증서, 찢어진 청구서"], ["01:40", "서재 — 필기 재현. 유서는 위조되었음"]]}

P2_CHOICES_EN = {"type": "table", "tag": "CHOICES", "heading": "Key Choices in Chapter 2", "body": "The decisions that matter most in the Pig Cage Walled City, based on our playthrough.", "columns": ["Decision", "Effect", "Tip"], "rows": [["Side with Chiffon or refuse his schemes", "Changes your standing with Chiffon and the Priestess's Curse thread", "Siding with him moves the Opera Theater path forward faster"], ["Trust Kiki & Max or report them", "Sets up the siblings' role in later chapters", "Trusting them costs nothing now and pays off later"], ["Pay the butler over Junior's theft", "Keeps the peace in the Wharf vs your wallet", "Paying avoids a bigger public scene"], ["Datura: choose Red", "Mrs. Reed's rewind opens the Opera Stage loophole", "The favorite does not matter — picking 'Wait' at the Opera Stage does"], ["Makeup: choose Probably Not", "Triggers a Worldline Shift and the suspicious bottle", "Always pick it to keep the clue chain alive"], ["Reenact the writing exactly", "Reveals the shadow behind the desk — the forged note", "Follow the lamp order: on, wash brush, dip ink, write, then move the lamp"]]}

P2_CHOICES_ZH = {"type": "table", "tag": "抉择", "heading": "第二章关键抉择", "body": "根据我们的通关记录，猪笼城寨中最重要的选择。", "columns": ["抉择", "影响", "建议"], "rows": [["站在 Chiffon 一边，还是拒绝他的把戏", "改变你与 Chiffon 的关系以及「女祭司的诅咒」线", "站他这边会更快推进歌剧院路线"], ["信任 Kiki 与 Max，还是举报他们", "决定兄妹俩在后面章节的作用", "现在信任他们没有代价，之后会回报"], ["为 Junior 偷窃的事花钱摆平管家", "维持码头和平 vs 花钱", "付钱可以避免更大的公开冲突"], ["曼陀罗：选红色", "Mrs. Reed 的回溯开启歌剧院舞台漏洞", "选哪种花不重要——在歌剧院舞台处选「等等」才重要"], ["化妆品：选「大概不是」", "触发世界线偏移，发现可疑的瓶子", "一直选它，保持线索链不断"], ["严格重演书写过程", "揭示书桌后的影子——伪造的遗书", "按灯的步骤来：开灯、洗笔、蘸墨、写字，再移灯"]]}

P2_CHOICES_JA = {"type": "table", "tag": "選択", "heading": "第2章の重要選択", "body": "プレイ記録に基づく、猪籠城で最も重要な選択。", "columns": ["選択", "影響", "アドバイス"], "rows": [["シフォンの味方をするか、企みを断るか", "シフォンとの関係と「巫女の呪い」編に影響", "味方するとオペラ劇場ルートが早く進む"], ["キキとマックスを信じるか、通報するか", "後の章での兄妹の役割を決める", "今は信じるのが無料で、後で報われる"], ["ジュニアの窃盗で執事に金を払うか", "埠頭の平和 vs 財布", "払えば大きな騒動を避けられる"], ["チョウセンアサガオ：赤を選ぶ", "ミセス・リードの巻き戻しでオペラ舞台の抜け穴が開く", "好みは関係ない — オペラ舞台で「待って」を選ぶのが重要"], ["化粧品：「おそらく違う」を選ぶ", "ワールドラインシフトと怪しい瓶を発見", "常に選んで手がかりの連鎖を保つ"], ["執筆を正確に再現する", "机の後ろの影 — 偽造された遺書を暴く", "ランプの順序：点ける、筆を洗う、インクに浸す、書く、そして動かす"]]}

P2_CHOICES_KO = {"type": "table", "tag": "선택", "heading": "2장의 핵심 선택", "body": "플레이 기록 기준, 돼지우리 성곽 도시에서 가장 중요한 선택.", "columns": ["결정", "효과", "팁"], "rows": [["시퐁 편을 들거나 계획을 거절하기", "시퐁과의 관계와 '여사제의 저주' 이야기에 영향", "편을 들면 오페라 극장 루트가 더 빨리 진행됨"], ["키키와 맥스를 믿거나 신고하기", "남매의 이후 챕터 역할을 결정", "지금 믿는 것은 무료이고 나중에 보답받음"], ["주니어 도둑질에 집사에게 돈 지불", "부두의 평화 vs 지갑", "지불하면 더 큰 공개 소동을 피함"], ["다투라: 빨간색 선택", "리드 부인의 되감기로 오페라 무대 허점 개방", "어떤 꽃을 좋아하는지는 중요하지 않음 — 오페라 무대에서 '잠깐' 선택이 핵심"], ["화장품: '아마 아닐 거야' 선택", "월드라인 시프트와 수상한 병 발견", "항상 선택해 단서 연결을 유지"], ["필기를 정확히 재현하기", "책상 뒤 그림자 — 위조된 유서를 드러냄", "램프 순서: 켜기, 붓 씻기, 잉크 담그기, 쓰기, 그다음 옮기기"]]}
WALKTHROUGH = {
  "sections": { "en": EN + P2_EN, "zh-CN": ZH + P2_ZH, "zh-TW": None, "ja": JA + P2_JA, "ko": KO + P2_KO },
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


