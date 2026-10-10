---
name: habit-four-laws-audit
description: 四定律诊断。当用户有一个「做不到的好习惯」或「戒不掉的坏习惯」——"我坚持不了早起""我就是戒不掉刷手机""为什么我明知道该做却做不动"——时使用。把行为拆成提示-渴望-反应-奖励四环，找出卡住的那一环，给一个最先改的替换动作。
input_schema:
  required: [target_behavior, direction, failure_description]
  optional: [attempts_tried, environment_context, emotional_intensity]
output_schema:
  primary: {stuck_ring: string, failed_law: string, first_replacement_action: string}
  secondary: [awareness_note, cautions, follow_up_prompts]
---

# 四定律诊断：把「做不到」拆成提示-渴望-反应-奖励

**来源**：《Atomic Habits》第3章 How to Build Better Habits in 4 Simple Steps、第4章 The Man Who Didn't Look Right、第7章 The Secret to Self-Control、第15章 The Cardinal Rule of Behavior Change | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我知道该做，但就是做不动/开始不了"（好习惯建不起来）
- 用户说"我戒了好多次，就是戒不掉"（坏习惯停不下来）
- 用户给出一个具体行为（早起、健身、刷短视频、吃夜宵）但说不清卡在哪
- 用户试过靠打鸡血/靠意志力，失败了，想搞清机制
- 用户问"为什么别人做得到我做不到"

**不应触发**：
- 用户只是想把模糊愿望变成一个带提示的启动句 → 走 habit-starter-design
- 用户想从"我想要某个结果"改写成"我想成为哪种人" → 走 habit-identity-votes
- 用户已经维持了一阵、现在是中断/看不到效果/平台期 → 走 habit-streak-plateau
- 用户处在抑郁、自伤、成瘾急性期（酒精/药物戒断）→ 先转专业资源，不做四定律拆解

## R：原文锚点

> "Any habit can be broken down into a feedback loop that involves four steps: cue, craving, response, and reward."（第3章，Chapter Summary）（已据原文核）

> "If a behavior is insufficient in any of the four stages, it will not become a habit. Eliminate the cue and your habit will never start. Reduce the craving and you won't experience enough motivation to act. Make the behavior difficult and you won't be able to do it. And if the reward fails to satisfy your desire, then you'll have no reason to do it again in the future. Without the first three steps, a behavior will not occur. Without all four, a behavior will not be repeated."（第3章，The Science of How Habits Work）（已据原文核）

> "The Four Laws of Behavior Change are a simple set of rules we can use to build better habits. They are (1) make it obvious, (2) make it attractive, (3) make it easy, and (4) make it satisfying."（第3章，Chapter Summary）（已据原文核）

> "The process of behavior change always starts with awareness. You need to be aware of your habits before you can change them."（第4章，Chapter Summary）（已据原文核）

> "The Cardinal Rule of Behavior Change: What is immediately rewarded is repeated. What is immediately punished is avoided."（第15章，Chapter Summary）（已据原文核）

> "Self-control is a short-term strategy, not a long-term one. You may be able to resist temptation once or twice, but it's unlikely you can muster the willpower to override your desires every time."（第7章，Chapter Summary）（已据原文核）

## I：核心解释

1. **一个行为＝四个环串起来的一条链**：提示（cue：什么触发了它）→ 渴望（craving：你想通过它换到什么状态）→ 反应（response：你实际做的动作）→ 奖励（reward：做完得到的回报）。四环按固定顺序跑，你几乎察觉不到。（R1）
2. **缺任何一环，这个行为就不成立**：没有提示它永远不开始；渴望不够你不会动；行为太难你做不到；奖励不解渴你下次没有理由再做。（R2）诊断的关键就是找"哪一环断了"。
3. **四条定律＝四个环的扳手**：建好习惯用 obvious / attractive / easy / satisfying 拧正；戒坏习惯就把这四个扳手反过来——invisible / unattractive / difficult / unsatisfying。（R3）
4. **坏习惯和好习惯共用一套框架**，不是两套。所以"戒不掉"和"做不到"是同一个诊断动作，只是改的方向相反。
5. **"戒不掉"通常不是意志力问题，是环境里的提示问题**：书里明说自制力是短期策略，纪律好的人不是更能忍，而是"spend less time in tempting situations"——把提示从环境里拿掉，比每次硬扛可靠。（R6、第7章）
6. **最难的一环往往是奖励的即时性**：坏习惯的代价在未来、甜头在当下；好习惯反过来（当下是苦的、回报在未来）。这就是为什么单靠"我知道它对"推不动你。（R5、第15章）

## A1：来源应用 — 书里的两个诊断动作

书里给出的第一步不是"改"，而是"看见"。两个动作直接照抄：

