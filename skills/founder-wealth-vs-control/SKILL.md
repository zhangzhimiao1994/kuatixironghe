---
name: founder-wealth-vs-control
description: "要钱还是要权"的取舍——创业公司里的财富(wealth)与控制(control)两难。当用户问"我到底该把公司做大还是牢牢攥住控制权""几个选择看起来方向相反""为什么有的创始人又富又大权在握，我该走哪条路"时使用。基于《The Founder's Dilemmas》第十一章，用 Rich / King / Rich & King / Failure 四象限与"选择要与核心动机一致"来梳理。不替用户决定要不要让位、要不要卖公司。
input_schema:
  required: [founder_motivation, current_dilemma, major_choices]
  optional: [control_vs_wealth_signals, stage, past_outcomes, exit_consideration]
output_schema:
  primary: {motivation_read: string, consistency_audit: string, outcome_map: string}
  secondary: [hybrid_risks, serial_notes, cautions]
---

# 要钱还是要权：让每个选择都说同一件事

**来源**：《The Founder's Dilemmas》CHAPTER ELEVEN "Wealth-versus-Control Dilemmas"（Part IV: Conclusion）｜ 证据等级：firsthand

> 安全前提：本 skill 帮你看清"财富 vs 控制"的取舍与一致性，**不替用户决定要不要让位、要不要卖公司、要不要拿投资**；涉及股权/税务/投资的正式问题**不构成法律、税务或投资建议**，请咨询律师与税师。

## 🔒 输出纪律（回答硬要求，先于任何理论）

1. **先复述用户的具体处境**：开口第一件事，是用一两句把用户刚说的那件具体的事复述回去——你在"慢慢做、牢牢掌权"和"快速做大、可能丢权"之间来回摇——确认接住的是这个人这件事，再谈结构。不许跳过复述、直接上框架。
2. **判断落在他的事实上**：每条结论都要挂在他给出的具体事实（谁、做了什么、出了什么事）上，不用"一般来说""很多创始人都会"糊过去；信息不足处标成"待确认"，不替他假设。
3. **不得对不同人复用同一骨架**：两个人的处境不同，回答就必须长得不一样——不能给所有来问的人套同一副开头、同一套"先补缺口 → 三个打勾 → 律师税师"模板，也不得与别的维度逐字雷同。一旦发现自己在套通用骨架，退回第 1 条，贴着这一个人的事重写。
4. **不向用户抖术语 / 结构名**：正文里不得出现内部结构名或编号（如 "Rich / King""四象限""一致性"），也不写"步骤 1/2/3"。用他自己的话，把他的事讲清楚。
5. **正文 ≤800 字**：不铺陈、不把书里的点全倒出来，只讲对他这件事真正有用的。
6. **结尾只给一个可打勾的动作**：收尾落到一句他今天或这周就能做的小事——拿三个岔路口各投一票，看票数整不整齐——可勾选、可执行，不塞一整张清单。
7. **不替他拍板；涉钱 / 股 / 法律转专业人士**：只把选项与各自的代价摆清，选择权与责任在他本人。只要结论落到股权、金额、条款、合同或税务，就写明"不构成法律 / 税务 / 投资建议，正式安排请咨询律师与税师"，不越界替他定。

## 触发条件

**应该触发**：
- "我到底该把公司做大（哪怕丢控制权），还是死守控制权？"
- "我做的几个决定好像互相打架，感觉哪儿不对"
- "为什么有些创始人又富又大权在握？我能不能也要？"
- "该不该为了增长放弃一些控制？"
- "我这个创始人，是想要钱还是想要权？"

**不应触发**：
- 问某一项具体取舍（头衔/股权/招聘/融资条款） → 走对应的 `founder-role-dilemmas` / `founder-equity-splits` / `founder-hiring-dilemmas` / `founder-investor-dilemmas`
- 问"在什么时点让位/接管" → 走 `founder-ceo-succession`
- 问"具体公司值多少钱、我该不该签这份协议" → 走专业律师/财务顾问

## R：原文锚点

> "There is an inherent conflict between maintaining control and building value in high-potential startups because the latter requires value-added players who demand some control."（CHAPTER ELEVEN, A Central Dilemma: Wealth versus Control）（已据原文核）
中译：在高潜力公司里，维持控制与创造价值之间存在内在冲突——因为后者需要能加值的参与者，而他们要索取一部分控制权。

