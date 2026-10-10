---
name: deepwork-quality-leisure
description: 用有质量的休闲替代被动娱乐（娱乐型站点/短视频/资讯流）。当用户说"我一有空就刷短视频停不下来""删了 App 又换网站继续刷""晚上和周末一刷就没了""明知道刷完空虚还是停不下来""想让休息时间过得有点质量"时使用。照 Bennett 的"一天中的一天"思路，先把晚上和周末预先安排好（阅读、结构化爱好、运动、见真人），用有质量的休闲填空，让退不掉的娱乐站点失去抓力。这不是戒网，也不做道德评判；判断某工具该不该留请走 deepwork-craftsman-tools。
input_schema:
  required: [leisure_windows, current_default, preferred_activities]
  optional: [tempting_sites, energy_level, in_person_available]
output_schema:
  primary: {vacuum_windows, preplanned_leisure_plan, quality_alternatives}
  secondary: [reading_program, vacuum_fill_defaults, review_point]
---

# 有质量的休闲：把"一天中的一天"先安排好，让娱乐站点失去抓力

**来源**：《Deep Work》Rule #3: Quit Social Media，子策略 *Don't Use the Internet to Entertain Yourself*（并引 Arnold Bennett《How to Live on 24 Hours a Day》） | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我一有空就刷短视频/资讯站，停不下来。"
- "我已经删了那个 App，但现在换个网站继续刷。"
- "晚上和周末一刷就没了，回头看一片空白。"
- "等电梯、排队、吃饭的空档，手就不自觉去摸手机。"
- "我想让休息时间过得有点质量，但又不想把自己逼成戒网。"

**不应触发**：
- 用户要判断某个社交/工作工具该不该留（走 deepwork-craftsman-tools 逐工具算账）
- 用户要处理浅层工作太多、下班关不掉（走 deepwork-shallow-shutdown）
- 用户要练"能专注多久"本身、或想处理无聊（走 deepwork-embrace-boredom）
- 用户要选深度工作的排程方式（走 deepwork-depth-philosophy）
- 用户要戒断的是成瘾行为、或出现自伤念头 → 指向专业帮助

## R：原文锚点

> "These sites are especially harmful after the workday is over, where the freedom in your schedule enables them to become central to your leisure time."（Rule #3, *Don't Use the Internet to Entertain Yourself*）（已据原文核）

> "these network tools are not something you join and therefore they're not something you can remove from your life by quitting (rendering the previous two strategies irrelevant)."（同上）（已据原文核）

> "Put more thought into your leisure time."（同上）（已据原文核）

> "when it comes to your relaxation, don't default to whatever catches your attention at the moment, but instead dedicate some advance thinking to the question of how you want to spend your "day within a day.""（同上）（已据原文核）

> "Addictive websites of the type mentioned previously thrive in a vacuum: If you haven't given yourself something to do in a given moment, they'll always beckon as an appealing option. If you instead fill this free time with something of more quality, their grip on your attention will loosen."（同上）（已据原文核）

> "give your brain a quality alternative"（同上）（已据原文核）

> "the mental faculties are capable of a continuous hard activity; they do not tire like an arm or a leg. All they want is change—not rest, except in sleep."（同上，引 Bennett）（已据原文核）

## I：核心解释

1. **娱乐型站点和社交工具不是一回事**：社交服务是"加入"的，可以用退出实验处理；资讯/短视频类站点书里说"not something you join"，删不掉、退不掉，永远一次点击之遥——所以只能换方法，不能靠移除。
2. **最危险的是下班之后**：日程一自由，这些站点就成了你休闲时间的中心。你以为在放松，其实是把注意力交给"精心设计来抓你"的算法（书里说这是 a blur of distracted clicks on least-common-denominator digital entertainment）。
3. **它还会钝化你抵抗分心的能力**：书里说，等电梯、等剧情、等饭好，随手刷就把每个空档填满，这会 weaken your mind's general ability to resist distraction，让之后想做深度工作时更难集中。
4. **Bennett 的解法是"多想一步"**：不要默认当下抓到什么就刷什么，而是提前想清楚"一天中的一天"要怎么过——把晚上和周末**预先安排好**。
5. **机制是"真空"**：娱乐站点在真空里才猖狂。你不给当下安排别的事，它们永远是诱人的选项；你用更有质量的东西填满，它们的抓力就松了。
6. **结构化休闲不会让你更累**：书里借 Bennett 说，心智不像手脚会累，它要的是 change，不是 rest（除了睡眠）。给头脑填上有意义的事，你反而结束得更满足、第二天更放松。

