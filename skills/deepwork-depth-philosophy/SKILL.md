---
name: deepwork-depth-philosophy
description: 深度工作排程方式的选择。当用户说"我想每天留整块时间做重要的事却总排不进去""我该早上固定做还是攒着整块的几天做""周末到底该不该看工作消息""我试过专门空出时间但几天就崩了"时使用。按你的岗位产出形态、日程自主度、深度工作熟练度，从禁欲/双峰/节奏/新闻记者四种排程方式里选定一种，并给出为什么不是另外三种。不评价你有没有意志力。
input_schema:
  required: [job_output, schedule_autonomy, focus_skill]
  optional: [non_deep_commitments, prior_attempts, work_environment]
output_schema:
  primary: {chosen_philosophy, why_this_one, why_not_the_other_three}
  secondary: [ritual_requirements, first_week_plan, switch_trigger]
---

# 深度工作排程：从四种方式里挑一种，并说清为什么不是另外三种

**来源**：《Deep Work》Rule #1: Work Deeply，*Decide on Your Depth Philosophy* | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我想每天留出整块时间做最重要的事，可事情一件接一件，排不进去。"
- "我是该每天早上固定做深度工作，还是攒着整块的几天做？"
- "我周末到底该不该看工作消息？"
- "我试过关掉通知专门做重要的事，坚持不了几天。"
- "我一有空隙就先想把邮件清干净。"

**不应触发**：
- 用户要练的是"能专注多久"本身（走 deepwork-embrace-boredom）
- 用户要处理的是浅层工作太多、下班关不掉（走 deepwork-shallow-shutdown）
- 用户要决定某个 App 该不该继续用（走 deepwork-craftsman-tools）
- 用户已经稳定地在做深度工作，只是问某个具体任务怎么做（本 skill 管"排程方式"，不管任务本身）

## R：原文锚点

> "You must be careful to choose a philosophy that fits your specific circumstances, as a mismatch here can derail your deep work habit before it has a chance to solidify."（Rule #1, *Decide on Your Depth Philosophy*）（已据原文核）

> "This philosophy attempts to maximize deep efforts by eliminating or radically minimizing shallow obligations."（Rule #1, *The Monastic Philosophy of Deep Work Scheduling*）（已据原文核）

> "This philosophy asks that you divide your time, dedicating some clearly defined stretches to deep pursuits and leaving the rest open to everything else."（Rule #1, *The Bimodal Philosophy of Deep Work Scheduling*）（已据原文核）

> "This philosophy argues that the easiest way to consistently start deep work sessions is to transform them into a simple regular habit... to generate a rhythm for this work that removes the need for you to invest energy in deciding if and when you're going to go deep."（Rule #1, *The Rhythmic Philosophy of Deep Work Scheduling*）（已据原文核）

> "I call this approach, in which you fit deep work wherever you can into your schedule, the journalist philosophy."（Rule #1, *The Journalistic Philosophy of Deep Work Scheduling*）（已据原文核）

## I：核心解释

1. **先接受一个前提：意志力是有限的，会耗尽。** 书里引用 Hofmann 与 Baumeister 的研究——人们一整天都在和欲望搏斗，"Desire turned out to be the norm, not the exception."；而由于自控会消耗有限的意志力，那些诱惑常常赢。所以排程的目标不是"下决心多做深度工作"，而是**用固定套路减少进入与维持专注所需的意志力**（Rule #1 引言）。
2. **四种方式解决同一个问题，代价不同。** 禁欲派砍掉绝大部分浅层；双峰派把时间切成"深度段"与"开放段"；节奏派把深度工作变成每天同一时段的固定习惯；新闻记者派见缝插针、随时切进深度模式。选错方式会让习惯"在稳固之前就崩掉"（R 第一条）。
3. **选哪种，取决于三件事**（本书给的判据，不是性格测试）：
   - **岗位产出形态**：若你的贡献是书里说的"discrete, clear, and individualized"（离散、清晰、个人化，如写书、做理论），禁欲派才现实。
   - **日程自主度**：双峰派要求你能消失至少一整天（书里点名 "the minimum unit of time for deep work in this philosophy tends to be at least one full day"）；而"one of the most common among deep workers in standard office jobs"的是节奏派。
   - **熟练度**：新闻记者派"is not for the deep work novice"——从浅层快速切进深度靠的是练出来的能力和既有职业成就带来的自信；新手用它会迅速耗光意志力。
4. **节奏派与双峰派的取舍，是强度与总量的取舍。** 书里说双峰派可能达到最强的深度强度，但节奏派"works better with the reality of human nature"，一年下来总的深度小时数常常更高（*The Rhythmic Philosophy*）。
5. **选好方式只是一半，还要配"仪式"。** 书里要求仪式固定三件事：在哪里做、做多久；开始后怎么工作（如禁用网络、按某个指标盯着自己）；怎么支持你的工作（咖啡、食物、走路、把材料摆好以减少摩擦）（*Ritualize*）。

