---
name: attach-conflict-principles
description: 冲突当下的五条安全原则。当用户"正在吵，想找一句不火上浇油的话""一争执就升级或冷战抽离""翻旧账、泛化、拿人格说事"时使用。把冲突当下落成一句"关火"的话加一个安全动作，并附 oxytocin 的预防提醒。平日里怎么把需要说出口 → attach-secure-communication。
input_schema:
  required: [the_fight, who_escalates, escalation_pattern]
  optional: [attachment_style_context, is_intimacy_centered, past_attempts]
output_schema:
  primary: {deescalation_line: string, the_secure_move: string, principle_hit: string}
  secondary: [red_flags, oxytocin_reminder, follow_up_questions]
---

# 冲突当下：五条安全原则，把火关掉

**来源**：《Attached》第 12 章「Working Things Out: Five Secure Principles for Dealing with Conflict」 | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我们已经吵起来了，我这一刻说什么才不火上浇油"
- "一争执他就冷战/抽离，我怎么把这架按在事情上"
- "吵架时我总忍不住泛化：'你总是…你从不…'"
- "我想判断这次吵架到底安不安全、有没有越线"

**不应触发**：
- 还没开口、想先把真实需要写成一段话 → 转 attach-secure-communication
- 反复为琐事吵、其实是亲密度协商 → 转 attach-anxious-avoidant-trap
- 想学操控/话术让对方就范 → 拒绝，本 skill 只教诚实地关火与表达
- 判断对方是什么依恋类型 → 转 attach-style-reading
- 暴力/威胁/人身攻击已发生 → 转安全出口，不做冲突演练

## R：原文锚点

> "1. Show basic concern for the other person’s well-being. 2. Maintain focus on the problem at hand. 3. Refrain from generalizing the conflict. 4. Be willing to engage. 5. Effectively communicate feelings and needs."（第 12 章，「Five Secure Principles for Resolving Conflict」）（已据原文核）

> "1. Getting sidetracked from the real problem. 2. Neglecting to effectively communicate your feelings and needs. 3. Reverting to personal attacks and destructiveness. 4. Reacting “tit for tat” to a partner’s negativity with more negativity. 5. Withdrawing. 6. Forgetting to focus on the other’s well-being."（第 12 章，「Insecure Conflict Strategies to Avoid」）（已据原文核）

> "Don’t expect your partner to know what you’re thinking. If you haven’t told him/her what’s on your mind, s/he doesn’t know!"（第 12 章）（已据原文核）

> "We get a boost of oxytocin in our brain during orgasm and even when we cuddle—which is why it’s been tagged the “cuddle hormone.”"（第 12 章，「Preventing Conflict—Attachment Biology 101」）（已据原文核）

> "Douse the flame before it becomes a forest fire—attend to your partner’s upsets before they escalate."（第 9 章，安全原则清单 Examples of Secure Principles）（已据原文核）

## I：核心解释

1. **吵多少不重要，怎么吵才重要**：书里说，连安全型伴侣也会吵；真正区分两人关系满意度、影响亲密度的，不是分歧的多少，而是怎么分歧、为什么分歧。冲突可以是两人靠近、加深联结的机会。（第 12 章）
2. **先分清两类冲突**：bread-and-butter 型是共同生活必然产生的琐事分歧（看哪个频道、空调几度、吃中餐还是印度菜），它逼你学会妥协；intimacy-centered 型是亲密度协商，见第 8 章，往往一个让到底。（第 12 章）
3. **安全型五原则不是魔法，是可学的方法**：先关心对方福祉 / 就事论事 / 不把冲突泛化 / 愿意留在现场参与 / 有效地把感受和需要说出来。（第 12 章）
4. **两条最常被违反的**：一是把冲突泛化成对人格的贬低（"你总是…""你从不…"）；二是干脆不说、指望对方读心——"If you haven’t told him/her what’s on your mind, s/he doesn’t know!"（第 12 章）
5. **不安全的人为什么回避正面冲突**：焦虑者被触发时会用 protest behavior（指责、哭、冷处理）去"留下记号"，回避者用去激活策略（找对方毛病、抽离）来拉开距离；研究显示两组都比安全型更少用正向冲突策略、更多攻击与退出。（第 12 章）
6. **预防比补救便宜**：oxytocin（"拥抱激素"）在性高潮和拥抱时都会飙升；为工作牺牲与伴侣的亲近，其实也少了这份 oxytocin，会让人对周遭更不宽容、更容易起冲突。书中建议别把周日早晨的拥抱换成加班。（第 12 章）

