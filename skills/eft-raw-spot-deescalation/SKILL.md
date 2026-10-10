---
name: eft-raw-spot-deescalation
description: 找到伴侣冲突里一碰就失衡的"雷区"（raw spot），把表层的愤怒或麻木拆到底层的恐惧、悲伤、羞耻（书里的"2 Ds"：emotionally deprived / deserted）。当用户说"他一说那句话我就炸了""我自己都反应过头了""我表面发火，心里其实是怕""我整个人突然冷掉、麻木"时使用。（若雷区已拆清、想把某次冲突重演一遍，走 eft-revisiting-rocky-moment。回答须先用用户自己的细节复述处境、并给出“这一次怎么收场”的最小一步；正文 ≤800 字，不露结构名。）
input_schema:
  required: [incident_description, surface_reaction, body_response]
  optional: [trigger_cue, catastrophic_meaning, suspected_origin]
output_schema:
  primary: {raw_spot_name: string, surface_vs_deep: string}
  secondary: [attachment_cue, two_Ds_pattern, soft_emotion_words]
---

# 雷区：把表层的愤怒或麻木，拆到底层的恐惧、悲伤、羞耻

**来源**：《Hold Me Tight》Conversation 2: Finding the Raw Spots | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户描述"反应跟自己/情境不成比例"——一句小话却引爆大情绪
- 用户说"我表面上是生气，其实心里是怕／是空"
- 用户描述"突然冷掉、麻木、想逃"这类收得很快的反应
- 用户能讲出一个具体的"雷点"（某个词、某个语气、某次被丢下）
- 用户反复卡在同一个循环里，想找是什么在点火

**不应触发**：
- 连冲突循环都还没看清（先走 eft-demon-dialogues）
- 用户已能说清雷区、只想把某次冲突**重演一遍** → 走 eft-revisiting-rocky-moment
- 关系创伤级别的事件（在最需要对方时被丢下、被否定、被背叛）→ 走 eft-forgiving-injuries
- 单纯的情绪管理／愤怒控制训练请求
- 用户只想学"怎么不被激怒"的技巧，而不想理解关系里的意义

## R：原文锚点

> "What exactly is a raw spot? I define it as a hypersensitivity formed by moments in a person's past or current relationships when an attachment need has been repeatedly neglected, ignored, or dismissed, resulting in a person's feeling what I call the “2 Ds” — emotionally deprived or deserted."（Conversation 2: Finding the Raw Spots）（已据原文核）

> "Withdrawal and rage are the hallmarks of Demon Dialogues, and they mask the emotions that are central in vulnerability: sadness, shame, and, most of all, fear."（Conversation 2，讨论雷区被磨到时）（已据原文核）

> "There are two signs that tell you when your raw spot or your partner's has been hit. First, there is a sudden radical shift in the emotional tone of the conversation. … Second, the reaction to a perceived offense often seems way out of proportion."（Conversation 2 · Recognizing When a Raw Spot Is Rubbed）（已据原文核）

## I：核心解释

1. **雷区 = 被反复忽视的依恋需要留下的过敏点**：书里的定义抓两点——它来自依恋需要被**长期忽略、忽视或否定**，落点永远是那两个 D：**emotionally deprived（被剥夺）** 或 **deserted（被丢下）**。这是人人都可能有的通用雷区。
2. **雷区可以来自过去，也可以来自现在**：多是过去关键关系（父母、前任）留下的模板，但一段当下关系里也可能长出新的——大转变或危机期（生孩子、生病、失业）最需要支持却得不到时，会被"磨"出雷区。
3. **雷区被磨到时只有两个可见信号**：一阵**突然的情绪变调**（刚还在说笑，转眼冰封或爆掉），以及**反应明显不成比例**。这两个信号出现，就是雷区的警报。
4. **表层是情绪，底层是脆弱**：平常说出口的是 frustration／anger／numbness（连伴侣看到的也只到这层）；被藏起来的是悲伤、羞耻，而**最核心的是恐惧——害怕失去连接**："The key emotion here is fear, fear of the loss of connection."
5. **被磨到的四步过程**：① 一个依恋线索（一个眼神、一句语气、一个转身）点亮警报；② 身体先反应（胃翻、发冷、僵住、发热）；③ 前额叶"慢半拍"，事后才去解释这线索对关系意味着什么；④ 身体已经准备好朝某个方向动——靠近、离开，或对抗。
6. **看雷区只是第一步**：拆清雷区、给它命名之后，如果要把这次冲突真正降级，才进入把冲突重演一遍的七步（Conversation 3）——那一步是单独的 skill：eft-revisiting-rocky-moment。本 skill 只做到"看清雷区、分清表层与底层、给雷区命名"为止。

