---
name: habit-identity-votes
description: 身份导向。当用户盯着结果却推不动——"我想减肥/想看更多书/想变自律""我要拿到某个结果但坚持不下来"——时使用。把"我想得到某个结果"改写成"我想成为哪种人"，再设计一个每天能做、当天能打勾的小行动（回答要咬住具体行为与时刻，≤800 字）。
input_schema:
  required: [desired_outcome, failed_attempts, current_self_statement]
  optional: [recurring_self_labels, audience, time_horizon]
output_schema:
  primary: {identity_statement, daily_vote_action, identity_conflict}
  secondary: [reframe_from_outcome, evidence_log_design, cautions]
---

# 身份导向：从「我要某个结果」到「我要成为哪种人」

**来源**：《Atomic Habits》第2章 How Your Habits Shape Your Identity (and Vice Versa)、第16章 How to Stick with Good Habits Every Day、第20章 The Downside of Creating Good Habits | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户反复设定一个结果目标（减重、写作、学会某技能）却总是回到原点
- 用户说"我知道我该坚持，就是坚持不了"并想要一个更稳的抓手
- 用户说"我就是这种人"（"我不是早起的人""我数学一直很差"）并想改这个自我设定
- 用户问"怎么才能真的变成自律的人/健康的人"
- 用户想要一个比"打卡数字"更本质的动机来源

**不应触发**：
- 用户还没把模糊愿望变成一个带提示的可执行动作 → 先走 habit-starter-design
- 用户已经养成习惯、现在卡在中断/看不到效果/平台期 → 走 habit-streak-plateau
- 用户要的是"哪一环断了"的机制诊断 → 走 habit-four-laws-audit
- 用户用身份概念给自己定罪或攻击别人 → 转 B 节灰色地带

## R：原文锚点

> "There are three levels at which change can occur. ... The first layer is changing your outcomes. ... The second layer is changing your process. ... The third and deepest layer is changing your identity. ... Outcomes are about what you get. Processes are about what you do. Identity is about what you believe."（第2章，Three Layers of Behavior Change）（已据原文核）

> "Behavior that is incongruent with the self will not last. You may want more money, but if your identity is someone who consumes rather than creates, then you'll continue to be pulled toward spending rather than earning."（第2章）（已据原文核）

> "Every action you take is a vote for the type of person you wish to become. No single instance will transform your beliefs, but as the votes build up, so does the evidence of your new identity."（第2章，The Two-Step Process to Changing Your Identity）（已据原文核）

> "It is a simple two-step process: Decide the type of person you want to be. Prove it to yourself with small wins."（第2章）（已据原文核）

> "The goal is not to read a book, the goal is to become a reader. The goal is not to run a marathon, the goal is to become a runner."（第2章）（已据原文核）

> "Your identity emerges out of your habits. ... the word identity was originally derived from the Latin words essentitas, which means being, and identidem, which means repeatedly. Your identity is literally your 'repeated beingness.'"（第2章，The Two-Step Process to Changing Your Identity）（已据原文核）

> "The tighter we cling to an identity, the harder it becomes to grow beyond it."（第20章，Chapter Summary）（已据原文核）

## I：核心解释

1. **三层变化，方向决定成败**：结果（你得到什么）、过程（你做什么）、身份（你相信什么）。多数人从结果出发（"我要瘦 40 斤"），书里主张从身份出发（"我要成为哪种人"）——因为方向从内往外的习惯才持久。（R1）
2. **行为与自我不一致，就撑不久**：这不是道德问题，是机制问题。你不信的自我设定会把你拽回老路。（R2）
3. **每一票都在积累证据**：一次行动不改变信念，但票数攒起来，你对自己的"证据"就变了。书里用选举比喻——**不需要全票，只要多数**。（R3）
4. **两步法**：先决定要做哪种人，再用一连串小胜向自己证明。（R4）
5. **从结果倒推身份**：你可能不知道想成为谁，但你知道想要什么结果。书里给的问句是"**Who is the type of person that could get the outcome I want?**"——从结果倒着推回身份。（第2章）
6. **身份是习惯喂出来的，不是想出来的**：identity 本义就是"反复的存在"（repeated beingness）。所以改身份，实际路径是改你重复的动作。（R6）
7. **身份也是双刃剑**：它给你动力，也会把你锁死。书里主张"keep your identity small"，别让单一身份变成脆弱的一整块。（R7）

