---
name: jung-active-imagination
description: 荣格「主动想象（active imagination）」轴线。当用户说"我睡前总看到一个形象/一个场景，甩不掉""我想跟心里那个声音对话，可一坐下来就头脑空白""什么叫主动想象？跟白日梦有什么区别"时使用。给反复出现的形象/场景/声音一块自主的空间，让它在想象里自己动、自己说话；本人保持清醒的"我"在场并记录下来，结束后回到现实、对这场相遇采取一个态度——既不是被动白日梦，也不是控制剧情。
input_schema:
  required: [recurring_image_or_voice, stance_toward_it, present_capacity]
  optional: [sleep_onset_or_hypnagogic, journal_or_art_history, somatic_or_artistic_channel, crisis_signs]
output_schema:
  primary: {starting_point: string, autonomy_marker: string, ego_standpoint: string}
  secondary: [recording_method, reality_return_action, referral_note, follow_up_prompts]
---

# 主动想象（Active Imagination）：让形象自己动，我保持在场

**来源**：荣格全集 Vol 7（¶341–370：《The Technique of Differentiation between the Ego and the Figures of the Unconscious》）· Vol 8（¶131, 166–193：《The Transcendent Function》）· Vol 13（¶20–23：《The Secret of the Golden Flower》评注）· Vol 18（¶392–406：The Tavistock Lectures）| 证据等级：primary（逐字原文，locator 见 R 节）

## 触发条件

**应该触发**：
- 反复出现的形象 / 场景 / 声音：`我睡前总看到一个形象/一个场景，甩不掉`、`有一张脸/一个地方总回到我脑子里`
- 想跟内在的某个声音对话却做不下去：`我想跟心里那个声音对话，但一坐下去就头脑空白`
- 概念澄清：`什么叫主动想象？跟白日梦有什么区别？`
- 已经在做类似的事但卡住：`我照着别人的方法试过，脑子一片空白`、`那画面一闪就没了`
- 反复的梦/意象想做点什么，但不满足于只给它找一个符号去解释
- 想找一个"既不控制、也不被动放空"的内在练习

**不应触发**：
- 伴严重解离、听幻、失现实感、"被附体/被控制"体验 → 先精神科/就医评估，本 skill 不进入
- 急性自伤/自杀意念、正在发生的危机 → 先危机处置（见 E 步骤1）
- 只想要"解一个梦的意思" → 路由 `jung-dream-work`
- 想分析"我为什么老被同一件事触发" → 路由 `jung-complex-archetype`
- 把想象内容当预言/启示求解读 → 明确拒绝（见 B 与黑名单）

## R：原文锚点

> "By “human” experience I mean that the person of the author should not just be included passively in the vision, but that he should face the figures of the vision actively and reactively, with full consciousness."
> — CW 7, ¶342, p4109

> "It is no weakness, no spineless surrender, but a hard achievement, the essence of which consists in keeping your objectivity despite the temptations of the mood, and in making the mood your object, instead of allowing it to become in you the dominating subject."
> — CW 7, ¶348, p4112

> "the fantasy, to be completely experienced, demands not just perception and passivity, but active participation."
> — CW 7, ¶350, p4113

> "we must not take the fantasies literally when we approach the question of interpreting them. While we are in the grip of the actual experience, the fantasies cannot be taken literally enough. But when it comes to understanding them, we must on no account mistake the semblance, the fantasy-image as such, for the operative process underlying it."
> — CW 7, ¶353, p4114

> "Through her active participation the patient merges herself in the unconscious processes, and she gains possession of them by allowing them to possess her. … That is the transcendent function born of the union of opposites."
> — CW 7, ¶368, p4122

> "Fantasies are no substitute for living; they are fruits of the spirit which fall to him who pays his tribute to life."
> — CW 7, ¶369, p4123

> "The method of “active imagination,” hereinafter described, is the most important auxiliary for the production of those contents of the unconscious which lie, as it were, immediately below the threshold of consciousness and, when intensified, are the most likely to irrupt spontaneously into the conscious mind. The method, therefore, is not without its dangers and should, if possible, not be employed except under expert supervision. … The method of active imagination, therefore, is not a plaything for children."
> — CW 8, ¶131 前言（Prefatory Note）, p4482–4483

> "He must make himself as conscious as possible of the mood he is in, sinking himself in it without reserve and noting down on paper all the fantasies and other associations that come up."
> — CW 8, ¶167, p4501