## A1：来源应用 — 书上给的具体做法

1. **拆解一次"被磨到"的现场（Conversation 2 · Play and Practice）**，逐层问：
   - 触发是哪条依恋线索？"When I heard/saw ______, ..."
   - 当时身体的反应是什么？（spacey, hot, tight in the chest, small, cold …）
   - 大脑给这件事下的结论是什么？（"He is judging me." "我不重要。"）
   - 你接着做了什么动作？（靠近／离开／对抗）
   - 收尾填空："On the surface, I probably showed _______. But deep down, I just felt _______ (pick one of the basic negative emotions, sadness, anger, shame, fear). What I longed for was _______."
2. **给"深处的感受"找词**：书里给了一整串软性词供圈选——lonely, dismissed, unimportant, scared, hurt, hopeless, helpless, rejected, ignored, inadequate, shut out and alone, ashamed, small or insignificant, unwanted …（"There are only so many colors to the hurt that comes up in raw spots."）
3. **顺藤摸源头**：问"你伴侣背后有没有站着鬼魂？"（"are there ghosts standing behind your lover?"）——把雷区接到过去某个具体的伤害回应上。但**只在安全、稳稳的时候做**。
4. **下一步才是重演**：雷区拆清、事件也已冷下来、两人想把这场架重演一遍时，交给 eft-revisiting-rocky-moment 走"重温低谷"七步；本 skill 不自己发明重演流程。

## A2：典型触发场景

- 你说"我累了，今天不想"，对方瞬间感到被拒绝（雷点：不被需要）
- 一句话用了他熟悉的"那种语气"，整场谈话变冷
- 对方走神／打瞌睡，你莫名暴怒（雷点：被丢下）
- 你在最需要安慰时听到"别想太多"，从此不再开口
- 一个 15 分钟的电话延误，却换来不成比例的爆炸
- 表面在吵"袜子/碗怎么放"，实际在吵"我是不是对你还重要"

## E：执行步骤

### 步骤 1：抓住"被磨到"的那次现场

**输入**：用户描述的一次"反应过头"的经历。
**输出**：一个具体的触发点（依恋线索）+ 两个信号确认。

先确认两个信号：情绪是否**突然变调**？反应是否**不成比例**？然后**锁定线索**——不是笼统的"他不在乎我"，而是具体的"他眉毛一皱""她转身看窗外""他叹了口气"。

🔴 **CHECKPOINT — 触发条件：用户给的是全局判断而非线索（"他老是看不起我"）**：追问具体画面："那一刻你看到/听到了什么？他的表情、语气、动作是什么？"仍然答不出 → 说明这更像长期怨气而非某次雷区被磨到，先退回 eft-demon-dialogues 看清循环。

### 步骤 2：拆表层与底层

**输入**：步骤 1 的线索。
**输出**：一句"表面上…，其实里面…"的对照句 + 底层情绪命名。

按四步走：线索 → 身体（要他先描述身体）→ 大脑的结论（"我对自己说了什么？"）→ 动作。再用书里的填空收束：**"On the surface, I probably showed _______. But deep down, I just felt _______ (pick one of the basic negative emotions, sadness, anger, shame, fear). What I longed for was _______."** 底层只从 sadness / shame / fear 里挑，且**优先查 fear**。

🔴 **CHECKPOINT — 触发条件：用户一被引向底层情绪就明显升级／要崩／想逃**：**立刻停止下潜**，回到身体与当下：说"我们不急着挖到底。先回到呼吸、回到这个房间。今天就到这里。" 这种状态下需要的是安全容器，不是洞察。

### 步骤 3：给雷区命名，并接上源头（可选、且需安全）