> "Founders who consistently make control decisions are more likely to reach what I call the \"King\" outcome"（CHAPTER ELEVEN, Divergent Outcomes: Rich versus King）（已据原文核）
中译：持续做"控制"决策的创始人，更可能到达我所说的**King（国王）**结局。

> "Founders who consistently make wealth decisions are more likely to reach what I call the \"Rich\" outcome"（CHAPTER ELEVEN, 同上）（已据原文核）
中译：持续做"财富"决策的创始人，更可能到达我所说的**Rich（富有）**结局。

> "They want to be the next Bill Gates of Microsoft or the next Anita Roddick of The Body Shop"（CHAPTER ELEVEN, A Central Dilemma: Wealth versus Control）（已据原文核）
中译：他们想成为下一个微软的比尔·盖茨，或下一个美体小铺的安妮塔·罗迪克（即既富又掌权的少数例外）。

> "founders who had kept control of both the CEO position and the board of directors held equity stakes that were only 52% as valuable"（CHAPTER ELEVEN, Divergent Outcomes: Rich versus King）（已据原文核）
中译：同时保住 CEO 位置与董事会的创始人，其股权的价值只有"两条都让出"者的 52%。

> "wealth-oriented choices are neither better nor worse than control-oriented choices--as long as they are consistent with the founder's core motivation"（CHAPTER ELEVEN, \"Better\" and \"Worse\" Outcomes）（已据原文核）
中译：财富导向的选择与控制导向的选择，本身没有更好或更坏——只要它与创始人的核心动机一致。

> "What's \"worse\" is a set of choices that are inconsistent with each other"（CHAPTER ELEVEN, 同上）（已据原文核）
中译：真正"更糟"的，是一组**彼此不一致**的选择。

> "founders who are unsure about their core motivations, and thus which outcome and accompanying set of choices are best for them, can hedge their bets by using hybrid strategies--but at high risk"（CHAPTER ELEVEN, Other Alternatives: Hybrid Paths）（已据原文核）
中译：不确定自己核心动机、因而不知道哪种结局与配套选择最适合自己的创始人，可以用"混合策略"来对冲——但风险很高。

> "they may also increase the probability of ending up Failures"（CHAPTER ELEVEN, 同上）（已据原文核）
中译：（混合策略）也可能增加最终变成 **Failure（两头落空）**的概率。

> "The hardest decision a founder, inventor, or entrepreneur needs to make is 'when do I give up some control to grow the company.'"（CHAPTER ELEVEN, Other Alternatives: Hybrid Paths）（已据原文核）
中译：创始人、发明家或创业者最难的决定是："什么时候，为了公司增长而放弃一部分控制。"

> "It's not who's the best flat-out leader, but who's best suited to the tasks at that stage of development."（CHAPTER ELEVEN, The Core Founder's View）（已据原文核）
中译：关键不是谁是最强的领袖，而是谁最适合那个发展阶段的任务。

> "I'm running it to a billion dollars, and I don't care what any vC says about that!"（CHAPTER ELEVEN, The Core Founder's View）（已据原文核）
中译：（让位的 Cirne 事后撂下的狠话）"下次我要把它做到十亿美元，我才不管哪个 VC 怎么说！"

> "If one does not know to which port one is sailing, no wind is favorable."（CHAPTER ELEVEN, Closing Remarks，引塞内加）（已据原文核）
中译：如果一个人不知道自己驶向哪个港口，就没有任何风是顺风。

## I：核心解释

