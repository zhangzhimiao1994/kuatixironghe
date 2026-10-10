---
name: eft-hold-me-tight-talk
description: 帮用户准备并进行一次"抱紧我"对话——说的人先说出"我最怕什么"，再直接说出"我最需要你什么"；听的人学会在场、不反驳。当用户说"我想跟他好好谈一次，但一开口就吵""我不知道怎么说出我真正想要的""我需要他，但我说不出口""TA 一表达需求我就想解释、想逃"时使用。
input_schema:
  required: [what_user_longs_for, attachment_fear, role_who_speaks]
  optional: [handles_from_earlier_talks, terrible_ifs, listener_reaction_pattern]
output_schema:
  primary: {fear_statement: string, need_statement: string, are_invitation: string}
  secondary: [handles_list, terrible_ifs_list, listener_presence_script]
---

# 抱紧我：说出"我最怕什么"，再直接说"我最需要你什么"

**来源**：《Hold Me Tight》Conversation 4: Hold Me Tight — Engaging and Connecting | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户想"认真谈一次"，但每次一开口就变成争吵或沉默
- 用户知道自己需要对方，却开不了口，或开口就变成指责／要求
- 用户想帮伴侣，但一听到对方表达情绪就想"解决问题、解释、反驳"
- 双方已经做过前面的循环/雷区工作，想更进一步
- 用户问"我到底该怎么说出我的需要，才不会被当成发牢骚"

**不应触发**：
- 关系里还在反复的循环里打转、基本安全尚未建立 → 先走 eft-demon-dialogues / eft-raw-spot-deescalation
- 未愈合的重大伤害（在最需要对方时被丢下、被背叛）挡在前面 → 先走 eft-forgiving-injuries；书里明说必须先能处理 Conversation 1–3、建立基本安全，才谈得上这次
- 用户想找"话术套路"去操控或逼对方就范
- 有暴力、害怕对方、严重成瘾或长期婚外情 → 不在对话脚本适用范围

## R：原文锚点

> "Conversation 4 has two parts. The first — What Am I Most Afraid Of? — requires further exploring and elaborating on the deeper feelings you tapped into in the previous conversations. ... The second part — What Do I Need Most from You? — is crucial, the tipping point encounter in EFT."（Conversation 4，导言）（已据原文核）

> "It involves being able to openly and coherently speak your needs in a way that invites your partner into a new dialogue marked by accessibility, responsiveness, and engagement, an A.R.E. conversation."（Conversation 4，对第二部分的定义）（已据原文核）

> "If we don't learn to let our partner really see our attachment needs in an open, authentic way, the chances of getting these needs met are minuscule. We have to send the signal loud and clear for our partner to get the message."（Conversation 4）（已据原文核）

> "Being present is the secret here, rather than responding in any set way."（Conversation 4 · Play and Practice，给倾听方的指引）（已据原文核）

## I：核心解释

1. **这是一次"连接"的对话，不是"解决"的对话**：它的目的不是把问题谈出结论，而是让两个人在情感上真正对上。书里把它比作跳探戈——比前面几次谈话高一个层级。
2. **它分两半**：第一半 **What Am I Most Afraid Of?（我最怕什么）**——把前面的深层情绪一路探到"地面层"，找到依恋的核；第二半 **What Do I Need Most from You?（我最需要你什么）**——直接、明白地说出**此刻只有你能满足**的依恋需要。书里称第二半是 EFT 的"临界点时刻"。
3. **恐惧与渴求是一枚硬币两面**："Fear and longing are two sides of the same coin." 说清恐惧，自然会带出需要。
4. **它是 A.R.E. 对话**：目标是让对方感到——**Accessibility（我能靠近你吗？）**、**Responsiveness（你能在情感上回应我吗？）**、**Engagement（我知道你珍视我、留在我身边吗？）**。合起来一句话就是"Are you there, are you with me?"。
5. **信号要响、要清楚**：含糊的信息（抱怨、指责、"你怎么不说话"）养着循环；只有把需要说成**清楚、连贯**的信号，伴侣才有机会接住。"His engagement is the solution for her."
6. **谁先说很重要**：书里建议**更退开的那一方先开始**——因为主动抗议的那一方更容易被伤害与恐惧绊住，很难在没有对方先递出信号的情况下先伸手。
7. **倾听方的秘密是"在场"**：不需要标准答案。确认你听见了、感谢对方愿意说、并表达你愿意回应——这就是正面的第一步。

## A1：来源应用 — 书上给的具体做法

