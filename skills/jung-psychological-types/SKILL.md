---
name: jung-psychological-types
description: 荣格心理类型（两态度×四功能）。当用户说"我跟我伴侣/同事总在同一个点上互相说不通""测出来 INFP，我到底是不是内向""应酬完像被抽干""一到临场拍板就僵住，事后又懊恼"时使用。用内倾/外倾两态度与思维/情感/感觉/直觉四功能，定位主导功能、辅助功能，以及被压进无意识的劣势功能，解释他长期卡在哪、一激动在哪失控。
input_schema:
  required: [recurring_conflict, energy_drain_pattern, freeze_or_blowup_moment]
  optional: [test_result_claim, childhood_pressure, relationship_pattern, dream_symbols_of_two_animals]
output_schema:
  primary: {attitude_hypothesis: string, dominant_function: string, auxiliary_function: string, inferior_function: string}
  secondary: [development_path_via_auxiliary, self_check_examples, boundary_flags]
---

# 心理类型：两态度 × 四功能 —— 你在哪里卡住，又在哪里失控

**来源**：荣格全集 Vol 6《Psychological Types》第十章「General Description of the Types」、第十一章「Definitions」、附录「Four Papers on Psychological Typology」（第三章 3『A Contribution to the Study of Psychological Types』、第四章 4『Psychological Typology』）；Vol 8「On Psychic Energy / b. Extraversion and Introversion」「Psychological Factors Determining Human Behaviour」补充 | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我跟我伴侣（同事/父母）总在同一个点上互相说不通，谁也没法说服谁"
- "测出来 INFP / INTJ，我到底是不是内向？见完人就像被抽干"
- "平时想得挺清楚，一到临场要拍板就僵住，事后又懊恼"
- "平时挺稳，一吵架/一被否定就爆一句最伤人的话，说完自己也吓一跳"
- "我知道自己擅长什么，但总在一些小事上特别笨、特别容易上头"

**不应触发**：
- 需要精神科评估（抑郁发作、双相、ADHD、人格障碍）→ 转专业，类型不能代替诊断
- 纯职业规划、要不要跳槽 → 走生涯/决策类 skill
- 用户想要一次"四选一测试"或要一个字母结论 → 本 skill 不出题、不下判词
- 用户只想给第三方贴标签（"我老板绝对是 INTJ"）→ 拒绝替他人判定
- 急性危机（自伤意念、家暴、精神病性症状）→ 先安全，见 B 节

## R：原文锚点

> "The former I would call attitude-types, distinguished by the direction of their interest, or of the movement of libido; the latter I would call function-types."
> — CW 6, ¶556, p3424（译自英文本）

> "The introvert's attitude is an abstracting one; at bottom, he is always intent on withdrawing libido from the object, as though he had to prevent the object from gaining power over him. The extravert, on the contrary, has a positive relation to the object."
> — CW 6, ¶557, p3424（译自英文本）

> "Now, when orientation by the object predominates in such a way that decisions and actions are determined not by subjective views but by objective conditions, we speak of an extraverted attitude. When this is habitual, we speak of an extraverted type."
> — CW 6, ¶563, p3428（译自英文本）

> "the introvert is distinguished from the extravert by the fact that he does not, like the latter, orient himself by the object and by objective data, but by subjective factors."
> — CW 6, ¶620, p3476（译自英文本）

> "Sensation establishes what is actually present, thinking enables us to recognize its meaning, feeling tells us its value, and intuition points to possibilities as to whence it came and whither it is going in a given situation."
> — CW 6, ¶958, p3667（译自英文本）

> "Closer investigation shows with great regularity that, besides the most differentiated function, another, less differentiated function of secondary importance is invariably present in consciousness and exerts a co-determining influence."
> — CW 6, ¶666, p3513（译自英文本）

