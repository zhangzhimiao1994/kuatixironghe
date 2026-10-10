---
name: deepwork-shallow-shutdown
description: 浅层工作封顶。当用户说"我一天忙到晚却没做成一件真正重要的事""邮件会议填满整天""感觉自己时间被切碎""不知道一天该少做哪些事"时使用。用"培训一个聪明应届生接手要几个月"给任务分深浅，给浅层定上限（30–50%）、定固定下班点、用纸面时间块排一天。到点收工那一刻怎么做（收工仪式）走 deepwork-shutdown-ritual。不评价用户是否自律。
input_schema:
  required: [task_list, work_end_time, deep_work_goal]
  optional: [boss_context, schedule_habit, email_load]
output_schema:
  primary: {shallow_classification, shallow_budget, fixed_schedule_plan, time_block_plan}
  secondary: [email_rules, weekly_review_prompt]
---

# 浅层封顶：给浅层划条线，给一天排上纸面时间块

**来源**：《Deep Work》Rule #4: Drain the Shallows ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- "我一天忙到晚，却没做成一件真正重要的事。"
- "邮件和会议把一整天填满了，我的正事只能在夜里做。"
- "我想知道自己是不是把太多时间花在浅层工作上了。"

**不应触发**：
- 用户在问下班后怎么真正关掉、收工仪式怎么做（走 deepwork-shutdown-ritual）
- 用户在问该用哪种深度工作排程方式（走 deepwork-depth-philosophy）
- 用户在练"能专注多久"本身（走 deepwork-embrace-boredom）
- 用户在问某个 App 该不该留（走 deepwork-craftsman-tools）
- 用户所在岗位的"浅层"是职责本身（值班、急救、客服一线）→ 不能按 30–50% 硬套，先守住职责

## R：原文锚点

> "Shallow Work: Noncognitively demanding, logistical-style tasks, often performed while distracted. These efforts tend to not create much new value in the world and are easy to replicate."（Introduction）（已据原文核）

> "How long would it take (in months) to train a smart recent college graduate with no specialized training in my field to complete this task?"（Rule #4, *Quantify the Depth of Every Activity*）（已据原文核）

> "For most people in most non-entry-level knowledge work jobs, the answer to the question will be somewhere in the 30 to 50 percent range (there’s a psychological distaste surrounding the idea of spending the majority of your time on unskilled tasks, so 50 percent is a natural upper limit, while at the same time most bosses will begin to worry that if this percentage gets too much lower than 30 percent you’ll be reduced to a knowledge work hermit who thinks big thoughts but never responds to e-mails)."（Rule #4, *Ask Your Boss for a Shallow Work Budget*）（已据原文核）

> "I call this commitment fixed-schedule productivity, as I fix the firm goal of not working past a certain time, then work backward to find productivity strategies that allow me to satisfy this declaration."（Rule #4, *Finish Your Work by Five Thirty*）（已据原文核）

## I：核心解释

1. **先把深浅的尺子立起来。** 书里对浅层的定义是"不需要认知投入、后勤式的任务，常在心不在焉时完成，且容易复制"。有些事一眼就浅（查邮件、约电话会），有些很模糊（编辑学术稿、做季度销售 PPT、开项目状态会）——所以书里给了一个可操作的判据：**要培训一个聪明应届生接手你这项任务，需要几个月？**
2. **应届生问题的用法**：需要很多个月才能接手 = 用到你"hard-won expertise"的深度任务；一两周能上手 = 浅层。书里演示：#1 编辑学术论文 → 约 50–75 个月；#2 做季度销售 PPT → 约 2 个月；#3 开项目状态会 → 约 3 个月。它是个思想实验，不是真去招人。
3. **浅层要有硬上限，不能凭感觉。** 书里建议去问"我该花多少比例的时间在浅层工作上"，非入门级知识工作岗的答案多在 **30–50%**。定了就守住——这一步的作用是把"每一件看起来都合理"的碎片，汇成一个能被看见的总量。
4. **固定下班点（fixed-schedule productivity）= 先钉"几点必须收工"，再倒推做法。** 书里说这是"meta-habit"，简单但影响面极广；如果只能挑一个行为把焦点重新掰回深度，这个该排在前列。它逼你进入稀缺心态：任何超出你最深努力的事务都变得可疑，默认答案是"不"。
5. **纸面时间块让"剩下的时间"也有归宿。** 每天开工前把工作时段切成块、每块给一件事，最小三十分钟。估时不准、被打断都是常态，书里说不要执着于"守住计划"，要的是"对剩下的时间始终保持有意识的决定"。