## A1：来源应用 — 书里那套"安排休闲"

书里先坦白：Bennett 把"读诗与名著"当作提升中产灵魂的道德方案，作者自己都不买账（觉得 antiquated and classist）。但**逻辑内核**——你既应当、也能够刻意地用工作之外的时间——今天仍然成立。

**照书的具体做法**：
- **提前决定**："figure out in advance what you're going to do with your evenings and weekends before they begin."
- **结构化爱好**（structured hobbies）：能给出具体动作与具体目标的填时间方式。
- **固定阅读计划**（à la Bennett）：每晚固定时间，推进一组**刻意选定**的书。
- **运动**，以及 the enjoyment of good (in-person) company——见真人。

**作者的示范**：孩子睡后，他预先安排的休闲活动就是读一本有趣的书；结果手机和电脑从下班到第二天早上都"remain neglected"。

**收尾口径**：若要消掉娱乐站点对时间与注意力的成瘾性拉扯，就"give your brain a quality alternative"——否则你会 allow your mind to bathe for hours in semiconscious and unstructured Web surfing。目标不是效率，是像 Bennett 说的那样 live, and not just exist。

## A2：典型触发场景

- 一有空档（排队、等电梯、吃饭）手就摸向手机。
- 删了 App 却换资讯网站/短视频网页继续刷。
- 晚上躺床上刷到半夜，第二天疲惫。
- 周末本想休息，回头发现全耗在了无意识点击上。
- 想给休息时间找点"更有质量"的过法，但不知道从哪下手。

## E：执行步骤

### 步骤1：标出"娱乐真空"出现的时间窗

**输入**：用户一天的作息与自由时间。
**输出**：2–3 个最容易滑进刷手机的时段（如通勤、午休、晚饭后、睡前）。

书里说这些站点专挑下班后的自由时间下手；先找出你自己的自由时段。

🔴 **CHECKPOINT — 触发条件：用户说"我只是想少刷点，给我个每天不超过多少分钟的上限"**：本 skill 不给通用时长上限（那是 deepwork-shallow-shutdown 的活）。回应：这里改问——这些时段你想拿来做点什么更有质量的事？

### 步骤2：为每个时段预先安排一件有质量的休闲

**输入**：步骤1 的时间窗 + 用户已有的兴趣/资源。
**输出**：每个时段对应一件具体活动（阅读计划 / 结构化爱好 / 运动 / 见真人），且要提前想好、有具体目标。

照书：figure out in advance what you're going to do with your evenings and weekends before they begin；structured hobbies 要"generate specific actions with specific goals"。

🔴 **CHECKPOINT — 触发条件：用户安排的"替代"是"那我看另一个平台的视频/换刷别的资讯"**：这不是质量替代，是被动娱乐换皮。拉回书里标准：要的是 change、是具体动作与具体目标，而不是另一种 least-common-denominator digital entertainment。

### 步骤3：把"真空"填上——给碎片空档定默认动作

**输入**：步骤1 标出的碎片空档。
**输出**：每个空档的一个默认替代动作（而非"刷手机"）。

机制：站点在真空里猖狂；你给当下安排了别的，它们就不 beckon 了。

🔴 **CHECKPOINT — 触发条件：用户说"我就是要无聊时有个东西看"**：提醒——把每个空档都填满会 weaken your mind's general ability to resist distraction；这里追求的不是消灭无聊，是别让刷手机当默认。真要练"能忍受无聊/专注"，走 deepwork-embrace-boredom。

### 步骤4：回应"这样休息还算休息吗"的反诘，并定复查点

**输入**：用户担心结构化休闲会累、会毁掉放松。
**输出**：一句回应 + 一个复查点。

