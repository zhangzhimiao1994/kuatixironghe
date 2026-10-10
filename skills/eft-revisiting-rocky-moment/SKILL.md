---
name: eft-revisiting-rocky-moment
description: 把一次已经冷下来的冲突重新演一遍——按书里"重温低谷"七步走（停战→认自己的步→认自己的感受→认自己对对方的影响→对对方的软情绪好奇→说出自己更软的情绪→站到同一边），让一场越滚越大的架变成能一起复盘的"共同因"。当用户说"我们想重演上次那场架""我想拉他回去把刚才那段重来一遍""can we just go back and do that again""怎么才能不每次都滚到最后"时使用。
input_schema:
  required: [incident_to_replay, both_partners_moves, cooling_status]
  optional: [surface_emotions_each, deeper_fears_each, raw_spots_known]
output_schema:
  primary: {seven_step_replay: string, deescalation_summary: string, standing_together_statement: string}
  secondary: [moves_summary, impact_owned, rewind_signal]
---

# 重温低谷：把一次已经冷下来的冲突按七步重演一遍

**来源**：《Hold Me Tight》Conversation 3: Revisiting a Rocky Moment | 证据等级：firsthand

## 触发条件

**应该触发**：
- 一次已经冷下来的冲突想"重演一遍"、"回去把刚才那段重来"
- 用户说"我知道我们怎么越滚越大的，但想一步步看清是第几句开始拐弯的"
- 两人想练"在一场架的中途把它停下来"，而不是事后才后悔
- 已经能认出循环、能叫出雷区名字，想把这套语言练到"踏错地就能马上跑开"
- 用户引用书里那句"can we just go back and do that again?"

**不应触发**：
- 雷区本身还没拆清（还说不出表层 vs 底层情绪）→ 先走 eft-raw-spot-deescalation
- 连冲突循环都还没看清 → 先走 eft-demon-dialogues
- 未愈合的关系创伤（在最需要对方时被丢下、被背叛）挡在前面 → 走 eft-forgiving-injuries，而不是普通的"重演"
- 想把"重演"当审判、逼对方当场认错 → 这不是找共同因的练习
- 有暴力、害怕对方、严重成瘾或长期婚外情 → 不在对话脚本适用范围（见 B 节安全出口）

## R：原文锚点

> "In this conversation, you'll see how to take charge of moments of emotional disconnection, or mis-attunements, as attachment theorists call them, and tip them away from dangerous escalation and toward safety and security."（Conversation 3: Revisiting a Rocky Moment · 开篇）（已据原文核）

> "Here are the steps that can set them on the path to greater harmony: 1. Stopping the Game."（Conversation 3 · De-escalating Disconnection；其后各步的原文标题依次为 "2. Claiming Your Own Moves." "3. Claiming Your Own Feelings." "4. Owning How You Shape Your Partner's Feelings." "5. Asking About Your Partner's Deeper Emotions." "6. Sharing Your Own Deeper, Softer Emotions." "7. Standing Together."）（已据原文核）

> "Although voicing your deepest emotions, sometimes sadness and shame, but most often attachment fears, may be the most difficult step for you, it is also the most rewarding."（Conversation 3 · 第 6 步 Sharing Your Own Deeper, Softer Emotions）（已据原文核）

> "When I'm calmer, I search him out. “Hmm, can we just go back and do that again?” I ask. Then we press the mental rewind button and replay the incident."（Conversation 3 · 作者自己的"重播"做法）（已据原文核）

> "They no longer see each other as adversaries, but as allies."（Conversation 3 · 第 7 步 Standing Together）（已据原文核）

## I：核心解释

1. **这是第 3 号对话，位置很明确**：不是第一次看见循环（Conversation 1），也不是拆雷区（Conversation 2），而是把一次真实的冲突**慢动作重演一遍**，学会在中途把它拐向安全。
2. **重演的对象是"已经冷下来"的一件具体事**：书里建议挑 2–3 周内、不太难的一件小事先练；正在燃烧的架不重演，先停战。
3. **目标是降级、恢复情绪平衡**，不是解决问题、也不是立刻亲密：让两人被踩到脚之后能转身做损伤控制，能"hold on to their emotional balance a lot more often and a lot more easily"。
4. **七步是一条固定路径**（书里按顺序列出）：① Stopping the Game ② Claiming Your Own Moves ③ Claiming Your Own Feelings ④ Owning How You Shape Your Partner's Feelings ⑤ Asking About Your Partner's Deeper Emotions ⑥ Sharing Your Own Deeper, Softer Emotions ⑦ Standing Together。
5. **关键在 ④ 与 ⑥**：认自己那一步怎么推对方失衡，以及说出自己更软的恐惧/悲伤；书里说第 6 步"may be the most difficult step for you, it is also the most rewarding"。少了这两步，重演就只是各自陈述委屈。
6. **这是练出来的技能，不是一次性的手术**：书里说要"It takes practice, going over an unsettling past encounter again and again until it makes coherent sense"；练久了会"They feel the ground shaking sooner, and they are able to escape it faster."。
7. **降级有两个关键认知**：一，冲突关键点上伴侣怎么回应，可以深深地伤到对方；二，伴侣那些负面的反应，往往是在绝望地应对自己的依恋恐惧。
8. **重演 ≠ 已经安全依恋**：书里说重演完不代表两人已经"securely bonded"，只代表"they know how to stop a rift before it widens into an unbridgeable abyss"。