## A1：来源应用 — 书里 Rule #4 的具体做法

- **Schedule Every Minute of Your Day（纸面时间块）**：在专用笔记本上，每天开工前划出当天的时段，每块分配一件事（最小三十分钟），类似的碎事可以合并成一个"任务块"。两个必然出问题——估时不准、被打断；被打断就在下一个空档重画剩下的。书里给了三个稳定技巧：**保守估时**、**"溢出条件块"**（给一件时间不确定的事多排一个"要么继续、要么干别的"的块）、**多用、用长任务块**。并允许"重要洞察出现就推翻当天计划"。
- **Quantify the Depth of Every Activity**：对每项任务套应届生问题，得出月数，再"bias your time toward the former"（把时间偏向深度那一侧）。
- **Ask Your Boss for a Shallow Work Budget**：和 boss 谈一个明确比例并守住；先给对方解释"深/浅"是什么。若答案是"需要多少浅层就做多少"，书里说这告诉你**这个岗位不支持深度工作**，该开始规划换岗。
- **Finish Your Work by Five Thirty**：fixed-schedule productivity。书里举 Radhika Nagpal 的例子——设每周五十小时上限，然后用"一年只出差五次""限制每年审稿数"这类硬配额去满足它。拒绝时"to be clear in my refusal but ambiguous in my explanation for the refusal"（说得清楚，但不给能被人拆解的具体借口），也不要给一个会吞掉你日程的"安慰奖"（如"我参加不了委员会，但可以帮你看提案"）。
- **Become Hard to Reach（邮件三招）**：**sender filter**（让发信人先自我筛选，如只留一个"有意思的机会"专用地址并声明"我只会回复合适的机会"）；**process-centric email**（回信时先说清这件事是什么项目、现在到哪一步、下一步是什么，一次说清以减少来回）；**professorial 不回复**（三条判据：信息含糊难以合理回应、不是你会感兴趣的问题或提议、回了没有好事不回也没有坏事——则不回）。

## A2：典型触发场景

- 日历上排满会议，一天下来没有一段属于自己的大块时间。
- 邮件一打开就是两小时，正事只能拖到夜里。
- 想给团队引入"少开点会、多做点事"，但不知道从哪下手。

## E：执行步骤

### 步骤1：抓任务清单，逐项打"深浅分"

**输入**：用户当前手上的任务清单（或由用户口述）。
**输出**：每项任务标注——应届生接手需要几个月 + 归为深/浅。

用书里那句话做判据。例："编辑一篇学术稿 → 50–75 个月（深）""做季度销售 PPT → 约 2 个月（浅）""参加项目状态会 → 约 3 个月（浅）"。

🔴 **CHECKPOINT — 触发条件：用户是入门/一线岗，任务几乎全是浅层**：不要粗暴地劝用户"拒绝浅层"。书里明说入门级要**先积累技能**再往职责里加深度任务。改为：帮用户在现有浅层里找出可"批处理、可压缩"的部分，腾出小块时间做技能成长。

### 步骤2：给浅层定一个上限

**输入**：步骤1 的分类结果。
**输出**：一个具体比例（书里的默认区间 30–50%）+ 一句守住它的说法。

🔴 **CHECKPOINT — 触发条件：用户说"我老板不可能同意给我定这个比例"**：分两种处理。① 能谈 → 先按书里做"和 boss 的预算对话"，给对方解释深/浅；② 谈不动 → 引用书里的话：一个把"需要多少浅层就做多少"当答复的岗位，是不支持深度工作的岗位，该开始规划换岗——但这属于职业决策，别替用户下结论，只把这条逻辑摆在桌上。

### 步骤3：定固定下班点

**输入**：用户当前的实际收工时间 + 想要的收工时间。
**输出**：一个被钉死的收工时间 + 至少两条为满足它而设的"硬配额"。

照书里：先定时间，再倒推。硬配额可参考 Nagpal——限制出差次数、限制某项重复性工作（审稿/接私活/加群）的数量。拒绝时"说清楚、不解释细节"。