> "Critical attention must be eliminated. Visual types should concentrate on the expectation that an inner image will be produced. … Audio-verbal types usually hear inner words … Others at such times simply hear their “other” voice."
> — CW 8, ¶170, p4502

> "Once the unconscious content has been given form and the meaning of the formulation is understood, the question arises as to how the ego will relate to this position, and how the ego and the unconscious are to come to terms. … At this stage it is no longer the unconscious that takes the lead, but the ego."
> — CW 8, ¶181, p4507–4508

> "The position of the ego must be maintained as being of equal value to the counter-position of the unconscious, and vice versa."
> — CW 8, ¶183, p4508

> "Taking it seriously does not mean taking it literally, but it does mean giving the unconscious credit, so that it has a chance to co-operate with consciousness instead of automatically disturbing it."
> — CW 8, ¶184, p4508

> "A fantasy is more or less your own invention, and remains on the surface of personal things and conscious expectations. But active imagination, as the term denotes, means that the images have a life of their own and that the symbolic events develop according to their own logic—that is, of course, if your conscious reason does not interfere. You begin by concentrating upon a starting point."
> — CW 18, ¶397, p12357

> "when you concentrate on a mental picture, it begins to stir, the image becomes enriched by details, it moves and develops. Each time, naturally, you mistrust it and have the idea that you have just made it up … But you have to overcome that doubt, because it is not true."
> — CW 18, ¶398, p12357

> "Perhaps I could start by having a fantasy about that poster. I might for instance imagine that I am myself in the poster, that the scenery is real…"
> — CW 18, ¶393, p12355

> "But by objectifying them, the danger of their inundating consciousness is averted and their positive effect is made accessible."
> — CW 18, ¶406, p12362

> "they did nothing (wu wei2) but let things happen. … We must be able to let things happen in the psyche. … Consciousness is forever interfering, helping, correcting, and negating, never leaving the psychic processes to grow in peace. … To begin with, the task consists solely in observing objectively how a fragment of fantasy develops."
> — CW 13, ¶20, p9131

> "criticism is still likely to start in afterwards in the attempt to interpret the fantasy, to classify it, to aestheticize it, or to devalue it. … But each time the fantasy material is to be produced, the activity of consciousness must be switched off again."
> — CW 13, ¶21, p9132

> "These exercises must be continued until the cramp in the conscious mind is relaxed, in other words, until one can let things happen, which is the next goal of the exercise. In this way a new attitude is created, an attitude that accepts the irrational and the incomprehensible simply because it is happening."
> — CW 13, ¶23, p9133

## I：核心解释

1. **主动想象不是白日梦，也不是控制剧情**。荣格把两者分得很清："梦/幻想（fantasy）或多或少是你自己的发明，停留在个人事物和意识期待的表面；而主动想象意味着图像有它自己的生命，象征事件按它自己的逻辑发展——前提是你的意识理性不去干涉"（CW 18 ¶397）。白日梦由"我"编剧，主动想象由形象自己走。

2. **起点必须很小、具体**。不需要宏大主题，一个海报、一个反复出现的画面、一个梦里的碎片就够。荣格讲那个年轻画家怎么也"进不去"，最后正是从车站墙上的一张风景海报开始，"想象我自己就在那张海报里"（CW 18 ¶393–395）。**起点越不起眼，越容易让形象自己动。**

3. **保持清醒的"我"在场，并且记录**。不是把自己交给图像、失去意识，而是"面对幻象中的人物，主动地、有反应地、以完整的意识去应对"（CW 7 ¶342）；"把情绪作为对象，而不是让它成为支配你的主体"（CW 7 ¶348）；"沉入其中、毫不保留，并把浮上来的一切幻想与联想写在纸上"（CW 8 ¶167）。**清醒 + 记录，是它和白日梦、和恍惚状态的分界线。**

4. **让它在想象里自己动、自己说话，而不是替它说话**。意识一开始只做一件事：把表达的形式交给无意识内容，"把主导权尽量留给无意识抛上来的偶然念头"，这一步对意识的立场"往往是一种挫折"（CW 8 ¶178）；期间"不要急着解释、分类、审美化或贬低"（CW 13 ¶21）。

