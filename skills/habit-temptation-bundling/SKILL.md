---
name: habit-temptation-bundling
description: 让习惯不可抗拒。当用户"知道该做、却提不起劲"，或想用自己爱做的事去拉动该做的事——"我知道该运动但总先刷剧""帮我把想做的事和该做的事绑一起""有没有办法让我愿意做无聊但要紧的事"——时使用。用多巴胺驱动的期待、超常刺激与诱惑捆绑（Premack 原理），把该做的事和一个真想做的事绑成一条链。
input_schema:
  required: [habit_to_start, thing_you_want, current_resistance]
  optional: [existing_rewards, time_slots, past_bind_attempts]
output_schema:
  primary: {bundle_chain: string, anticipation_design: string, unlock_condition: string}
  secondary: [supernormal_check, premack_note, cautions]
---

# 诱惑捆绑：把"该做的"和"想做的"绑成一条链

**来源**：《Atomic Habits》第8章 How to Make a Habit Irresistible（含 THE DOPAMINE-DRIVEN FEEDBACK LOOP、HOW TO USE TEMPTATION BUNDLING...、Chapter Summary）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我知道该运动 / 该打那通电话 / 该写那部分，可就是提不起劲"
- 用户总是"先刷剧 / 先看新闻 / 先刷手机"，然后正经事拖到没时间
- 用户问"有没有办法让我愿意做那些无聊但要紧的事"
- 用户一想到要做某件事就抗拒、能拖就拖
- 用户想把自己爱做的事当牵引力，去拉动该做的事

**不应触发**：
- 用户连一个明确行为都还没有，只是"想变自律" → 先走 `habit-starter-design`
- 用户要的是"四环里哪一环断了"的机制诊断 → 走 `habit-four-laws-audit`
- 用户要处理的是坏习惯的渴望来源（为什么越焦虑越想刷）→ 走 `habit-bad-habit-reframe`
- 用户要的是"加入一群同样在做的人"带来的吸引力 → 走 `habit-social-circle`
- 用户其实是想给自己找一个"可以刷剧 / 打游戏"的正当理由 → 转 B 节灰色地带

## R：原文锚点

> "Habits are a dopamine-driven feedback loop."（第8章，THE DOPAMINE-DRIVEN FEEDBACK LOOP）（已据原文核）

> "dopamine is released not only when you experience pleasure, but also when you anticipate it."（第8章，THE DOPAMINE-DRIVEN FEEDBACK LOOP）（已据原文核）

> "It is the anticipation of a reward—not the fulfillment of it—that gets us to take action."（第8章，THE DOPAMINE-DRIVEN FEEDBACK LOOP）（已据原文核）

> "Scientists refer to these exaggerated cues as supernormal stimuli."（第8章）（已据原文核）

> "A supernormal stimulus is a heightened version of reality—like a beak with three red dots or an egg the size of a volleyball—and it elicits a stronger response than usual."（第8章）（已据原文核）

> "We have the brains of our ancestors but temptations they never had to face."（第8章）（已据原文核）

> "The more attractive an opportunity is, the more likely it is to become habit-forming."（第8章）（已据原文核）

> "Temptation bundling works by linking an action you want to do with an action you need to do."（第8章，HOW TO USE TEMPTATION BUNDLING TO MAKE YOUR HABITS MORE ATTRACTIVE）（已据原文核）

> "more probable behaviors will reinforce less probable behaviors"（第8章，HOW TO USE TEMPTATION BUNDLING...）（已据原文核）

> "The habit stacking + temptation bundling formula is:"（第8章，HOW TO USE TEMPTATION BUNDLING...）（已据原文核）

> "Doing the thing you need to do means you get to do the thing you want to do."（第8章，HOW TO USE TEMPTATION BUNDLING...）（已据原文核）

> "Engineering a truly irresistible habit is a hard task, but this simple strategy can be employed to make nearly any habit more attractive than it would be otherwise."（第8章，HOW TO USE TEMPTATION BUNDLING...）（已据原文核）

