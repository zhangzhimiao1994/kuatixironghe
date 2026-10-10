---
name: founder-role-dilemmas
description: 创业团队的角色、头衔与决策权分配。当用户纠结"谁当 CEO / 给谁什么头衔""两个人要不要分权""平等决策还是一个人拍板""要不要让合伙人进董事会"时使用。给出头衔、重叠角色 vs 分工、平等 vs 层级、董事会席位的取舍（《The Founder's Dilemmas》第五章）。不替用户决定谁当 CEO；治理与股权安排不构成法律建议。
input_schema:
  required: [team_setup, role_question, decision_style]
  optional: [idea_owner, commitment_levels, prior_relationship, board_seats]
output_schema:
  primary: {title_plan: string, decision_structure: string, risk_notes: string}
  secondary: [division_of_labor, board_advice, cautions]
---

# 角色与决策权：谁拿头衔、谁拍板

**来源**：《The Founder's Dilemmas》CHAPTER FIVE "Role Dilemmas: Positions and Decision Making"｜ 证据等级：firsthand

> 安全前提：本 skill 帮你看清角色与决策结构的取舍，**不替用户决定谁当 CEO / 谁让位**；涉及股权、董事会条款的正式安排**不构成法律、税务或投资建议**，请咨询律师与税师。

## 🔒 输出纪律（回答硬要求，先于任何理论）

1. **先复述用户的具体处境**：开口第一件事，是用一两句把用户刚说的那件具体的事复述回去——你和合伙人两个人都想要 CEO 这个位子，一直用"我们一起决定"拖着——确认接住的是这个人这件事，再谈结构。不许跳过复述、直接上框架。
2. **判断落在他的事实上**：每条结论都要挂在他给出的具体事实（谁、做了什么、出了什么事）上，不用"一般来说""很多创始人都会"糊过去；信息不足处标成"待确认"，不替他假设。
3. **不得对不同人复用同一骨架**：两个人的处境不同，回答就必须长得不一样——不能给所有来问的人套同一副开头、同一套"先补缺口 → 三个打勾 → 律师税师"模板，也不得与别的维度逐字雷同。一旦发现自己在套通用骨架，退回第 1 条，贴着这一个人的事重写。
4. **不向用户抖术语 / 结构名**：正文里不得出现内部结构名或编号（如 "egalitarian / hierarchical""co-CEO""三 R"），也不写"步骤 1/2/3"。用他自己的话，把他的事讲清楚。
5. **正文 ≤800 字**：不铺陈、不把书里的点全倒出来，只讲对他这件事真正有用的。
6. **结尾只给一个可打勾的动作**：收尾落到一句他今天或这周就能做的小事——列一行"谁在承诺 / idea / 资本上占优"——可勾选、可执行，不塞一整张清单。
7. **不替他拍板；涉钱 / 股 / 法律转专业人士**：只把选项与各自的代价摆清，选择权与责任在他本人。只要结论落到股权、金额、条款、合同或税务，就写明"不构成法律 / 税务 / 投资建议，正式安排请咨询律师与税师"，不越界替他定。

## 触发条件

**应该触发**：
- "我和合伙人都在争 CEO，这事怎么定？"
- "要不要给团队里每个人都挂个 C 头衔？"
- "我们俩平起平坐好，还是必须有个拍板的人？"
- "该不该让合伙人也进董事会？"
- "idea 是我的，CEO 是不是就该我来当？"

**不应触发**：
- 问"股权怎么分、现金拿多少" → 走 `founder-equity-splits`
- 问"关系/角色/报酬三样怎么对齐" → 走 `founder-three-rs`
- 问"该招谁、要不要开除人" → 走 `founder-hiring-dilemmas`
- 问"要不要拿投资人钱、要不要让位" → 走 `founder-investor-dilemmas` / `founder-ceo-succession`

## R：原文锚点

> "Titles are imbued with a symbolic significance and can translate into real authority."（CHAPTER FIVE, Executive Titles: Who Wants Them?）（已据原文核）
中译：头衔承载象征意义，并能转化为真实的权力。

