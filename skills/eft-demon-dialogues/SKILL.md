---
name: eft-demon-dialogues
description: 识别伴侣间反复出现的冲突循环（互相指责／一追一退／双方都退开）。当用户说"我们又为同一件事吵起来""每次都是这个套路""他先挑刺我就反击""一追一逃，谁都不肯先低头""我们现在连吵都懒得吵"时使用。把"谁的错"改写成"我们被同一个循环套住"，让循环本身成为共同的敌人。
input_schema:
  required: [recent_fight_description, both_partners_moves, fight_recurrence]
  optional: [surface_emotions, who_pursues_who_withdraws, relationship_duration]
output_schema:
  primary: {named_cycle: string, cycle_loop: string, common_enemy_reframe: string}
  secondary: [partner_moves_map, early_warning_signal, co_created_cycle_name]
---

# 冲突循环：把"谁的错"改写成"我们被同一个循环套住"

**来源**：《Hold Me Tight》Conversation 1: Recognizing the Demon Dialogues | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户描述"同一个架反复吵"，但每次都换个主题（钱、家务、孩子、性）
- 用户说"我们一开口就是这个套路""我知道会怎样，但停不下来"
- 一方持续追问／指责，另一方沉默／躲开，角色固定
- 用户把问题定义成对方的性格缺陷（"他就是自私""她太敏感"）
- 两人已经不吵了，但"同屋如室友""礼貌得像客气人"，谁都不再提需求

**不应触发**：
- 需要判断是否留下／离开一段有暴力、控制的关系（走安全出口，见 B 节）
- 单次、情境性的偶发不快（没形成循环）
- 纯外部压力事件（失业、丧亲）本身，而不是它引发的互动循环
- 用户只想学"如何赢这场争论"或"怎么让他闭嘴"

## R：原文锚点

> "We get stuck in three basic patterns — I call them the Demon Dialogues — when we cannot connect safely with our partner."（Conversation 1: Recognizing the Demon Dialogues，导言）（已据原文核）

> "Change starts with seeing the pattern, with focusing on the game rather than the ball."（Conversation 1，开篇案例）（已据原文核）

> "The secret to stopping the dance is to recognize that no one has to be the bad guy. The accuse/accuse pattern itself is the villain here, and the partners are the victims."（Conversation 1 · Demon Dialogue 1 — Find the Bad Guy）（已据原文核）

> "The more I _________, the more you _________ and then the more I _________, and round and round we go."（Conversation 1 · Play and Practice，填空句）（已据原文核）

## I：核心解释

1. **三种循环（Demon Dialogues，恶魔对话）**：书里只给三种基本模式——① **Find the Bad Guy（找坏人）**：互相指责、抢先定义对方是坏人，等价于"不是我，是你"；② **Protest Polka（抗议波尔卡）**：一方追问／抗议，另一方退开／沉默，也叫 Demand-Withdraw、Criticize-Defend，最常见也最黏；③ **Freeze and Flee（冻住与逃开）**：也叫 Withdraw-Withdraw，两个人都退出舞池。
2. **循环不是谁的过错，是依恋警报**：当我们无法安全连上伴侣时，只有两条路——关掉情绪、否认需要（退开），或听见焦虑、为被看见而战（追逼）。选哪条取决于过去与现在关键依恋关系教给我们的习惯，**不是固定的性格**："our strategy is not fixed. We can be critical in one relationship, and withdraw in another."
3. **循环会自我锁死**："The more you attack, the more dangerous you appear to me, the more I watch for your attack, the harder I hit back." 每一招都在召唤并强化下一招；久了只需一点 negativity 的火星就能点着。
4. **Freeze and Flee 最危险**："In dance terms, suddenly no one is on the floor; both partners are sitting out. This is the most dangerous dance of all." 双方都很礼貌、围绕实务还算配合，但已经没有任何（正或负的）情感连接。
5. **敌人是循环，不是人**：救关系的方向是"we can then learn to see the polka as the enemy, not our partner."——两个人**站到同一边**，给循环命名、一起喊停。
6. **别掉进"内容隧道"**：书里叫 Content Tube——拿一个又一个具体例子去证明"你错了、是你先开始的"。争论细节的真假只会加深循环；要看的是**这一步怎么勾出下一步**。

## A1：来源应用 — 书上给的具体做法

- **苍蝇视角（a fly on the wall reporting to the *Fly Gazette*）**：把这次冲突写成旁观者的报道——发生了什么、你出了哪招、对方被勾出哪招，而不是"谁有理"。
- **只描述自己的步子**：书里给追逼方常用的动词是 push, pull, slap, attack, criticize, complain, pressure, blow up, yell, provoke, try to get close, manage；给退开方的是 move away, shut down, get paralyzed, push the feelings away, hide out, space out, try to stay in my head, fix things。
- **填空句找循环**："The more I （动词）, the more you （动词）, and then the more I （动词）, and round and round we go."
- **一起给循环起名**：案例里 Jim 和 Pam 把它叫 "Who is lousy?" loop；Todd 和 Bella 叫 the Vortex；Ken 和 Mia 叫 the "spiral"。**名字要具体、属于你们俩**，之后用它当警报词。
- **先看见，再停下**：书里强调三步——① Stay in the present，只看此刻发生了什么；② Look at the circle，看清批评的圆圈同时卷住两个人，"There is no true 'start' to a circle"；③ 把圆圈本身当成敌人，并想清楚不打破它的后果。