## A1：来源应用 — 书里给的具体做法

以 Claire 和 Peter 那场架为范本，书里逐步示范了七步：

1. **① Stopping the Game**：把"我/你"换成"我们"。Peter 的示范是 "Can we stop this? Aren't we both defeated in this spiral?"；Claire 于是改口："This is the place we always go to. We get trapped here."——停战不是认输，是换一个代词。
2. **② Claiming Your Own Moves**：各自只认自己的动作，再合成一句短摘要——书里的版本是 "Claire loses it while Peter plays impervious; Claire gets louder and threatens; Peter sees her as impossible and tries to escape."。允许自嘲（书例 "The impervious rock and the bossy broad."）。
3. **③ Claiming Your Own Feelings**：说自己的表层情绪，不 disguise 成指责；可用"parts"的说法，书例 "part of me is numb. It's my automatic response when we get stuck like this. But I guess part of me is shaken up, too."
4. **④ Owning How You Shape Your Partner's Feelings**：承认自己那一步怎么把对方拉进螺旋。书例 Peter："In these fights, I defend and then stop talking. That's when my shutting down gets you all freaked out, isn't it? You start to feel like I am not here with you."
5. **⑤ Asking About Your Partner's Deeper Emotions**：对对方的软情绪真正好奇，而不是只顾自己的伤。书例 Peter："I get into thinking that you are just out to put me down. But in these situations, you are not just mad, are you? Under all that noise and raging you are hurting, aren't you?"
6. **⑥ Sharing Your Own Deeper, Softer Emotions**：说出自己更软的情绪，让伴侣看见你吵架时真正在赌什么。书例 Claire："I am hurting but it's hard to tell you that. I have this sense of dread. I can feel it like a lump in my throat."
7. **⑦ Standing Together**：从对手变成盟友。书例 Peter："I like it when we can stop and turn down the volume. … Even if we are not quite sure where we go next, this is a lot better."
8. **"重播"的比喻**：书里作者自己的做法——等自己冷静，回头找伴侣："can we just go back and do that again?"，然后 "press the mental rewind button and replay the incident."
9. **书里第二个案例**（Kerrie 和 Sal）示范"认出自己对伴侣的影响"与"认出恐惧怎么驱动对方"：Sal 被追问"等待她是什么感觉"后，从愤怒底下说出 "It's agonizing" 和 "I don't feel important to her at all."；Kerrie 则第一次看见自己的疏远怎样点着了对方的依恋恐惧。

## A2：典型触发场景

- 吵完冷静下来，一方说"我们能不能回去把刚才那段重来一遍"
- 一件事过去几天了，两人坐下来慢放它，想看清从第几句话开始拐弯
- 卡在"我们都知道这个圈，但一进去就出不来"，想练中途喊停
- 想学会在踏错地的那一刻马上警觉（书里："They feel the ground shaking sooner, and they are able to escape it faster."）
- 两人刚给某个雷区起好名字，想拿它去回放最近一次被磨到的架
- 一方总说"我要把话说清楚"，其实想要的是一次能站同一边的复盘

## E：执行步骤

### 步骤 1：Stopping the Game（停战，把"我/你"换成"我们"）

**输入**：一件已经冷下来的具体冲突。
**输出**：一次停火 + 一句用"我们"说的话。

先确认这件事**已经冷下来**（不在现场、情绪不再烧）。让两人各说一句"我们又进了那个圈"，把代词从 I/you 改成 we。书里的示范句是 "Can we stop this? Aren't we both defeated in this spiral?"

🔴 **CHECKPOINT — 触发条件：话题还是烫的，一提起就又要吵起来**：**不硬推七步**。只做这一步（停战 + 用 "we"），各自降温，改天再重演。书里作者自己的做法就是等冷静之后再说 "can we just go back and do that again?"

### 步骤 2：Claiming Your Own Moves（只认自己的步）

**输入**：步骤 1 的停战。
**输出**：一句两人都同意的"我的步 → 你的步 → 我的步"短摘要。

各自只描述**自己**的动作，再一起压成一句摘要（书例："Claire loses it while Peter plays impervious; Claire gets louder and threatens; Peter sees her as impossible and tries to escape."）。允许用自嘲的绰号。

