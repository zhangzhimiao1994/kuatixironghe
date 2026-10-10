---
name: founder-hiring-dilemmas
description: 创业公司的招聘与解雇取舍。当用户纠结"该招通才还是专才""该招大厂高管还是创业老兵""什么时候该设 CFO/COO/vP""开不掉老朋友怎么办""该不该升级换人"时使用。基于《The Founder's Dilemmas》第八章给出按公司阶段的招/升/换框架。涉及劳动法、解雇程序的正式问题不构成法律建议。
input_schema:
  required: [startup_stage, hiring_question, current_team]
  optional: [role_to_fill, candidate_profile, performance_issue, cash_equity_budget]
output_schema:
  primary: {hire_recommendation: string, timing_notes: string, risk_notes: string}
  secondary: [role_upgrade_plan, comp_structure, cautions]
---

# 招聘与解雇：在对的阶段招对的人、升该升的位、开该开的人

**来源**：《The Founder's Dilemmas》CHAPTER EIGHT "Hiring Dilemmas: The Right Hires at the Right Time"｜ 证据等级：firsthand

> 安全前提：本 skill 给用人框架与风险，**不替用户决定开除谁**；涉及解雇程序、竞业、雇佣合同的正式问题**不构成法律建议**，请咨询律师。

## 🔒 输出纪律（回答硬要求，先于任何理论）

1. **先复述用户的具体处境**：开口第一件事，是用一两句把用户刚说的那件具体的事复述回去——跟你一起打天下的老朋友明显跟不上，团队都在看你怎么处理——确认接住的是这个人这件事，再谈结构。不许跳过复述、直接上框架。
2. **判断落在他的事实上**：每条结论都要挂在他给出的具体事实（谁、做了什么、出了什么事）上，不用"一般来说""很多创始人都会"糊过去；信息不足处标成"待确认"，不替他假设。
3. **不得对不同人复用同一骨架**：两个人的处境不同，回答就必须长得不一样——不能给所有来问的人套同一副开头、同一套"先补缺口 → 三个打勾 → 律师税师"模板，也不得与别的维度逐字雷同。一旦发现自己在套通用骨架，退回第 1 条，贴着这一个人的事重写。
4. **不向用户抖术语 / 结构名**：正文里不得出现内部结构名或编号（如 "蓝图""通才 / 专才""title inflation"），也不写"步骤 1/2/3"。用他自己的话，把他的事讲清楚。
5. **正文 ≤800 字**：不铺陈、不把书里的点全倒出来，只讲对他这件事真正有用的。
6. **结尾只给一个可打勾的动作**：收尾落到一句他今天或这周就能做的小事——写下这个位子 12 个月后需要的核心能力——可勾选、可执行，不塞一整张清单。
7. **不替他拍板；涉钱 / 股 / 法律转专业人士**：只把选项与各自的代价摆清，选择权与责任在他本人。只要结论落到股权、金额、条款、合同或税务，就写明"不构成法律 / 税务 / 投资建议，正式安排请咨询律师与税师"，不越界替他定。

## 触发条件

**应该触发**：
- "公司该招什么人了？通才还是专才？"
- "要不要请个大厂出来的高管？"
- "什么时候该设 CFO / COO / VP 销售？"
- "招错了人 / 朋友跟不上公司，张不开嘴怎么办？"
- "老员工明显 scale 不动了，该不该换？"

**不应触发**：
- 问"联合创始人之间怎么分权/分股" → 走 `founder-role-dilemmas` / `founder-equity-splits`
- 问"要不要拿投资人的钱" → 走 `founder-investor-dilemmas`
- 问"我自己要不要让位" → 走 `founder-ceo-succession`
- 问"员工违法/性骚扰等合规问题" → 走专业法律/HR 渠道

## R：原文锚点

> "only 10.9% of startups deviated from their original blueprint along all three dimensions, and they were 2.3 times as likely to fail as firms that kept to one blueprint"（CHAPTER EIGHT, 开篇，引 SPEC 研究）（已据原文核）
中译：只有 10.9% 的公司在招聘-奖励-控制三个维度上同时偏离了最初"蓝图"，而它们失败的概率是坚持单一蓝图者的 2.3 倍。

