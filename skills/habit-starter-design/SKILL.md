---
name: habit-starter-design
description: 启动设计。当用户只有一个模糊愿望——"我要多运动""我想多读书""我要变自律"——却从没定过时间地点时使用。把它变成带明确提示的启动句（执行意图/习惯堆叠），再缩到两分钟内的版本。
input_schema:
  required: [vague_wish, current_routines, past_start_failures]
  optional: [time_constraints, location_context, supporting_people]
output_schema:
  primary: {start_sentence, two_minute_version, cue_chosen}
  secondary: [habit_stack_chain, commitment_device, cautions]
---

# 启动设计：把"我要多运动"变成一句能执行的启动句

**来源**：《Atomic Habits》第5章 The Best Way to Start a New Habit、第13章 How to Stop Procrastinating by Using the Two-Minute Rule、第14章 How to Make Good Habits Inevitable and Bad Habits Impossible | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我要开始多运动/多读书/学英语/写日记"但没有任何时间地点
- 用户反复"开始"又从没真正开始，想要一个可执行的起点
- 用户问"我该把新习惯安排在什么时候、哪里"
- 用户已经有具体习惯、想把它挂到一个已有日常动作上
- 用户想给自己设一个"最小启动版"以防半途而废

**不应触发**：
- 用户要的是"我想成为哪种人"的身份改写 → 走 habit-identity-votes
- 用户已有习惯，卡在中断/看不到效果/平台期 → 走 habit-streak-plateau
- 用户要诊断"哪一环断了" → 走 habit-four-laws-audit
- 用户处在过劳/急性倦怠/抑郁期，连两分钟都安排不动 → 先转 B 节安全分支

## R：原文锚点

> "People who make a specific plan for when and where they will perform a new habit are more likely to follow through."（第5章；原文该句前有 "The punch line is clear:"，此处按引文惯例调整首字母大写）（已据原文核）

> "The simple way to apply this strategy to your habits is to fill out this sentence: I will [BEHAVIOR] at [TIME] in [LOCATION]."（第5章）（已据原文核）

> "The habit stacking formula is: 'After [CURRENT HABIT], I will [NEW HABIT].'"（第5章）（已据原文核）

> "Many people think they lack motivation when what they really lack is clarity. It is not always obvious when and where to take action."（第5章）（已据原文核）

> "use the Two-Minute Rule, which states, 'When you start a new habit, it should take less than two minutes to do.' ... A new habit should not feel like a challenge. The actions that follow can be challenging, but the first two minutes should be easy."（第13章）（已据原文核）

> "Standardize before you optimize. You can't improve a habit that doesn't exist."（第13章，Chapter Summary）（已据原文核）

> "A commitment device is a choice you make in the present that controls your actions in the future."（第14章）（已据原文核）

## I：核心解释

1. **卡住你的人多半不是缺动机，是缺清晰**：书里原话——"they lack motivation when what they really lack is clarity"。模糊的"多运动"没给大脑任何可执行的信号。（R4）
2. **执行意图＝把时间地点钉死**：两个最常见的提示就是时间和地点。填出"我将在[时间]在[地点]做[行为]"这一句，就是给自己造一个显式提示。（R2）
3. **习惯堆叠＝拿一个已经在做的动作当提示**：与其新造提示，不如把新行为挂到一个雷打不动的旧习惯后面，"After [CURRENT HABIT], I will [NEW HABIT]."。（R3）
4. **两分钟规则＝把入口缩到不可能拒绝**：任何习惯都能缩出两分钟版——读一页、穿跑鞋、打开笔记。重点是"先建立'现身'这个习惯"，不是做满两分钟。（R5）
5. **先标准化，再优化**：一个不存在的习惯没法改进。先让它存在，再谈强度。
6. **需要时用承诺装置把入口变窄**：书里 Victor Hugo 把衣服锁起来写作——"a choice you make in the present that controls your actions in the future"。（R6）

## A1：来源应用 — 书里的三个现成工具

