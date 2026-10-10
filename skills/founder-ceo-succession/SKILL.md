---
name: founder-ceo-succession
description: 创始人 CEO 被"职业 CEO"替换的前因、过程与善后。当用户问"公司做起来后创始人 CEO 为什么反而会被换掉""要不要请职业经理人来做 CEO""被换下来后我该留还是走"时使用。基于《The Founder's Dilemmas》第十章把 succession 当作一个可管理的流程。不替用户决定要不要让位、要不要卖公司。
input_schema:
  required: [startup_stage, ceo_situation, founder_role]
  optional: [board_composition, performance_signals, founder_motivation, successor_candidates]
output_schema:
  primary: {succession_readiness: string, process_options: string, founder_role_plan: string}
  secondary: [search_notes, transition_risks, cautions]
---

# 创始人 CEO 的继任：让位是一个流程，不是一场事故

**来源**：《The Founder's Dilemmas》CHAPTER TEN "Failure, Success, and Founder-CEO Succession"｜ 证据等级：firsthand

> 安全前提：本 skill 解释 succession 的机制与善后选项，**不替用户决定要不要让位、要不要卖公司**；涉及雇佣、股权、治理条款的**不构成法律/税务/投资建议**，请咨询律师与税师。

## 🔒 输出纪律（回答硬要求，先于任何理论）

1. **先复述用户的具体处境**：开口第一件事，是用一两句把用户刚说的那件具体的事复述回去——投资人暗示该请个更资深的 CEO，你拿不准该主动谈还是先扛着——确认接住的是这个人这件事，再谈结构。不许跳过复述、直接上框架。
2. **判断落在他的事实上**：每条结论都要挂在他给出的具体事实（谁、做了什么、出了什么事）上，不用"一般来说""很多创始人都会"糊过去；信息不足处标成"待确认"，不替他假设。
3. **不得对不同人复用同一骨架**：两个人的处境不同，回答就必须长得不一样——不能给所有来问的人套同一副开头、同一套"先补缺口 → 三个打勾 → 律师税师"模板，也不得与别的维度逐字雷同。一旦发现自己在套通用骨架，退回第 1 条，贴着这一个人的事重写。
4. **不向用户抖术语 / 结构名**：正文里不得出现内部结构名或编号（如 "succession""coach, then replace""成功的悖论"），也不写"步骤 1/2/3"。用他自己的话，把他的事讲清楚。
5. **正文 ≤800 字**：不铺陈、不把书里的点全倒出来，只讲对他这件事真正有用的。
6. **结尾只给一个可打勾的动作**：收尾落到一句他今天或这周就能做的小事——用一句话写下你更在乎控制还是财富——可勾选、可执行，不塞一整张清单。
7. **不替他拍板；涉钱 / 股 / 法律转专业人士**：只把选项与各自的代价摆清，选择权与责任在他本人。只要结论落到股权、金额、条款、合同或税务，就写明"不构成法律 / 税务 / 投资建议，正式安排请咨询律师与税师"，不越界替他定。

## 触发条件

**应该触发**：
- "为什么创始人 CEO 常常被投资人换掉？"
- "公司要请职业 CEO 了，我该参与搜索还是回避？"
- "被换下来以后，我该留在公司还是离开？"
- "投资人暗示该换 CEO 了，我该怎么应对？"
- "我想自己先提出让位，这样好不好？"

**不应触发**：
- 问"要不要拿某轮投资" → 走 `founder-investor-dilemmas`
- 问"我到底要钱还是要权" → 走 `founder-wealth-vs-control`
- 问"创始人之间谁当 CEO / 怎么分权" → 走 `founder-role-dilemmas`
- 问"该怎么开掉某个下属" → 走 `founder-hiring-dilemmas`

## R：原文锚点

> "the more quickly a founder-CEO leads the startup through these early stages, the more quickly he or she will need to develop new skills or capabilities and the sooner he or she may find the challenges winning the race"（CHAPTER TEN, Succeeding at Product Development）（已据原文核）
中译：创始人 CEO 越快把公司带过早期阶段，就越快需要长出新技能，也就越早可能发现"挑战跑赢了自己"。

