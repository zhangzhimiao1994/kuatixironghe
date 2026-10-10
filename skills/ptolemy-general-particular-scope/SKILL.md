---
name: ptolemy-general-particular-scope
description: 通用与特定之分的取舍。当用户问“该先看大势还是先看个人”“国族与时代的大势怎么压过个人”“这层象征分析从哪儿入手”，或想让星盘类象征材料别滑向命定论时使用。按托勒密的分法，先把要分析的对象分成通用（国族、地域、城市）与特定（个人）两支，通用优先；再把通用支落到“地域亲缘”与“日月食等天象”两大要点上，并把整套说法限定在自然理性之内。
input_schema:
  required: [analysis_question, subject_type]
  optional: [time_hint, region_hint]
output_schema:
  primary: {layer_split: string, priority_note: string, entry_point: string}
  secondary: [two_essentials, safety_limit]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 通用与特定之分：先定层次，再谈个人

**来源**：《Tetrabiblos》BOOK THE SECOND, CHAPTER I: GENERAL DIVISION OF THE SUBJECT（Ashmand 译本）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户拿着一份要分析的材料问“这层象征分析该先看什么、从哪儿切入”
- 用户把“时代／国家／群体的大势”和“某个人的处境”混在一起问，需要先分层
- 用户问“一个地方、一个时代的大势，是不是压得过个人”
- 用户在做象征层推演，想先划一条“只谈倾向、不谈命中注定”的边界
- 用户要判断：某个问题该落到国族／地域／城市，还是落到个人

**不应触发**：
- 用户已经明确要分析某个地区／民族的性格 → 走 `ptolemy-region-familiarity`
- 用户拿着一个具体的日月食问细节（地域、时间、种类、性质）→ 走 `ptolemy-general-event-eclipse`
- 用户问年／季／月的天气与大气状况 → 走 `ptolemy-annual-atmosphere`
- 用户要某个人的本命盘细节 → 不在本书第二卷范围，走个人命盘类方法
- 用户只想要一句“这事会不会发生” → 本 skill 只定层次与边界，不给结论

## R：原文锚点

> "care shall be taken to confine the whole doctrine within the limits of natural reason."（BOOK THE SECOND, CH. I: GENERAL DIVISION OF THE SUBJECT）（已据公版原文核）

> "The foreknowledge to be acquired by means of Astrology is to be regarded in two great and principal divisions."（BOOK THE SECOND, CH. I）（已据公版原文核）

> "The first, which may be properly called General, or Universal, concerns entire nations, countries, or cities; and the second, denominated Particular, or Genethliacal, relates to men individually."（BOOK THE SECOND, CH. I）（已据公版原文核）

> "general events are produced by causes greater and more compulsatory than the causes of particular events"（BOOK THE SECOND, CH. I）（已据公版原文核）

> "particular events, or individual affections, are comprehended in those of general influence."（BOOK THE SECOND, CH. I）（已据公版原文核）

> "It is therefore especially necessary, in desiring to investigate particular events, to treat first of those which are general."（BOOK THE SECOND, CH. I）（已据公版原文核）

> "the appropriate familiarity of the zodiacal signs and the fixed stars with the several regions which may be concerned"（BOOK THE SECOND, CH. I）（已据公版原文核）

> "the eclipses of the Sun and Moon, and such transits as may be made by the planets"（BOOK THE SECOND, CH. I）（已据公版原文核）

## I：核心解释

