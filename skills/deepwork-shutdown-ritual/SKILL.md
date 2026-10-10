---
name: deepwork-shutdown-ritual
description: 收工后真正关掉工作思绪。当用户说"下班了脑子还在转""关不掉""一停工就内疚""晚上老惦记没回的邮件"，或"白天被会议切碎、只能熬夜补"时用。先复述用户的具体处境，再分辨是"停不下来"还是"没有整块时间"，两类分开处理，不套同一套动作。涉及持续耗竭、失眠、长期低落时先转专业求助。不评价用户是否自律。
input_schema:
  required: [work_end_time, unfinished_items, evening_pattern]
  optional: [inbox_load, ritual_attempts, weekend_pattern, fragmentation_source]
output_schema:
  primary: {closure_action, completion_phrase, no_incursion_rule}
  secondary: [downtime_reasons, weekly_review_prompt]
---

# 收工：先分清是哪一类"关不掉"

**来源**：《Deep Work》Rule #1 *Be Lazy* ｜ 证据等级：firsthand

## 触发条件



**应触发**：关不掉、反刍、做梦排任务、一休息就内疚、周末看工作消息毁心态；或白天被会议/消息切碎、只能熬夜补。

**不触发**：定浅层比例或固定下班点（shallow-shutdown）／练专注力（embrace-boredom）／选排程（depth-philosophy）／选工具（craftsman-tools）／持续疲惫失眠低落（🛑 转安全）。

## R：原文锚点



> "In more detail, this ritual should ensure that every incomplete task, goal, or project has been reviewed and that for each you have confirmed that either (1) you have a plan you trust for its completion, or (2) it’s captured in a place where it will be revisited when the time is right."（Rule #1, *Be Lazy*）（已据原文核）

> "When you work, work hard. When you’re done, be done."（Rule #1, *Be Lazy*）（已据原文核）

> "once your workday shuts down, you cannot allow even the smallest incursion of professional concerns into your field of attention. This includes, crucially, checking e-mail, as well as browsing work-related websites."（Rule #1, *Be Lazy*）（已据原文核）

> "If you need more time, then extend your workday, but once you shut down, your mind must be left free to encounter Kreider’s buttercups, stink bugs, and stars."（Rule #1, *Be Lazy*）（已据原文核）

> "A shutdown habit, therefore, is not necessarily reducing the amount of time you’re engaged in productive work, but is instead diversifying the type of work you deploy."（Rule #1, *Be Lazy*）（已据原文核）

> "it should take a week or two before the shutdown habit sticks—that is, until your mind trusts your ritual enough to actually begin to release work-related thoughts in the evening."（Rule #1, *Be Lazy*）（已据原文核）

## I：核心解释



1. **为什么靠"说一句我下班了"关不掉：Zeigarnik 效应。** 书里说这个效应描述的是"未完成的任务会支配我们的注意力"。如果五点钟直接停下、宣布"今天到此为止"，脑子里那些没解决的义务会"keep battling for your attention throughout the evening（a battle that they'll often win）"。所以关不掉不是意志问题，是缺一个把未完成事项交接出去的动作。
2. **收工仪式就是对 Zeigarnik 效应的算法。** 它不要求你为清单里每一件事都写计划（书里说那是"a burdensome requirement"），只要求：把每件没完成的事**要么配一个你信得过的完成计划，要么放进一个会在恰当时候被再看到的地方**——剩下交给系统。书里说："Your mind... is released from its duty to keep track of these obligations at every moment—your shutdown ritual has taken over that responsibility."
3. **书里给收工三条支持理由。** ① 离线助洞见（unconscious thought theory）：让意识脑休息，无意识才接手处理最复杂的难题——所以收工"is not necessarily reducing the amount of time you're engaged in productive work, but is instead diversifying the type of work you deploy"；② 恢复注意力（attention restoration theory）：走神散步、做饭听歌、陪孩子玩、跑步这类事和散步看夕阳一样给定向注意力充电，但前提是**不受打扰**；③ 晚间能做的多半不重要：一天的深度容量（书里引 Ericsson：专家每天高强度专注不过四小时上下）在工作时间内已用完，夜里塞的多是低价值浅层活。
4. **硬边界：收工后任何工作思绪都不许闯入，包括查邮件。** 书里说"even the smallest incursion"都不行——瞥一眼工作消息会产生"a self-reinforcing stream of distraction"，把收工的好处抵消很久（书里举的例：周六早上瞄到一封让人不安的邮件，整个周末都被它的含义缠住）。
5. **用一个固定完成语结束。** 书里本人的仪式以说 "Shutdown complete" 收尾；书里承认它"听起来傻"，但它给大脑一个简单线索：可以把工作思绪放掉一整天了。
6. **它一两周才抓牢，别指望第一天见效。** 书里说仪式要多花十到十五分钟，且要一两周大脑才"trusts your ritual"、开始在傍晚真正放手；一旦抓牢会变成固定习惯，"skipping the routine will fill you with a sense of unease"。
7. **与"定固定下班点"的分工。** 钉下"几点必须收工"是 Rule #4 的 fixed-schedule productivity（走 deepwork-shallow-shutdown）；本 skill 管的是**到点那一刻怎么做**——把未完成的事交接出去、然后真正放开。两者要一起用。