> "the founder-CEO's very success at leading a fast-growing startup through product development is likely to accelerate his or her own obsolescence and replacement"（CHAPTER TEN, 同上）（已据原文核）
中译：创始人 CEO 在"带着快速成长的公司完成产品开发"上的**成功本身**，很可能加速他自身的过时与被替换。

> "One of the toughest jobs I have is firing CEOs who have succeeded in rapidly growing their companies."（CHAPTER TEN, Implications for Succession）（已据原文核）
中译：我最难的工作之一，就是开除那些把公司成功带向快速成长的 CEO。

> "The founder-CEO says, 'Okay, I'm ready for this,' but they don't have a clue what it means. They think it's a title change, not the tidal change it really is."（CHAPTER TEN, After the Succession）（已据原文核）
中译：创始人 CEO 嘴上说"好，我准备好了"，但根本不知道这意味着什么。他们以为只是换个头衔，其实是**一场海啸**。

> "If the company tanks, I'm gone. But if it's a big hit, I'm also gone."（CHAPTER TEN, Implications for Succession）（已据原文核）
中译：公司要是垮了，我走人；可要是大获成功，我照样得走人。

> "You can replace a CEO, but you can't replace a founder."（CHAPTER TEN, Keeping the Founder: High Risk, High Return?）（已据原文核）
中译：CEO 可以换，创始人换不掉。

> "What helped me get through the shock was the realization that the world's best speedboat captain isn't able to pilot an oil tanker."（CHAPTER TEN, Smoothing the Transition: The Board's Role）（已据原文核）
中译：帮我走出震惊的，是想通了一件事：世界上最好的快艇船长，也开不了油轮。

> "a new organ being transplanted into a body that will try to reject it"（CHAPTER TEN, Keeping the Founder: High Risk, High Return?）（已据原文核）
中译：（有投资人把第一位非创始 CEO 比作）移植进一个会排斥它的身体里的新器官。

> "when the founder triggers the change, he or she is less likely to leave the startup immediately"（CHAPTER TEN, Closing Remarks）（已据原文核）
中译：由创始人自己触发这次更换时，他更不可能立刻离开公司。

> "they can gain some control over when they lose control of the startup"（CHAPTER TEN, Closing Remarks）（已据原文核）
中译：创始人可以对自己"在何时失去对公司的控制"获得一些主动权。

> "Triggering one's own demise as CEO is wrenching but, for some founders, is worth the price if it can ensure their remaining a prince of the realm after relinquishing the throne."（CHAPTER TEN, Closing Remarks）（已据原文核）
中译：自己触发自己的下台很痛苦，但对某些创始人来说，只要能确保交出王位后仍是王国的"亲王"，就值得。

> "the new CEO is being hired to do what the founder-CEO either could not do"（CHAPTER TEN, Sources of Successors）（已据原文核）
中译：新 CEO 被请来，是为了做成创始人 CEO 做不到的事。

> "coach, then replace"（CHAPTER TEN, Closing Remarks）（已据原文核）
中译：（投资人描述的处理顺序是）先辅导，再替换。

> "by that time, more than half of startups have replaced their founder-CEOs"（CHAPTER TEN, 开篇）（已据原文核）
中译：到第三轮融资时，已有一半以上的公司换掉了他们的创始人 CEO。

## I：核心解释