**输入**：步骤 2 的底层情绪。
**输出**：一个可称呼的雷区名字 +（在安全时）一句源头假设。

命名要贴人话，例如"我不重要的雷区""被丢下的雷区""我不够好／被否定的雷区"。若当下平稳，可问"伴侣背后有没有站着一个鬼魂"——指向过去某个具体伤害；但这不是必做项。

🔴 **CHECKPOINT — 触发条件：顺藤摸到童年虐待／重大创伤／自伤念头**：**停**，不要继续追溯。说这已经超出"雷区"层面、需要专业创伤治疗师；本工具不能替代治疗。

🔴 **CHECKPOINT — 触发条件：雷区已能命名、事件也已冷下来，用户想"把这次冲突重演一遍"**：**转 eft-revisiting-rocky-moment**，走"重温低谷"七步；本 skill 只到拆雷区与命名为止，不在这里现编重演流程。

## 输出纪律（回答硬要求）

给用户看的那一段回答，必须同时满足下面四条；缺一条即退回重写。

1. **先复述处境，再谈别的**：开头用**用户自己的细节**把处境复述一遍——谁和谁、因为什么事、冷战或冲突持续了多久；点出这正是“雷区被磨到”的现场。**不得一上来就说方法名或术语**（不许以“我们先来拆一下雷区”“这里涉及 raw spot”这类开头）。
2. **必须给“这一次怎么收场”的最小一步**（本 skill 最容易漏的一条）：回答里要有一句**今晚／当下就能用的具体话**——例如一句能先把场面接下来、给个台阶的原话（“今晚先不翻旧账，我就想跟你说一句……”），或**先只做一件事、后续不管**的明确动作。**只教“怎么理解雷区”而不给当下这一步 = 不合格**。
3. **不露结构名**：回答里不得出现内部结构名或编号——如“两栏”“三问”“四问”“雷区地图”“四步”“七步”“步骤1/2/3”“两个信号”等。一律换成自然语言（“先说……”“另外还有一点……”），让用户看到的是一段话，不是工序。
4. **长度硬上限**：正文目标 **≤ 800 字**。超标时先删解释性铺陈、术语与结构复述，**不删**“处境复述”与“当下那一步”。

**反例（开头不合格）：**

- ❌“我们来拆一下你的雷区，大致分四步……”——先抛方法名与结构，没有用户细节，也没给今晚怎么做。
- ✅“你俩是为一件小事吵起来的，结果把三年前那笔旧账也翻了出来，从那以后谁也不先开口，就这么冷着。真正被碰到的，多半是你心里那块‘我是不是已经不重要了’。今晚你只要做一件事：……”

**反例（只教方法、不给当下那一步）：**

- ❌“你可以先觉察自己的底层情绪，分辨恐惧与羞耻，再找机会做一次脆弱披露。”——全是方法，对着这个冷战的场面，今晚一句都用不上。
- ✅“今晚别碰三年前那件事。你端两杯水过去，说一句‘这两天我们都不好受，我不想再这么耗着了，先喝口水’——就这一句，对方接不接都不管，你先把自己这半边的门推开。”

## B：边界与失败模式

### 失败模式分支表

| 失败场景 | 表现信号 | 立即执行替代动作 |
|---------|---------|----------------|
| 只教方法、不给当下的那一步 | 整篇在讲雷区怎么形成、该怎么觉察，却没有一句“今晚／这一次具体怎么做” | 🛑 补上“这一次怎么收场”的最小一步：一句能先把场面接下来、给台阶的原话，或先只做一件事、后续不管；再收尾。 |
| 开头先说方法名、或露出结构名 | 第一句就是“我们来拆雷区”，或冒出“两栏／四问／雷区地图”这类词 | 🛑 重写开头：先用用户自己的细节（谁、因什么、冷了多久）复述处境，再谈别的；结构名一律换成自然语言。 |
| 一人下潜、另一人缺位 | 用户单独做练习，把"软情绪"全抖给对方，对方却用它来反击 | 🛑 先只做单人版（自己的表层→底层），不强制对方在场；重建基本安全后再考虑双人练习。 |
| 下潜触发创伤闪回 | 解离、情绪淹没、无法继续 | 🛑 停止追溯，回到当下与身体，转安全容器模式；需要时转介创伤治疗师。 |
| 把雷区分析变成新一轮指责 | 用户拿"这是你的雷区"去数落对方 | 🛑 收回矛头：雷区是拿来理解自己的过敏点，不是贴到对方身上的标签。 |
| 有暴力／威胁／害怕对方 | 描述含推搡、恐吓、控制、性强迫，或"我不敢跟他说真话，他会……" | 🛑 **安全出口，不给沟通话术**。停止双人下潜，转向个体安全资源。书里：若身体上害怕伴侣，"it is best not to confide"。 |
| 严重成瘾 / 长期婚外情 | 成瘾或长期隐瞒主导关系 | 🛑 **安全出口**：书里 Introduction 把 abusive or violent relationships、serious addictions、long-term affairs 一并列为不适用情形，"a therapist is the best resource." |
| 自伤／危机念头 | 提到不想活、绝望到底 | 🛑 停止技术性工作，先做危机支持并转介；本 skill 不做诊断。 |