> "Experience shows that the secondary function is always one whose nature is different from, though not antagonistic to, the primary function. Thus, thinking as the primary function can readily pair with intuition as the auxiliary, or indeed equally well with sensation, but, as already observed, never with feeling."
> — CW 6, ¶668, p3515（译自英文本）

> "In these cases the most differentiated function is always employed in an extraverted way, whereas the inferior functions are introverted; in other words, the superior function is the most conscious one and completely under conscious control, whereas the less differentiated functions are in part unconscious and far less under the control of consciousness."
> — CW 6, ¶575, p3436（译自英文本）

> "A classic example of this is the extraverted feeling type, who enjoys an excellent feeling rapport with the people around him, yet occasionally “happens” to express opinions of unsurpassable tactlessness. These opinions spring from his inferior and half-conscious thinking, which, being only partly under his control and insufficiently related to the object, can be quite ruthless in its effects."
> — CW 6, ¶575, p3436（译自英文本）

> "a man identifies more or less completely with the most favoured and hence the most developed function. It is this that gives rise to the various psychological types"
> — CW 6, ¶763, p3564–3565（译自英文本）

> "These functions may properly be called inferior in a psychological but not psychopathological sense, since they are in no way morbid but merely backward as compared with the favoured function."
> — CW 6, ¶763, p3565（译自英文本）

> "the inferior function undergoes a regressive development; it reverts to the archaic … stage and becomes incompatible with the conscious, favoured function."
> — CW 6, ¶764, p3565（译自英文本）

> "the approach to the unconscious and to the most repressed function is disclosed, as it were, of its own accord, and with adequate protection of the conscious standpoint, when the way of development proceeds via the auxiliary function"
> — CW 6, ¶670, p3516（译自英文本）

> "The unconscious functions exist in an archaic, animal state. Hence their symbolic appearance in dreams and fantasies is usually represented as the battle or encounter between two animals or monsters."
> — CW 6, ¶671, p3516（译自英文本）

> "The inferior function always puts us at a disadvantage because we cannot direct it, but are rather its victims."
> — CW 6, ¶956, p3667（译自英文本）

> "The four functions are somewhat like the four points of the compass; they are just as arbitrary and just as indispensable."
> — CW 6, ¶958, p3667（译自英文本）

> "As a rule, whenever such a falsification of type takes place as a result of parental influence, the individual becomes neurotic later, and can be cured only by developing the attitude consonant with his nature."
> — CW 6, ¶560, p3427（译自英文本）

> "The typical form his neurosis takes is psychasthenia, a malady characterized on the one hand by extreme sensitivity and on the other by great proneness to exhaustion and chronic fatigue."
> — CW 6, ¶626, p3481（译自英文本）

> "The second modality is extraversion and introversion. It determines the direction of psychic activity, that is, it decides whether the conscious contents refer to external objects or to the subject. … This modality operates so persistently that it builds up habitual attitudes, that is, types with recognizable outward traits."
> — CW 8, ¶250, p4545（译自英文本）

## I：核心解释

1. **态度不是性格，是力比多朝哪流。** 荣格把"内倾/外倾"定义成兴趣与力比多（心理能量）的**方向**：外倾朝客体去、内倾从客体撤回（¶556、¶557）。所以它不是"话多话少/爱不爱社交"，而是"决定权交给自己，还是交给外部条件"（¶563、¶620）。

2. **两种态度是两套适应策略，不是好坏的。** 荣格说它们"以各自的方式同样成功"：一个靠大量关系，一个靠垄断（¶556 上下文）。极端化才出事——外倾的危险是"被客体吸进去、完全在客体里丢掉自己"（¶565）；内倾的典型代价是过度敏感 + 慢性疲惫（¶626）。

3. **四功能两两分工，一对判断、一对知觉。** 感觉说"有什么"、思维说"是什么/意味着什么"、情感说"值不值/好不好"、直觉说"会往哪儿去"（¶958）。思维与情感是**判断**功能（互相排斥），感觉与直觉是**知觉**功能（互相排斥，且不排斥任何判断功能——¶668）。