## A1：来源应用 — 书里的两个做法

- **倒推问句**：用户通常只知道想要的结果。用书里的话往下问——"谁，是那种能拿到这个结果的人？"书里的例子：> "'Who is the type of person who could write a book?' It's probably someone who is consistent and reliable. Now your focus shifts from writing a book (outcome-based) to being the type of person who is consistent and reliable (identity-based)."（第2章）
- **"一个健康的人会怎么做？"**：书里的朋友靠这一问减了 100 多磅。> "Would a healthy person walk or take a cab? Would a healthy person order a burrito or a salad? She figured if she acted like a healthy person long enough, eventually she would become that person. She was right."（第2章）把身份变成一天里反复可用的小问句。
- **计票（habit tracker）**：书里说追踪不只是打卡，它"provides visual proof that you are casting votes for the type of person you wish to become"（第16章）——把记录当成"我在为这个身份投票"的证据链。

## A2：典型触发场景

- 减重复胖，反复在节食和暴食之间循环
- 想写作/做内容，一停就再也没开始
- 想练琴/练球，练几天就问"有什么用"然后放下
- 明明想早睡，深夜还是刷手机，第二天自责
- 总说"我不是那种能坚持的人"

## E：执行步骤

### 步骤0：先咬住具体行为与具体时刻（防两题同骨架）

先给一句**身份落脚**，再补问**具体行为**与**具体时刻**——否则回答会滑成一堆换谁都能套的身份口号，或反过来只剩动作、把身份整体推迟掉。

- 先问断在**哪一环**：早起就问是前一晚睡太晚、闹钟响后睡回去、还是起来没事干。
- 再问**几点、什么诱因**：刷手机就问一般几点、躺床上还是坐桌前、一拿起是为躲什么。
- 同一用户的不同问题各咬各的细节，**禁止用同一段骨架换个词复用**。

### 步骤1：从用户真正在盯的结果起步

**输入**：用户的愿望。
**输出**：一个说清的结果 + 一句他现在的自我陈述。

不要一上来就否定结果导向。接受结果作为**入口**（书里也说先从这里开始没问题），同时把他旧的自我陈述抓出来（"我不是早起的人"）。

🔴 **CHECKPOINT — 触发条件：用户张口就是"我就是这种人"式的负向身份（"我天生就懒""我这辈子就这样"）**：这是身份被当成了判决 → 记下这句作为要改写的对象，并明确说"身份不是刻在石头上的"（第2章："Your identity is not set in stone."）。若伴随严重自我否定/自伤 → 转 B 节安全分支。

### 步骤2：倒推身份（用书里的话术）

**输入**：步骤1 的结果。
**输出**：一句身份陈述（"我是……的那种人"）。

照抄书里问句：> "Who is the type of person that could get the outcome I want?" 让用户自己回答，再把它压成一句"我是___的人"。

🔴 **硬规则 — 首轮回复必须落一句正面的、可迁移的身份陈述，且这句必须能用用户自己给出的事实当场兑现**（"你是那种……的人"，用形容词/特质而非单一角色名词）。兑现的写法：从用户给的事实里取一条具体的（`failed_attempts` 里试过几次、每次卡在第几天/哪一环，或 `current_self_statement` 里的原话），把它当作身份句的依据，让句子听起来像从他的证据里推出来的结论，而不是一句总结他人的好话——例："你三次都断在第四天——这说明你不是坚持不了，你是那种需要把第一步缩到最小的人"。因为 `failed_attempts` / `current_self_statement` 都是必填输入，**首轮永远有可兑现的素材，不存在"先落口号、等细节再补"的例外**。**凡不能用他的任何一条具体事实兑现的身份句，一律不许写**——那样的句子就是空泛褒奖（"你这种人往往对自己有要求"），见反例黑名单第 7 条。身份落脚与细节追问**并行**推进，不得把身份整体推迟到问诊之后；正文开头就应出现这句，不能只剩动作与"看多数"。

写身份时**尽量用形容词/特质，不用单一角色名词**，因为角色会变、会碎（第20章："I'm an athlete" 改写成 "I'm the type of person who is mentally tough and loves a physical challenge."）。（R7）