🔴 **CHECKPOINT — 触发条件：用户借"我的步"其实在数落对方（"我的步就是被逼成这样"）**：把话收回自己身上。只准用动词描述自己做了什么；一旦滑回"都是你害的"→ 先退回 eft-demon-dialogues 看清循环。

### 步骤 3：Claiming Your Own Feelings（认自己的感受）

**输入**：步骤 2 的步数图。
**输出**：各自一句表层的愤怒 / 麻木 / 慌乱。

说自己的表层情绪，别把它伪装成指责；可以用"parts"的说法（书例："part of me is numb. It's my automatic response when we get stuck like this. But I guess part of me is shaken up, too."）。

🔴 **CHECKPOINT — 触发条件：一方说着说着升级、要崩、想逃**：**先停**，回到身体与当下（"我们先不急着往下走，回到呼吸、回到这个房间"）。这种状态要的是安全容器，不是继续重演。

### 步骤 4：Owning How You Shape Your Partner's Feelings（认自己对对方的影响）

**输入**：步骤 3 的表层情绪。
**输出**：一句"我这一招是怎么把你推失衡的"。

这一步不可省：承认自己那步怎么把对方拉进螺旋。书例 Peter："In these fights, I defend and then stop talking. That's when my shutting down gets you all freaked out, isn't it? You start to feel like I am not here with you."

🔴 **CHECKPOINT — 触发条件：用户用"我其实很脆弱／我很可怜"回避这一步（只谈自己受伤、不谈自己对对方的作用）**：补做第 ④ 步。脆弱不是免责——"我承认我这步怎么推了你"必须说出口。

### 步骤 5：Asking About Your Partner's Deeper Emotions（对对方的软情绪好奇）

**输入**：步骤 4 的认账。
**输出**：一次对对方底层情绪的询问，并让对方感到被听见。

从"只顾自己的伤"转到对对方的软情绪真正好奇。书例 Peter："I get into thinking that you are just out to put me down. But in these situations, you are not just mad, are you? Under all that noise and raging you are hurting, aren't you?"

🔴 **CHECKPOINT — 触发条件：好奇心变成新一轮审问／逼供（"你到底怕什么，说！"）**：**放慢**。先自己猜一个版本、请对方纠正，而不是逼对方当场交出答案。

### 步骤 6：Sharing Your Own Deeper, Softer Emotions（说出自己更软的情绪）

**输入**：步骤 5 的彼此好奇。
**输出**：一句自己的恐惧 / 悲伤 / 羞耻。

书里说这一步 "may be the most difficult step for you, it is also the most rewarding"。说出更深、更软的情绪，让伴侣看见你吵架时真正在赌什么。书例 Claire："I am hurting but it's hard to tell you that. I have this sense of dread. I can feel it like a lump in my throat."

🔴 **CHECKPOINT — 触发条件：一方说出脆弱后立刻被反击／被拿来对付，或用户明显害怕对方**：**立即停**，转 B 节安全出口，不再继续披露。书里明说：对伴侣的善意有实质怀疑、甚至身体上害怕对方时，"it is best not to confide"。

### 步骤 7：Standing Together（站到同一边）

**输入**：步骤 6 的彼此披露。
**输出**：一句"我们怎么互相钩住"的总结 + 一句下次可用的预警。

把两人从对手变成盟友。书例 Peter："I like it when we can stop and turn down the volume. … Even if we are not quite sure where we go next, this is a lot better." 强调这是练出来的技能、不是一次就会：书里说要一遍遍重演，直到它 "makes coherent sense"。

🔴 **CHECKPOINT — 触发条件：用户把这次重演当成"问题解决了／关系没事了"**：降级期待——重演只求"停得下来、看得到"，不求立刻亲密。书里说这不代表两人已经安全依恋，只代表 "they know how to stop a rift before it widens into an unbridgeable abyss"。

## B：边界与失败模式

### 失败模式分支表