- **Habits Scorecard（习惯记分卡）**：把一天的日常行为列出来，每条后面标 +（好）/ –（坏）/ =（中性）。书里特别强调：**一开始什么都不要改，只是看**。"The goal is to simply notice what is actually going on. Observe your thoughts and actions without judgment or internal criticism."（第4章，The Habits Scorecard）
  判断标准用这一问：> "Does this behavior help me become the type of person I wish to be? Does this habit cast a vote for or against my desired identity?"（第4章）
- **Pointing-and-Calling（指差确认）**：像东京地铁司机那样，把正在做的动作和它即将带来的后果说出声。书里的例子：> "I'm about to eat this cookie, but I don't need it. Eating it will cause me to gain weight and hurt my health."（第4章）出声会把后果变"实"，不让你无意识滑回老路。

书里还给了一份现成的四定律清单（第15/17章附录式小结），诊断时逐条对：建好习惯 1.1 Scorecard、1.2 执行意图、1.3 习惯堆叠、1.4 设计环境；2.1 诱惑捆绑、2.2 加入对的圈子、2.3 动机仪式；3.1 减少摩擦、3.2 预备环境、3.3 掌握决定性时刻、3.4 两分钟规则、3.5 自动化；4.1 即时强化、4.2 让"什么都不做"也爽、4.3 习惯追踪、4.4 绝不连续错过两次。戒坏习惯反着来：1.5 移除提示；2.4 重构心态、2.5 重构坏习惯的期待；3.6 增加摩擦；4.5 找问责伙伴/签习惯契约。

## A2：典型触发场景

- 说了半年要健身，卡在"下班后就瘫着"
- 每晚睡前刷手机两小时，删了 App 又装回来
- 想每天读书，书买回来了没翻过
- 戒夜宵/戒烟，撑两天就复吸
- 明知该早点睡，躺下还是继续刷

## E：执行步骤

### 步骤1：锁定一个具体行为 + 方向

**输入**：用户的原话。
**输出**：一个可命名的行为，方向是"建"还是"戒"。

**输入**：target_behavior；**输出**：direction（build / break）+ 一句话行为定义。
追问把笼统换成具体：不是"我要健康"，而是"每天晚上刷短视频"或"每天运动"。

🔴 **CHECKPOINT — 触发条件：用户给的是一团情绪（"我就是很丧、什么都坚持不了"）而不是一个行为**：泛化情绪不是习惯问题 → 先追问"最近一次具体是什么行为、什么时刻"。若仍拿不出 → 转 B 节「情绪不落地」分支，不硬套四环。

### 步骤2：先做觉察，不急着改

**输入**：步骤1 的行为。
**输出**：一份 Habits Scorecard 片段 + 一句指差确认式复述。

照 A1 让用户列出与这个行为相关的日常（提示前后各发生了什么），只标 +/–/=，不改。若用户愿意，用"我正要做 X，它会带给我 Y"出声复述一次。

### 步骤3：逐环拆解，找断点

**输入**：步骤2 的觉察片段。
**输出**：四环各自的当前内容。

四问（问题按方向调）：
- **提示 cue**：这个行为被什么触发？（时间、地点、情绪、前一个动作、某个人、某个 App 通知）
- **渴望 craving**：你想通过它换到什么**状态**？（书里："You do not crave smoking a cigarette, you crave the feeling of relief it provides." —— 第3章）
- **反应 response**：实际动作是什么？难不难、要几步、累不累？
- **奖励 reward**：做完立刻得到什么？这个回报是即时的还是延迟的？

🔴 **CHECKPOINT — 触发条件：四问里用户对某一环怎么都想不出答案**：不要替他编。那一环"看不见"本身可能就是关键（提示常常是无意识的，第4章："you don't need to be aware of the cue for a habit to begin"）。留一个提问让用户回去观察一天再答。

### 步骤4：定位卡住的那一环 → 对应哪条定律失守

**输入**：步骤3 的四环内容。
**输出**：stuck_ring + failed_law。

对照表：

| 断点 | 好习惯"建不起来"的表现 | 坏习惯"戒不掉"的表现 | 失守的定律 |
|------|----------------------|--------------------|-----------|
| 提示 | 想不起要做、时间地点没定 | 到处都是触发源（手机、零食柜） | 1st（obvious / 反 invisible） |
| 渴望 | 觉得这习惯无聊、没吸引力 | 觉得它特别"香"、特别解压 | 2nd（attractive / 反 unattractive） |
| 反应 | 太难、步骤太多、太累 | 太方便、零摩擦就能做 | 3rd（easy / 反 difficult） |
| 奖励 | 做完没回报、看不到进展 | 做完马上爽 | 4th（satisfying / 反 unsatisfying） |

书里对应的扳手话术（第7、15章）：建好习惯——"Make the cues of your good habits obvious and the cues of your bad habits invisible"；戒坏习惯——找一个立刻的代价，"make them painful in the moment"。

### 步骤5：给一个最先改的替换动作

**输入**：步骤4 的断点。
**输出**：first_replacement_action（一个，本周就能做）。