1. **先分两支**：整本书要谈的“预先知道”，被分成两大支——一支叫通用（General／Universal），管国族、国家、城市；一支叫特定（Particular／Genethliacal），管个人的事。任何象征层分析，第一步都先问“这片内容落在哪一支”。（R2、R3）
2. **通用优先**：书里给了三条理由——通用事件由更大、更具强制性（compulsatory）的原因产生；范围更广、力量更大的本性必然支配范围更小者；而特定事件本身被包含在通用影响之中。所以通用支排在前面。（R4、R5）
3. **所以先通用、后特定**：想查特定事件，必须先论通用事件。这不是偏好，是书里的操作次序。（R6）
4. **通用再分两小支**：按作用对象分，有“整片国土”与“某些城市／地区”两小支；按成因分，战争、瘟疫、饥荒、地震、洪水这类由大原因产生、要隔很久才出现；季节寒暑、天气温和或严酷、物产丰歉这类由较轻原因产生、出现得更频繁。（补充：对第 3088–3099 行两处分法的归纳）
5. **通用支的两大要点**：一是黄道十二宫与恒星同“各地区”的亲缘（familiarity）；二是这些有亲缘的天区里偶发的征象——日月食，以及行星晨见与在留驻（stations）时的过运。（R7、R8）
6. **自然理性之界**：整套说法要“限定在自然理性之内”。这不是装饰——它意味着后面所有推演都只谈倾向与较可能，不承诺必然。象征层分析必须戴着这条边界说话。（R1）

## A1：来源应用 — 书上给的具体做法

- **先置顶通用性更高的一支**：书里明确要求“给了通用支优先”，理由是它管的时间更长、力量更大、且个人被包在其中。（R4、R5、R6）
- **按对象层级找入口**：先落到“整片国土”，再落到“某些城市或地区”，最后才是个人。（R3）
- **调查通用事件先立两要点**：其一，查该地区与黄道宫、恒星的亲缘；其二，看该天区里是否发生日月食、行星是否晨见或留驻。（R7、R8）
- **用自然理性收敛结论**：凡是要下判断的地方，都收在“自然理性”内，不越界成断语。（R1）

## A2：典型触发场景

1. 用户把“今年是不是大环境不好”和“我今年怎么办”揉成一句问出来
2. 用户拿着一个国家的材料，问“这层象征分析该从哪儿下手”
3. 用户在写一份跨体系分析，不知道该先写大势还是先写个人
4. 用户担心象征层分析变成“算命”，想先给它上一条“只谈倾向”的边界
5. 用户问“一个地区的大势会不会盖过某个人的选择”

## E：执行步骤

### 步骤1：判定落在哪一支

**输入**：用户的问题 + 分析对象。
**输出**：一句判定——这是通用支（国族／地域／城市）还是特定支（个人）。
照 R2、R3，先分清对象是谁。

🔴 **CHECKPOINT — 触发条件：对象其实是个人，但用户问的是大势**：先说明“通用优先”，把大势做在前面，再谈个人被大势覆盖的部分；不要跳过通用直接算个人。

### 步骤2：通用支再分两小支

**输入**：步骤1 判为通用的问题。
**输出**：对象层级（整片国土／某些城市／某些地区）+ 成因层级（大原因／季节小原因）。
照第 3088–3099 行的两处分法。（补充：对该处分法的归纳）

🔴 **CHECKPOINT — 触发条件：用户给不出地区或大致时空信息**：先追问地区与大致时段；若确实给不出，就只停在框架层，不下任何倾向性结论。

### 步骤3：立两大要点，指向下游

**输入**：步骤2 定下的地区与层级。
**输出**：两条入口——①地区亲缘（转 `ptolemy-region-familiarity`）；②天象征象（日月食转 `ptolemy-general-event-eclipse`，年季时令转 `ptolemy-annual-atmosphere`）。
照 R7、R8。

🔴 **CHECKPOINT — 触发条件：既无地点也无时间锚点**：不推演。明确告诉用户“前提不足”，请其补齐大致时空信息。

### 步骤4：划安全边界

**输入**：前面定下的层次与入口。
**输出**：一句限定语——“本层只作倾向性推演，限定在自然理性之内，不作必然结论”。
照 R1。