## A1：来源应用 — 书上的两张工具

1. **五条安全原则清单 + 六个"冲突中要避免的不安全策略"**（第 12 章）：sidetracked 偏离真问题 / 不表达感受与需要 / 人身攻击与破坏 / tit for tat 以恶报恶 / 抽离 / 忘了关心对方。对照自己这次犯了哪几条。
2. **冲突工作坊六例**（第 12 章，判断 secure/insecure 并写出可用的替代）：
   - Marcus & Daria（已订的巴西单身邮轮）——Marcus 泛化+偏离真问题 → 应就事论事地回应 Daria 的顾虑。
   - Daria 的退让道歉——她把感受说成"自己不合理" → 应有效表达需要。
   - Ruth & John（车上谈女儿数学）——John 属 secure 示范：不还击、就事论事、确认对方担忧。
   - Steve & Mia（酒吧邀约）——Steve 抽离；Mia 的表达太像攻击。两人都 insecure。
   - Emma & Todd（看别的女人）——Todd 抽离+贬低；Emma 属 secure 示范。
   - Dan & Shannon（保姆道谢）——Shannon 属 secure：不泛化、不反击、就事论事，一句真诚道歉就把火降下来。
3. **敏感话题原则**（第 12 章）：像"见孩子"这类敏感话题应当一直摆在桌上——"Assume that they’re important, even if they aren’t raised"，宁愿打开谈也不要埋着。
4. **冲突当先记住的几条**（第 12 章）：一场吵不散一段关系；怕被拒绝就把恐惧说出来，别让它支配你；别默认伴侣的坏情绪是你的错；信任对方会关心回应，然后照直说需要；别假设你懂对方的意思，拿不准就问。

## A2：典型触发场景

- 吵到一半对方抽离/冷处理，你不知道怎么不升级
- 一句话说出口就把旧账全翻出来
- 冲突从"这件事"变成"你这个人"
- 想判断这次争执到底走的是 secure 还是不 secure
- 长期被工作挤压，两人越来越容易起冲突

## E：执行步骤

### 步骤1：判断冲突类型

**输入**：这场吵架。 **输出**：bread-and-butter 还是 intimacy-centered。

问：我们在争的是具体安排（看哪个台、去哪），还是"我们要多近"？若是亲密度协商，可并入 attach-anxious-avoidant-trap。（第 12 章）

🔴 **CHECKPOINT — 触发条件：出现人身攻击、摔东西、推搡、威胁**：停止冲突演练，转 B 节安全出口。

### 步骤2：定位违反了哪条安全原则

**输入**：双方各说了什么。 **输出**：命中的"不安全策略"。

对照六个 don'ts：偏离真问题 / 不表达需要 / 人身攻击 / tit for tat / 抽离 / 忘了关心对方。（第 12 章）

🔴 **CHECKPOINT — 触发条件：用户把"安全/不安全"当标签去给人定罪**：纠正——五原则是自查用的，不是判人；只描述互动。

### 步骤3：给一句当下"关火"的话

**输入**：命中的不安全策略。 **输出**：一句话，同时做到先关心对方 + 就事论事 + 不泛化 + 不抽离。

参考书里 John 的回应结构（第 12 章）：先说明自己的状态（"I’m really exhausted and the driving is sapping all of my energy."），再确认对方的担忧（"I am very worried about this too, but I can barely concentrate on the road as it is."）。