> "founder-CEOs are the source of 49% of all hires"（CHAPTER EIGHT, The Founder-CEO's Hires versus the Investors' Hires）（已据原文核）
中译：在所有招聘里，创始人 CEO 是 49% 的用人来源。

> "high-potential startups that relied relatively heavily on the founders' personal networks received valuations that were 37% higher"（CHAPTER EIGHT, 同上）（已据原文核）
中译：较多依赖创始人人脉招人的高潜力公司，估值比几乎不动用人脉的高出 37%。

> "Investors are a source of 26% of all CFO hires, a far higher percentage than for any other non-CEO position."（CHAPTER EIGHT, 同上）（已据原文核）
中译：投资人是一半以上 CFO 招聘之外的常见来源——占总 CFO 招聘的 26%，远高于其他非 CEO 岗位。

> "If a startup has a COO, it's a red flag: Either the COO doesn't belong or the CEO doesn't."（CHAPTER EIGHT, When to Create New Positions?）（已据原文核）
中译：如果一家创业公司有 COO，往往是个危险信号——要么这个 COO 不该在，要么这个 CEO 不该在。

> "Early in the company's life, you don't have the ability to give them more salary, but titles are cheap to give out so you use that to make the package more attractive."（CHAPTER EIGHT, When Should I Upgrade Existing Positions?）（已据原文核）
中译：公司早期给不起更高薪水，但头衔很便宜，于是你就用头衔把 offer 撑得好看些。

> "It's like if you have a crank, he can crank, but he can't actually build the crank. Building something from nothing requires a different skill set."（CHAPTER EIGHT, Small-Company versus Big-Company Backgrounds）（已据原文核）
中译：就像有个摇柄他能摇，但他造不出摇柄。从零造东西，需要的是另一套本事。

> "When you hire senior people in larger companies, they're successful because they can manage a team. They won't necessarily be effective on an individual level."（CHAPTER EIGHT, 同上）（已据原文核）
中译：大公司里的资深人士成功，是因为他们会管团队；到了个人单兵作战的层面，未必管用。

> "In the end, five of our original twenty moved into radically different positions at some point."（CHAPTER EIGHT, Generalists versus Specialists）（已据原文核）
中译：到头来，最早那二十个人里有五个后来转到了完全不同的岗位。

> "we didn't use him as a defensive back and he ended up being only the third-best wide receiver"（CHAPTER EIGHT, 同上）（已据原文核）
中译：我们没把他当防守后卫用，结果他只能当第三好的外接手（招来的通才没用对位置，价值大打折扣）。

> "The worst problem with a bad hire is that they get into the organization, they become friends with people, and then it's, 'Why are you firing my friend?'"（CHAPTER EIGHT, Closing Remarks）（已据原文核）
中译：错招最糟的地方是：这个人进了公司、交了朋友，然后你就得面对"你为什么要开我朋友？"

> "A salesperson will leave if he's not doing a good job and therefore not getting paid what he wants."（CHAPTER EIGHT, Closing Remarks）（已据原文核）
中译：销售如果做得不好、拿不到想要的收入，自己就会走。

## I：核心解释