> "our regressions showed that idea people were far more likely than non-idea people to become CEOs"（CHAPTER FIVE, Executive Titles: Who Gets Them?）（已据原文核）
中译：我们的回归显示，ideas 的提出者成为 CEO 的可能性远高于非提出者。
（同节数据：idea founders 47% 当了 CEO，non-idea founders 只有 12%。）

> "The first ideal type is the egalitarian or consensus approach."（CHAPTER FIVE, Decision-Making Approaches: Egalitarian versus Hierarchic）（已据原文核）
中译：第一种理想型是平等 / 共识式。

> "Hierarchical teams have a formal process for making decisions and a clear hierarchy, with a single person responsible for final decisions."（CHAPTER FIVE, 同上）（已据原文核）
中译：层级式团队有一套正式的决策流程和清晰的层级，由一个人对最终决定负责。

> "Consensus is a worthy goal, but as a decision-making standard, it can be an obstacle to action or a recipe for lowest-common-denominator compromise."（CHAPTER FIVE, The Problems of Egalitarianism）（已据原文核）
中译：共识是个值得追求的目标，但作为决策标准，它可能成为行动的障碍，或通向"最小公约数"式的妥协。

> "One thing I am clear about now: Two people at the wheel is the worst way to drive."（CHAPTER FIVE, Duos versus Trios）（已据原文核）
中译：我现在很清楚一件事：两个人同时握方向盘，是最糟的开法。

> "Two kings fighting over a throne can leave the kingdom devastated."（CHAPTER FIVE, The Benefits of Egalitarianism）（已据原文核）
中译：两个国王争一张王座，可能把王国打成废墟。

> "Teams of friends, for example, were 8% less likely to name a CEO than were teams of nonfriends."（CHAPTER FIVE, When Are Founders Likely to Choose Egalitarianism?）（已据原文核）
中译：例如，朋友组成的团队任命 CEO 的概率比非朋友团队低 8%。

> "Given these long-term dangers, teams should be more hesitant to assign C-level titles to themselves without consciously weighing the pros and cons."（CHAPTER FIVE, Closing Remarks）（已据原文核）
中译：鉴于这些长期风险，团队在没认真权衡利弊之前，应更谨慎地给自己发 C 级头衔。

## I：核心解释

1. **头衔不是装饰，是权力**：头衔带象征意义，也会变成真实权威；CEO 这个位子通常是早期最难的谈，也是最重要的谈。谁拿 CEO，往往决定后面谁对分歧有最终话语权。（R1）
2. **按贡献拿头衔，但会固化**：实际分配里，全职投入者、idea 提出者、以及带来人力/社会/资金资本（连续创业经验、投入的种子资金、资历）的人更容易拿到高级头衔。idea 提出者当 CEO 的比率高出约 47% vs 12%；但 idea 提出者与 CEO 岗位的匹配度常随公司成熟而下降。（R2、R10）
3. **两种理想型各有代价**：平等/共识型利于建立信任、契合朋友团队"平等"的预期；层级/专职型能快速调动资源、问责清晰。共识在高速变化环境里往往决策太慢；独裁 CEO 会漏掉复杂信息、制造派系。（R3、R4、R5）
4. **两人平等最危险**：1:1 的僵局没有结构性出口，最终常常要靠一个人彻底交出控制权或走人。（R6、R7）
5. **重叠角色 vs 分工**：技能互补（如 Jobs/Wozniak）适合分工；背景相似、都是通才的团队容易重叠，早期灵活但会"踩脚"，且分工一旦定死又不随公司演变调整，就会成为负担。
6. **头衔会"通胀"且难回收**：早期为了抢人给高头衔（"title inflation"），到后期要替换或降级时非常痛苦；CEO 头衔还有"惯性"，能力跟不上时很难换。（R9）
7. **董事会席位是零和的**：创始人席位通常少于创始人数，且随每轮融资收缩；让非 CEO 创始人进董事会，容易在管理层内部制造角色混乱，并妨碍董事会对 CEO 的坦诚反馈。

## A1：来源应用 — 书里给的具体做法