## I：核心解释

1. **习惯是多巴胺驱动的反馈回路**：凡是高度成瘾的行为（吸毒、吃垃圾食品、打游戏、刷社交媒体）都伴随更高的多巴胺；吃喝、社交这些最基础的习惯也一样。多巴胺不只是"快乐"，它是"动机"。（R1）
2. **多巴胺在期待时就升，不只在享用时升**：赌徒在押注前、瘾君子在看见粉末时就已经多巴胺飙升。真正推动行动的是**预期**，不是得到。（R2、R3）
3. **现代世界是一堆超常刺激**：动物会对放大版的红点、排球大的蛋反应更猛；人也一样——薯片、奶昔、多巴胺化的社交媒体、修过的广告图，都是被工程化的"放大版现实"。我们带着祖先的大脑，面对祖先没遇到的诱惑。（R4、R5、R6）
4. **越有吸引力，越容易成习惯**：所以第二定律的目标就是"让它有吸引力"，能把一个行为变得更诱人，就能提高它发生的概率。（R7）
5. **诱惑捆绑＝把"想做的"和"该做的"绑一起**：这条策略的机制就是，用一个你真想做的动作，去带动一个你该做的动作。（R8）
6. **Premack 原理**：更可能发生的行为会强化不太可能发生的行为。哪怕你并不想处理积压的邮件，只要它意味着你能顺便做一件真想做的事，你就会逐渐被条件化去做它。（R9）
7. **与习惯堆叠合成公式**："After [CURRENT HABIT], I will [HABIT I NEED]. After [HABIT I NEED], I will [HABIT I WANT]."——先做一个已有动作，再做一个该做的（need），最后才解锁一个想做的（want）。（R10）
8. **关键是让"该做"变成通往"想做"的门**：做到最后，人开始期待打那三个电话或做十个波比跳，因为它意味着能看最新体育新闻、能刷一会手机。（R11、R12）

## A1：来源应用 — 书里给的具体做法

- **Ronan Byrne 的健身车**：这位都柏林工科生想看 Netflix，又想多运动。他把健身车和笔记本 / 电视连起来，写程序让 Netflix 只有在他骑到一定速度时才播放——一慢下来，剧就暂停，直到他重新蹬起来。"eliminating obesity one Netflix binge at a time."
- **ABC 的 TGIT**：ABC 把周四晚看自家剧（该做）和放松、喝红酒、吃爆米花（想做）绑在一起，还把周四夜包装成"Thank God It's Thursday"。久而久之，"周四晚八点"就意味着放松与娱乐，开电视这个动作就更有吸引力。（"The reward gets associated with the cue, and the habit of turning on the television becomes more attractive."）
- **书里给的其他捆绑点子**：只在健身房读八卦杂志、看真人秀；只在处理积压工作邮件时去做美甲。
- **公式三例**：`After I get my morning coffee, I will say one thing I'm grateful for（need）. / After I say one thing I'm grateful for, I will read the news（want）.`；午休回来先打三个客户电话，再查 ESPN；伸手拿手机前先做十个波比跳，再刷 Facebook。

## A2：典型触发场景

- 想去健身房但一看到跑步机就烦，总把运动推到"明天"
- 需要写报告 / 回邮件，却先刷半小时短视频
- 想练琴 / 学外语，但一坐下就想看剧
- 家务、报销、整理房间这类"该做但无聊"的事长期堆积
- 用户已经把"想做的事"变成了拖延的入口（先娱乐，正经事没做）

## E：执行步骤

### 步骤1：锁定"该做"的动作，找出真正的"想做"

**输入**：用户想启动的行为；一件他真心喜欢、平时会主动去做的事。
**输出**：一对明确的 need / want（该做 / 想做）。
两条都要具体到能想象的画面："打三个客户电话"（need）＋"看昨晚的比赛集锦"（want）。
🔴 **CHECKPOINT — 触发条件：用户举不出任何"想做"的事，或他说的"想做"其实是同一个成瘾行为（继续刷手机）**：先别搭链条，转 `habit-four-laws-audit` 诊断，或转 `habit-bad-habit-reframe` 处理渴望；把成瘾本身当奖励只会加固坏习惯。