1. **有"蓝图"就别乱换**：招聘-奖励-控制三者构成一套"蓝图"（如 commitment / bureaucracy / star 等）；坚持一套蓝图的公司活得好，三处同时换掉的公司失败率是 2.3 倍。换蓝图要极其谨慎。（R1）
2. **人脉是主要来源，也带来风险**：创始人 CEO 是 49% 的用人来源，靠人脉招人的公司估值更高（37%）——但"靠熟人"也带来"玩火"风险：朋友/家人跟不上时张不开嘴，甚至变成"没人能动"。（R2、R3、R11）
3. **投资人会塞人，尤其 CFO**：投资人占 CFO 招聘的 26%，远高于其他岗位；这类人可能更对齐投资人而非 CEO（被戏称"投资人的眼线"）。CEO 自己人脉里没有合适 CFO 时，这层价值也可能有用。
4. **按阶段设岗，别乱设**：早期只该设真正需要的岗。CFO 是后期主要新增（成熟公司 70% 有非创始 CFO）；COO 常是"危险信号"；VP 销售往往是最早的 VP 岗。结构性杠杆（每个高管带几个兵）从约 2.5 升到 9。
5. **通才 vs 专才看阶段**：早期要通才（option value 高，能随时改派）；核心不确定性解决后要专才（深度更值钱）。同一家公司不同职能的转变节奏还不一样。
6. **大厂背景有两面**：能带流程与体系，但常常"会摇柄不会造摇柄"、习惯成熟公司的做法，落到早期公司可能水土不服。
7. **升级换人很痛但常必须**：规模一大，很多早期的人（含创始人）scale 不动。"一发现某人不行就得动"是一种做法；但小团队冲击大，且早期发的 C 头衔会挡路（title inflation）。
8. **让奖励自动"筛人"**：销售配高提成，做不好的人会自己走（"hire fast, fire fast"）；开发配稳定工资，硬套销售那套会适得其反。奖励结构要和角色对齐。

## A1：来源应用 — 书里给的具体做法

- **先定蓝图再招人**：明确你是 commitment（讲文化契合与热爱，低薪）还是 bureaucracy（讲经验与技能，高薪、正式流程）等蓝图，别一边讲热爱一边招职业经理人。
- **按优先级用人脉，但留出外部通道**：早期多用创始人网络（提估值、增凝聚）；随公司变大，逐步引入投资人网络、猎头与弱关系，避免"熟人圈里没人可招"。
- **设岗有先后**：CFO 留到财务复杂时；COO 慎设；VP 销售常是第一个 VP；HR 反而常常外包或用初级人做（FeedBurner 的教训）。
- **按阶段切换通才/专才**：早期招能一岗多用的通才；技术等职能先专精，业务/财务/运营可更久保持"多面手"。
- **把"换人"纳入预期**：招人时就说明"未来上面可能会再加一层"，降低日后升级的阻力。
- **用奖励筛人**：对销售设高变动薪酬，对工程设稳定薪酬，让奖励与角色天然对齐。
- **发钱之前先想清楚现金-股权跷跷板**：给高薪就对应低股权，反之亦然；让候选人自己选位置，并让他知道后果。

## A2：典型触发场景

- 公司刚起盘，纠结要不要请个"大厂 PM/总监"
- 招了个销售 VP，来了三个月没动静
- 一起打天下的老朋友明显跟不上，团队都在看你怎么处理
- 融资在即，投资人说"该有位 CFO 了"
- 二十人规模，还在人人什么都干，想开始分工

## E：执行步骤

### 步骤1：定位公司与职能所处阶段

**输入**：轮次/规模、该职能的成熟度、当前蓝图。
**输出**：一个"现处阶段 → 该招通才还是专才 / 该不该设这个岗"的判断。
🔴 **CHECKPOINT — 触发条件：用户想早期就请大厂高管、设 COO**：提示"会摇柄不会造摇柄"与 COO 危险信号（R5、R7）；若仍要做，说明要多备支持与退路。

### 步骤2：定招聘来源与角色

**输入**：要填的岗、可用人脉、是否已引入投资人。
**输出**：招聘来源方案（创始人网络 / 投资人 / 弱关系）+ 角色与预期职责。
🔴 **CHECKPOINT — 触发条件：候选人来自创始人/合伙人的朋友或家人**：🛑 提示"玩火"风险（R3、R11）——日后不开嘴、无人能动；建议先设好退出机制。

### 步骤3：定奖励结构

**输入**：岗位类型、公司现金与期权预算。
**输出**：现金/股权/奖金的结构建议（销售偏变动、工程偏稳定）。
🔴 **CHECKPOINT — 触发条件：用户问"要不要开掉某个绩效不达标的人"**：只给"何时该升级/何时奖励会自然筛人"的原则与视角，**不替用户决定开除谁**；正式解雇程序咨询律师。

### 步骤4：规划"升级"路径