5. **结束后要回到现实，对这场相遇采取一个态度——这是第二个、也是更重要的阶段**。"当内容被赋形、意思被理解之后，问题就变成：'我'要如何对这场相遇表态、如何与之达成和解；这时主导权不再属于无意识，而属于'我'"（CW 8 ¶181）；两个立场要"被赋予同等分量"（CW 8 ¶183）。**不在想象里解决，而是在现实里对它有立场。**

6. **认真 ≠ 当真**。"认真对待不等于照字面当真，而是给无意识应有的分量，好让它有机会与意识合作，而不是自动干扰意识"（CW 8 ¶184）。幻想不能替代生活——"幻想不能替代生活；它们是精神的果实，落给那个对生活尽了本分的人"（CW 7 ¶369）。

7. **输出是谈话层，不是神秘解读**。单条回复 ≤800 字；不说"其实是一个符号/原型"这类术语；不把内容解释成预言、启示或事实。

## A1：来源应用 — 从"甩不掉的东西"到一个可用的起点

荣格的方法起点从来不是"你想聊什么"，而**是你身上已经在自行重复的那个东西**——一个画面、一个场景、一个声音（CW 18 ¶393；CW 8 ¶167）。越是甩不掉、越是自己回来，越适合当起点：

| 用户提供 | 荣格式读法 | 收口到 |
|---------|-----------|-------|
| 睡前总看到的形象/场景 | 它已经在你不请自来地重复，说明自带能量 | 把最清楚的那一格画面当作起点 |
| 想对话的"内在声音/评判者" | 每个人心里都有一支"内在批评者"，先听见它说什么（CW 8 ¶170） | 让它把话说完，不打断、不辩论 |
| 一闪就没了 / 一坐就空白 | 意识太紧（"意识的痉挛"，CW 13 ¶22–23） | 缩小到一格静物（一张海报/一个房间），只描述、不推进 |
| 已经做过但卡住 | 多半卡在"急着解释/分类/审美化"（CW 13 ¶21） | 关掉解释，回到"只观察它怎么动" |
| 有天赋用画/塑/身体表达 | 手有时比脑子先懂（CW 8 ¶171） | 用画画/捏塑/身体动作当通道，事后再补记录 |

## A2：典型触发场景

- 反复梦到同一个地方/同一个人，醒来很久还在
- 睡前"看见"一个形象或场景，闭上眼反而更清楚
- 心里总有一个声音在评头论足，想跟它说句话却不知从何开口
- 一闭眼就想"我现在要开始想象了"，然后脑子一片空白
- 试着想象却总在"我是不是在编""这有什么意义"里打转
- 已经把意象画下来/写下来，但不知道下一步该做什么
- 找到一个"既不控制情节、也不被动放空"的内在练习
- 想问"主动想象和白日梦到底差在哪"

## E：执行步骤

> 输出纪律：每一步的输出是**给用户看的结构 + 动作**，不是解读。**所有单条对用户的回复 ≤800 字**；不出现"原型/无意识/超越功能"等术语；不把内容说成预言或事实。

### 步骤1：安全与边界筛查（先于一切想象作业）

**输入**：用户主诉原文，加上"是否伴解离、听幻、失现实感、被控制感、自伤意念"。
**输出**：一句边界判定——① 是否可进入想象作业；② 是否需要先给精神科/就医或危机资源。

🔴 **支路判定（硬规则，先于步骤2）**：主诉落在**睡前／反复／侵入性画面**者，**一律走 A 支（隔屏观察）**——即便用户主动说"我想走进去看看"，也不改。理由：这类材料自带能量、又紧贴入睡边界，采用沉浸引导会抹掉观察距离（CW 18 ¶406），对易解离者最危险。

🔴 **CHECKPOINT — 触发条件：出现严重解离、"听到清晰声音在对我说"、失现实感、被附体/被控制感，或急性自伤/自杀意念**：**先停想象作业**。明确讲：这已超出"想象练习"的范围，需要**精神科/心理科评估**；有自伤/危机线索 → 给资源 **12356 / 010-82951332 / 110 / 120**。**若**用户伴失现实感或听幻**而**仍要求继续**则**不进入步骤2，改为陪伴 + 转介话术。

### 步骤2：定一个起点（形象 / 场景 / 声音）——两条**互斥**支路

**输入**：反复出现或此刻最清楚的一个形象、场景或内在声音。
**输出**：一句可复用的"起点描述"（越小越具体越好）。

> 硬规则：步骤2 只有两条支路，**按材料二选一、不可混用**。**已有现成形象**（尤其睡前／反复／侵入性）→ **一律 A 支**；**完全没有任何浮上来的形象** → **才用 B 支**。判不准时，按 A 支处理。