### 步骤2：确认这个"想做"是奖励，不是逃避

**输入**：步骤1 的 want。
**输出**：一个判断——它是能带来正反馈的享受，还是用来躲开 task 的麻醉。
判断问句："做完这件事之后，你是觉得被喂饱、有精神，还是更空、更累？"前者能做奖励，后者只会污染整条链。
🔴 **CHECKPOINT — 触发条件：want 是刷无限信息流 / 报复性熬夜这类"用完更糟"的行为**：换一个真正回血的 want（听一张专辑、和朋友通个电话、吃一样好东西），否则链条会变成"用该做的事换又一个坏习惯"。

### 步骤3：用公式搭出捆绑链条

**输入**：need 与 want。
**输出**：一句照着书里公式写的捆绑句：`After [已有动作]，我做 [need]；做完 [need]，我才去做 [want]。`
直接套用书里的格式，让它变成一条有前后顺序的规则，而不是"两件事同时干"。
🔴 **CHECKPOINT — 触发条件：用户把 want 变成随时可得（还没做 need 就先享受）**：链条失效。加一个**解锁条件**——want 只有在 need 完成后才发生（参照 Byrne 的配速门槛：速度不够，剧就停）。

### 步骤4：给链条设一个具体的解锁条件

**输入**：步骤3 的链条。
**输出**：一个可验证的解锁门槛（做到什么才解锁 want）。
门槛要客观：骑到某个速度、写完某一个段落、打通三通电话。这样"期待"才有落点，多巴胺才在**做之前**涨起来。
🔴 **CHECKPOINT — 触发条件：need 太大、一次根本做不完，导致永远解锁不了 want**：把 need 缩到两分钟的最小版本（细节走 `habit-starter-design`），先让链条跑通、能被兑现。

### 步骤5：跑一周，观察期待有没有真的升起来

**输入**：已建立的一到两条链条。
**输出**：一条保留 / 调整 / 放弃的决定。
问用户：这一周里，你开始**期待**做那件该做的事了吗？如果期待出现了，按 R11，链条在起作用；如果完全没有，多半是 want 不够诱人或门槛太苛刻。
🔴 **CHECKPOINT — 触发条件：链条让用户觉得像被管教 / 被惩罚（"不先干活就不许爽"）**：换掉惩罚框架，回到"doing the thing you need to do means you get to do the thing you want to do"——它是**打开奖励的钥匙**，不是剥夺。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把 want 当无条件奖励 | 还没做 need 就先享受了 | 🛑 链条没有牵引力——加客观的解锁条件（参照 Byrne 的速度门槛）。 |
| want 本身是坏习惯 | 用刷手机、赌博、酗酒当奖励 | 🛑 停止。它会把该做的事变成坏习惯的诱饵，反向加固成瘾；换一个回血的 want，或转 `habit-bad-habit-reframe`。 |
| 绑得太复杂 | 一条链里塞四五件事 | 🛑 书里只要求"一个想做的 + 一个该做的"；砍到最短。 |
| 同时做（多任务） | 一边打电话一边看剧，两边都崩 | 🛑 书里 ABC 的例子是"同一时段、同一氛围"，不是"同一秒做两件要动脑的事"。让 want 出现在 need **之后**，不是同时。 |
| 用超常刺激硬拉 | 把游戏、成人内容当奖励去驱动习惯 | 🛑 超常刺激会反过来吃掉普通奖励的吸引力（书里的"放大版现实"）；选正常强度的享受。 |
| 门槛太苛刻 | 永远解锁不了，链条形同虚设 | 🛑 缩 need，让链条先能跑通；细节转 `habit-starter-design`。 |
| 把它当惩罚 | "不干活就不许爽"的管教口吻 | 🛑 换回钥匙框架：need 是通往 want 的门，不是剥夺。 |
| 伴随成瘾 / 心理危机 | 酒精、赌博、重度依赖，或提到不想活 | 🛑 走安全兜底分支，指向专业资源，本策略不替代成瘾治疗。 |