### 步骤3：检查身份冲突

**输入**：步骤2 的身份陈述 + 用户的实际行为。
**输出**：identity_conflict（哪个旧设定在和新设定打架）。

照 R2 找冲突：新身份是"健康的人"，但用户的行为/自我设定是"靠外卖和甜食解压的人"——冲突不解决，光喊口号没用。

🔴 **CHECKPOINT — 触发条件：新身份与用户现实中不得不承担的角色明显冲突**（如"我是自由创作者"vs 必须照顾家人的照护者）：不要把身份写成和现实对撞的口号 → 降级为可兼容的版本（"我是那种在有限时间里也能守住一件小事的人"）。必要时转 B 节灰色地带。

### 步骤4：设计"一票"

**输入**：步骤3 的身份。
**输出**：daily_vote_action（一个当天就能投的最小动作）。

原则：小到能天天做，且**动作本身就是新身份的凭据**。书里的话：> "Each time you write a page, you are a writer."（第2章）用两分钟规则（第13章）把它缩到最小——"读一页""穿上跑鞋""写下第一句"。细节走 habit-starter-design。

对用户**只说人话**：不出现"投一票""计票""旧设定"这类内部隐喻，就说"今天能做的一件小事""你原来那句自我陈述"；并且这个动作必须**当天能打勾**（写下来、做完划掉）。整段回答正文控制在 **800 字以内**，结尾落在这个动作上。

### 步骤5：计票 + 处理失票

**输入**：步骤4 的动作。
**输出**：evidence_log_design + 一句关于"不必全票"的说明。

设计一个记录方式（纸上打勾、日历、盒子里的回形针都行，见第16章 Paper Clip Strategy）。同时把书里的选举比喻讲清：> "You don't need a unanimous vote to win an election; you just need a majority."（第2章）投了一两张坏票不会毁掉选举，别用完美主义把整场作废。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 身份变成新判决 | "我要成为自律的人"，做不到就骂自己"果然不是那块料" | 🛑 纠偏：身份是**累积的证据**不是一次性资格。引 R3——票会投错，只要多数。 |
| 用身份羞辱自己或他人 | "你就是个失败者体质" | 🛑 立即停止。身份框架是自助工具，不是判决书，也不许用来给他人贴标签。 |
| 身份太窄变脆 | "我就是个跑者"，受伤后整个人崩掉 | 🛑 按第20章"keep your identity small"，重写成可迁移的特质（"我是那种重视身体、肯长期投入的人"）。 |
| 只喊身份不动手 | 用户满足于"我是自律的人"的新标签 | 🛑 引 R6/R4：身份由重复喂出来，没有票就没有身份。把落点拉回步骤4的一个动作。 |
| 拿褒奖充当身份陈述 | 首轮身份句是"你这种人往往对自己有要求""能试三年的人是有要求的人""你其实很自律"这类好话 | 🛑 空泛褒奖不是身份句：它夸的是普遍人性或已经发生的事实，推不出他下一步该成为谁。删掉，改用他给的一条具体事实当场兑现（"你三次都断在第四天——你是那种需要把第一步缩到最小的人"）；兑不出就删，不得用褒奖顶替。 |
| 结果导向被妖魔化 | 用户以为目标完全没用 | 🛑 正常化：书里说目标是"setting a direction"用的，只是别只盯它（第1章）。 |
| 抑郁/自伤/严重自我否定 | "我这种人不配变好""活着没意思" | 🛑 停止身份工作，转 B 节安全分支，给专业资源，做陪伴。 |
| 内部隐喻抖给用户 | 回答里冒出"投一票""旧设定""选举""计票" | 🛑 这些是内部工作语，不得出现在给用户的回答里；一律改说人话（"今天能做的一件小事""你原来那句自我陈述"）。 |
| 两题一个骨架 | 换人换题，回答开头和结构几乎一样，都是"从结果倒推身份"再喊一句口号 | 🛑 先走步骤0（问清具体行为与时刻）再给身份；不同问题咬不同环节与诱因，禁止复用同一段骨架。 |
| 回答过长、没落点 | 通篇讲道理，结尾没有一个能打勾的动作 | 🛑 正文压到 800 字以内，结尾必带一个**当天能打勾**的具体动作。 |