## A2：典型触发场景

- 为"谁先挑起"复盘一整晚，最后谁也没赢（Find the Bad Guy）
- 她越说越多、越激动，他越少说、越沉默（Protest Polka）
- 他为"被拒绝"而追、她为"被要求"而退，越追越退（Protest Polka）
- 两人各自沉迷工作／手机／孩子，"礼貌但冰冷"（Freeze and Flee）
- 用"求性／给性"来替代情感靠近，被拒绝后升级为追逼或封闭
- 争吵主题换不停，但情绪的"音乐"一模一样

## E：执行步骤

### 步骤 1：回到最近一次冲突的具体现场

**输入**：用户口述的一次"又吵了"的经过。
**输出**：一段可复述的、只讲当下发生什么的事件描述。

先要具体：什么时候、谁说了什么、身体怎么反应、然后发生了什么。提醒"只看此刻，不翻旧账"。

🔴 **CHECKPOINT — 触发条件：用户只给泛化描述（"我们总是吵""他这人就这样"）**：信息不足 → 追问最近一次具体情形：最近一次是什么时候、当时在哪、第一句话是什么、你当时的身体感觉是什么？如果用户答的仍是评价（"他很过分"），把它翻成行为（"他做了什么"）。

### 步骤 2：画出循环——各自的招数

**输入**：步骤 1 的现场。
**输出**：一张"我的招 → 你的招 → 我的招"的双人步骤图。

先把矛头从对方身上收回：让用户只用动词描述**自己**多数时候那一步。再用填空句锁定闭环："The more I （　）, the more you （　）, and then the more I （　）, and round and round we go." 提醒这不是定罪，是看见。

🔴 **CHECKPOINT — 触发条件：用户持续把起因归结为对方（"都是他先…"）**：别跟着争对错 → 承认"圆圈没有真正的起点"（"There is no true 'start' to a circle."），然后把问题换成"他那一步之后，你做了什么？"如果用户坚持只谈对方的错 → 转 B 节「把循环当武器」。

### 步骤 3：判断属于哪一种循环

**输入**：步骤 2 的双人步骤图。
**输出**：一个命名（Find the Bad Guy / Protest Polka / Freeze and Flee），或"混合／过渡"。

对照三种模式：双方都在攻击→ Find the Bad Guy；一方追、一方退→ Protest Polka；双方都退、长期冷漠→ Freeze and Flee。注意 Freeze and Flee 常有"过渡"特征：它多半是从 Protest Polka 演变来的。

🔴 **CHECKPOINT — 触发条件：出现害怕、威胁、控制、暴力，或用户明显在恐惧对方**：**立即停在此处，不要继续做"双方都参与的循环"分析**。走 B 节「安全出口」：不给任何共同沟通话术，转向个体安全资源。

### 步骤 4：给循环起名，把它变成共同的敌人

**输入**：步骤 3 的判定。
**输出**：一个两人都认可的名字 + 一句"一起喊停"的警报语。

一起给循环取名（越具体越好，允许自嘲）；然后约定一句双方都能说的警报语，例如"我们又进了那个圈""这是我们共同的敌人，不是彼此"。案例里 Ken 说的版本很好用："We are getting stuck here. ... We don't have to do this. Let's stop."

🔴 **CHECKPOINT — 触发条件：一方拒绝参与、说"这是他的问题，你自己跟他做"**：不强行拉齐 → 说明这一步只需**一个人**先看见循环、先停止火上浇油，也能改变循环；不必等对方同意。

### 步骤 5：站到同一边，收尾

**输入**：步骤 4 的名字与警报语。
**输出**：一份"共同因"声明 + 一次小约定。

把两人的矛头都转向循环：列出这个循环已经拿走了什么（亲密度、安全感、时间）。重申方向："we can then learn to see the polka as the enemy, not our partner." 这一步只求**停止并看清**，不求立刻亲密——书里说把攻击-攻击的架停下来"is just the first step"。

🔴 **CHECKPOINT — 触发条件：用户以为"命名了就解决了"**：降级期待 → 命名只是喊停，不是修复。深层恐惧与需要要留给下一个 skill（eft-raw-spot-deescalation）。

## B：边界与失败模式

### 失败模式分支表