- **执行意图**（第5章，源自英国 248 人的锻炼实验）：让用户填原句。书里的成功变体是把整句写全——> "During the next week, I will partake in at least 20 minutes of vigorous exercise on [DAY] at [TIME] in [PLACE]." 那一组有 **91%** 的人每周至少锻炼一次，对照组只有 35–38%，而"只做动机宣讲"的那一组几乎没有提升。
- **习惯堆叠**（第5章，源自 BJ Fogg）：列两栏——"每天雷打不动会做的事"和"每天必然发生的事"（太阳升起、收到短信、一首歌放完）。从第一栏挑一个当锚点。书里的早晨栈示例：> "After I pour my morning cup of coffee, I will meditate for sixty seconds." > "After I meditate for sixty seconds, I will write my to-do list for the day."
- **两分钟规则**（第13章）：映射"从很容易到很难"的梯度。书里的例子：跑马拉松很难，但"穿上跑鞋"很容易——那才是网关习惯（gateway habit）。其他例子：> "'Read before bed each night' becomes 'Read one page.' ... 'Run three miles' becomes 'Tie my running shoes.'"

书里还提醒挑锚点的两个标准（第5章）：提示要**具体且立刻可做**（作者自己的反面教材是"午休时做十个俯卧撑"太含糊，改成"合上笔记本电脑时，在桌边做十个俯卧撑"就清楚了）；锚点的**频率要和新习惯一致**（要每天做，就别挂在一个只在周一发生的旧习惯上）。

## A2：典型触发场景

- "我要开始健身"，但没说哪天几点在哪
- "我想每天读书"，书买了没动
- 想练英语口语，从没定过练习时间
- 想写东西，一直停在"等有灵感"
- 想把冥想挂到早上那杯咖啡后面

## E：执行步骤

### 步骤1：把愿望改写成具体行为

**输入**：用户的模糊愿望。
**输出**：一个动词明确的行为（不是领域，是动作）。

领域词（"运动""学习""写作"）要压成动作（"快走 20 分钟""背 10 个单词""写 100 字"）。

🔴 **CHECKPOINT — 触发条件：用户说的是一个领域/身份而非行为（"我要变自律""我要健康"）**：这不是启动设计能直接处理的粒度 → 要么再往下问出具体行为，要么先转 habit-identity-votes 做身份改写。

### 步骤2：选提示——执行意图还是习惯堆叠

**输入**：步骤1 的行为 + 用户日常。
**输出**：cue_chosen + start_sentence。

二选一（第5章）：
- 若用户日程较稳 → **执行意图**：让他填全 "I will [BEHAVIOR] at [TIME] in [LOCATION]."
- 若用户生活里已有雷打不动的动作 → **习惯堆叠**："After [CURRENT HABIT], I will [NEW HABIT]." 帮他从"每天必然发生的事"里挑锚点。

若用户不确定何时开始，书里建议从**一周/一月/一年的第一天**起步，因为那时"hope is usually higher"（第5章）。

🔴 **CHECKPOINT — 触发条件：用户挑的锚点不稳定（如"周末运动后"却想每天做）或用词含糊（"午休时""有空时"）**：按 A1 的两个标准纠偏——具体到可立刻执行、频率与新习惯一致。含糊就换个锚点。

### 步骤3：缩到两分钟版本

**输入**：步骤2 的启动句。
**输出**：two_minute_version（网关习惯）。

把行为砍到"第一步"的粒度：不是"跑三公里"，是"穿上跑鞋"；不是"读书半小时"，是"读一页"。（R5）

### 步骤4：验证启动句的四个条件

**输入**：start_sentence + two_minute_version。
**输出**：过审的最终句，或标注需要修的点。

逐一检查：
- [ ] 时间/地点（或锚点）**具体、可立刻执行**，没有"有空时"这类模糊词
- [ ] 锚点频率和习惯频率**一致**
- [ ] 两分钟版**真的在两分钟内**能完成
- [ ] 第一动作**不需要额外准备**（跑鞋不在门口就先把它挪到门口）

🔴 **CHECKPOINT — 触发条件：用户说"这也太小了，没意义"**：引 R5/R6 与第13章——"The point is not to do one thing. The point is to master the habit of showing up." 先标准化再优化；并给两分钟规则的一种玩法："do it for two minutes and then stop"（第13章）。