4. **功能是分化的等级，不是四个抽屉。** 一个人几乎不可能四种功能同时发育（¶763）；社会逼他先发展最顺手那一项，于是人往往**整个认同于**那个最发展的功能（¶763）——这就是"类型"的来源。剩下的功能没有被删除，只是**滞后**：荣格特别强调这是"心理学意义上的劣势，不是病理学意义上的"（¶763）。

5. **主导—辅助—劣势，是一条能量梯度。** 主导功能（最分化、完全在意志控制下）＋辅助功能（次要、但"性质不同又不与主导相抗"，靠它支撑主导，¶666、¶668）＋劣势功能（滞后、部分无意识、不受意志支配，¶575、¶764）。思维不能拿情感当辅助，只能配直觉或感觉（¶668）。

6. **劣势功能：被淹的部分，也是失控的来源。** 主导功能吸走越多力比多，劣势功能就越退化、越"古老"，与意识立场**不相容**（¶764）；它在情绪一上来时替你说出最伤人的那句话——荣格举的例子是"情感型好脾气的人偶尔'脱口'说出极度不得体的话，那出自他半意识的劣势思维"（¶575）。一句话：**劣势功能你指挥不动，它反过来指挥你**（¶956）。

7. **类型是罗盘，不是判词。** 荣格把四功能比作罗盘上的四个方位——"同样任意，也同样的不可或缺"（¶958），他说自己"绝不肯在心理学的航行中放下这副罗盘"（¶959 上下文）。罗盘用来定方向，不用来给人盖戳。

## A1：来源应用 — 荣格本人的用法

- **当罗盘，不当分类柜。** 类型是"家族肖像"：它把共同特征挑出来、放大，个人的东西被同等程度地抹平（¶666 上下文）。所以只能用来**比较和定向**，不能拿来当终审判决。
- **发展路径：先走辅助功能，不要硬攻劣势功能。** 荣格明确警告：分析师一上来就想直接把最被压抑的功能从无意识里拽出来，**注定失败**，还会让来访者变成对分析师的强迫性依赖；正确走法是**经由辅助功能**——理性类型经由某个非理性功能，非理性类型经由某个理性功能，"这给了来访者更宽的视野，也足够保护他的意识立场不被无意识侵入"（¶670）。
- **类型的"被伪造"会出问题。** 若父母态度过强、把与自己相反的态度强加给孩子（违背孩子的天生倾向），这个"类型的伪造"往往让个体日后神经症化，只有**发展回与他本性相合的态度**才能好转（¶560）。这条正对"测出来 INFP，我到底是不是内向"——**先看来访者自己累不累，而不是看字母**。
- **两种态度的两种代价要分开说。** 外倾：卷进客体、忽略自己身体与主观需要，直到身体以症状喊停（¶565 上下文）。内倾：过度敏感、容易耗尽、慢性疲惫（¶626）。
- **劣势功能会在梦里现形。** 无意识功能处于"古老、兽性"的状态，所以它在梦与幻想里常被表现成**两只动物/两只怪物相斗**（¶671）——这是识别"我的劣势功能在哪"的一条线索。

## A2：典型触发场景

- 伴侣/同事间"永远吵不完的同一个话题"：一个要讲道理讲事实，一个在说"你到底在不在乎我"（判断功能错位）。
- 测完 MBTI 拿着字母回来求证，或反过来被字母框住："我是不是必须外向一点？"
- 应酬、团建、见完客户之后像被抽干，要好几天才缓过来（内倾的能量账）。
- 临场拍板就僵住：要在一个具体、突发、需要即时反应的场合做决定时手脚发麻（劣势功能在知觉/判断上失灵）。
- 平时温和，一被触到某个点就爆一句最不该说的话，事后自己都不理解（劣势功能冲破意识立场）。
- 长期"卡在一个位置"：升不上去、也换不了方向，因为整个自我认同都押在了那个最擅长、也最贵的功能上。
- 反复梦见两只猛兽/两个人在打架、拉锯（劣势功能的象征）。

