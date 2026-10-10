---
name: mindset-maintain-change-willpower
description: 当改变已经开始、状态刚好转，你却担心会退回旧模式时使用。把"意志力是有就有、没有就没有的东西"这套固定读法，换成"改变是需要策略和主动维护的过程"，让一次好转不再以"又放弃了一次"收场。
input_schema:
  required: [changed_thing, relapse_pattern, lapse_story]
  optional: [maintenance_habit, past_lapse_response, support]
output_schema:
  primary: {maintenance_plan, lapse_reframe, willpower_view}
  secondary: [if_then, mirror_question, cautions]
---

# 维持改变：把「意志力」换成「需要维护的系统」

**来源**：《Mindset》第8章 Changing Mindsets: A Workshop（Mindset and Willpower、The Growth Mindset and Self-Control、Maintaining Change） ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我戒了/瘦了/好了，可我怕又回到原来的样子"
- 用户刚坚持了一阵，一放松就自责"我果然没有意志力"
- 用户把反复失败解释成"我这个人就是不行、管不住自己"
- 用户想要一个能长期维持的机制，而不是再下一次决心
- 用户说"每次好转之后就不做了，然后又掉回去"

**不应触发**：
- 用户还停在"要不要开始"、说不清触发点在哪 → 走 mindset-trigger-reframe
- 用户要改的是对外说的话（怎么夸孩子、怎么反馈别人）→ 走 mindset-help-others-change
- 用户的问题是"我整体上用的是哪套读法" → 走 mindset-reaction-diagnosis
- 用户处在成瘾/戒断的急性医疗风险里（如酒精戒断、暴食催吐等躯体危险）→ 先就医，见 B 节安全兜底

## R：原文锚点

> "If you're strong and have willpower, you can do it. But if you're weak and don't have willpower, you can't."（第8章 Mindset and Willpower）（已据原文核）

> "willpower is not just a thing you have or don't have. Willpower needs help."（第8章 Mindset and Willpower）（已据原文核）

> "They realize that to succeed, they'll need to learn and practice strategies that work for them."（第8章 The Growth Mindset and Self-Control）（已据原文核）

> "They think actively about maintenance. What habits must they develop to continue the gains they've achieved?"（第8章 The Growth Mindset and Self-Control）（已据原文核）

> "instead of beating themselves up, they ask: 'What can I learn from this? What will I do next time when I'm in this situation?'"（第8章 The Growth Mindset and Self-Control）（已据原文核）

> "It's a reminder that you're an unfinished human being and a clue to how to do it better next time."（第8章 The Growth Mindset and Self-Control）（已据原文核）

> "It's amazing—once a problem improves, people often stop doing what caused it to improve. Once you feel better, you stop taking your medicine."（第8章 Maintaining Change）（已据原文核）

> "But change doesn't work that way. When you've lost weight, the issue doesn't go away."（第8章 Maintaining Change）（已据原文核）

> "change from a judge-and-be-judged framework to a learn-and-help-learn framework. Their commitment is to growth, and growth takes plenty of time, effort, and mutual support."（第8章 Maintaining Change）（已据原文核）

## I：核心解释

1. **固定型把意志力当成一个"有没有"的开关**：有就做得成，没有就做不成（R1）。于是这种人往往"下定决心"却不为成功做任何特殊准备——书里点名的结局是"Quitting is easy. I've done it a hundred times."（第8章）。
2. **成长型把意志力看成需要被"扶着走"的东西**：光靠扛不够，得靠提前造条件、靠策略（R2、R3）。书里的例子全是"提前排布"而不是临场硬拼——把甜点留在屋外、提前想好在餐馆点什么、每周安排一次放纵、考虑多运动（第8章）。
3. **好转本身就是风险点**：书里的原话是——一旦问题好转，人往往就停止做那些让问题好转的事（R7）。这不是道德缺陷，是"觉得自己好了"之后的自然松懈。
4. **所以改变要"主动维护"**：不是好转就结束，而是回头问"要维持这些收获，我必须养成哪些习惯"（R4）。这就是本 skill 和"下决心"的分别——产出是一套维护习惯，不是一句誓言。
5. **挫折照固定脚本会一路退回**：固定型的剧本是"我破了戒→说明我不行→干脆放弃"。书里那句"If you're weak... you can't."（R1）就是这个剧本的开头。
6. **挫折照成长脚本是数据点**：成长型的反应不是自责，而是问"这次我能学到什么？下次遇到同样情形我改做什么"（R5）。书里把每次失手定位成"提醒你还是一个未完成的人，也是下次怎么做得更好的线索"（R6）——它是学习过程，不是"好你"和"坏你"之间的战争。
7. **维持不是靠意志，是靠结构**：书里用减肥、孩子爱学习、伴侣沟通三个例子说明，变化"have to be supported or they can go away faster than they appeared"（第8章）。最后落到一句框架转换：从"评判与被评判"转到"学习与帮助学习"，并且承认成长要"大量的时间、努力和相互支持"（R9）。
8. **别把成长策略当技巧清单用**：书里警告，如果人心里还停在固定型，只是照抄成长型的动作，是会反噬的——"This is why mindset change is not about picking up a few tricks. In fact, if someone stays inside a fixed mindset and uses the growth strategies, it can backfire."（第8章）。