**A 支：已有现成形象（睡前／反复／侵入性画面默认走此支）——只做隔屏观察。**
- 做法：**不进入**那个画面，而是**隔一段距离、像看一块屏／一幅画框**那样看着它。
- 只允许问三类问题：**"它离你多远？""画框（边界）落在哪里？""你坐在哪里看它？"**
- 🚫 **绝对禁止**出现"走进／站进去／我本人就在里面／进入那个场景"这类**沉浸语**。
- 为什么：把形象**客体化**，才能避免意识被它淹没（CW 18 ¶406）；对易解离者尤其危险——观察距离一旦抹掉，人可能被卷进画面。
- 内在声音 → 起点就是"让它说第一句话"，先只记下它的原话（同样只"听"，不"进去"）。

**B 支：无任何现成形象——才用"自造起点"（海报技术）。**
- **若**用户说"我想对话"却**没有**任何具体形象/场景 → **则**借一个**真实、中性、无害的小物件当门**：一张海报、窗外一栋楼、房间一角。
- **只有这一支**才允许"进入"式引导，如"先想象我自己就在那张海报的画面里"（CW 18 ¶393–395）。
- 理由：这是荣格针对"从零造起点"给的技术（CW 18 ¶393）；它属于**无现成材料**的场景，**不得**套用到 A 支已有的侵入性材料上。

🔴 **CHECKPOINT — 触发条件：用户一坐就头脑空白、或反复说"我编不出来"**：这是"意识的痉挛"（CW 13 ¶22–23），不是没天赋。**若**用户**没有**任何浮上来的画面**则**把要求降到最低："只描述你眼前真实看到的一样东西，一小格就行，不许它动也行。"缩小到一格静物即可，**不要**让他去"想一个有意义的故事"。

### 步骤3：给它自主空间——让形象自己动、自己说话

**输入**：步骤2 的起点。
**输出**：一段"它自己动/自己说"的记录（谁的走位、谁开的口、哪一步不是你安排的）。

- 只做一件事：把表达权交给画面，"把主导权尽量留给无意识抛上来的偶然念头"（CW 8 ¶178）。
- **判断自主性的唯一标准**：是否有一步**不是你编的**、让你略感意外甚至不舒服的转折（CW 18 ¶398）。若全是"我安排的"，说明还在白日梦层。
- **戒律**：这一步不解释、不分类、不审美化、不贬低（CW 13 ¶21）。

🔴 **CHECKPOINT — 触发条件：用户急着"把剧情掰到自己想要的方向"（"我要它变成……"）**：**立即拉回**——这正是白日梦/控制剧情。**若**用户坚持要控制走向**则**把场景停掉，改问："先不管它该去哪，刚才它自己想往哪走？哪怕只有一点点。"

### 步骤4：保持清醒的"我"在场 + 记录

**输入**：步骤3 的经过。
**输出**：一份书面/图画记录，且用户**用他自己的话**确认`我始终清楚这是我在看，不是外面来的`（**不逐字复述定句**——不把它做成口令／仪式）。

- 立场：像面对真人一样"主动地、有反应地、以完整意识应对"，不是被动地看（CW 7 ¶342）。
- **若走 A 支**：记录里连同"隔屏"信息一起记——它离你多远、画框落在哪、你坐在哪里看它。
- 记录方式随人：写下来、画出来、捏出来、用身体动出来都行（CW 8 ¶170–171；CW 13 ¶22）。事后回填文字记录。
- 保持"我"在场 = 情绪是对象，不是支配者（CW 7 ¶348）。

🔴 **CHECKPOINT — 触发条件：用户报告"我分不清那是不是真的发生了""身体动不了/回不来"**：**立即停止想象、做接地动作**（站起来、说出今天日期与眼前三样东西、喝水）。**若**接地后仍**没有**恢复现实感 → **则**转步骤1 的转介通道，今天不再继续。

### 步骤5：回到现实，对这场相遇采取一个态度（第二舞台）

**输入**：步骤4 的记录。
**输出**：一句"我的立场"——你**在现实里**要对这场相遇怎么办。