- **按统一标准定头衔，而不是谁嗓门大**：把 (a) 全职投入程度、(b) 是否 idea 提出者、(c) 人力/社会/资金资本 摆到台面上比。idea 提出者若拿 CEO，要单独再评估他是否"在所有维度上"都最适合，还是更适合挂 chairman/CTO/CSO 来安放热情与愿景。
- **认真讨论 egalitarian vs hierarchical，而不是默认**：明确两种理想型的利弊，按团队能力和公司阶段选一个，并预期它**要随阶段演变**（多数团队早期平等、后期走向层级；79% 一开始就命名 CEO，融资首轮后升到 94%）。
- **避免"回避冲突式"的假平等**：多人抢 CEO 时，用"共同决策""co-CEO"来和稀泥是拖延与问责不清的开端；即便 co-CEO 偶尔有效（如 iWon），也应是深入讨论过陷阱后主动选的，不是躲谈判的结果。
- **平衡两者的打法**：可借鉴"consensus-with-qualifications"——先求全票；无共识则 CEO 与相关职能 VP 拍板，但拍板前在公开场合听取所有人意见；也可用"四分卫"模型：一人叫战术，全员回 huddle 给信息，再叫下一个战术。
- **角色要随阶段调整**：分工不是一锤定音，FeedBurner 团队用了两家公司才把角色磨合清楚。
- **董事会席位慎配**：多数情况下不把 CEO 以外的在职高管放进董事会；若一定要放，可用"仅观察员""一年任期""CEO 退席的闭门会"等折中。

## A2：典型触发场景

- 两人创业，一个技术一个业务，都在心里觉得自己该当 CEO
- 创始团队为了"显得公平"，给所有人都挂了 C 头衔
- 公司变大了，早拿 C 头衔的联合创始人明显跟不上，但不好动
- 融资要组董事会，合伙人们争那一个创始人席位
- 三人团队里有两个人天天为方向吵，第三人走了以后更失控

## E：执行步骤

### 步骤1：盘点角色分配的三个客观输入

**输入**：每位创始人的全职/兼职承诺、是否 idea 或 IP 提出者、带来的人力/社会/资金资本。
**输出**：一张"贡献 × 头衔"对照，标出谁在哪一项占优。
🔴 **CHECKPOINT — 触发条件：有人坚持"idea 是我提的所以 CEO 必须是我"**：提醒 R2 数据（idea 者 47% 当 CEO，但匹配度会随成熟下降）；建议把"热情与愿景"安放到 chairman 或 CTO/CSO，不等于必须 CEO。

### 步骤2：选决策结构（egalitarian 还是 hierarchical）

**输入**：团队背景相似度、是否朋友/同事、公司所处阶段。
**输出**：一个明确的决策结构（平等共识 / 层级拍板 / consensus-with-qualifications）。
🔴 **CHECKPOINT — 触发条件：团队想用"共同决策"或"co-CEO"来回避谁拍板的谈判**：🛑 指出这是"回避冲突式假平等"（R5、R6、R7），是拖延、问责不清与日后爆雷的种子；推动把谈判做完。

### 步骤3：规划角色的动态调整

**输入**：当前分工 + 可预见的阶段变化（产品完成、融资、规模扩大）。
**输出**：一张"现阶段角色 → 下一阶段可能需要谁补位/让位"的清单。
🔴 **CHECKPOINT — 触发条件：用户据此要对某人降级或撤掉头衔**：只给原则与风险，让用户自己和对方谈；正式的人事与法律安排请咨询专业人士，本 skill 不替其决定。

### 步骤4：定董事会席位安排

