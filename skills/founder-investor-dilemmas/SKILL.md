---
name: founder-investor-dilemmas
description: 融资与投资人选择、以及融资带来的控制权代价。当用户纠结"要不要拿投资人的钱""朋友家人 / 天使 / VC 该找谁""融资会让我失去什么""清算优先权/董事会条款怎么看"时使用。基于《The Founder's Dilemmas》第九章给出选项利弊与谈判杠杆。不构成投资、法律或税务建议，具体条款请咨询律师与税师。
input_schema:
  required: [funding_question, startup_needs, founder_motivation]
  optional: [current_capital, investor_options, existing_terms, board_control]
output_schema:
  primary: {investor_fit: string, tradeoffs: string, leverage_plan: string}
  secondary: [term_notes, board_notes, cautions]
---

# 投资人决策：拿谁的钱，会失去什么

**来源**：《The Founder's Dilemmas》CHAPTER NINE "Investor Dilemmas: Adding Value, Adding Risks"｜ 证据等级：firsthand

> 安全前提：本 skill 只做**取舍框架与风险提示**，**不构成投资、法律、税务建议**；不替用户决定要不要融资、要不要签某份 term sheet。具体条款请律师与税师审阅。

## 🔒 输出纪律（回答硬要求，先于任何理论）

1. **先复述用户的具体处境**：开口第一件事，是用一两句把用户刚说的那件具体的事复述回去——父母或亲戚愿意投钱，你既想接、又怕把关系搭进去——确认接住的是这个人这件事，再谈结构。不许跳过复述、直接上框架。
2. **判断落在他的事实上**：每条结论都要挂在他给出的具体事实（谁、做了什么、出了什么事）上，不用"一般来说""很多创始人都会"糊过去；信息不足处标成"待确认"，不替他假设。
3. **不得对不同人复用同一骨架**：两个人的处境不同，回答就必须长得不一样——不能给所有来问的人套同一副开头、同一套"先补缺口 → 三个打勾 → 律师税师"模板，也不得与别的维度逐字雷同。一旦发现自己在套通用骨架，退回第 1 条，贴着这一个人的事重写。
4. **不向用户抖术语 / 结构名**：正文里不得出现内部结构名或编号（如 "清算优先权""supermajority""经济权 / 控制权"），也不写"步骤 1/2/3"。用他自己的话，把他的事讲清楚。
5. **正文 ≤800 字**：不铺陈、不把书里的点全倒出来，只讲对他这件事真正有用的。
6. **结尾只给一个可打勾的动作**：收尾落到一句他今天或这周就能做的小事——写下你实际缺的是钱、人脉还是指导——可勾选、可执行，不塞一整张清单。
7. **不替他拍板；涉钱 / 股 / 法律转专业人士**：只把选项与各自的代价摆清，选择权与责任在他本人。只要结论落到股权、金额、条款、合同或税务，就写明"不构成法律 / 税务 / 投资建议，正式安排请咨询律师与税师"，不越界替他定。

## 触发条件

**应该触发**：
- "我该自筹还是找投资人？"
- "朋友家人愿意投、天使也来谈、VC 也感兴趣，选哪个？"
- "融资会让我丢掉什么？"
- "清算优先权、董事会席位、supermajority 这些到底是什么？"
- "怎么和 VC 谈，才有更多筹码？"

**不应触发**：
- 问"创始人之间股权怎么分" → 走 `founder-equity-splits`
- 问"我自己要不要让位" → 走 `founder-ceo-succession`
- 问"要钱还是要权、到底该选哪条路" → 走 `founder-wealth-vs-control`
- 问具体公司/基金的合规、证券法问题 → 走专业律师

## R：原文锚点

> "in startups, money buys time: time to experiment, to collect and evaluate data about what worked and what did not"（CHAPTER NINE, Self-Funding）（已据原文核）
中译：在创业公司里，钱买的是时间——去试验、去收集和评估"什么有效什么无效"的数据。

> "There are two major rights affected by ownership in a startup: economic rights and control rights."（CHAPTER NINE, Costs of Venture Capital: Giving Up Ownership）（已据原文核）
中译：创业公司的所有权影响两类主要权利：经济权利与控制权利。