只改**一个**环、只给**一个**动作，别一次上四条定律。从断点选扳手：
- 断在提示（建）：把行为绑到"我 X 之后"（habit stacking）或定死"周几几点在哪"（执行意图）→ 细节走 habit-starter-design
- 断在提示（戒）：移除/隐藏触发源（第7章："Remove a single cue and the entire habit often fades away."）
- 断在渴望：诱惑捆绑——把想做的事和该做的事绑在一起（第8章）
- 断在反应：把好习惯缩到两分钟内、把坏习惯加摩擦
- 断在奖励：加一个即时强化（第15章："reinforcement... using an immediate reward to increase the rate of a behavior."）

🔴 **CHECKPOINT — 触发条件：用户说"我知道该怎么做，可我就是控制不住/我就是懒"**：这是把系统问题读成人格问题 → 引 R6 或第1章"the problem isn't you. The problem is your system." 把注意力从自我审判拉回可改的那一环。若用户同时出现情绪极度低落/自伤 → 转 B 节安全分支。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 情绪不落地 | 用户给不出任何具体行为，只有"我很丧、坚持不了" | 🛑 不硬套四环。先降级为倾听，问"最近一次具体是哪个行为、什么时刻"。持续泛化 → 考虑情绪/抑郁议题而非习惯议题。 |
| 把诊断当人格判决 | "所以我就是没毅力的人呗" | 🛑 纠偏：引用第1章"the problem isn't you. The problem is your system." 断点是你周围结构的断点，不是你的缺陷。 |
| 一次想改四条 | 用户要求把四环全改掉 | 🛑 拒绝。一次只改一个环、一个动作，其余留到下一轮。 |
| 成瘾急性期 | 酒精/药物依赖、严重的赌博/游戏成瘾已影响功能 | 🛑 停止自助拆解，转专业戒断/成瘾治疗资源。 |
| 拿框架攻击自己 | 用户用"我渴望的是逃避"来羞辱自己 | 🛑 正常化：坏习惯在当下确实在替你解决问题（第4章："All habits serve you in some way—even the bad ones"）。看清它服务什么，才有得换。 |
| 抑郁/自伤信号 | 出现"活着没意义""不想存在" | 🛑 停止习惯诊断，转 B 节安全分支，给专业资源，做陪伴。 |

### 边界规则

1. **不做诊断，不替代心理/医学评估**：本 skill 只拆行为机制。
2. **先觉察，后改动**：跳过步骤2直接给方案，通常会失败——书里反复强调行为改变从觉察开始。
3. **一次只动一环**：四定律是菜单不是清单。
4. **安全兜底**：出现临床抑郁、自伤、自杀意念、物质依赖急性戒断，**停止**框架工作，明确告知需要专业人员并指向当地心理援助资源（如各地心理援助热线；中国大陆可拨 12356，紧急时拨 120/110）。不做诊断、不保证效果。

### 用户自查清单

- [ ] 我能说出自己卡住的**是一个具体行为**，而不是一团情绪
- [ ] 我为它做过一次**只观察、不评判**的觉察
- [ ] 我能逐环说出自己的**提示 / 渴望 / 反应 / 奖励**
- [ ] 我能指出**断在哪一环**，并说出它对应哪条定律
- [ ] 我选定了**一个**最先改的动作，且知道它这周怎么落地

**勾选 4+ 项**：诊断到位。**≤2 项**：回到对应步骤重做，或考虑是否需要 B 节分支。

## 📖 练习手册

**四环拆解卡**：画四个方框（提示-渴望-反应-奖励），把你的行为填进去。再用不同颜色标出哪几环是"帮你的"、哪几环是"卡你的"。

**反演练习**：拿一个坏习惯，把四定律逐条反写——原本 obvious 的提示，怎么让它 invisible？原本 easy 的反应，怎么增加摩擦？写不出四条没关系，写出一条就是本周的动作。

（配套练习笔记写到 用户批准的位置。）

## 🚫 反例与黑名单

1. **急性精神症状 / 重度抑郁 / 自伤 / 物质依赖戒断期** → 先转专业评估，本框架不适用急性期。
2. **纯外部困境**（失业、战乱、灾害）→ 习惯诊断不能替代现实援助，先谈资源和处境。
3. **用四环给人格定罪**（"你就是被多巴胺控制了"）→ 🛑 停止。框架是自助工具，不是道德批判。
4. **把坏习惯说成纯粹愚蠢** → 违反书里立场：每个习惯都在当下解决了一个问题（第4章）。

### 灰色地带（需谨慎判断）

5. **用户只有一个很模糊的愿望**（"我想活得更有秩序"）→ 先让它落地成一个行为，否则回到步骤1 的 CHECKPOINT。
6. **断点跨多环**（提示和奖励同时断）→ 只挑**最先松**的那一环先动，说清"其余的我们下一轮再说"，避免过载。
7. **用户在专业治疗/成瘾康复中** → 优先遵循治疗师方案，本框架仅作补充理解。