### 边界规则

1. **不做诊断，不做人格判决**：本 skill 改写的是**自我陈述**，不是判定用户是什么人。
2. **身份要小、要柔**：单一身份会脆（第20章）。宁可多留几个可迁移的特质。
3. **不能停在口号**：身份必须落到每天能做、当天能打勾的一件小事上，否则等于没做。
4. **安全兜底**：出现临床抑郁、自伤、自杀意念、进食障碍的严重信号，**停止**身份工作，明确告知需要专业人员并指向当地心理援助资源（如各地心理援助热线；中国大陆可拨 12356，紧急时拨 120/110）。不做诊断、不保证效果。
5. **回答红线（对用户可见文字）**：正文 ≤800 字；结尾必带一个当天能打勾的具体动作；首轮身份句必须用用户给出的一条具体事实当场兑现（禁用"你这种人往往对你有要求"式空泛褒奖）；不出现"投一票""旧设定""计票"等内部隐喻；不同问题不套同一骨架。

### 用户自查清单

- [ ] 我拿到了一句**正面的、可迁移的身份陈述**（"你是那种……的人"），它出现在第一轮回复里
- [ ] 这句身份句**能用我给出的哪一条具体事实当场兑现**（试了几次、断在第几天、卡在哪一环）？兑不出就删掉重写，不得用"你其实很自律"这类褒奖顶替
- [ ] 我能说清我原先盯的**结果**是什么
- [ ] 我能把它倒推成**一句"我是……的人"**
- [ ] 我能指出**原来的哪句话/哪个行为**在和新身份打架
- [ ] 我有一个**每天都能做、当天能打勾的最小动作**
- [ ] 我知道**有几天没做到也没关系**，看多数

**勾选 4+ 项**：身份工作到位。**≤2 项**：回到对应步骤重做，或考虑转 B 节。

## 📖 练习手册

**身份-证据两栏表**：左栏写"我想成为的人"，右栏写"今天做的那件小事"。连着记一周，周末看哪一栏在长、哪一栏在空。

**换问句练习**：把一天里的几个小决定（走还是打车、看剧还是看两页书）改写成"一个___的人会怎么做？"，用它替你做决定。（这一问法出自第2章，见 A1。）

（配套练习笔记写到 用户批准的位置。）

## 🚫 反例与黑名单

1. **急性精神症状 / 重度抑郁 / 自伤 / 进食障碍** → 先转专业评估，本框架不适用急性期。
2. **用身份给别人定罪**（"你妈就是那种人"）→ 🛑 停止。本工具只用于使用者自己。
3. **把身份当免责声明**（"我这种人不擅长社交"）→ 这是第2章点名的"认知沉睡"（cognitive slumber），要把它识别出来并改写，不是接受。
4. **拿身份当新的完美主义标准**（"真正自律的人从不断"）→ 违反 R3 的多数原则，降到"多数时候投对"。

5. **把内部隐喻抖给用户**（"投一票""旧设定""选举""计票"）→ 🛑 这些是内部工作语（对应原文 votes / identity conflict），对用户一律说人话；书里的选举比喻不在本 skill 之外复述。
6. **两题一个骨架**（身份口号换个词就能套给任何人）→ 🛑 不先问具体行为与时刻就上身份模板。早起咬"断在哪一环"，刷手机咬"一般几点、什么诱因"。
7. **拿褒奖充当身份陈述**（"你这种人往往对自己有要求""能试三年的人是有要求的人""你其实很自律"）→ 🛑 这类句子的共同点：换任何一个试过几次的人都能套上，不依赖他的具体事实，是空泛褒奖而非身份落脚。判定法：这句话能不能用他给的**哪一条具体事实**当场兑现？兑不出就是褒奖，删掉重写。

### 灰色地带（需谨慎判断）

8. **用户的旧身份有真实价值**（"我是顾家的人"）→ 不要求抛弃，而是把新身份设计成与之兼容的更大版本，而非对立面。
9. **用户在重大转行/身份丧失期**（退役、卖公司、移民）→ 优先做身份重塑的陪伴（第20章的"redefine yourself"），别急着定 KPI 式的动作。
10. **用户在专业治疗中** → 优先遵循治疗师结论，本框架仅作补充理解。