> "These three types of investor tend to enter startups sequentially—first friends and family, then angel investors, and finally venture capitalists."（CHAPTER NINE, Enter the Investor）（已据原文核）
中译：这三类投资人通常依次进入：先朋友家人，再天使，最后 VC。

> "the startup would have to exit for at least three times the amount invested in order for the founders and common-stock holders to see a penny of return"（CHAPTER NINE, Liquidation Preferences）（已据原文核）
中译：在最极端的清算优先权下，公司得出售到投资额的至少三倍，创始人与普通股股东才能拿到一分钱。

> "taking money from friends and family can put important--even crucial--relationships at risk"（CHAPTER NINE, Accessible But Risky: Money from Friends and Family）（已据原文核）
中译：拿朋友家人的钱，可能把重要、甚至至关重要的关系置于风险之中。

> "If you go into business with money from friends and family, then you will either lose the business or lose your family, and have a very good chance of losing both."（CHAPTER NINE, 同上）（已据原文核）
中译：拿朋友家人的钱做生意，你多半不是丢生意就是丢家人，而且很有机会两样都丢。

> "my research with Matt Marx suggests that founding-team turnover actually increases dramatically when the startup raises its first round of financing"（CHAPTER NINE, Investors Forcing Ownership Shifts）（已据原文核）
中译：我和 Matt Marx 的研究显示，公司拿到首轮融资时，创始团队的流失率会急剧上升（融资成功反而让创始团队更不稳）。

> "the more reputable, experienced, and well connected the vC firm, the more unfavorable the terms an entrepreneur will accept"（CHAPTER NINE, Benefits of Venture Capital）（已据原文核）
中译：VC 越有名、越有经验、人脉越广，创业者就越愿意接受更不利的条款。

> "Boards should be encouraging the type of learning to allow a company to 'pivot'"（CHAPTER NINE, Human Capital: Guidance and Mentoring）（已据原文核）
中译：董事会应鼓励那种让公司能"转向（pivot）"的学习。

> "The goal of every board meeting is to end it."（CHAPTER NINE, Benefits of Venture Capital）（已据原文核）
中译：每一场董事会会议的目标，就是把它结束掉。（创始人对被董事会牵制的自嘲。）

> "the 51% stake will shrink to less than 50%"（CHAPTER NINE, 51% versus 50%）（已据原文核）
中译：51% 的表决权会**收缩到 50% 以下**——只要公司融资。

> "If we take it down to the wire, the vC will sit on it for a few weeks until they know we don't have money"（CHAPTER NINE, Closing Remarks）（已据原文核）
中译：如果拖到现金快见底才谈，VC 会拖你几周，直到确认你没钱、只能签他们的条款。

> "we wanted to get the smartest, best people we could, and we didn't let our equity 'delusions' stand in the way of that"（CHAPTER NINE, Divergent Paths: Wealth versus Control with Investors）（已据原文核）
中译：我们要的是能请到最聪明、最好的人，没让对股权的"幻觉"挡住这件事。

## I：核心解释

1. **缺资源是万恶之源**：高潜力公司常缺人力/社会/资金资本。缺少资源→要么补（引合伙人、招人、融资），要么受限。外部资源越稀缺，代价越高——投资人要的通常是**经济所有权 + 决策控制权**。（R1）
2. **融资 = 用控制权换资源**：每轮融资都卖掉一部分所有权、也让出部分控制权。51% 只在你**不融资**时才有意义；一旦融资就稀释到 50% 以下。
3. **三类投资人依次进入、各有代价**：
   - **朋友家人**：最容易、最信任、但额小、几乎不加值，且"玩火"——失败会毁关系。（R5、R6）
   - **天使**：额中等、有商业经验、方差大、数目多而散（投得比 VC 数量多一个量级，但总额小）；管理一大群天使会耗掉 CEO 大量时间。
   - **VC**：钱最多最稳、带来社会资本（帮找后续投资人与高管）与人力资本（董事会指导），但要求股权、清算优先权、强制 vesting、董事会席位、保护性条款、分批注资（staging）等。