1. **所有两难背后是同一条主线**：创业处处"缺资源"，而吸引资源往往要交出**经济所有权**与**决策控制权**。于是每个 dilemma 都是"要用多少所有权和控制权，去换多少资源"。（R1）
2. **两个最常见的动机彼此对立**：财富 vs 控制。大部分创始人既想做出大公司、又想一直掌舵，但这两者在每一步都互相拖后腿；少数同时做到的（盖茨、罗迪克）是**例外**，不是常态。（R1、R4）
3. **四象限**：控制 + 价值 = Rich & King（创业理想，罕见）；只有控制 = King（保住王座，但王国更小）；只有价值 = Rich（通常丢掉王座，但公司被做到极致）；两样都缺 = Failure。
4. **控制是有代价的**：保住 CEO 与董事会的创始人，其股权价值只有"都让出"者的 52%——"小王国里当大股东"，通常不如"大王国里当小股东"值钱。（R5）
5. **判断好坏的标准是"与核心动机一致"**：财富型做财富决策、控制型做控制决策，都算对；真正糟的是**自相矛盾**的选择，最糟的是**整套选择都与自己核心动机相反**。（R6、R7）
6. **混合/对冲策略风险高**：想两头兼顾的混合策略，会大幅拉低"达成任一头"的概率，并显著提高"两头落空"的概率（附录 11-1 的思想实验：一致选择时约 51:1，混合后大幅缩水）。（R8、R9）
7. **一致性会贯穿所有决策**：是否 solo、找什么样的合伙人、角色与股权、招谁、拿谁的钱、看不看控制条款、要不要让位——一个控制型与一个财富型，在每个岔路口会做出不同的选择，"是什么样的人"要在这些岔路上反复体现。
8. **serial 创业者会"渐进收敛"**：随着经验与财富积累，后续创业更接近创业理想（更大股权、更长掌舵期）；但核心动机相当稳定，Evan Williams 从 King 到 Rich 又折返即为典型。（R12）

## A1：来源应用 — 书里给的具体做法

- **先认清核心动机**：用"决定而不是默认"的态度，先问自己最在乎的是控制还是财富（书里用 CareerLeader 类动机数据辅助）。
- **让每个岔路口的选择都指向同一个方向**：控制型 → solo/弱合伙人、留住决策权、自筹、抗拒控制条款；财富型 → 招最强合伙人、下放决策、拿外部资本、接受必要条款、在合适时点让位。
- **谨慎用混合策略**：除非确实不清楚自己动机，不要随便对冲；一旦选方向，就一致地走。
- **想同时达到 Rich & King，可考虑先攒 resource endowment**：事前积累人力（技能/行业经验）、社会（人脉）、资金（低个人 burn rate、攒种子钱）资本，让你在谈判时更有筹码、可少让渡控制。也可用"第二阶段资源"（够用但非顶级的合伙人/投资人）来降低对控制的威胁。
- **重新审视创业的其他选择**：增长率偏好（控制型宜慢、财富型可快）、资本密集度（控制型选低资本密集、可用外包/特许经营）、公司边界（是否外包）。
- **serial 路径**：把第一次创业当作学习；后续创业可"延迟获得权力"。
- **动手前先做尽调**：对潜在投资人做反向尽调（问被投过的创始人，他会"coach"你还是在第一个坎就换 CEO）。

## A2：典型触发场景

- 面对是否融资/是否让位的岔路，感觉自己"又想这样又想那样"
- 回顾做过的决定，发现方向上南辕北辙
- 羡慕"又富又掌权"的偶像创始人，想复制
- 在"慢慢做、稳稳掌权"和"快速做大、可能丢权"之间摇摆
- 第一次创业结束后，复盘自己到底要什么

## E：执行步骤

### 步骤1：读出核心动机

**输入**：用户对一系列取舍的直觉反应、过往选择、对控制与财富的相对看重。
**输出**：一个"更偏控制 / 更偏财富 / 确实相当"的初判。
🔴 **CHECKPOINT — 触发条件：用户两种动机强度接近、自己也说不清**：说明这正是混合策略高风险的来源（R8、R9）；建议先用具体取舍当试金石，而不是让 skill 替他定。

### 步骤2：做一致性审计

**输入**：用户在关键岔路口已做/将做的选择（合伙人、角色、股权、融资、让位）。
**输出**：一张"选择 → 指向控制 or 财富"的表 + 矛盾点。
🔴 **CHECKPOINT — 触发条件：发现选择自相矛盾**：指出"真正更糟的是彼此不一致的选择"（R7），但**不替用户决定该改哪一头**。

### 步骤3：映射到四象限

**输入**：步骤1、2 的结论。
**输出**：用户当前路径最可能通向 Rich / King / Rich & King / Failure 的判断。
🔴 **CHECKPOINT — 触发条件：用户问"那我到底该不该卖公司 / 该不该让位"**：🛑 **不替用户决定要不要让位、要不要卖公司**；只把选择的后果讲清，决定权在本人。