🔴 **CHECKPOINT — 触发条件：用户要求“必然／一定”或想把结论说成灾难预告**：拒绝命定论措辞，回到倾向性表达；若牵扯天灾／灾异／群体恐慌，按 B 节安全兜底处理。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 把框架当结论用 | 只做了分层，就给出“某国将如何” | 🛑 本 skill 只定层次与入口，具体判断转下游三个 skill |
| 通用结论直接套到个人 | 用“某地区的人如何”去断言某个具体人 | 🛑 通用支只谈倾向与群体分布，个人要另走个人命盘类方法 |
| 缺时空锚点硬推 | 只有一句“看看大势”就下断语 | 🛑 回到步骤2、3 的 CHECKPOINT，先问清地区与大致时段 |
| 写成命定论 | 用“注定／必然／逃不掉” | 🛑 回到步骤4，改用 R1 的自然理性措辞 |
| 层次越做越细却停不下来 | 在通用与特定之间反复切换 | 🛑 按“通用优先”一次性排序：先通用支全部做完，再落个人 |
| 把古代的群体成见当事实 | 把书里的民族描述当作真实人群的断言 | 🛑 见 `ptolemy-region-familiarity` 的边界规则：那是象征素材，不是事实判断 |

### 边界规则

1. **本 skill 只管“分层与边界”**：不含任何地域、天象、气候的具体读法，那些在下游三个 skill。
2. **通用优先是操作次序**，不是价值判断：不代表个人不重要，只代表先看大势再看个人。
3. **必须留白**：给不出时空信息就不推，宁缺勿假。
4. **与相邻 skill 分工**：地区画像 → `ptolemy-region-familiarity`；日月食等全体性事件 → `ptolemy-general-event-eclipse`；年季时令与天象 → `ptolemy-annual-atmosphere`。
5. **安全兜底**：本层是象征层的推演，不替代任何专业判断。涉及就医、用药、心理危机时，只做提醒与陪伴，不做诊断；涉及天灾、灾异、群体性内容时，只作倾向性推演，不作预言、不引起恐慌。

### 用户自查清单

- [ ] 我说清了这个问题落在通用支还是特定支
- [ ] 我按“通用优先”排了次序，没有跳过通用直接算个人
- [ ] 我要么能给出地区与大致时段，要么明确说明前提不足
- [ ] 我没有把框架里的分层当成具体结论
- [ ] 我给结论加上了“只谈倾向、不作必然”的限定

**勾选 4+ 项**：层次与边界到位。**≤ 2 项**：多半是拿框架当结论，或忽略了前提，回到对应步骤。

## 📖 练习手册

**两分练习**：写三个你最近想问的问题，逐个判定它落在通用支还是特定支，并说明理由。

**优先次序练习**：拿一个“国族大势”与“个人处境”混在一起的问题，按书里三条理由（更大原因、更强本性支配、个人被包含）写一句话说明谁优先。

**边界句练习**：给你的分析写一句收尾限定语，把结论限定在“自然理性之内”。

## 🚫 反例与黑名单

1. **拿分层框架去下具体结论** → 🛑 框架只负责定位，判断归下游 skill。
2. **把通用结论直接安到某个具体人头上** → 🛑 群体倾向 ≠ 个人命运。
3. **写成命定论（注定／必然／逃不掉）** → 🛑 违背“限定在自然理性之内”。
4. **没有时空锚点也照推** → 🛑 前提不足时停在框架层。
5. **把古代的民族描述当成对真实人群的事实断言** → 🛑 见 region skill 的灰区处理。

### 灰色地带（需谨慎判断）

1. **“一个企业／一个球队”算通用还是特定**：书里只分了“整片国土／某些城市”与“个人”。介于两者之间的团体，按“它影响的范围更接近群体还是更接近个人”来归支（补充）。
2. **一个人同时被大势与个人因素影响**：先做通用支，再把它对个人的覆盖作为特定支的约束，不要反过来让个人结论去推翻大势。
3. **用户只想要一句安慰性的“吉凶”**：说明本层只定层次、不给吉凶结论，把具体问题导向对应下游 skill。