- **用"把手"（handles）**：书里把那些能打开内心深处的比喻、词、短语叫 handles——例如"a shattered heart / overwhelmed / anxious / freaking / fleeing"。把抽象的大词（如 Charlie 的"disquietude"）拆成具体的感受。
- **列"可怕的如果"（Terrible Ifs）**：把"如果我承认了你的感受，最糟会怎样"一条条列出来，底下往往藏着核心恐惧（我会无助、我会被丢下、我就不是个够好的伴侣）。
- **第一半的话术骨架**："我最怕的是______。如果我停下不想办法、只是待在你说的话里，我怕______。"
- **第二半的话术骨架**：书里给了一串可以直接圈选的句子——"I need to feel, to sense that: I am special to you … I am wanted by you … I am loved and accepted, with my failings … I am needed … I can count on you to be there for me, to not leave me alone when I need you the most … I can ask you to hold me and to understand that just asking is very hard for me."
- **对倾听方**："respond by saying what it was like to hear the disclosures. Was it easy or hard to understand the message? ... Examine the feelings together." 然后**交换角色**，让对方也走一遍。
- **说出来的好处**：即使不完美，说出来本身就有力量。书里 Charlie 说完后说："It feels good now, to be able to say these things. I did not shatter. Kyoko is still here, and I feel stronger somehow."

## A2：典型触发场景

- 把"我累了"说出口，对方听成拒绝，于是又吵起来
- 想求安慰，开口却成了"你到底在不在乎这个家"
- 对方哭或说难受时，你本能地开始讲道理／列方案
- 两人都不吵了，但也不敢真的靠近
- 长期用性、用做事、用"陪伴式沉默"代替真正说出需要
- 一方给了台阶（"来抱抱"），另一方却因为怕再受伤而僵住

## E：执行步骤

### 步骤 1：确认前提与角色

**输入**：用户的关系现状与本次谈话的意图。
**输出**：确认"安全底线"是否具备 + 谁先说。

先确认上一次的循环能被喊停、彼此能听懂"雷区"这套语言（否则先退回前两个 skill）。然后判断谁更退开：**由更退开的那方先说**；另一方先当倾听者。

🔴 **CHECKPOINT — 触发条件：还存在未处理的重大伤害，挡住这次谈话（"我一想起那次就说不下去"）**：**不硬推**。转 eft-forgiving-injuries，先把那道伤单独谈。书里明说必须先能处理 1–3 号对话、建立基本安全，才能做这次对话。

### 步骤 2：第一部分——"我最怕什么"

**输入**：之前积累的"把手"和有过的可怕如果。
**输出**：一句清楚的恐惧陈述。

从"把手"出发，一路问到最底：我到底怕失去什么？允许用户用书里那串软词起步；把大而抽象的词拆成具体感受；最后用一个具体的"最怕"收住。

🔴 **CHECKPOINT — 触发条件：用户一直停在愤怒或分析、碰不到恐惧（"我才不怕，是他不讲理"）**：**不入戏地追问**一次——"如果这块怒气底下还压着一样怕，会是什么？"若还是碰不到 → 不勉强，改为只做第二半（直接陈述需要），或降回 eft-raw-spot-deescalation 继续拆。

### 步骤 3：听的人先在场，不反驳、不解释、不修

**输入**：步骤 2 的恐惧陈述。
**输出**：一次"被听见"的回应（确认 + 感谢 + 愿意回应）。

给倾听方三件事：① 确认你听懂了什么；② 感谢对方愿意冒这个险；③ 说清你愿意靠近。**不要**立刻反驳、辩解、给方案。书里强调："no one takes the risk of being rebuffed by disclosing … unless the other person really matters."

🔴 **CHECKPOINT — 触发条件：倾听方退回习惯（"可是你也有错""这不就是上次……"）或变得防御**：**喊暂停**，把倾听方的难也当成信息："你刚才想解释，那说明这件事也碰到了你的雷区。我们先记下，等会儿换你说。"然后按书里的顺序**交换角色**。

### 步骤 4：第二部分——"我最需要你什么"

**输入**：步骤 2 的恐惧 + 步骤 3 的在场。
**输出**：一句直接、具体的需要陈述（A.R.E. 邀请）。

把需要说成**具体的、此刻只有对方能给的**请求（"我需要你抱抱我，告诉我我对你重要""我需要知道即使我搞砸了，你也不会走"）。提醒对方：这是在发出邀请，不是命令；对说的人：允许自己难堪，甚至允许就"说不出口"这件事本身先说出口。

🔴 **CHECKPOINT — 触发条件：用户把需要说成指责或泛泛要求（"你以后多关心我一点""你总是……"）**：**改写成 A.R.E. 语言**——回到"我"、"此刻"、"只有你能给的具体动作"。若对方用"这很过分吗／就这点要求？"轻描淡写 → 温和地把焦点拉回对方的感受："听见这些，你心里发生了什么？"

### 步骤 5：交换角色 + 留下关键句

**输入**：第一轮两半的成果。
**输出**：双向各一句恐惧句与需要句 + 一份可复用的关键句清单。

交换角色，让倾听方也走一遍两半。结束后各自写下这一轮里**最关键的几句话**（书里建议如此：写下关键句能帮你们日后继续澄清），并确认下一次需要时可以怎么开口（例如约定一个信号语）。

🔴 **CHECKPOINT — 触发条件：出现害怕对方／担心披露会被用来对付自己**：**立即停**，转 B 节安全出口，不给脆弱披露脚本。书里原文把这条线画得很清楚。

## B：边界与失败模式

### 失败模式分支表