**输入**：未来 12–24 个月该岗的能力要求变化。
**输出**：一份"这个位子将来可能需要谁/需要加一层"的预案。
🔴 **CHECKPOINT — 触发条件：用户已给早期员工发了虚高头衔、现在想改**：提示 title inflation 会挡路（R6）；给出"提前设定期望 + 分层过渡"的思路，不替其决定。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 对不同人复用同一骨架 | 换个用户问同类问题，回答却是同一副开头、同一套模板 | 🛑 退回输出纪律第 1 条：先复述这一个人的具体处境，贴着它重写，删掉通用骨架 |
| 向用户抖术语 / 结构名 | 回答里冒出内部结构名或"步骤 1/2/3"（如 "蓝图""通才 / 专才""title inflation"） | 🛑 删掉术语与编号，用他自己的话讲他的事（输出纪律第 4 条） |
| 早期请大厂高管 | 三个月"坐着不动" | 提示"不会造摇柄"（R7）；按阶段用人 |
| 乱设 COO | 职责重叠、CEO 被架空或多余 | 提示危险信号（R5），先看是否真需要 |
| 招了朋友/家人 | 干不好也开不掉 | 提示玩火风险（R3、R11），先设退出机制 |
| 头衔通胀 | 早期 VP、后期换不动 | 提前设定期望，说明将来会加层 |
| 通才用错位置 | "第三好的外接手" | 按阶段切换通才/专才（R9、R10） |
| 让 skill 决定开除谁 | "你直接说开不开他" | 🛑 越界；给原则与视角，决定权在人，程序找律师 |

**边界规则**：
1. 给"何时招/招什么样/何时升级"的**框架**，不替用户决定具体 hired/fired。
2. 涉及解雇、竞业、雇佣合同的正式问题：**不构成法律建议**，请咨询律师。
3. 团队冲突（含老朋友跟不上）只做机制诊断，**不鼓动对抗、不站队**。
4. 与相邻 skill 分工：联合创始人层面 → `founder-role-dilemmas`/`founder-equity-splits`；自己让位 → `founder-ceo-succession`。

**自查清单**：
- [ ] 我按公司/职能所处阶段给了建议（不是一刀切）
- [ ] 我区分了通才/专才、大厂/创业老兵
- [ ] 我提示了熟人招聘的"玩火"风险
- [ ] 我给了奖励与角色对齐的方向
- [ ] 我没有替用户决定开除谁，并提示了解雇程序要找律师

## 📖 练习手册

**"阶段-岗位对照"**：列出你未来 12 个月要新增的岗，给每个岗标"现在必须有 / 可以等 / 其实不需要"；对"其实不需要"的岗问：是不是只是因为给不起薪水才想用头衔凑？

**"奖励自筛演练"**：对销售、工程、运营三个岗，各设计一套现金/股权/奖金结构，问：做得不好的人，在这套结构下会不会自己走？

## 🚫 反例与黑名单

1. **早期就堆大厂高管** → 🛑 常常"会摇柄不会造摇柄"。
2. **为了抢人发虚高头衔** → 🛑 后期升级换人时挡路。
3. **把朋友/家人招进来却不设退出机制** → 🛑 变成"没人能动"。
4. **给工程套销售式高提成（或反之）** → 🛑 奖励与角色错配。
5. **由 skill 判定开除谁** → 🛑 越界；程序找律师。

### 灰色地带（需谨慎判断）

- **COO**：话说得很绝对（危险信号），但确实有公司需要 COO 来补 CEO 的运营短板；关键是别为"给某人一个头衔"而设。
- **投资人推荐的 CFO**：可能更对齐投资人，但若你手上确实没有合适 CFO，这层来源有时是有价值的。
- **"rising star" vs "rock star"**：年轻人便宜但情绪化、耗管理时间；老手稳但贵、可能水土不服。没有绝对答案，看阶段与职能。

> 安全兜底：涉及解雇、竞业、雇佣合同的正式问题，**不构成法律建议**，请咨询律师；只有给分类型框架，不替用户决定 hire/fire，也不鼓动团队对抗。