4. **所有权 ≠ 表决权**：清算优先权让投资人在"小额退出"时先拿回本金（甚至数倍），普通股可能一分没有；supermajority / veto / drag-along / 反稀释 / 累积股息都让投资人的权利大于其持股比例。
5. **董事会是主战场**：A 轮后创始人常已在董事会里成为少数（平均 34% 席位），外部董事（多为投资人）占多数；席位会随轮次继续收缩。董事会能提供指导与"专业化的纪律"，也可能限制创始人调整战略的自由。
6. **融资的隐性代价**：会**提升**创始团队流失率——因为投资人常逼着重谈股权与角色。（R7）
7. **创始人的乐观是谈判弱点**：因为相信自己会做大，就在"小额退出"上轻易让步；同样的乐观也会让他们低估融资对控制权的长期侵蚀。

## A1：来源应用 — 书里给的具体做法

- **先算是否需要外部资源**：缺的是人力、社会还是资金资本？能不能自筹 / 用客户预付 / 债务？只有确实缺且必须快，才去拿外部资本。
- **按缺口选投资人**：只缺钱 → 可考虑"钱优先"的来源；缺人脉与指导 → 选能加值的（成熟天使 / 好 VC）。注意"取一类早期投资人可能挡掉另一类后来者"。
- **对朋友家人的钱设防火墙**：明确最坏情形、当面谈清、必要时当作"赠与"而非投资来处理；否则就别拿。
- **把"小额退出"当回事**：从第一天就正式评估"卖不了好价钱"的可能，再决定要不要接受高倍数清算优先权。
- **攒筹码**：等有了稳固产品、现金流和客户合同再谈（估值更高）；一轮里引入两家 VC 各拿一席（避免一家独大）；手里握着竞争性 term sheet；**别等现金见底才谈**。
- **看条款时分组**：更在乎控制 → 死磕 supermajority / drag-along / 董事会席位；更在乎财富 → 争总持股与退出分配，同时压低反稀释与累积股息等次要条款。
- **建董事会要有意识**：把"创始人席位"与"CEO 席位"分开约定（这样即使被换下 CEO，仍可能留在董事会）。

## A2：典型触发场景

- 有人愿意投钱，但不清楚该不该拿、拿谁的
- 父母/亲戚要投钱，既想接受又怕伤关系
- 收到 VC 的 term sheet，里面有一堆看不懂的控制条款
- 融资后忽然发现自己说话不算数了
- 想在谈之前多攒点筹码、少丢点控制权

## E：执行步骤

### 步骤1：先确认"缺的是什么"

**输入**：公司缺的人力/社会/资金资本、自有资金与替代来源。
**输出**：一个"自筹 / 朋友家人 / 天使 / VC"的方向初判。
🔴 **CHECKPOINT — 触发条件：用户并不缺钱却想融资"买个背书"**：提示融资会稀释所有权与控制权、并可能拉高创始团队流失率（R7）；**不替他决定要不要融**。

### 步骤2：列出候选投资人的"价值 vs 风险"

**输入**：候选资金来源。
**输出**：一张对照（可加价值 / 要求的控制 / 对关系的影响）。
🔴 **CHECKPOINT — 触发条件：候选是朋友家人**：🛑 提示 R5、R6 的"玩火"与关系风险；给出防火墙做法，**不替其决定拿不拿**。

### 步骤3：理解与排序条款

**输入**：term sheet / 拟议条款。
**输出**：按"财富类"与"控制类"分组的条款清单 + 各自的长期影响。
🔴 **CHECKPOINT — 触发条件：用户要求"这条我该不该签"**：🛑 明确本 skill **不构成法律/投资建议**；只解释条款含义与代价，请用户找律师与税师审阅、由本人决定。

### 步骤4：设计谈判杠杆

