---
name: habit-streak-plateau
description: 维持与平台期。当用户已经做了但走不下去——"我断了""做很久了没效果""我卡住了、腻了"——时使用。分开处理三种掉队：中断了、长期看不到效果（潜能潜伏平台期）、到平台期无聊了，各给对应的维持动作。
input_schema:
  required: [dropout_type, habit_duration, current_state]
  optional: [tracking_method, motivation_level, past_recovery_attempts]
output_schema:
  primary: {failure_diagnosis, recovery_action, maintenance_adjustment}
  secondary: [review_ritual, measurement_audit, cautions]
---

# 维持与平台期：中断了、没效果、还是腻了？

**来源**：《Atomic Habits》第1章 The Surprising Power of Atomic Habits、第16章 How to Stick with Good Habits Every Day、第19章 The Goldilocks Rule、第20章 The Downside of Creating Good Habits | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我断了几天/几周，感觉前功尽弃了"
- 用户说"我坚持 X 个月了，一点效果都看不到"
- 用户说"我做着做着就没意思了/腻了/坚持不下去"
- 用户在用打卡/追踪，关心"链子断了怎么办"
- 用户问"是不是该换个方法/换个计划"

**不应触发**：
- 用户还没真正开始（没有带提示的启动句）→ 走 habit-starter-design
- 用户要的是"哪一环断了"的机制诊断 → 走 habit-four-laws-audit
- 用户要的是"我想成为哪种人"的身份改写 → 走 habit-identity-votes
- 用户处在抑郁/倦怠急性期，连维持都谈不上 → 先转 B 节安全分支

## R：原文锚点

> "Never miss twice. If you miss one day, try to get back on track as quickly as possible. ... Missing once is an accident. Missing twice is the start of a new habit."（第16章，How to Recover Quickly When Your Habits Break Down）（已据原文核）

> "The first mistake is never the one that ruins you. It is the spiral of repeated mistakes that follows."（第16章）（已据原文核）

> "If you find yourself struggling to build a good habit or break a bad one, it is not because you have lost your ability to improve. It is often because you have not yet crossed the Plateau of Latent Potential."（第1章，What Progress Is Really Like）（已据原文核）

> "In the early and middle stages of any quest, there is often a Valley of Disappointment. You expect to make progress in a linear fashion and it's frustrating how ineffective changes can seem during the first days, weeks, and even months."（第1章）（已据原文核）

> "The greatest threat to success is not failure but boredom. ... Professionals stick to the schedule; amateurs let life get in the way."（第19章，Chapter Summary）（已据原文核）

> "The Goldilocks Rule states that humans experience peak motivation when working on tasks that are right on the edge of their current abilities. Not too hard. Not too easy. Just right."（第19章）（已据原文核）

> "When a measure becomes a target, it ceases to be a good measure."（第16章，Knowing When (and When Not) to Track a Habit，Goodhart's Law）（已据原文核）

## I：核心解释

1. **"走不下去"是三种不同的病，要先分开**：①中断（slipped：漏了一天/几天）②看不到效果（Plateau of Latent Potential / Valley of Disappointment）③平台期无聊（bored）。三种的处置完全不同，混在一起会越搞越糟。
2. **中断的处方是"绝不连续错过两次"**：书里把第一条解释得很明确——毁掉你的不是第一次失误，是紧接着的螺旋。一次是意外，两次是新习惯的开始。（R1、R2）
3. **看不到效果不是你没进步，是突破还没到阈值**：书里的冰 cube 类比——25 到 31 度冰都没化，32 度才化。前面不是白做功，是"被储存"了。抱怨没效果，就像抱怨冰在 31 度时没融化。（R3、R4）
4. **平台期的真正敌人是无聊，不是失败**：习惯一旦变平淡，大脑会去找新鲜感，于是你不停换方法——哪怕旧方法还在起作用。（R5）
5. **平台期要的是"刚好难一点"**：按 Goldilocks，任务要落在能力的边缘（不太难也不太空），才有持续动机。书里说流状态大约是超出当前能力 4% 的难度。（R6）
6. **长期要有一个复盘机制**：书里建议周期性回顾（Annual Review / Integrity Report），防止在自动运行里悄悄退化——"habits + deliberate practice = mastery"。（第20章）
7. **别被指标反噬**：追踪一旦变成唯一目标，你会为了数字而牺牲目的（Goodhart's Law）。（R7）