- 关键翻面：内容成型后，问题变成"'我'如何对这场相遇表态、如何与之达成和解；**这时主导权属于'我'**"（CW 8 ¶181）。
- 两个立场同等分量：形象的诉求与"我"的判断都要摆上桌（CW 8 ¶183）。
- 落一个**现实动作**：改一件小事、说一句话、做一个决定、或明确"我暂时只看着它"——都算立场。
- **认真 ≠ 当真**：不照字面把它当预感或命令（CW 8 ¶184）。

🔴 **CHECKPOINT — 触发条件：用户把想象内容当成预言/事实来求验证（"这是不是意味着我要出事？""这是不是上天的提示？"）**：**明确拒绝**。**若**用户把内容**当成**现实预言或外部指示**则**触发 B 表「把内容当预言/事实」行：重申"认真对待不等于照字面当真"（CW 8 ¶184），把它带回"它对你意味着什么、你想怎么回应"。

### 步骤6：收束——不让想象替代生活

**输入**：前五步产出。
**输出**：一个把这次相遇接回日常的动作 + 一句收束。

- 边界句：**幻想不能替代生活**（CW 7 ¶369）。
- 收束动作示例：把记录放进抽屉、去做今天本来就该做的一件现实之事、或约定"下一次再看它"。

🔴 **CHECKPOINT — 触发条件：用户越来越想把时间花在想象里、现实事务开始塌陷**：提醒 **"这是一场相遇，不是一次逃离"**；**若**用户**没有**把现实任务做完就想再做一次**则**先把现实那件事做完，再回来。

## B：边界与失败模式

### 失败模式表

| 触发情况 | 具体表现 | 🛑 处理动作 |
|---------|---------|-----------|
| **失败：对睡前／反复／侵入性画面用了"走进去"的沉浸引导** | 出现"走进／站进去／我本人就在里面"；观察距离被抹掉，人差点被卷进画面 | 🛑 **立即停**。改回 A 支隔屏观察：只问"它离你多远／画框落在哪／你坐在哪里看它"。引 CW 18 ¶406：把形象客体化才能避免意识被淹没。对易解离者尤其危险。 |
| 失败：做成了被动放空 | 顺着念头漫游、昏昏欲睡、事后什么也记不清 | 🛑 拉回"清醒的我 + 记录"。引 CW 8 ¶167、CW 7 ¶342：以完整意识应对，并把浮上来的一切写下来。 |
| 问题：控制剧情 | "我要它变成……""这走向不对，重来" | 🛑 停场景。问"它自己想往哪走？"引 CW 18 ¶397：图像有它自己的生命，意识理性别干涉。 |
| 症状：一坐就头脑空白 | "闭眼就一片白""我编不出来" | 🛑 降级到最小起点。引 CW 13 ¶22–23「意识的痉挛」：只描述眼前一格静物，只观察、不推进。 |
| 情况：出现失现实/听幻/被吞没 | "分不清是不是真的""回不来""听得太清楚" | 🛑 立即停止 + 接地；仍不缓解 → 转精神科评估；危机给 12356 / 010-82951332 / 110 / 120。 |
| 失败：把内容当预言/事实 | "这是不是预感？是不是指示？" | 🛑 明确拒绝。引 CW 8 ¶184：认真不等于照字面当真；不把内容当预言或事实。 |
| 问题：把相遇变成定罪或夸大 | "果然我很糟""我是不是有特殊使命" | 🛑 拉回中立。引 CW 7 ¶348：情绪是对象不是主体；这是个案经验，不是身份判决、也不是天选信号。 |
| 症状：越做越糟、结束更悬 | 做完更焦虑/恐惧，悬在想象里收不了场 | 🛑 暂停练习 3 天；先把步骤5 的"现实立场 + 收束动作"补上；持续恶化 → 转介。 |

### 边界规则

1. **不诊断、不替代心理治疗**：这是反思与练习框架，不是治疗。持续功能损害/创伤/抑郁 → 转介专业帮助。
2. **不把想象内容当预言或事实**：它是心灵的表达，不是外部指示（CW 8 ¶184）。
3. **认真 ≠ 当真**：既要给它分量，又不照字面处理。
4. **清醒 + 记录是底线**：不能失去现实感、不能不给"我"留位置。
5. **不控制、不放空**：编剧的是白日梦，失守的是恍惚；主动想象两边都不是。
6. **幻想不替代生活**：现实义务优先（CW 7 ¶369）。
7. **严重解离/听幻/失现实感 → 先就医**：安全筛查先于一切（E 步骤1）。

### 用户自查清单