## E：执行步骤

### 步骤1：分三类信号，不先问字母

**输入**：用户对关系的抱怨、疲惫的时刻、僵住或失控的瞬间。
**输出**：三栏清单——①重复冲突的话术；②能量往哪流/在哪被抽干；③临场僵住或情绪失控的原话。

先把这些**原话**抄下来（不加工）。问三类问题，每类至少一个具体场景：
- "你们卡住的到底是"讲不清道理"还是"没被在乎"？"
- "最近一次见完人像被抽干，是哪种场合？"
- "最近一次'晚了半拍才反应过来'或'说完就后悔'，具体发生了什么？"

🔴 **CHECKPOINT — 触发条件：用户直接要一个类型/字母结论**：不要给判词。说："我不给你下型号，我帮你看你的功能怎么排布、你卡在哪。型号是别人测的，你的例子是你自己的。" → 直接进步骤 2。

### 步骤2：推断态度（内倾/外倾）——看"决定权交给谁"

**输入**：步骤1 的能量流向栏。
**输出**：一句话态度假设 + 两条用户自己的例证。

判断不靠"爱不爱说话"，靠两句：
- 事情到来时，他先问"外面是怎么要求的"，还是先问"我自己怎么看/怎么感觉"（¶563、¶620）？
- 恢复能量靠往外冲（关系、行动）还是靠撤回自己（独处、整理）？

🔴 **CHECKPOINT — 触发条件：用户拿测试结果反驳（"我测出来是 E，怎么会累"）**：先分清两件事——**社交技能**和**能量方向**不是一回事。一个技巧纯熟的外倾者也可能累，一个内倾者也能在熟悉的场合很活跃。用他的**恢复方式**校正，不用字母校正（¶560 的"伪造类型"）。

### 步骤3：定位主导功能

**输入**：用户"最信得过、最不费力、最拿得出手"的能力。
**输出**：主导功能候选（思维/情感/感觉/直觉 之一）+ 它"完全在意志控制下"的证据（¶575）。

问："哪一类的判断或感知，是你的默认动作，几乎不用想？"四选一的**功能语言**（不是四选一测试）：
- 总是先讲逻辑对不对 → 思维；总是先掂量值不值得、别人好不好受 → 情感；
- 总是先抓到具体细节、当下事实 → 感觉；总是先感到"这事要往哪儿去" → 直觉。

🔴 **CHECKPOINT — 触发条件：用户说"我四个都行/都不行"**：那是**未分化**的标志（¶705 定义），不是"全能"。不要强行指派主导功能——回到步骤1 找"他越投入就越忽略什么都行、哪件事一做就顺"的场合。

### 步骤4：定位辅助与劣势功能——用"配不上主导"的规则

**输入**：步骤3 的主导功能。
**输出**：辅助功能（与主导不同、但不对立）＋ 劣势功能（主导的**对立面**）。

规则来自原文：判断功能（思维/情感）**不能**当彼此的辅助（¶668）。所以：
- 主导是思维 → 辅助只能是感觉或直觉；劣势必是情感。
- 主导是情感 → 辅助只能是感觉或直觉；劣势必是思维。
- 主导是感觉 → 辅助只能是思维或情感；劣势必是直觉。
- 主导是直觉 → 辅助只能是思维或情感；劣势必是感觉。

劣势功能的线索就是步骤1 里的③栏：**你越信不过、一用就笨、一激动就冒出来的那项**（¶764、¶956）。

🔴 **CHECKPOINT — 触发条件：用户开始把劣势功能当"缺陷"自责**：按住。引 ¶763——它是"心理意义上的滞后，不是病理"，"并不病态，只是相对滞后"。不是你有毛病，是能量被主导功能占满了。