## A1：来源应用 — 书里的收工仪式



- **本人五步仪式（照书逐条）**：① 最后看一眼邮箱，确认没有必须马上回的；② 把脑子里或一天里随手记下的新任务**转入正式任务清单**；③ 打开这些清单，**快速扫过每一张清单的每一项**，再看未来几天的日历（这两步确保没有紧急的事被忘掉、没有截止日期或约会在逼近）；④ 用这些信息为**第二天排个大致计划**；⑤ 说完成语（书里说 "Shutdown complete"）——工作思绪到此为止。
- **完成语**：固定同一句话。书里说它"provides a simple cue to your mind that it’s safe to release work-related thoughts for the rest of the day"。
- **收工后的硬要求**：不查邮件、不刷工作网站，连最短暂的一次都不行。书里说"If you need more time, then extend your workday"，但一旦收工就完全放开。
- **三条支持理由**（书里）：离线助洞见、恢复注意力、晚间多做的是低价值浅层。
- **退出机制**：书里说要多花十到十五分钟、一两周才成习惯；这不是"又一件待办"。

## A2：典型触发场景



- 下班回家还在想某个没回复的消息或没结束的会议。
- 周末瞄一眼工作群，整个周末的心态都被搅乱。
- 躺床上脑子里自动播放明天的待办。
- 一停工就内疚，觉得"我是不是不够拼"。
- 试过对自己说"下班了"，但大脑不听，夜里又偷偷打开邮件。

## E：执行



### 先复述，再出手（硬要求）

先用自己的话复述用户的具体处境：几点下班、被什么切碎（哪些会/哪些群）、卡在哪一步、做梦梦到什么、焦虑到几点。没对准他的原话，不许先给方法，也别用客套话搪塞。

### 输出硬要求

- **先复述用户自己的细节再给动作**：先把他说的"几点下班、被什么切碎、焦虑到几点"用他的话讲一遍，再说怎么做；顺序颠倒即不合格。
- **正文 ≤800 字**：不铺陈、不列长清单，只说他要的那几步。
- **不露结构名**：不出现"E 节""分支""步骤2""失败模式""CHECKPOINT"这类内部名称，只说人话。

### 先分流：两类，两套走法（硬要求）

- 停不下来：人下班了却关不掉——反刍、做梦排任务、一休息就内疚。先处理"怎么关"。
- 没整块时间：白天被会议/消息切碎，只能熬夜补。先处理"怎么让它进得去"。
两类分别处理，不得都套同一套收尾动作。

#### 停不下来 → 交接没做完的事

停不下来，是没做完的事一直占着注意力。把今天没处理完的事过一遍：每件要么配一个信得过的下一步，要么放进一个之后会再看到的地方；最后说一句固定的话收尾（如"收工了"）。收工后连一封工作消息都不看——瞥一眼也会牵出一串分心。真做不完就延长今天，一旦收了就彻底放开。要一两周才见效。

🔴 **CHECKPOINT**：给动作之前先停下确认两件事，缺一不给动作——① 没把两类弄混：他讲的是"人下班了、脑子却关不掉"（反刍/内疚/做梦排任务），不是"白天被切碎、只能熬夜补"；两样都沾时以他先说、最疼的那一类为主，绝不混成一套。② 接下来要说的交接动作具体到"时间+地点"：今晚几点、在哪儿（书桌/餐桌/手机备忘）、逐件写下一步还是丢进明天会再看的清单——说不出"几点、在哪"就不过关。

#### 没整块时间 → 抢回一段写得出时段、关得掉入口的整块时间

别先动收工那头。先挑一个具体时段，把它从会议和群里抢回来。给动作前先按下面顺序说清四件事：