1. **换 CEO 是常见结局**：到 C 轮前，过半公司已换掉创始 CEO；17% 换了不止一次。换的直接好处是"专业 CEO 能做创始人做不到的事"，但过程常常剧烈。（R13、R15）
2. **谁来触发很关键**：73% 由董事会或他人触发，仅 27% 由创始人自己触发。自触发通常最平顺，且后续待遇更好（更可能参与搜索、留任高管、留在董事会）；被董事会"炒"则最紧张。（R9、R10、R11）
3. **三种类型**：自愿让位（创始人主动，最少摩擦）／因失败被炒（里程碑连失、董事会认为换人能更好）／**成功的悖论**——产品开发成功或融资成功后，公司需要的技能换了，创始人反而因此被换。（R1、R2、R3）
4. **成功的悖论为什么会发生**：完成产品开发后，公司从"技术团队"变成"多功能公司"（销售、市场、客服、财务），需要的技能与创始人强项常常错位；而创始人对早期员工与原始想法的忠诚，会让他做不出必要的人事与战略调整。把公司带得越快，过时得越快。（R1、R2）
5. **融资成功同时是控制权丧失**：每轮融资把董事会控制权从创始人手里拿走；而董事会正是"雇/炒 CEO"的机构。所以成功融资 = 更可能被换。（引 Ch9）
6. **新 CEO 几乎都从外部找**：小团队内部少有合适人选；创始人也常被拉进搜索（既是提供信息，也是求支持），但创始人参与可能拖慢流程、吓退优秀候选人（"全民公投"式面试）。（R12）
7. **善后才是最长的路**：多数被换的创始人**留任**（约 63% 作高管），很多人还在董事会（自触发时 96%，被董事会触发时 60%）。保留创始人是"高风险高回报"：他能贡献知识、人脉与员工买账，但也可能（尤其控制型、心怀不满者）掣肘新 CEO。新 CEO 常失败，所以留个创始人当"保险"也合理。（R6、R8）
8. **董事会应把它当流程（coach, then replace）**：投前就用"rich-vs-king test"判断创始人会不会死扛 succession；投后做定期、坦诚、书面的绩效反馈；需要时先辅导、再替换。创始人若担心被换，应在拿钱前主动把 succession 议题摆上桌。（R14）

## A1：来源应用 — 书里给的具体做法

- **把 succession 当流程**：从投前谈预期、投后定期复盘，到"coach, then replace"，一路管理，而不是等爆雷。
- **创始人主动"抢在董事会前面"**：自己发起 succession，能换到更好的善后（留任、进董事会、主导搜索）。
- **搜寻：内外结合但现实**：内部候选人常不够；要准备打持久战（Wily 找了 13 个月、看了 120 份简历）；可用 bridge CEO（临时 CEO）或"两阶段过渡"（先当 COO 再接手）降低冲击。
- **让候选人接受"双标"**：若创始人参与搜索，候选人要同时满足投资人与创始人；创始人常偏好与自己背景相似者（homophily），但差异大、能补短板的候选人往往更合适。
- **善后用三 R 操作**：与新 CEO 建立关系（先共事/咨询）、明确新角色（把创始人从日常决策里温和移出、只在特定领域负责）、用奖励（部分买断、过渡奖金、加快 vesting）兑现"让位得利"。
- **对创始人**：想清楚是要控制还是要财富——控制型更可能死扛并落到"被炒"的结局。

## A2：典型触发场景

- 融资谈判中 VC 暗示"将来需要一位更有经验的 CEO"
- 公司产品做成了、要走向规模化，创始人却越来越吃力
- 被换下来后纠结"留任高管还是走人"
- 董事会开始正式评估创始 CEO 的绩效
- 想自己先提出让位，以换取更好的善后安排

## E：执行步骤

### 步骤1：判断当前 succession 的信号与阶段

**输入**：公司阶段、产品/融资里程碑、董事会构成、绩效信号。
**输出**：一个"是否已到 succession 临界点"的定性判断 + 触发方是谁。
🔴 **CHECKPOINT — 触发条件：用户问"我是不是该让位"**：🛑 **不替用户决定要不要让位**；给出信号与后果，由本人与其董事会决定。

### 步骤2：判断"谁触发、怎么触发"

**输入**：创始人动机（财富/控制）、与董事会的关系。
**输出**：自触发 vs 被触发的后果对比 + 建议的沟通时点。
🔴 **CHECKPOINT — 触发条件：用户担心被"炒"却想回避谈 succession**：提示主动谈能换来更好的善后（R10、R11）；但**不替他决定谈或不谈**。

### 步骤3：规划继任者搜索与过渡

**输入**：现任团队、可选内外候选人、过渡方式偏好。
**输出**：搜索方案（外部为主）+ 过渡形式（bridge CEO / 两阶段）。
🔴 **CHECKPOINT — 触发条件：候选人由投资人一手推荐、创始人只是"盖章"**：提示"双标"现实与 homophily 陷阱；**不替用户选定人选**。

### 步骤4：规划创始人善后角色