### 步骤5（可选）：加一个承诺装置或环境预备

**输入**：过审的启动句。
**输出**：commitment_device（可选）。

第14章的做法：预先付费的课程、提前预约、把衣服锁起来、把零食换成小包装、定时断网（Nir Eyal 的路由器定时器）。原则是把好习惯的入口变"只要开始就行"、把坏习惯的出口变"要多花力气才能做"。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 启动句仍然含糊 | "每天有空的时候运动一下" | 🛑 不给过审。回到步骤2，把时间地点钉死，或换一个稳定的锚点。 |
| 频率不匹配 | 想每天冥想，却挂在"每周一开例会"后面 | 🛑 引第5章：锚点频率要和习惯一致。换锚点。 |
| 两分钟版被嫌小 | "读一页有什么用" | 🛑 引 R5/第13章：先现身，强度后加；用小步进阶（habit shaping，第13章）。 |
| 准备工作没到位 | 跑鞋在柜子最里面 | 🛑 先做"预备环境"（第14章）：把第一动作要用的东西挪到必经过的路上。 |
| 用启动设计逃避真正的身份问题 | 用户反复设计新习惯却从不想成为谁 | 🛑 转 habit-identity-votes：没有身份牵引，再漂亮的启动句也是空的。 |
| 过劳/倦怠/抑郁 | 用户连两分钟都安排不动、提不起劲 | 🛑 停止排习惯，转 B 节安全分支，先照顾状态。 |

### 边界规则

1. **不做诊断，不替代专业评估**：本 skill 只设计可执行起点。
2. **一次只启动一个习惯**：同时启动多个会互相挤占提示和注意力。
3. **进入门槛必须真的低**：任何"其实要花 20 分钟"的伪两分钟版都要拆到真正两分钟。
4. **安全兜底**：出现临床抑郁、急性倦怠、自伤、自杀意念，**停止**习惯设计，明确告知需要专业人员并指向当地心理援助资源（如各地心理援助热线；中国大陆可拨 12356，紧急时拨 120/110）。不做诊断、不保证效果。

### 用户自查清单

- [ ] 我的行为是**一个具体动作**，不是领域词
- [ ] 我有一条**完整的启动句**（时间地点，或"在 X 之后"）
- [ ] 我的提示**具体、可立刻执行**，且**频率匹配**
- [ ] 我有**一个真的能在两分钟内做完**的版本
- [ ] 我第一动作需要的**东西已经就位**

**勾选 4+ 项**：设计到位。**≤2 项**：回到对应步骤重做，或考虑转 B 节。

## 📖 练习手册

**两栏锚点清单**：左栏写"每天雷打不动做的事"（起床、刷牙、倒咖啡、下班换鞋、坐下吃饭、上床），右栏写"每天必然发生的事"（太阳升起、收到消息、一首歌结束）。从里面挑你的堆叠锚点。

**强度梯度表**：把目标写成"很容易→很难"的五档（穿跑鞋 / 走十分钟 / 走一万步 / 跑 5K / 跑马拉松），每天只要求落在最低那一档，稳了再上一档。

（配套练习笔记写到 用户批准的位置。）

## 🚫 反例与黑名单

1. **急性抑郁 / 过劳 / 自伤** → 先照顾状态与转介，不排习惯。
2. **一次给人排五六个新习惯** → 🛑 拒绝。一次一个。
3. **把两分钟规则当最终目标** → 它是**入口**不是终点；惯常后要按 habit shaping 升级（第13章）。
4. **把它当成拖延的新形式** → 书里点名的 "motion vs. action" 陷阱：一直优化启动方案而不真正开始（第11章）。

### 灰色地带（需谨慎判断）

5. **用户强行要求一个现实中不稳定的锚点**（夜班、婴儿、频繁出差）→ 用"事件锚"替代"时间锚"，并把两分钟版再往下压。
6. **用户想启动的是戒断类目标**（戒酒、戒赌）→ 这超出"启动设计"，优先走 habit-four-laws-audit 的移除提示 + 专业支持。
7. **用户在专业治疗/康复中** → 优先遵循治疗师方案，本框架仅作补充理解。