| 失败场景 | 表现信号 | 立即执行替代动作 |
|---------|---------|----------------|
| 把识别循环变成新一轮指责 | 用户拿"你的招"去数落对方（"看，书里说你在 stonewalling"） | 🛑 立即收回矛头。说："名字是给循环用的，不是贴在人身上的。我们只描述步子，不给人贴标签。" |
| 只谈对方那一步 | 用户反复讲对方的错，拒绝说自己的动作 | 🛑 重申圆圈无起点；把问题换成"他那步之后你做了什么？"；仍拒绝 → 只做单人版（我先看见自己的步）。 |
| 有暴力/威胁/害怕对方 | 描述里有推搡、砸物、恐吓、跟踪、性强迫，或说"我怕他" | 🛑 **安全出口，不给沟通话术**。停止"双方共同循环"框架，转向个体安全与专业资源。书里明说这本不适合 abusive or violent relationships，"In those instances, a therapist is the best resource." |
| 严重成瘾 / 长期婚外情 | 长期隐瞒、成瘾行为主导关系 | 🛑 **安全出口**。书里把 serious addictions 与 long-term affairs 一并列为不适用情形；此时正向沟通无法建立。 |
| 急性危机 / 自伤念头 | 情绪崩解、绝望、提到不想活 | 🛑 停止技术性工作，先做危机支持并转介专业帮助；本 skill 不做诊断。 |
| 一方长期拒绝任何参与 | 拒绝复盘、拒绝谈论 | 🛑 不做双人练习，改做单人"看清我自己的步子"；等待意愿，不强行拉扯。 |

### 边界规则

1. **对事不对人**：循环是敌人，两个人都是受害者（"the partners are the victims"）。
2. **不制造新的罪名**：书里的动词表是用来**描述步子**，不是用来控诉。
3. **暴力不是"循环的一步"**：任何暴力、威胁、控制都必须单列，走安全出口，不给对等沟通脚本。
4. **命名 ≠ 修复**：看见是第一步；深层恐惧与需要是下一步的事。
5. **适用前提**：这不是"谁赢"的工具，也不是给施害行为做豁免的借口。

### 用户自查清单

- [ ] 我能说出我们循环里**两个人的**步子（不只是对方的）
- [ ] 我能把它归到三种模式之一（或明确说"混合"）
- [ ] 我们给了它一个**属于我们俩**的名字
- [ ] 我们约定了一句可以随时喊停的**警报语**
- [ ] 我清楚：**要对付的是循环，不是彼此**
- [ ] 如果出现暴力／害怕／成瘾，我知道该走安全出口而不是继续这套练习

**勾选 4+ 项**：可以进入下一步（处理雷区与深层情绪）。
**≤ 2 项**：多半卡在"只谈对方"或"期待一次命名就解决"——回到步骤 2 或步骤 5。

## 📖 练习手册

配套 5 天练习（自行做或与伴侣一起）：
1. **苍蝇报道**：把最近一次冲突写成《苍蝇日报》的旁观报道，只写可观察的动作。
2. **动词盘点**：贴出你自己的动词（追逼方／退开方两组），圈出你最常用的三个。
3. **闭环填空**：完成 "The more I ______, the more you ______, and then the more I ______, and round and round we go."
4. **命名与暗号**：给循环取名，定一句警报语，并各自说说这个名字让情绪"音乐"变了什么。
5. **拿走清单**：列出这个循环已经让你们失去了什么（书里原题：What has this dance taken away from you?）。

## 🚫 反例与黑名单

以下场景**禁止**用本 skill，或必须降级处理：

1. **用"循环"给伤害行为开脱**（"不是我的错，是循环让我打人／出轨"）→ 🛑 停止。循环解释互动，不为行为负责；暴力和背叛不能外包给"模式"概念。
2. **把"你的招"当新武器** → 循环概念变成控诉工具，等于换个说法吵架。
3. **强迫受伤的一方"一起喊停"** → 若一方正处在恐惧／被控制中，平等对话的前提不存在，先走安全出口。
4. **把三人及以上家庭、亲子冲突直接套用** → 书里确实提到波尔卡也发生在亲子、手足间，但本 skill 的脚本是为**一对伴侣**写的；其他关系需另做调整。
5. **急性精神症状期** → 先转专业评估，不在此阶段做模式分析。

### 灰色地带（需谨慎判断）

6. **用"这是我的循环招数"来回避对话**（"不是你的问题，是我的模式"反复使用）→ 概念变成隔离墙而非连接工具。此时应转向 eft-hold-me-tight-talk：看清循环应通向更深的对话，而非更深的沉默。
7. **两人对"我们属于哪种循环"各执一词** → 不必统一。说："我们不必先争出是哪一种，只要都看见这个圈会转起来、而且会越转越紧就够。"先做能共同承认的那部分。
8. **用户想要"鉴定"伴侣属于哪种类型** → 这是把关系问题个体化、贴标签。回应："我们不看谁是什么类型，只看两个人在这个圈里各自出了哪一步。"