| 失败场景 | 表现信号 | 立即执行替代动作 |
|---------|---------|----------------|
| 倾听方转成辩解或反攻 | "可是你……"、"那我的需要呢？"抢话 | 🛑 暂停，先确认"你听见了什么"，再约交换角色时把对方的委屈放进来。 |
| 一次谈话当终极方案 | 谈完就说"我们没事了"，之后不再做 | 🛑 正常化反复。书里说这是**正面连接事件**，需要一次次创造；不是一次性修补。 |
| 说的人把需要说成控诉 | "你从来就不……""你就不能……" | 🛑 改写成 A.R.E. 语言：我 + 此刻 + 具体动作。控诉只会重启循环。 |
| 一方完全缺席／拒绝听 | 拒绝参与、转身离开 | 🛑 不追逼。可先做单人版（把自己的恐惧与需要写清），把谈话留到对方愿意时；同时保护自己不被反复伤害。 |
| 披露后被立即反击／羞辱 | 对方拿你的脆弱当武器 | 🛑 停止继续披露，回到安全与边界；这本身就是重要信息，值得单独处理。 |
| 有暴力／威胁／害怕对方 | 推搡、恐吓、控制，或"说得太真我会被报复" | 🛑 **安全出口，不给沟通话术**。书里：若身体上害怕伴侣，"it is best not to confide … find a therapist or even reconsider being in the relationship." |
| 严重成瘾 / 长期婚外情 | 成瘾或长期隐瞒主导关系 | 🛑 **安全出口**：书里把这两种情形列为不适用，"a therapist is the best resource." |
| 自伤／危机念头 | 绝望到底、提到不想活 | 🛑 停止技术性工作，先做危机支持并转介；本 skill 不做诊断。 |

### 边界规则

1. **顺序不能跳**："抱紧我"建立在能看到循环、能处理雷区、有基本安全之上；缺了就补。
2. **目的是连接，不是说服**：说得清楚是为了"被听见"，不是为了"赢"。
3. **倾听 ≠ 解决**："Being present is the secret here"——比提供方案重要得多。
4. **有安全红线**：对伴侣的善意有实质怀疑、或身体上害怕对方时，**不要**暴露脆弱。
5. **一次不够**：这是要反复创造的时刻，不是一次性手术。

### 用户自查清单

- [ ] 我能说出**我最怕的是什么**（不是"我讨厌他怎样"）
- [ ] 我能说出**我最需要对方给我什么**（具体、此刻、只有他能给）
- [ ] 我说的是邀请，而不是命令或控诉
- [ ] 作为听的人，我做到了**在场**（确认+感谢+愿意回应），没有辩解
- [ ] 我们说好了**下次怎么开启**这种对话
- [ ] 我清楚：**哪些情况下不该做这次对话**（害怕、暴力、成瘾）

**勾选 4+ 项**：这次对话在正轨上。
**≤ 2 项**：多半还卡在基本安全或倾听方防御上——回到步骤 1 或步骤 3。

## 📖 练习手册

配套 5 天练习：
1. **把手清单**：把你说过的那些很重的词或比喻写下来（如"像掉进冰窖""心被摔碎"），逐个翻成感受。
2. **可怕的如果**：列三条"如果承认对方感受，我最怕会怎样"。
3. **需求句**：用书里的清单勾出最贴你的那几句，再改写成你自己的话。
4. **静默预演**：独自对着空椅子先把两半说完一遍，注意哪句让你哽住。
5. **正式对话 + 留句**：真做一次，事后各自写下关键句，约定下一次的开启信号。

## 🚫 反例与黑名单

以下场景**禁止**用本 skill，或必须降级处理：

1. **当成管控工具**：拿"抱紧我"话术去逼对方表态、给承诺、当场认错 → 🛑 这是操控，不是连接。
2. **跳过前面的对话直接做** → 没有基本安全时的脆弱披露，往往换来二次受伤。
3. **在害怕对方的关系里做** → 🛑 书里对安全线写得很直白：身体上害怕伴侣时不要披露。走安全出口。
4. **把对方的一次迟疑判定为"不爱我"** → 书里提醒，披露的一方常常需要**反复说、耐心说**，对方才慢慢学会用新的眼光看你。
5. **要求对方按标准脚本回应** → "Being present is the secret here, rather than responding in any set way." 强迫式回应等于又一种要求。

### 灰色地带（需谨慎判断）

6. **只有一方愿意做** → 仍可做**单人版**：他说"我想跟你谈一次"就够了。但不要反复单方面掏心而长期得不到回应——那不是练习，是消耗。
7. **两人对"谁更退开"看法相反** → 不必争。可让**更愿意先试的人**先开始，或按当时情绪浓度决定；重要的是**交换角色**，两边都要走一遍。
8. **用户只想要"话术模板"不想碰情绪** → 那就只是背台词。回应："台词可以给你，但真正让对话接通的是你说这句时带着什么。我们先看看那句'我最怕'是什么。"
9. **这是在治疗中的伴侣** → 优先遵循治疗师安排；本 skill 是补充理解与练习工具，不替代治疗方案。