回应（照书引 Bennett）：心智不像手脚会累，它要的是 change 而非 rest；"Won't a structured evening leave you exhausted—not refreshed—the next day?" 这个担心误解了什么给人充电——给头脑填上有意义的事，你结束得更满足、第二天更放松。

复查：一周后回看哪些时段被成功替代、哪些又滑回娱乐站点；滑回的时段回步骤2 重排。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把质量休闲变成任务清单 | 休闲排得像 KPI，反而更累 | 书里要的是 quality alternative，不是又一份 to-do；选你真想做的活动 |
| 用被动娱乐换皮 | "我把短视频换成刷资讯网页了" | 这不算替代；回到"具体动作+具体目标"的结构化活动 |
| 想靠删除解决 | "我卸载了，但换个网站还是会刷" | 娱乐站点退不掉；只能靠填空，不能靠移除 |
| 变成戒网/道德审判 | "我太堕落了，必须彻底断网" | 拉回：这不是善恶问题；是给注意力找质量替代，不做悔过 |
| 成瘾/自伤关联 | 刷到影响睡眠、情绪，或出现自伤念头 | 🛑 停止，指向专业帮助 |

### 边界规则

1. **不做道德评判**：不给"戒网光荣/不戒就堕落"的腔调。书里的框架是中性的：这是注意力的安排，不是悔过。
2. **不追求"消灭无聊"**：填空档是拿回默认选项，不是训练"永不无聊"。要练忍受无聊与专注本身，走 deepwork-embrace-boredom。
3. **质量替代由用户定**：读诗与名著是 Bennett 的口味，作者都不强推；照书只需"刻意安排 + 有质量"，具体是什么由用户选。
4. **这不是工具取舍**：要判断某个社交/工作工具该不该留（逐工具打 +/0/－、30 天实验），走 deepwork-craftsman-tools。
5. **安全兜底**：若涉及成瘾影响生活、睡眠、情绪，或有自伤念头，指向专业资源（心理援助热线 12356；紧急情况拨 120/110），不做诊断。

### 用户自查清单

- [ ] 我说得出自己哪些时段是"娱乐真空"高发区
- [ ] 我为晚上的自由时间**提前**安排了具体活动，而不是临场决定刷什么
- [ ] 我的替代是结构化/带具体目标的（阅读/爱好/运动/见真人），不是换个平台继续刷
- [ ] 我知道娱乐站点退不掉，只能靠填空而非删除
- [ ] 我准备好回应"这样还算休息吗"的疑虑

**勾选 4+ 项**：安排到位。**≤2 项**：多半是没提前安排，回步骤2。

## 📖 练习手册

今晚开始：在**晚饭前**就写下今晚和这个周末打算做的两三件有质量的事（一本书读几页、一次运动、约一个真人）。睡前回看：哪段时间本来会滑进娱乐站点，被什么替代了？坚持一周（练习记录保存在用户批准的位置）。

## 🚫 反例与黑名单

1. **建议"删掉所有娱乐站点/彻底断网"** → 书里明说这类站点退不掉，硬删无效；关键是填空。
2. **把休闲排成苦役**（"今晚必须读完这一章名著"）→ 违背 quality alternative 的本意；有质量不等于强迫。
3. **给"每天刷不超过 X 分钟"的通用上限** → 不是本 skill 的活；要上限、要处理浅层工作走 deepwork-shallow-shutdown。
4. **用本 skill 去要求他人**（劝家人朋友别刷手机）→ 只用于自己；这是自己注意力的安排。
5. **把质量休闲当逃避工作的借口** → 书里的前提是"工作之外刻意安排"，不是拿休闲掩盖白天该做的深活。

### 灰色地带（需谨慎判断）

6. **用户说"我就是靠刷这些放松，也没觉得有代价"** → 不硬套。照书只问：这些时段有没有让你更被动、之后更难专注？有明显代价才处理。
7. **用户的"休闲"其实就是某个社交工具** → 判断该不该留那个工具走 deepwork-craftsman-tools；本 skill 只处理娱乐型站点的替代。
8. **用户问"上班那 8 小时也算我的生活吗"（Bennett 的 day within a day）** → 可展开 Bennett 的观点（别把上班当"一整天"、把其余当序章尾声），但重心落到可执行的一步：自由时间也要刻意安排。