- [ ] 我为一个**具体的**起点（形象/场景/声音）做过一次练习，而不是泛泛地"想象"
- [ ] 如果材料是睡前／反复／侵入性的画面，我**只做了隔屏观察**（能说出它离我多远、画框落在哪、我坐在哪里看它），**没有**"走进去"
- [ ] 过程中出现了**至少一步不是我编的**转折（或我已能识别"全靠我编"这个信号）
- [ ] 我**始终清楚"是我在看"**，并在结束后**做了记录**
- [ ] 我**没有**试图控制剧情，也**没有**失去现实感
- [ ] 我给这次相遇定了一个**现实里的态度/动作**，而不是只在想象里解决
- [ ] 我知道这不是预言、不是事实，也没有把它变成对自己的判决

**≥4 项**：练习在轨道上。**≤2 项**：多半卡在"控制剧情"或"头脑空白" → 回对应失败模式分支。

## 📖 练习手册

配套 7 天实操，每天只做一条，做完在对应步骤的 🔴 检查点回看完成情况。7 天依次为：
1. **安全自查**（步骤1）：写下有没有解离/听幻/失现实感/危机线索；有 → 先就医，不继续。
2. **圈定起点**（步骤2）：写下那个甩不掉的形象/场景/声音，一句话说清最清楚的一格。
3. **一格静物**（步骤2–3）：若无从下手，就盯住眼前一个小物件，只描述 3 句，不许它动。
4. **让它自己动**（步骤3）：给起点 15 分钟，只观察、不解释；结束时标注"哪一步不是我编的"。
5. **记录在场**（步骤4）：把这次经过写/画/捏出来，末尾**用你自己的话**记一句"我始终清楚这是我在看，不是外面来的"（不必逐字照抄；睡前／反复画面请只做隔屏观察）。
6. **现实立场**（步骤5）：对这场相遇写一个现实动作——改一件小事/说一句话/做一个决定。
7. **收束回生活**（步骤6）：把记录收起，做完一件今天本就该做的现实之事，写下"相遇到此，生活继续"。

## 🚫 反例与黑名单

以下场景**禁止**调用此 skill，或必须降级/转介：

1. **伴严重解离、听幻、失现实感、"被控制/被附体"体验** → 先精神科/就医评估；不做想象作业。
2. **急性自伤/自杀意念、正在发生的危机** → 先危机处置：**12356 / 010-82951332 / 110 / 120**。
3. **要求把意象解读成预言/启示/外部指示**（"这是不是征兆？该不该照做？"）→ 拒绝；不把内容当预言或事实（CW 8 ¶184）。
4. **想用本 skill 替别人做（"帮我分析我朋友看到的画面"）** → 拒绝：这是本人、在场的练习，不可代做。
5. **把本 skill 当心理治疗 / 当灵性捷径** → 持续功能损害 → 转介；幻想想替代生活是本框架明确反对的（CW 7 ¶369）。
6. **未做安全筛查就直接开始** → 先走 E 步骤1；危机资源常备。
7. **以"我在做主动想象"为由放弃现实义务** → 现实优先；相遇不是逃离。
8. **对睡前／反复／侵入性画面使用"走进／站进去／我本人就在里面／进入那个场景"类沉浸指令** → 一律 A 支隔屏观察；这是最危险的一类误用（易解离者被卷入画面）。沉浸式"进入"只属于 B 支"无现成形象 → 借无害小物件自造起点"（CW 18 ¶393）。

### 灰色地带

9. **用户把一次强烈意象当成"开了天眼/顿悟"**（"我看到的东西肯定是真的"）→ 不附和不否定其体验，但明确：这是心灵的表达，不是外部事实；把它转成"它对你想说什么、你想怎么回应"。
10. **用户在做心理治疗、想用本框架对冲治疗师结论** → 优先遵循治疗师；本框架是练习工具，不替代治疗。
11. **用户想象中出现性/攻击等强烈禁忌内容而羞耻** → 不做道德评判；提示"内容不必好看，也不必合意，先如实记录、别急着解释"（CW 13 ¶21），再在步骤5 决定态度。
12. **用户全程"编得很顺"、毫无意外** → 可能是聪明地做白日梦：请他把"哪一步是你临时决定的"标出来，或换一个他并不在意的起点重试（越不在意，越容易自主）。
13. **用户想要"标准答案"式的意象含义表** → 拒绝给固定解法；"意思要在你自己的记录和现实立场里长出来"，不外包给符号词典。