## A1：来源应用 — 书里的四种排程方式

书上给了四个范本（照书选，别自造第五种）：

- **禁欲派 Monastic**：Donald Knuth 自 1990 年起不再用邮箱，只留一个邮政地址，助理筛信、非紧急的三个月集中处理一次；Neal Stephenson 的声明是 "All of my time and attention are spoken for—several times over. Please do not ask for them."。适合产出离散清晰、能对价值主张一刀切的人。
- **双峰派 Bimodal**：Jung 平时在苏黎世行医、泡咖啡馆、讲学，只在 Bollingen 石屋闭关时完全无扰；Adam Grant 把课程压进一个学期，另一学期里每月有一两次连续两到四天的闭关。适合离不开大量非深度事务、但能挤出整段的人。
- **节奏派 Rhythmic**：Seinfeld 的"链条法"——每天写了笑话就在日历上画一个红叉，"Just keep at it and the chain will grow longer every day... Your only job next is to not break the chain."；Brian Chappell 每天五点半（后提前到四点四十五）写到七点半再去上班，自称 "both astronomically productive and guilt free"。
- **新闻记者派 Journalistic**：Walter Isaacson 度假时 "could retreat up to the bedroom for a while... he'd go up for twenty minutes or an hour"，见缝插针写完了八百多页的《The Wise Men》。作者自述这是他本人主用的方式，但他补充并不"纯用"——会在每周初、每日初先大致规划深度工作时间，以减少临场决策。

## A2：典型触发场景

- 全职上班 + 想读博/写书，问该早上挤两小时还是攒整块周末。
- 自由职业者，日程碎，问怎么把深度工作塞进去。
- 研究/创作型岗位，纠结要不要干脆关掉一部分沟通渠道。
- 刚换到标准办公室岗位，发现以前那套"整块闭关"行不通了。
- 试过一段时间某种方式后崩了，想知道是不是方式选错了。

## E：执行步骤

### 步骤1：确认"意志力有限"这个前提在你的描述里成立

**输入**：用户现在是怎么安排（或想怎么安排）深度工作的。
**输出**：一句判断——困难是"方式没定"，还是"方式定了但总被即时欲望打败"。

🔴 **CHECKPOINT — 触发条件：用户一开口就是"我就是不够自律/我意志力太差"**：不要顺着做品格评判。把话头拉回机制："书里的说法是——意志力像肌肉，会累，用一点少一点。我们要做的不是让你更能忍，而是设计一套让你**少用意志力**的固定套路。" 若用户描述的是持续的情绪耗竭、失眠、焦虑到影响生活 → 转 B 节安全分支，先谈休息与求助，不排深度工作。

### 步骤2：给岗位产出形态定性

**输入**：用户的工作产出是什么。
**输出**：产出属于"离散、清晰、个人化"（写书、做理论、独立创作）还是"多样、模糊、需要协作"（管理、运营、业务）。

用书里那把尺子：你的专业成功是否"comes from doing this one thing exceptionally well"？是 → 禁欲派进入候选；否 → 禁欲派基本排除。

### 步骤3：给日程自主度定性

**输入**：用户能否在正常工作日消失几小时到几天。
**输出**：能不能容纳"至少一整天"的无扰段。

- 能消失整段（哪怕只是每月一两次）→ 双峰派进入候选。
- 只能保证每天同一小块时间、boss 的消息还得及时回 → 节奏派进入候选。
- 日程完全不可预测、随时有空隙但都不长 → 新闻记者派进入候选。

### 步骤4：给熟练度定性并定案

**输入**：用户是否已能较轻松地进入深度状态、是否有拿得出手的既有成果。
**输出**：从四种里**选定一种**，并写出"为什么不是另外三种"。

🔴 **CHECKPOINT — 触发条件：用户的产出像禁欲派（离散清晰），但日程完全没有自主度（必须随时在线）**：不要硬推禁欲派。书里对这种 mismatch 有明确警告——选错方式会让习惯在稳固前就崩掉。把它降级成"在某个固定时段做局部沟通隔离"，或先用节奏派起步，并在步骤4 的"为什么不是禁欲派"里写清这个降级理由。

给"为什么不是另外三种"的模板（每条一句，必须引到上面 I、A1 的判据，不许写"你不适合"这类空话）：
- 不是禁欲派：因为你的产出是 ____（多样/协作型），砍掉浅层会伤到核心职责。
- 不是双峰派：因为你无法保证"at least one full day"的无扰段，或你能但熟练度撑不起整天的强度。
- 不是节奏派：因为你的日程无法固定同一时段，或你已能进入深度，节奏派会低估你达到的强度。
- 不是新闻记者派：因为书里明说它"is not for the deep work novice"，或你缺乏支撑快速切换的既有成果与自信。