**输入**：目前/预期的董事会席位数、创始人数、是否已引入投资人。
**输出**：创始人席位的分配建议 + 非 CEO 创始人入会的风险提示。
🔴 **CHECKPOINT — 触发条件：用户问"我能不能保证永远控制董事会"**：说明席位随每轮融资收缩、51% 也会被稀释；**不承诺控制**，具体治理条款请咨询律师。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 对不同人复用同一骨架 | 换个用户问同类问题，回答却是同一副开头、同一套模板 | 🛑 退回输出纪律第 1 条：先复述这一个人的具体处境，贴着它重写，删掉通用骨架 |
| 向用户抖术语 / 结构名 | 回答里冒出内部结构名或"步骤 1/2/3"（如 "egalitarian / hierarchical""co-CEO""三 R"） | 🛑 删掉术语与编号，用他自己的话讲他的事（输出纪律第 4 条） |
| 用假平等回避谈判 | "我们不分谁大谁小，一起决定就好" | 🛑 指出这会把冲突推迟并放大（R5–R7）；推动把 CEO 谈判做完 |
| 头衔通胀 | 早期人人 C 级，后期换不动 | 提醒 title inertia 与降级痛苦（R9），慎发头衔 |
| 拿 idea 当 CEO 唯一理由 | "想法是我提的，所以我说了算" | 指出匹配度会随阶段下降，热情可安放到别的头衔 |
| 把非 CEO 创始人塞进董事会当盟友 | 为了有人撑腰 | 指出它会造成管理层角色混乱、妨碍董事会坦诚（R8 反面对照） |
| 两人僵局拖到爆 | "我们俩吵了两年" | 提示 1:1 无出口，通常会以一方彻底交权或离开收场 |
| 替用户做人事决定 | "那你就让他当 CEO 吧" | 🛑 越界；给结构化取舍，选择权在人 |

**边界规则**：
1. 本 skill 给结构与风险，**不替用户决定谁当 CEO、谁让位**。
2. 涉及股权分配、董事会条款、雇佣合同的正式文件：**不构成法律/税务/投资建议**，请咨询律师与税师。
3. 涉及团队成员的人际冲突：只做结构与机制的诊断，**不鼓动对抗、不站队**。
4. 与相邻 skill 分工：报酬 → `founder-equity-splits`；三者对齐 → `founder-three-rs`；让位 → `founder-ceo-succession`。

**自查清单**：
- [ ] 我用了客观贡献标准，而不是让嗓门最大的人定头衔
- [ ] 我区分了 egalitarian / hierarchical 并说明了阶段演变
- [ ] 我提示了 head ≥ 2 人抢 CEO 时"假平等"的长期风险
- [ ] 我没有替用户决定谁当 CEO
- [ ] 我提示了正式条款需律师/税师

## 📖 练习手册

**"头衔审计"**：给团队每个人列出 (a) 全职程度、(b) 是否 idea/IP 提出者、(c) 投入的资金与资历、(d) 当前头衔。逐人问：这个头衔是按贡献给的，还是为了安抚给的？如果公司大 10 倍，他还能坐这个位子吗？

**"决策结构演练"**：拿一个团队真实分歧，分别用"平等共识"和"一人拍板"各走一遍，记下各自花的时间与结果。再用"consensus-with-qualifications"走第三遍。

## 🚫 反例与黑名单

1. **用 co-CEO / 共同决策来回避 CEO 谈判** → 🛑 假平等，把冲突推迟放大。
2. **给所有人 C 头衔求公平** → 🛑 头衔通胀 + 惯性，后期换不动。
3. **由本 skill 判定谁当 CEO** → 🛑 替用户做决定，越界。
4. **拿"idea 是我提的"当唯一依据** → 🛑 单维论证，忽略匹配度随阶段下降。
5. **承诺"永远控制董事会"** → 🛑 席位随融资收缩，不承诺。

### 灰色地带（需谨慎判断）

- **确实是互补型 co-CEO**：若两人技能互补、且是**深入讨论过陷阱机制后**主动选的，可能有效；与"躲谈判式假平等"要区分开。
- **技术创始人当 CTO 而非 CEO**：若创始人明确更爱做技术、且接受了非 CEO 头衔的象征落差，是合理配置。
- **非 CEO 创始人进董事会**：多数不建议，但在投资人席位强势、需要创始人团结制衡时，可能被临时采用——需说明代价。

> 安全兜底：涉及股权、投资人条款、雇佣与解雇的正式安排，**一律写明"不构成法律/税务/投资建议，重大决定请咨询律师与税师"**；涉及团队冲突只做机制诊断，不替用户做决定、不鼓动对抗。