| 失败场景 | 表现信号 | 立即执行替代动作 |
|---------|---------|----------------|
| 重演变成重炒 | 一进第 ①② 步又开始互相指责 | 🛑 回到第 ① 步只做停战 + 用 "we"；热度不降就改天再来。 |
| 用"我很脆弱"当挡箭牌 | 用"你看我多可怜"回避第 ④ 步（承认自己那步怎么推了对方） | 🛑 补做第 ④ 步：脆弱不是免责，"I get into thinking that you are just out to put me down." 这类必须说清。 |
| 跳步、只走一半 | 只停在"互相说感受"，不碰 ④ 与 ⑥ | 🛑 指明 ④ 与 ⑥ 是关键步；缺了它，重演只是各自陈述委屈。 |
| 反复升级、练不动 | 每次重演都吵起来或彻底关掉 | 🛑 只保留第 ① 步（停战 + 用 "we"），降低任务量；考虑专业陪伴。 |
| 把重演当一次性手术 | 做一次没完全好就判"没用" | 🛑 正常化重复：书里说要 "again and again"；把它当技能练，不是手术。 |
| 有暴力／威胁／害怕对方 | 描述含推搡、恐吓、控制、性强迫，或"我不敢跟他说真话，他会……" | 🛑 **安全出口，不给沟通话术**。停止双人重演，转向个体安全资源。书里：若身体上害怕伴侣，"it is best not to confide"。 |
| 严重成瘾 / 长期婚外情 | 成瘾或长期隐瞒主导关系 | 🛑 **安全出口**：书里 Introduction 把 abusive or violent relationships、serious addictions、long-term affairs 一并列为不适用情形，"a therapist is the best resource." |
| 自伤／危机念头 | 提到不想活、绝望到底 | 🛑 停止技术性工作，先做危机支持并转介；本 skill 不做诊断。 |

### 边界规则

1. **只重演已经冷下来的事**：正在烧的架先停战，不重演。
2. **目标是恢复平衡，不是解决**：降级是为安全，不是为立刻亲密。
3. **第 ④ 与 ⑥ 步不可省**：认自己对对方的影响、说出自己更软的恐惧，是这整套的关键。
4. **不追、不逼、不"逼供"**：对方还不安全时，一次都不必强推七步。
5. **脆弱披露有前提**：书里画了安全线——对伴侣善意有实质怀疑、或身体上害怕对方时，**不要**披露脆弱。
6. **不诊断、不替代治疗**：这里只做对话重演与情绪拆解，不做心理诊断。

### 用户自查清单

- [ ] 我挑的是一件**已经冷下来**的具体事件
- [ ] 我们能把代词从"我/你"换成"我们"（第 ① 步）
- [ ] 我说得出**自己那一步**的动作（第 ② 步）
- [ ] 我完成了第 ④ 步——承认**自己那步**怎么推了对方
- [ ] 我对对方的软情绪**好奇**，而不只是顾自己的伤（第 ⑤ 步）
- [ ] 我说出了自己更软的情绪（第 ⑥ 步）
- [ ] 我清楚**下一次的预警信号**是什么（第 ⑦ 步）

**勾选 5+ 项**：重演在正常轨道上，可继续练习。
**≤ 3 项**：多半卡在第 ④ 步（只谈自己受伤）或跳步——回到对应步骤，或先退回 eft-raw-spot-deescalation。

## 📖 练习手册

配套 6 天练习：
1. **选一件事**：挑 2–3 周内、不太难的一件小事，写成一两句可复述的经过。
2. **代词切换**：把当时说的"我/你"全改写成"我们"，读出声。
3. **步数图**：用动词描出"我的步 → 你的步 → 我的步"，再压成一句摘要。
4. **第 ④ 步单独练**：写一句"我这一招是怎么把你推失衡的"。
5. **第 ⑥ 步单独练**：写下你那时真正怕失去什么、最软的那句是什么。
6. **共同因**：把这次重播总结成一句"我们怎么互相钩住"的话，各写一版再合并；约定一句下次可用的预警语。

## 🚫 反例与黑名单

以下场景**禁止**用本 skill，或必须降级处理：

1. **把"重演"变成审判**（"现在你总该承认你错在哪了吧"）→ 🛑 停。重演的目标是找共同因，不是定罪。
2. **在危险关系里做脆弱披露** → 🛑 书里直接警告：若身体上害怕伴侣，"it is best not to confide"；此时应走安全出口，而非更深的自我暴露。
3. **跳过雷区直接重演** → 还没拆清表层/底层情绪就重演，容易又变成表层的对骂。先走 eft-raw-spot-deescalation。
4. **把"我脆弱"当免责** → 脆弱不是跳过第 ④ 步的借口。
5. **用本 skill 替代治疗** → 创伤级议题、抑郁、成瘾需专业帮助，这里只做理解与降级。

### 灰色地带（需谨慎判断）

6. **只有一方愿意重演，另一方缺席** → 先做单人版（走 ②③④⑥ 里属于自己的部分），不强制对方在场；重建基本安全后再考虑双人七步。
7. **重演中途发现底下是一道旧伤** → 它不是普通雷区，转 eft-forgiving-injuries 单独处理那道伤，再回来重演当下。
8. **两人只想学话术、不想碰情绪** → 回应："七步不是台词，真正让它接通的是你说第 ⑥ 步时带着什么。先看看那句最软的话是什么。"
9. **这是正在接受治疗的伴侣** → 优先遵循治疗师安排；本 skill 是补充理解与练习工具，不替代治疗方案。