### 边界规则

1. **只处理"吸引力"这一环**：本 skill 管第二定律（make it attractive）；提示摆放走 `habit-environment-design`，做不做得动走 `habit-four-laws-audit`。
2. **want 必须是"真的想做"，不是"该做"**：书里的定义就是 pair an action you want to do with an action you need to do。
3. **want 不得是有害行为**：赌博、酗酒、无节制刷屏当奖励，只会把好习惯染坏。
4. **解锁必须可验证**：期待要靠一个客观门槛才立得住。
5. **奖励放在"之后"，不放在"同时"**：避免多任务把两边都做烂。
6. **安全兜底**：涉及药物 / 酒精戒断、赌博成瘾、心理危机、自伤时，只做提醒与陪伴，指向专业人员与当地心理援助资源（中国大陆可拨 12356；紧急拨 120 / 110），不做诊断。

### 用户自查清单

- [ ] 我能说清**该做的**是什么、**想做的**是什么
- [ ] 我确认了那个"想做的"是**真享受**，不是逃避用的麻醉
- [ ] 我写了一句**前后有序**的捆绑句（need 在前，want 在后）
- [ ] 我有一个**客观的解锁条件**（做到什么才解锁）
- [ ] 这一周里，我开始**期待**做那件该做的事了

**勾选 4+ 项**：捆绑在工作。**≤ 2 项**：多半停在"want 随时可得"或"want 本身是坏习惯"，回到对应步骤。

## 📖 练习手册

**双栏链条表**：左栏写"该做的（need）"，右栏写"想做的（want）"，中间画一道"门"。每做成一次就在门上画一道。一周后看这道门有没有让你更愿意走向左栏。

**换一个门**：如果你对某个 want 已经麻木（刷完也没感觉），把它换成一件真正回血的事，看期待有没有重新升起来。

**降低门槛**：把最难的 need 缩到两分钟版本（只做开头），只在跑通链条的阶段用，之后再把门槛抬回去。

## 🚫 反例与黑名单

1. **用一个坏习惯当奖励** → 🛑 你等于在给坏习惯付薪水，它会越来越强。
2. **把"该做的"和"想做的"同时进行** → 🛑 该做的通常需要专注，同时做会让质量崩掉。
3. **没有解锁条件、'想做'随时可得** → 🛑 没有门槛就没有期待，链条不成立。
4. **把它说成"忍完才准爽"** → 🛑 惩罚框架会制造抗拒，书里要的是"该做的成为通往想做的门"。
5. **靠超常刺激（游戏 / 成人内容 / 无限信息流）硬拉** → 🛑 会把普通奖励的吸引力也一并抬高，越拉越麻木。
6. **期待一直没升起来还硬撑** → 🛑 说明 want 选错或门槛不合理，回去改，不要靠意志力补。

### 灰色地带（需谨慎判断）

7. **用户可能是在借这个框架讨要放纵**（"我不看剧就没法工作"）：先分清是牵引力还是借口——加一个客观解锁条件就能验出来。
8. **工作性质需要分心奖励**（如长期重复的体力 / 机械劳动可以边听播客）：这类"同时进行"可以被允许，因为该做的事不需抢占同一份注意力；但仍要以该做的事完成为准。
9. **reward 的强度因人而异**：有人靠一杯好咖啡就够，有人要更实质的奖励；按书里的原则（want 拉动 need）调，不套用别人的配方。
10. **想做的这件事本身有风险**（如以喝酒、抽烟当放松奖励）：不进入捆绑，改用一个更安全的 wanted 动作，必要时转 `habit-bad-habit-reframe`。