## A1：来源应用 — 书里给的具体做法

**意志力的正确用法（第8章 Mindset and Willpower，作者朋友 Nathan 减肥的反例与正例）：** Nathan 的固定读法是"我只要够强就能少吃"，结果每次都"我搞砸了"→再点甜点。作者给的正解是换成系统：饭前先把一部分拨出来、让餐馆打包带走、把盘子多填蔬菜让它"看起来更多"。原话——"There are lots of things you can do."（第8章）。

**维护清单（第8章 The Growth Mindset and Self-Control）：** 成长型的人在行动前就排布：把甜点留在屋外、提前想好在餐馆点什么、每周安排一次放纵、考虑多运动（原文见 I 第 2 条）。并主动想维护："What habits must they develop to continue the gains they've achieved?"（R4）。

**挫败后的两问（第8章）：** "What can I learn from this? What will I do next time when I'm in this situation?"（R5）。

**别松懈的提醒（第8章 Maintaining Change）：** 书里借戒酒无名会说明——他们告诉人"你将永远是酒瘾者"，为的是不让人自满、停止去做维持清醒必须做的事。

**收尾的每日一问（第8章 Learn and Help Learn）：** 成功之后问自己"What do I have to do to maintain and continue the growth?"（第8章），并把它和"When, where, and how will I act on my new plan?"一起用。

## A2：典型触发场景

- 戒糖/戒烟第 20 天，吃了一块蛋糕就认定"前功尽弃"，当晚报复性进食
- 情绪好转了一阵，重新熬夜、又不再运动，"感觉自己已经好了"
- 和伴侣关系缓和后，不再刻意做那些让关系变好的小动作，几周后又开始互相挑刺
- 孩子成绩刚有起色，家长就撤掉陪伴和反馈，"现在他自己就行了吧"
- 每次都是"决心→冲一阵→失手→自责→彻底放弃"的同一个循环

## E：执行步骤

### 步骤1：分清"要维持的是什么"和"退回去长什么样"

**输入**：用户的描述。
**输出**：一句"我在维持 ___"，加一句具体的复发画面（哪个时刻、什么动作、紧接着发生什么）。

不要停在"我想保持好状态"这种笼统话。逼出可直接观察的行为（如"加班到九点、路过便利店买整袋薯片"）。

🔴 **CHECKPOINT — 触发条件：用户描述的"退回去"涉及成瘾物质或躯体危险行为（大量饮酒、暴食后催吐、擅自停药）**：立即转 B 节安全分支，先转介就医/咨询专业人员，本流程只处理"好转后的维护"这一层。

### 步骤2：把"意志力观"从固定换到成长

**输入**：步骤1 的一句话。
**输出**：用户自己复述一句改写——"我不是缺意志力，是我还没为它建好支持。"

照 R1→R2 的对照做：先保留旧句（"我以前认为……"），再给出新句（"现在换成……"），两句都在。强调书里那句"Willpower needs help."不是安慰，是操作指令。

🔴 **CHECKPOINT — 触发条件：用户坚持"就是我不够强，别人都行"**：用 R3——成事的人不是靠更强的意志，是靠"学习和练习对自己有效的策略"。追问"你上一次做成的某件事，当时用了什么条件？"把注意力从"人格"挪到"条件"。

### 步骤3：做维护计划（而不是决心）

**输入**：步骤2 的新句。
**输出**：三条具体的"维护习惯"，每条都能被看见（何时、何地、做什么）。

对照 R4 与书里的策略清单：挑 2–3 个"提前造条件"的动作（清走诱因、预设餐馆选项、安排每周一次的弹性、加入运动），而不是"我会更自律"。拒绝任何以"我会努力"开头的条目。

### 步骤4：装 when / where / how，并写一句"好转期警报"

**输入**：步骤3 的习惯。
**输出**：每条习惯配一个 when/where/how；另写一句"当我开始觉得'我已经好了'，我要立刻恢复的动作是 ___"。

对照书里"once a problem improves, people often stop doing what caused it to improve"（R7）——这句警报直接针对好转期的松懈。计划要具体到能看见画面。

🔴 **CHECKPOINT — 触发条件：用户的"维护习惯"还是"每天 4 小时""完全戒断不许有例外"这类极端条**：打回，缩到当天就能完成、允许弹性（书里的"每周一次放纵"正是留出弹性）。过大过严的计划本身就是下次失手的伏笔。