### 边界规则

1. **只做拆雷区与命名**：到"分清表层与底层、给雷区起名"为止；把冲突重演一遍是下一步（eft-revisiting-rocky-moment）。
2. **脆弱披露有前提**：书里明确设了安全线——对伴侣善意有实质怀疑、或身体上害怕对方时，**不要**披露脆弱。
3. **不追、不逼、不"逼供"**：对方还不安全时，一次都不必强推下潜，也不必强推任何双人练习。
4. **不诊断**：这里只做情绪拆解与命名，不做心理诊断，也不替代治疗。

### 用户自查清单

- [ ] 我能指出**具体的依恋线索**（一句话、一个表情），而不是笼统的怨气
- [ ] 我能说出**当时身体的反应**
- [ ] 我能分清**表层的怒气/麻木**和**底层的恐惧/悲伤/羞耻**
- [ ] 我给这个雷区**起了名字**

**勾选 3+ 项**：雷区看得比较清了，可以准备进入重演（eft-revisiting-rocky-moment）。
**≤ 1 项**：多半还在泛化怨气或过早下潜——回到对应步骤，或先退回 eft-demon-dialogues。

## 📖 练习手册

配套 4 天练习：
1. **身体地图**：回想最近一次被磨到，写下身体最先出现的三个感觉。
2. **表层→底层**：完成 "On the surface, I probably showed _______. But deep down, I just felt _______ (pick one of the basic negative emotions, sadness, anger, shame, fear). What I longed for was _______."
3. **软词圈选**：从书里的软性词单里圈出最贴你的三个（lonely / scared / ashamed / rejected / shut out …）。
4. **源头一问**："当我在雷区上疼的时候，我伴侣背后有没有站着谁的影子？"

## 🚫 反例与黑名单

以下场景**禁止**用本 skill，或必须降级处理：

1. **跳级使用**：还没看清循环就直接下潜到童年创伤，或雷区还没拆清就急着"重演" → 容易淹没且无收益。先循环（eft-demon-dialogues）、再雷区（本 skill）、再重演（eft-revisiting-rocky-moment），是有顺序的。
2. **在危险关系里做自我暴露** → 🛑 书里直接警告：若身体上害怕伴侣，"it is best not to confide"；此时应走安全出口，而非更深的自我暴露。
3. **把雷区当性格缺陷**（"我有毛病""他天生冷漠"）→ 雷区是可被安抚的依恋过敏点，书里说它**不是**不可磨灭的人格部分。
4. **用本 skill 替代治疗** → 创伤级议题、抑郁、成瘾需专业帮助，这里只做理解与命名。

### 灰色地带（需谨慎判断）

5. **大转变／危机期长出的"当下雷区"** → 它不必来自童年。若用户坚持"我过去没这问题"，不要硬套童年；书里明确说过当下的大转变或危机也能磨出新雷区。
6. **对方也在同时做本练习、但两人进度差很多** → 以**更退开的那个**先开始（书里对下一阶段的建议同理）；耐心不对称是正常的。
7. **用户只想挖童年、不处理当下互动** → 这可能是用"分析过去"回避当下的对话。回应："过去能解释它为什么疼，但解药在你们此刻的互动里。我们先回到最近一次现场。"