### 步骤5：配套三件事的仪式

**输入**：选定方式。
**输出**：一段可执行的仪式描述，覆盖书里要求的三个问题——在哪里做、做多久；开始后怎么工作；怎么支持你的工作。

照书里的问题逐条填。例如双峰派："闭关地点=____；时长=一次连续____天；开始后=禁用网络、按____指标自查；支持=____"。

### 步骤6：定一个"换方式的信号"

**输入**：新方式的落地描述。
**输出**：一句"什么情况下该换"，防止用户崩掉时又归因于自己不够自律。

例：连续两周做不到固定时段 → 把节奏派降级为更短更固定的时段，或改成新闻记者派；能稳定做到且熟练度上来 → 升级到双峰。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把方式选错当"我不行" | 试了禁欲派两周崩了，结论"我就是做不了深度工作" | 回到书里的警告：mismatch 会让习惯在稳固前就崩；是方式不匹配，不是人不行。换一种重排。 |
| 用禁欲派逃避本职工 | 明明是协作/管理岗，却拿"我要闭关"切断该有的响应 | 书里承认大部分知识工作岗需要相当量的浅层；禁欲派只适用于产出离散清晰的人。 |
| 新手直接上新闻记者派 | 没练过、也没有既有成果背书，却想随时切进深度 | 书里明说"not for the deep work novice"；先练 deepwork-embrace-boredom，或先按节奏派起步。 |
| 双峰做成"想闭关就闭关" | 没有事先划清并公开的固定段 | 书里强调段要"well defined and well advertised"；临时起意的消失既伤关系也守不住。 |
| 只排程、不配仪式 | 定了时段，但每次开始前还在纠结用什么工具、做什么 | 回到 *Ritualize*：在哪、多久、怎么工作、怎么支持，四件事不落地就还得耗意志力。 |
| 长期耗竭/失眠/焦虑 | 用户描述持续疲惫、睡不着、提不起劲 | 🛑 停止排程讨论，转安全分支。 |

### 边界规则

1. **不做品格评判**：本 skill 只选排程方式、配仪式，不评价用户是否自律。"意志力有限"是书里的机制前提，不是对人的判决。
2. **不发明第五种方式**：书里就四种；用户的情况不符就回退到其中一种，不要自造新名词。
3. **方式可换**："choose a philosophy that fits your specific circumstances"——情况变了就重选，换不是失败。
4. **安全兜底**：若对话涉及持续的情绪耗竭、抑郁、失眠、或有自伤念头，立即停止排程工作，指向专业资源（心理援助热线 12356；紧急情况拨 120/110），不做诊断。

### 用户自查清单

- [ ] 我能说出我选的是四种里的哪一种（不是"混合着来"）
- [ ] 我能说出**为什么不是另外三种**，且理由基于岗位产出/自主度/熟练度
- [ ] 我按书里三个问题写好了仪式（在哪/多久、怎么工作、怎么支持）
- [ ] 我知道**什么信号出现时该换方式**
- [ ] 我没有把"做不到"归因于自己意志力差

**勾选 4+ 项**：排程到位。**≤2 项**：回到对应步骤重做，尤其别跳过步骤 2–4 就定案。

## 📖 练习手册

第一周先只做一件事：按选定的方式做，并记录每天**实际进入深度状态的时长**，一周后对着记录回看——是方式不合，还是仪式没配齐（练习记录保存在用户批准的位置）。

## 🚫 反例与黑名单

1. **把"意志力有限"当成"我很弱"的证明** → 🛑 机制说明不等于品格判决。
2. **给所有人推禁欲派**（把"关掉邮箱"当成通用的深度工作法）→ 书里明说适用人群有限，对多数岗位会伤及本职工。
3. **让新手直接上新闻记者派** → 违反书里"not for the deep work novice"的明示。
4. **用排程名义切断必须的响应**（医护、值班、危机响应等角色）→ 本 skill 不适用，先守住职责。
5. **把双峰/节奏做成"想做了才做"** → 那就不是排程，回到书里"ad hoc 不可行"的结论。

### 灰色地带（需谨慎判断）

6. **用户是创业者/自由职业者，产出既想清晰又想多样** → 先按"最像哪一种"选，再用两周实测；书里承认这类取舍需要练习和试验。若仍定不下来 → 转 deepwork-shallow-shutdown 先把浅层压下来，方式会更容易浮现。
7. **用户先问排程，其实真正卡点是"一停工就内疚"** → 这更接近收工问题，转 deepwork-shallow-shutdown 的固定下班点与收工仪式。
8. **用户在治疗/休假中** → 优先遵医嘱与休息安排；本 skill 只在其恢复后作为复工排程的参考。