## A1：来源应用 — 书里的四个维持工具

- **Never miss twice（绝不连续错过两次）**（第16章）：断了就尽快回到轨道。"I can't be perfect, but I can avoid a second lapse. As soon as one streak ends, I get started on the next one." 书里还给了复利论证：> "Don't put up a zero."——差的一天也维持住你已积累的复利。
- **Habit tracker / 别断链**（第16章，Jerry Seinfeld）："Don't break the chain"——把注意力放在"现身"而不是"这一条好不好"。书里也给了落地方式：记录紧跟在行为之后（"After [CURRENT HABIT], I will [TRACK MY HABIT]."）。
- **平台期的冰 cube 与石头切割**（第1章）：可以拿书里的原话给用户做心理支架——> "Your work was not wasted; it is just being stored. All the action happens at thirty-two degrees."
- **复盘与审查**（第20章）：书里作者自己的做法是每年十二月做 Annual Review，问三个问题——> "What went well this year? What didn't go so well this year? What did I learn?"；年中做 Integrity Report，问——> "What are the core values that drive my life and work? How am I living and working with integrity right now? How can I set a higher standard in the future?" 运动界的例子：Eliud Kipchoge 每次训练后记笔记，Katie Ledecky 每天记 1–10 分状态。

## A2：典型触发场景

- 旅行/生病/加班，打卡断了，一断就再没开始
- 健身几个月，镜子/体重没变化，想放弃
- 写作/练琴进入"重复到麻木"的阶段，提不起劲
- 打卡变成了"为数字而做"，开始糊弄
- 做到小有所成后，反而懈怠、退步

## E：执行步骤

### 步骤1：判断是三种掉队里的哪一种

**输入**：用户的状态描述。
**输出**：failure_diagnosis（中断 / 看不到效果 / 平台期）。

三问分流：
- **中断**：是"漏掉了一两天/一阵"？→ never miss twice
- **看不到效果**：是"每天都在做，但看不到结果"？→ Plateau of Latent Potential
- **平台期**：是"做得挺稳，但腻了/没意思了/想换方法"？→ Goldilocks + 复盘

🔴 **CHECKPOINT — 触发条件：用户分不清或三种混在一起（"我又断了，而且做了也没用，还特别烦"）**：不要一起处理 → 先处理**最近发生的那个**（通常是中断），把它稳住，再谈另两种。一次只答一种。

### 步骤2A：中断 → 绝不连续错过两次

**输入**：中断的事实与时长。
**输出**：recovery_action（今天就重启的最小动作）。

引 R1/R2 讲清机制：毁掉你的不是那一次，是它后面的螺旋。给一个**今天就能做的两分钟版**，让链子立刻接上。别补课、别加倍——补课式惩罚会让人更不想开始。

### 步骤2B：看不到效果 → 潜能潜伏平台期

**输入**：用户的投入与"没效果"的判定。
**输出**：给心理支架 + 一次"账本核对"。

用冰 cube / 竹子 / 石头切割的类比（第1章）说明"结果延迟"是复利过程的本性。同时做一次客观核对：他说的"没效果"是拿什么在衡量？有没有滞后指标正在变（睡眠、心情、能举起/能写下多少）？必要时提示 nonscale victory。

🔴 **CHECKPOINT — 触发条件：用户在做的是**破坏性**行为（极端节食、熬夜透支、只追一个体重数字到伤害自己）**：停止"坚持"话术 → 引 R7（Goodhart's Law）与他核对指标是否已伤害目的；出现进食障碍信号 → 转 B 节安全分支。

### 步骤2C：平台期 → 调到"刚好难一点" + 复盘

**输入**：平台期描述。
**输出**：maintenance_adjustment（一个升级或换指标的动作）。

按 Goldilocks（R6）做微调：加一点难度/新变化，让行为重新变新鲜——"Behaviors need to remain novel in order for them to stay attractive and satisfying."（第19章），但不要一次全推翻。书里 Steve Martin 的做法是每年把节目延长一两分钟、同时保留几个必笑的旧段子。

同时引入复盘机制（第20章）：做一次 Annual Review / Integrity Report 式的三问，判断该升级、维持还是回基本功。

### 步骤3：确认维持机制

**输入**：步骤2 的动作。
**输出**：maintenance_adjustment + review_ritual。