### 步骤5：预演一次失手，写好挫折脚本

**输入**：步骤4 的计划。
**输出**：一句"如果我破了戒，我不会说 ___（旧自责句），我会问 ___（两问）+ 下一步动作"。

照 R5、R6 写：失手后的动作是"这次能学到什么 / 下次改做什么"，并把失手定义成"线索"而不是"判决"。要求用户把新脚本念一遍。

🔴 **CHECKPOINT — 触发条件：用户说"计划都写了，但那天就是没做"**：不指责，回到书里的立场——一次失手"doesn't spell doom"（第8章），它是"下一次怎么做得更好"的线索。先把计划再缩小一档，再确认是不是缺了支持或协作。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把维护计划变成又一次决心 | "这次我一定管住自己" | 🛑 引 R2：意志力需要帮助。逼出三条"提前造条件"的动作，删掉所有"我会更自律"。 |
| 好转即松懈 | "我已经好了，不用再那么麻烦" | 🛑 引 R7：问题一好转，人往往就停止做让它好转的事。把"好转期警报"写进计划。 |
| 失手后全面崩 | 破一次戒就"反正前功尽弃" | 🛑 引 R5/R6：把它当数据点与线索，不是判决。落到两问 + 下一步。 |
| 计划过严无弹性 | "每天、完全、不许一次例外" | 🛑 缩到当天能完成，并像书里那样留出弹性（每周一次放纵）。 |
| 只抄动作、心态没换 | 用了成长型的招，心里还是"强/弱" | 🛑 引第8章那句警告：停在固定型却照用成长策略是会反噬的。先回步骤2 换读法。 |
| 把成瘾当小事处理 | 戒断抽搐、停精神科药、暴食催吐 | 🛑 停止本流程，转向专业医疗，做陪伴，见安全兜底。 |

### 边界规则

1. **本 skill 不替代医疗**：它处理的是"好转之后怎么维持"这一层。成瘾、进食障碍、精神科用药的调整都属医疗范畴，必须由专业人员判断。
2. **失手不是"你不行"**：书里明确把反复定位成"你是一个未完成的人"和"下一次怎么做得更好的线索"（R6），不要用本流程反过来强化自责。
3. **产出必须是习惯，不是誓言**：没有 when/where/how 的计划，视为未完成，退回步骤3/4。
4. **安全兜底**：若"退回去"涉及自伤、自杀念头、酒精或药物戒断的躯体危险、进食障碍的躯体损害，**立即停止**本流程，明确这需要专业人员与医疗帮助；出现自伤念头立即告知身边信任的人。中国大陆可拨 12356 或 010-82951332；紧急拨 120/110；应挂精神/心理科或成瘾门诊。不做诊断、不保证疗效。

### 用户自查清单

- [ ] 我能说清"我在维持什么"和"退回去的具体画面"
- [ ] 我有一句新的意志力读法（不是"我缺意志力"）
- [ ] 我有 3 条**能看见**的维护习惯（何时/何地/做什么），不是决心
- [ ] 我写了一句"好转期警报"，知道松懈时立刻恢复的动作
- [ ] 我为一次失手写好了脚本（两问 + 下一步），它不指向"我不行"

**勾选 4+ 项**：可执行。**≤2 项**：多半停在"下决心"没落到系统，回步骤3。

## 📖 练习手册

**两周维护日志**：连续 14 天，每天只记一件事——"今天我做的那个维护动作是什么、有没有做"。不做评判，只记录。周末回看，找出哪条习惯最先断掉，给它加一个"提前造条件"的支撑（照书里的策略清单）。

**失手两问卡**：把 R5 的两问抄在看得见的地方。下次破戒/复发时，先念一遍再决定下一步，禁止直接跳到"我完了"。

## 🚫 反例与黑名单

1. **把本流程当"再下一次决心"** → 与 R2 直接冲突，产出必须是习惯不是誓言。
2. **用好转型语言包装自责**（"我成长型不够"）→ 这是换了皮的固定型判词，回步骤2。
3. **只抄动作、心态仍停在强/弱** → 书里明说会反噬，先换读法。
4. **用"复原力"掩盖需要就医的信号** → 见 B 节安全兜底。

### 灰色地带（需谨慎判断）

5. **用户这次真的搞砸了，损失很实** → 不用"线索"去抹掉后果。先担后果、修补，再谈"下次改做什么"。
6. **计划有效但用户仍长期低落** → 维持住了行为也可能是别的在起作用，允许暂停，必要时应寻求专业支持。
7. **用户想用"维持"去控制别人**（"我维护好自己他就会回来"）→ 提醒：这套系统的受益人是"你自己的生活"，不要把成效押在别人的反应上。