1. **哪天哪一段**：选明天（或后天）最不被固定的那一档，写成明确起止——"周X 的 8:30–10:00"或"把 13:30 那场例会推到周五后空出的 13:30–14:30"，不许说"找一段时间"。
2. **关掉什么/推掉什么**：这段时间里把群消息通知设成免打扰（企业微信/钉钉/Slack）、日历标忙碌、拒收可拒的临时会；点名一个能推或能并的会。
3. **只放哪一件事**：这段里只做一件需要连续投入的具体事，写出它的名字（如"写完方案第 2 节""做完竞品对照表"），不是一串待办。
4. **可打勾的完成标准**：到点前做到哪一步算成，一句能打勾——如"10:00 前方案第 2 节写完发给 X"。

其余会议和消息集中到固定时段（如 11:00–11:30、16:30–17:00）统一处理，别让它们随时插进来。有了这段真正属于你的整块时间，"只能熬夜补"的紧迫感才会降。

🔴 **CHECKPOINT**：给动作之前先停下确认两件事，缺一不给动作——① 没把两类弄混：他讲的是"白天被会/群切碎、时间进不去"，不是"下班后关不掉"；别把交接未完成事项那套搬过来。② 抢时间的动作已具体到"哪天哪个时段、关什么通知/推什么会、那段只放哪一件具体事、拿什么打勾"；只要还停在"抢一段不被打断的时间"这种通用话，就退回第 1 步重写。

## B：边界与失败模式



### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 仪式做成表面功夫 | 说了下班，晚上仍偷看邮件 | 书里说哪怕一次小闯入也会毁掉恢复；回到步骤3 的硬规则，要么延长工作日，要么彻底放开。 |
| 清单清不完就不做仪式 | 觉得"反正做不完，走形式没意义" | 回到 R 第一条：仪式不要求完成，只要求把每件事计划好或存好。 |
| 完成语怕傻、省掉 | 跳过最后一步，大脑收不到"可以放手"的线索 | 书里明说这句"听起来傻"但有作用；固定同一句，认真说。 |
| 仪式变负担 | 把收工做成又一件焦虑源 | 它只是十来分钟的固定动作；简单、固定即可，不必做得完美。 |
| 以为一天就能见效 | 头两天没效果就放弃 | 书里说一两周才抓牢；先坚持两周再评判。 |
| 长期耗竭/失眠 | 用户描述持续疲惫、睡不着、提不起劲 | 🛑 转安全分支。 |

### 边界规则

1. **不做品格评判**：不评价用户是不是自律、是不是"工作狂"或"懒"。本 skill 只调收工这一动作。
2. **不发明步骤**：五步仪式与完成语都来自书；要加自己的动作必须标（补充）。
3. **收工不是借口**：书里说"If you need more time, then extend your workday"——仪式是纪律，不是把该做的事推掉的理由。
4. **安全兜底**：若用户描述持续耗竭、失眠、焦虑，或有自伤念头，停止时间管理讨论，指向专业资源（心理援助热线 12356；紧急情况拨 120/110），不做诊断。

### 用户自查清单

- [ ] 我有一个被钉死的**收工时间**
- [ ] 我有一套**固定顺序的五步收工仪式**，每次都走
- [ ] 我有一句**固定的完成语**
- [ ] 收工后我**连一封邮件都不看**（守住硬边界）
- [ ] 我给它**至少两周**再评判效果

**勾选 4+ 项**：仪式到位。**≤2 项**：多半只说了"下班"没走仪式，回步骤2 补齐。

## 📖 练习手册



第一周只做一件事：连续七天在同一时间走完整套五步仪式、说同一句完成语，并记下"收工后有没有偷看工作消息"。两周后再回看——书里说大脑要一两周才信任仪式、开始真正放手（练习记录保存在用户批准的位置）。

## 🚫 反例与黑名单



1. **说"下班了"但不走仪式** → 违反 R 第一条；未完成的任务没被交接，会继续霸占注意力。
2. **收工后偷看邮件/工作网站** → 书里说哪怕最短暂的一次也会生成一串自我强化的分心，毁掉恢复。
3. **把收工仪式当借口逃避该做的事** → 书里说"If you need more time, then extend your workday"，这是纪律不是借口。
4. **省掉完成语嫌它傻** → 书里本人也承认它"cheesy"，但它正是给大脑的"可以放手"信号。
5. **把仪式做成又一件负担** → 简单固定即可，十来分钟，不是新工作。

### 灰色地带（需谨慎判断）

6. **用户是自由职业/远程办公，没有硬性下班点** → 更需要自己钉一个；先走 deepwork-shallow-shutdown 定固定下班点，再走本仪式。
7. **用户是管理者，晚上要临时处理紧急事务** → 允许"延长工作日"，但缩短、推后仍要补上仪式，别让打断变成常态（补充）。
8. **用户在做治疗/处于 burnout 恢复期** → 优先休息与遵医嘱，本 skill 只作复工后重建节奏的参考。