三样各有其位：
- 平时维持 → habit tracker（别断链，记录紧跟行为）
- 断了 → never miss twice
- 周期 → 定期复盘

🔴 **CHECKPOINT — 触发条件：用户把追踪本身变成了负担（"我就是为了打勾才做，早就糊弄了"）**：这是 R7 的典型 → 让他看 Goodhart's Law，改成"追踪一周/一月一次 + 换更贴合目的的指标"，而不是每天死磕数字。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 一次失误被读成前功尽弃 | "断了三天，全白费了，算了" | 🛑 引 R1/R2：一次是意外。今天就重启，别补偿式加倍。 |
| 用"内在成长"掩盖糊弄 | "虽然没效果，但我成长了"却什么都没做 | 🛑 引第20章：Habits + Deliberate Practice = Mastery；复盘要看行为证据，不只看感觉。 |
| 追指标追到伤自己 | 极端节食、只盯体重、为数量牺牲质量 | 🛑 引 R7，停用该指标，转更贴合目的的衡量；严重时转进食障碍/专业资源。 |
| 平台期就推翻重来 | 一腻就换方法、换计划 | 🛑 引 R5：无聊是头号敌人；做法是"加一点难度/变化"，不是推倒。 |
| 情绪长期低落 | "做什么都没劲、活着没意思" | 🛑 停止维持话术，转 B 节安全分支，给专业资源，做陪伴。 |
| 用 never miss twice 硬扛进行伤 | 带伤/带病坚持 | 🛑 身体和心理健康优先于链子；宁可断链也不硬撑，断后按步骤2A 重启。 |

### 边界规则

1. **不做诊断，不替代专业评估**：本 skill 只做维持与复盘的判断。
2. **三种掉队分开处理**：一次只答一种，别混着修。
3. **追踪是工具不是目的**：别让数字吃掉这件事本身的意义（R7）。
4. **安全兜底**：出现临床抑郁、急性倦怠、进食障碍、自伤、自杀意念，**停止**维持话术，明确告知需要专业人员并指向当地心理援助资源（如各地心理援助热线；中国大陆可拨 12356，紧急时拨 120/110）。不做诊断、不保证效果。

### 用户自查清单

- [ ] 我能说清我这次是**中断 / 看不到效果 / 平台期**里的哪一种
- [ ] 我知道**第一次失误不是终点**，第二次才是真正要防的
- [ ] 如果"看不到效果"，我能说出我拿**什么**在衡量、它是否已经变了
- [ ] 如果腻了，我有一个**只加一点难度/变化**的调整，而不是推倒重来
- [ ] 我有一个**周期复盘**的动作（周/月/年）

**勾选 4+ 项**：维持工作到位。**≤2 项**：回到对应步骤重做，或考虑转 B 节。

## 📖 练习手册

**链子重启卡**：写下你断链的那天发生了什么。然后只做一件事——把"今天就做两分钟版"写进今天的固定动作后面（habit stacking + tracking）。

**复盘三问**（照第20章）：每月末问——什么进展顺利？什么不顺利？我学到了什么？连续三个月，回看你自己写的轨迹。

**平台期体检**：当你想"换方法"时，先问——旧方法真的失效了吗，还是我只是腻了？把答案写下来再决定。

（配套练习笔记写到 用户批准的位置。）

## 🚫 反例与黑名单

1. **急性抑郁 / 倦怠 / 进食障碍 / 自伤** → 先转专业评估与陪伴，不用维持话术。
2. **用"绝不中断"逼自己带病带伤硬扛** → 🛑 健康优先于链子。
3. **把断链当道德失败**（"我真没用"）→ 🛑 纠偏：一次失误是意外不是人格污点（R1）。
4. **把追踪数字当唯一真理** → 违反 R7，按步骤3 的 CHECKPOINT 处理。

### 灰色地带（需谨慎判断）

5. **用户的高强度计划本身就不合理**（每天两小时，从零开始）→ 平台期可能是设计问题不是意志问题，转 habit-starter-design 重新缩到两分钟。
6. **用户想放弃的是"该放弃的习惯"** → 不是所有中断都叫掉队；先区分"该坚持的"和"本来就该停的"。
7. **用户在专业治疗/康复中** → 优先遵循治疗师方案，本框架仅作补充理解。