### 步骤5：给发展路径 + 让他自己对照的例子（回答 ≤800 字）

**输入**：步骤2–4 的假设。
**输出**：一段**给来访者自己的**反馈：态度假设、主导/辅助/劣势各一句、一条发展建议、2–3 个他明天就能自检的例子。

- **发展建议照 ¶670 走**：**经由辅助功能**去松土，别硬攻劣势功能。例：主导思维者，先借感觉/直觉（主动去接触具体材料、记下身体信号、跟着"这事往哪去"的感觉走），**不要**逼自己"多谈谈感受"。
- **给自检例子，不给定论**："下次你在会上想立刻反驳的时候，停 3 秒，看那一句是不是从你平时信不过的那项功能里冒出来的。"
- **术语翻译成生活话**：说"你第一反应信的是哪只眼睛"，不说"你是 Te 主导"。

🔴 **CHECKPOINT — 触发条件：回答将要超过 800 字 / 出现内部编号与术语**：砍。删掉引文、页号、§编号、"主导/辅助/劣势功能"等名词，只留他**能复述出来**的一句话判断 + 例子。若他还想深挖，问他要不要就具体那一栏（关系/能量/失控）再展开。

## B：边界与失败模式

### 失败模式分支表

| 触发情况 | 具体表现 | 🛑 处理动作 |
|---------|---------|----------------|
| **情况**：用户逼你下"你就是 X 型"的结论 | 开口即"所以我就是 X 型吧？" | 🛑 若用户逼你下结论 不给型号 → 换成功能偏好语言："这不是你是谁，是你现在最顺手/最信不过的排序。排序会变。" |
| **情况**：用户拿 MBTI/DISC 字母要求对号入座 | 用字母把自陈和你的判断都框死 | 🛑 若拿字母入座 则 分清：荣格的四功能**不等于**任何商业测评 → 只谈功能与他的例子，不背书字母。 |
| **问题**：用户（或你想）要"把最弱那项练成强的" | 把劣势功能当短板要正面硬攻 | 🛑 若用户硬攻劣势功能 不按辅助功能走 → 按 ¶670：**经辅助功能**入手，因为直接攻劣势功能注定失败，还会制造依赖。 |
| **情况**：用户把劣势功能当耻辱自责 | "我怎么这么笨、这么弱，得补上" | 🛑 引 ¶763：这是"心理意义上的滞后，不是病理" → 不是你有毛病，是能量被主导功能占满了。 |
| **情况**：用户说"我四种功能都强/都弱" | 想要一个"全能"或"样样不行"的定位 | 🛑 记为**未分化**（¶705），不硬指派主导功能 → 回到具体场景，从"越投入越顺"和"一激动就冒头"两头夹出排序。 |
| **失败**：用户把任何失败都归给"我是这个型" | "我是这个型，所以我改不了" | 🛑 当用户把失败归给"我是这个型" 则不替行为免责 → 拉回具体处境与技能："类型解释倾向 → 不解释能力，也不为行为免责。" |
| **情况**：用户要分析伴侣/老板是"什么型" | 让你替第三方贴标签 | 🛑 拒绝："我看不到他的内心结构。这套东西是用来看你自己的。" |
| **情况**：回答开始堆"主导/辅助/劣势功能"等术语或超过 800 字 | 出现内部编号、§、页号 | 🛑 砍到他能复述的一句话判断 + 例子 → 他还想深挖，再就具体那一栏（关系/能量/失控）展开。 |
| **症状**：出现绝望、自我伤害、精神病性症状 | 急性危机信号 | 🛑 停类型工作，先安全 → 转专业帮助与热线（见下）。 |

### 边界规则