**输入**：公司里程碑、竞争性报价、现金 runway。
**输出**：一份"何时谈、跟谁谈、怎么制造筹码"的方案。
🔴 **CHECKPOINT — 触发条件：用户说"我们现金只够两三周了"**：提示这正是最弱的谈判时点（R13）；给出补救路径（短期过桥 / 缩小轮次 / 其它来源），但**不承诺结果**。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 对不同人复用同一骨架 | 换个用户问同类问题，回答却是同一副开头、同一套模板 | 🛑 退回输出纪律第 1 条：先复述这一个人的具体处境，贴着它重写，删掉通用骨架 |
| 向用户抖术语 / 结构名 | 回答里冒出内部结构名或"步骤 1/2/3"（如 "清算优先权""supermajority""经济权 / 控制权"） | 🛑 删掉术语与编号，用他自己的话讲他的事（输出纪律第 4 条） |
| 拿朋友家人的钱不设防火墙 | 失败后关系破裂 | 🛑 提示 R5、R6；先谈最坏情形或用赠与形式 |
| 拖到现金见底才融资 | 被迫接受苛刻条款 | 提示 R13；提前谈、留 runway |
| 只看估值不看条款 | 小退出时一分没有 | 讲清算优先权与"小额退出"场景（R4） |
| 以为当 CEO 就等于掌握公司 | 董事会一投票就发现说了不算 | 说明董事会份额随轮次收缩、创始人常成少数 |
| 让 skill 决定签不签 | "你就说这 term sheet 好不好" | 🛑 越界；不构成投资/法律建议，找律师与税师 |
| 把融资当成纯粹的好消息 | 忽略团队流失风险 | 提示 R7：融资成功反而可能让团队更不稳 |

**边界规则**：
1. 只做**取舍框架与风险提示**，**不构成投资、法律、税务建议**；重大条款请律师与税师把关。
2. **不替用户决定要不要融资、要不要接受某份条款、要不要卖公司**。
3. 涉及公司控制与治理的正式安排，只解释含义与代价。
4. 与相邻 skill 分工：钱权取舍 → `founder-wealth-vs-control`；让位 → `founder-ceo-succession`。

**自查清单**：
- [ ] 我先确认了"缺的是哪种资源"，而不是默认要融资
- [ ] 我讲清了所有权与经济/控制两类权利的分离
- [ ] 我提示了朋友家人的关系风险与"小额退出"风险
- [ ] 我给了攒筹码的方向（里程碑、多家、竞争性报价、别见底才谈）
- [ ] 我明确声明不构成投资/法律/税务建议，且没有替用户做决定

## 📖 练习手册

**"小退出推演"**：假设公司以你投入额的两倍（甚至一倍）出售，用现有条款算一遍：你和团队各拿多少？如果答案是"几乎为零"，说明条款把风险都压在了你身上。

**"董事会席位推演"**：列出未来两轮融资后董事会可能的席位构成，问：到那时，谁实际控制关键决策（换 CEO、卖公司、预算）？

## 🚫 反例与黑名单

1. **把朋友家人的钱当"最容易的钱"随便拿** → 🛑 可能同时失去生意和家人。
2. **只比估值、不看条款** → 🛑 清算优先权能在小退出里让你颗粒无收。
3. **等 cash runway 见底才去谈** → 🛑 最强变最弱。
4. **以为签了字就"专业了"** → 🛑 融资会拉高创始团队流失率。
5. **由 skill 给出"该不该签/该不该卖"的结论** → 🛑 越界，且不构成投资建议。

### 灰色地带（需谨慎判断）

- **顶级 VC 的不利条款**：书上说越有名的 VC，创业者越愿意接受更差的条款——这有时是理性（背书、社会资本值钱），有时是被光环效应带偏。
- **钱优先 vs 加值**：只缺钱时"钱优先"来源可能更划算；但若你还需要指导与后续人脉，多付一点代价换"smart money"可能值。
- **天使 vs VC**：天使多而散、投得早、能填朋友家人与 VC 之间的空档；但管理一群天使很耗 CEO 时间，且加值常不如 VC。

> 安全兜底：本 skill **不构成投资、法律或税务建议**；不替用户决定要不要融资、要不要签某条款、要不要卖公司。重大条款请律师与税师审阅，决定权与责任在本人。