### 步骤4：排纸面时间块

**输入**：用户的典型工作日。
**输出**：一份当天的时间块草稿。

时间块：开工前划块，最小三十分钟；用"溢出条件块"和保守估时；被打乱就在下一个空档重画。到点收工那一刻怎么做（看邮箱→转清单→扫清单日历→排明日计划→说完成语）走 deepwork-shutdown-ritual。

### 步骤5：一周后回看比例并调整

**输入**：一周的时间块/浅层记录。
**输出**：实际浅层占比 + 一个调整动作。

对照步骤2 定的上限。超了就找"最该砍的一件"，不足就保持。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把浅层当敌人全面开战 | 想 100% 深度，拒掉所有邮件会议 | 书里明说大部分知识工作岗需要相当量浅层；目标是"驯服"而非消灭。 |
| 时间块做成僵硬军规 | 一被打断就自责、非要死守计划 | 回到书里：估时不准和打断都是常态；目标是"对剩余时间保持有意识的决定"，不是守住计划。 |
| 拿数值当道德分 | 把 30–50% 当成"好坏评分"，超了就自责 | 比例是帮你看见总量的工具，不是品格评分；回到"把时间偏向深度那一侧"的动作。 |
| 忽略岗位性质硬套 | 一线/急救岗也去谈"浅层预算" | 先守住职责；这类岗位的"浅层"是本职，不套用本 skill 的比例。 |
| 长期耗竭/失眠 | 用户描述持续疲惫、睡不着、提不起劲 | 🛑 转安全分支。 |

### 边界规则

1. **不做品格评判**：不评价用户是不是自律、是不是"工作狂"或"懒"。本 skill 只调时间结构。
2. **不发明数字**：30–50% 是书里给的默认区间，不是硬标准；岗位不同可调，但要写清依据。
3. **换岗是职业决策**：书里给了"谈不动就考虑换岗"的逻辑，但把决定权交给用户，只摆事实。
4. **安全兜底**：若用户描述持续耗竭、失眠、焦虑，或有自伤念头，停止时间管理讨论，指向专业资源（心理援助热线 12356；紧急情况拨 120/110），不做诊断。

### 用户自查清单

- [ ] 我能对每项任务说出**应届生接手要几个月**
- [ ] 我有一个**写在纸上的浅层上限**，并知道这周实际占比
- [ ] 我有一个**被钉死的收工时间**
- [ ] 我在用**纸面时间块**排一天，且允许它被打乱后重画

**勾选 3 项**：结构到位。**≤1 项**：多半只做了一个动作，回对应步骤补齐。收工那一刻怎么做（收工仪式），走 deepwork-shutdown-ritual。

## 📖 练习手册

第一周先做两件小事：① 周一开工前用纸划块排一天（只排一天）；② 给浅层定个上限并记下实际占比（练习记录保存在用户批准的位置）。

## 🚫 反例与黑名单

1. **把"抓浅层"变成办公室政治**（拿本 skill 去要求同事都少发邮件）→ 先管自己；书里的比例对话是与 boss 的，不是拿来管别人的。
2. **用固定下班点逃避该做的事**（把紧急职责也推掉）→ 书里说"If you need more time, then extend your workday"，这条是纪律不是借口。
3. **给所有人套 30–50%** → 入门岗、一线岗不适用，书里对入门岗明确要"先积累技能"。
4. **把"应届生能接手"当成贬低他人** → 这条问题只用来给**你自己的任务**分类，不是给同事的能力打分。

### 灰色地带（需谨慎判断）

6. **用户是管理者，自己时间可控但团队时间不可控** → 书里的做法（浅层预算、时间块）仍然可用（收工那一刻怎么做走 deepwork-shutdown-ritual）；但"浅层预算"要先落到自己的工作，再谈团队（书里也提到希望办公室通讯有类似规则，但承认短期做不到）。
7. **用户真正的问题是"一停工就内疚"或晚上关不掉** → 这属于收工与注意力恢复，走 deepwork-shutdown-ritual（Rule #1 *Be Lazy*）；本 skill 只管浅层封顶。
8. **用户在做治疗/处于 burnout 恢复期** → 优先休息与遵医嘱，本 skill 只作复工后重建时间结构的参考。