1. **不诊断、不替代心理治疗。** 类型是理解的罗盘，不是诊断书，也不是急救箱。严重抑郁、双相、人格障碍评估 → 精神科。
2. **不下判词。** 不说"你就是 X 型"。只给功能偏好 + 发展方向 + 他能自己对照的例子。
3. **不做成四选一测试。** 不出题、不打分、不给字母结果。
4. **不把商业测评说成荣格。** MBTI、DISC 等是后来的商业工具，不声称等于荣格的类型学说。
5. **只聊本人，不替他人贴标签。**
6. **安全兜底**：若出现自伤/自杀意念、暴力或急性精神症状——**心理援助热线 12356**；**24 小时热线 010-82951332**；有即时危险拨打**紧急电话 110 / 120**。这些优先于任何类型分析。

### 用户自查清单

- [ ] 我能说出**自己的能量是往外流还是往回收**，并举出两个我自己的例子
- [ ] 我能指出自己**最信得过的那一项功能**（感觉/思维/情感/直觉）
- [ ] 我明白**辅助功能不能和自己的主功能对着干**（思维配感觉或直觉，不配情感，反之亦然）
- [ ] 我能认出**最信不过、一激动就冒头的那一项**，并且不把它当耻辱
- [ ] 我知道下一步是**经辅助功能松土**，不是硬攻最弱那项

**≥ 4 项**：功能排序看清了，可按 E 节继续。
**≤ 2 项**：回到 E 节步骤 1，从具体场景的原话重新收集，不要急于定指数。

## 📖 练习手册

配套 7 天，每天只做一条，做完在本节末尾回看：
1. **能量账本**：连续记三天——哪种场合结束后你回血、哪种结束后你被抽干。
2. **主导功能点名**：写下最近三次"几乎没费力就做对了"的判断，看它们属于哪一类。
3. **劣势功能日记**：记下三次"晚了半拍才反应过来"或"说完就后悔"的瞬间，写清当时情绪是什么。
4. **辅助功能小实验**：借与主导**不同类**的那项功能做一件小事（如思维主导者去实地摸一次具体材料）。
5. **翻译练习**：把一句内部判断改写成生活语言（不出现"主导/劣势功能"这类词）。
6. **梦里找两只动物**：留意有没有两兽/两人相斗的梦（¶671），记下它们各像什么。
7. **回看**：这一周里，你又在**同一个点**上卡住了吗？把它和你的劣势功能对上号。

## 🚫 反例与黑名单

以下场景**禁止**调用此 skill，或必须降级处理：

1. **要求一个型号/字母结论**（"你就说我是什么型吧"）→ 拒绝下判词，只给功能偏好与自检例子。
2. **把商业测评当荣格**（"荣格就是 MBTI 之父吧"）→ 纠正：四功能学说≠任何商业测评，不背书。
3. **替第三方做类型分析**（"帮我分析我伴侣/老板是什么型"）→ 只聊本人，不替他人贴标签。
4. **把类型当免责声明**（"我是这个型，所以我改不了"）→ 类型解释倾向，不为行为开脱，也不解释能力。
5. **用类型替代诊断或治疗**（抑郁/双相/人格障碍的评估请求）→ 转精神科。
6. **急性危机中的类型工作** → 先安全，见 B 节热线。

### 灰色地带

7. **用户说"我测出来 INFP，所以我是内向"** → 不背书字母。分清**社交技能**和**能量方向**：让他用"结束后靠什么回血"来校准，而不是用字母（¶560 的"类型伪造"正是说：被外部态度压出来的类型，会让人日后出问题）。
8. **用户说"我四种功能都很强/都很弱"** → 记为**未分化**（¶705），不要硬指派主导功能；先请他给具体场景，从"越投入越顺"和"一激动就冒头"两头夹出排序。
9. **用户想做"把劣势功能练成优势"** → 按 ¶670：不可行，也危险；方向是**经辅助功能**松土、保护意识立场，而不是正面强攻。若他坚持要"补齐短板"，把目标改成"在低风险场合多给它一点空间"，而不是"练到能靠它吃饭"。