🔴 **CHECKPOINT — 触发条件：用户想要的话是"让他就范/报复"**：拒绝，只做诚实的关火与表达，不做操控。

### 步骤4：把感受与需要说出来（第五原则）

**输入**：真实需要。 **输出**：一句用 need/feel/want 表述的话。

示范（第 12 章，Rebecca）："I know you hate going to my sister’s, but it would mean the world to me if you could come this one time."

🔴 **CHECKPOINT — 触发条件：用户还没到开口这一步，要的是"怎么把需要写清楚"**：转 attach-secure-communication，先写脚本、预判"接住的样子"。

### 步骤5：补一条预防提醒

**输入**：日常作息。 **输出**：一个具体可做的"亲近"小动作。

oxytocin（第 12 章）：别把周日的拥抱换成加班——"This small act might be enough to immunize your relationship against conflict for the next few days."

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 用五原则给对方定罪 | "都是他 insecure 才这样" | 🛑 原则是自查用的，不是判人；只描述互动。 |
| 把"关火"当认输 | 一句软化 = 低头 | 🛑 关火是为解决问题，不是分输赢。 |
| 在爆发点硬要"现在谈清楚" | 越吵越凶 | 🛑 先关火/换时机；书里说明在爆炸边缘沟通是自相矛盾（第 11 章），可转 attach-secure-communication。 |
| 泛化/翻旧账 | "你总是…你从不…" | 🛑 拉回具体这件事（第 12 章）。 |
| 表达需要变成指控 | "你根本不在乎" | 🛑 用 need/feel/want 重写（第 12 章）。 |
| 敏感话题一直不摆上桌 | 谁也不提，埋着 | 🛑 假设它重要，主动摆上桌（第 12 章）。 |
| 暴力/威胁情境 | 摔物、推搡、恐吓 | 🛑 立即安全出口，不做冲突演练。 |

### 边界规则

1. 安全型也会吵；分歧本身不是关系要坏了的证据。
2. 五原则管的是"怎么吵"，不是"不要吵"。
3. 关火优先于讲理。
4. 不指望读心：没说出来，对方就不知道。
5. 人身安全高于一切冲突目标。

### 用户自查清单

- [ ] 我判断了这是生活冲突还是亲密度冲突
- [ ] 我知道这次违反了哪条安全原则
- [ ] 我有一句当下"关火"的话
- [ ] 我把感受/需要说出来了（need/feel/want）
- [ ] 我留了一个日常"亲近"的小动作

**安全出口**：出现暴力、威胁、控制 → 停止冲突演练，先确保人身安全，联系可信任的人/当地求助（中国大陆 110；美国 1-800-799-7233）。（补充：热线为常识性安全资源）

## 📖 练习手册

书中来源：第 12 章五条安全原则与六个"不安全策略"清单；冲突工作坊六例（Marcus & Daria、Daria、Ruth & John、Steve & Mia、Emma & Todd、Dan & Shannon）；"敏感话题摆上桌"规则；oxytocin 的预防提醒（Preventing Conflict—Attachment Biology 101）。

## 🚫 反例与黑名单

1. **用"安全/不安全"给人贴标签** → 五原则是自查工具，不是判决书。
2. **把"关火"话背成台词、不看对方回应** → 沟通是双向取样。
3. **在暴力/被控制关系里演练"关火话术"** → 不适用，转安全出口。
4. **替用户断言"这次必须分手"** → 只给判断标准，不给判决。

### 灰色地带（需谨慎判断）

5. **对方是回避型、口头上不接但行动上有改** → 观察行动，别只盯语气（第 11 章，可转 attach-secure-communication）。
6. **敏感话题对方一直不主动提**（如见孩子）→ 书中建议：假设它重要，主动摆上桌（第 12 章）。
7. **用户在治疗中** → 与治疗师方案冲突时优先治疗师。