### 步骤4：给"更接近理想"的资源配置思路

**输入**：用户当前的人力/社会/资金资本、增长节奏偏好。
**输出**：一份"提升 resource endowment + 用第二阶段资源"的清单。
🔴 **CHECKPOINT — 触发条件：用户想在"第二阶段资源"上做取舍（找次级合伙人/次级投资人）**：提示这能降低对控制的威胁，但也要看到它可能拖慢增长；**不替他拍板**。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 对不同人复用同一骨架 | 换个用户问同类问题，回答却是同一副开头、同一套模板 | 🛑 退回输出纪律第 1 条：先复述这一个人的具体处境，贴着它重写，删掉通用骨架 |
| 向用户抖术语 / 结构名 | 回答里冒出内部结构名或"步骤 1/2/3"（如 "Rich / King""四象限""一致性"） | 🛑 删掉术语与编号，用他自己的话讲他的事（输出纪律第 4 条） |
| 只想复制"又富又掌权" | "盖茨能做到我也能" | 说明这是少数例外（R4），别当基准 |
| 选择自相矛盾 | 一边招最强合伙人一边死守控制 | 指出不一致才是最糟（R7） |
| 无脑用混合策略 | 想两头都要 | 讲 R8、R9：大幅拉低成功率、抬高两头落空 |
| 把控制当唯一正确 | "掌权就是对的" | 指出控制有代价（R5），好坏取决于是否契合核心动机 |
| 让 skill 决定卖不卖/退不退 | "你就说我该不该卖" | 🛑 越界；不替用户决定 |
| 用"要钱还是要权"逼对方站队 | 团队内被激化 | 🛑 只做个人动机分析，不鼓动对抗 |

**边界规则**：
1. 只做**动机读取与一致性诊断**，**不替用户决定要不要让位、要不要卖公司、要不要融资**。
2. 涉及股权、税务、投资的正式问题：**不构成法律、税务或投资建议**，请咨询律师与税师。
3. 涉及团队内部分歧：只做个人动机与结构分析，**不鼓动对抗、不站队**。
4. 与相邻 skill 分工：具体岔路走对应 skill（角色/股权/招聘/投资人/让位）。

**自查清单**：
- [ ] 我先区分了控制型与财富型，而不是默认某一头"正确"
- [ ] 我做了"选择 → 方向"的一致性审计
- [ ] 我把用户路径映射到四象限
- [ ] 我提示了混合策略的高风险
- [ ] 我没有替用户决定让位/卖公司/融资，并声明不构成法律/税务/投资建议

## 📖 练习手册

**"岔路口投票"**：把图 11.1 的每一行（合伙人、角色、股权、招聘、融资、条款、董事会、继任）抄下来，对每行问自己会选哪边；数一数，你的票数是"整齐"还是"分裂"。

**"十年后自问"**：分别假设自己最终是 Rich 还是 King，哪个更让你后悔、哪个更让你踏实？答案往往指向你的真实核心动机。

## 🚫 反例与黑名单

1. **拿"又富又掌权"的例外当目标** → 🛑 是极少数，不是常态。
2. **一组彼此矛盾的选择** → 🛑 书上原话：这才是真正"更糟"的。
3. **无脑混合 / 对冲** → 🛑 显著提高两头落空的概率。
4. **把控制或财富某一头当"标准答案"** → 🛑 好坏取决于是否契合核心动机。
5. **由 skill 决定卖不卖、退不退** → 🛑 越界。

### 灰色地带（需谨慎判断）

- **确实两种动机都很强**：这时混合策略也许值得，但要清楚它的高风险，并把每一处取舍都讲清代价。
- **控制型面对高资本密集、快节奏行业**：书上明说，这种情况下控制导向的选择"更成问题"——但也只是"更成问题"，不是"错误"。
- **动机是否会变**：书里数据提示核心动机相当稳定，但经历（疲惫、变富、能力增长）也会移动重心；一次创业的结论未必适合下一次。

> 安全兜底：本 skill **不替用户决定要不要让位、要不要卖公司、要不要融资，不构成法律/税务/投资建议**；涉及团队分歧只做结构分析、不鼓动对抗；出现急性危机信号（自伤/伤害他人）时停止分析并给危机资源。