**输入**：创始人技能与偏好、能否接受非 CEO 角色。
**输出**：一份"留任高管 / 董事会席位 / 离开"的选项清单与各自代价。
🔴 **CHECKPOINT — 触发条件：用户据此要谈股权买断、过渡奖金、加快 vesting**：只给方向与原则；正式条款**请律师与税师**，本 skill 不构成法律/投资建议。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 对不同人复用同一骨架 | 换个用户问同类问题，回答却是同一副开头、同一套模板 | 🛑 退回输出纪律第 1 条：先复述这一个人的具体处境，贴着它重写，删掉通用骨架 |
| 向用户抖术语 / 结构名 | 回答里冒出内部结构名或"步骤 1/2/3"（如 "succession""coach, then replace""成功的悖论"） | 🛑 删掉术语与编号，用他自己的话讲他的事（输出纪律第 4 条） |
| 把让位当"换头衔" | 创始人低估角色变化 | 讲 R4 的"海啸"，用三 R 做过渡 |
| 被董事会突然"炒" | 最紧张、善后最差 | 提示自触发更有利（R9、R10），能提前谈就提前谈 |
| 创始人死扛 | 拖垮公司或价值受损 | 提示控制型的风险；用"新 CEO 能补短板"论证（R12） |
| 保留一个不满的创始人 | 新 CEO 被掣肘 | 提示"高风险高回报"（R6、R8）；必要时隔离角色 |
| 让 skill 决定让不让位 | "你就说该不该退" | 🛑 越界；给机制与选项，决定权在本人 |
| 搜到合适人却拖成马拉松 | 13 个月、候选人被吓跑 | 用 bridge CEO / 两阶段过渡，控制流程 |

**边界规则**：
1. 只解释 succession 的**机制、过程与善后选项**，**不替用户决定要不要让位、要不要卖公司**。
2. 涉及雇佣、股权买断、vesting、治理条款：**不构成法律/税务/投资建议**，请咨询律师与税师。
3. 涉及创始人与董事会/新 CEO 的冲突：只指出结构性成因，**不鼓动对抗、不站队**。
4. 与相邻 skill 分工：钱权取舍 → `founder-wealth-vs-control`；投资人条款 → `founder-investor-dilemmas`。

**自查清单**：
- [ ] 我讲清了三种 succession（自愿 / 失败 / 成功的悖论）
- [ ] 我说明了"自触发 vs 被触发"的善后差别
- [ ] 我给了搜索与过渡（bridge / 两阶段）的方向
- [ ] 我讲了创始人的善后角色与"留任是高风险高回报"
- [ ] 我没有替用户决定让不让位，并提示正式条款找律师

## 📖 练习手册

**"里程碑自审"**：列出公司已完成的关键里程碑（产品、融资、客户）。每完成一个，问：公司现在最需要的 CEO 能力，和我擅长的是不是同一套？

**"提前谈 succession"演练**：写一段你打算跟董事会开诚布公谈 succession 的话，重点不是"我要不要走"，而是"我们如何一起把这件事管理好"。

## 🚫 反例与黑名单

1. **以为换了头衔只是换头衔** → 🛑 是"海啸"，要用三 R 系统过渡。
2. **死扛到被董事会炒** → 🛑 善后最差；能自触发就自触发。
3. **保留一个不满的控制型创始人又给他实权** → 🛑 新 CEO 会失败。
4. **让候选人经历"全民公投"式面试** → 🛑 吓跑最好的人。
5. **由 skill 判定"该不该让位/该不该卖"** → 🛑 越界。

### 灰色地带（需谨慎判断）

- **bridge CEO（临时 CEO）**：对控制型创始人更易接受，但他到期会走，需要后续安排。
- **两阶段过渡（先当 COO 再接手）**：更平顺，但周期长、变数多。
- **创始人留任**：常常必要（保险 + 知识），但必须管理其与新 CEO 的权责边界。

> 安全兜底：本 skill **不替用户决定要不要让位、要不要卖公司，不构成法律/税务/投资建议**；涉及冲突只指出结构成因、不鼓动对抗；出现急性危机信号（自伤/伤害他人）时停止分析并给危机资源。
