---
name: ptolemy-general-event-eclipse
description: 日月食与彗星等全体性事件的判读。当用户问“这次日月食意味着什么”“某年某地的大势”“彗星或食相颜色怎么读”时使用。按托勒密四支走：地域（哪些国家城市）、时间（起止与强度）、种类（落在人／兽／作物哪一类）、性质（吉凶由哪颗行星主导），再加颜色与彗星。全程只作倾向性推演，不作灾难预言、不引起恐慌。
input_schema:
  required: [eclipse_or_omen, event_time, relevant_region]
  optional: [eclipse_kind, obscuration_hours, ruling_planet, colours]
output_schema:
  primary: {locality: string, timing: string, quality: string}
  secondary: [kind_affected, colour_comet_note, safety_limit]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 全体性事件判读：地域、时间、种类、性质

**来源**：《Tetrabiblos》BOOK THE SECOND, CH. V（MODE OF PARTICULAR PREDICTION IN ECLIPSES）、CH. VI（THE REGIONS OR COUNTRIES TO BE CONSIDERED AS LIABLE TO BE COMPREHENDED IN THE EVENT）、CH. VII（THE TIME AND PERIOD OF THE EVENT）、CH. VIII（THE GENUS, CLASS, OR KIND, LIABLE TO BE AFFECTED）、CH. IX（THE QUALITY AND NATURE OF THE EFFECT）、CH. X（COLOURS IN ECLIPSES; COMETS, AND SIMILAR PHENOMENA）（Ashmand 译本）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户拿着一次具体的日月食，问“意味着什么、影响哪些地方”
- 用户问某次食相的影响“多久、什么时候开始、什么时候最强”
- 用户问“这次事件落在人、牲畜、作物还是别的哪一类上”
- 用户问“这次是偏吉还是偏凶，由哪颗行星主导”
- 用户问食相的颜色、或彗星等天象怎么读

**不应触发**：
- 用户问的是一片地区的常态性格 → 走 `ptolemy-region-familiarity`
- 用户问的是年／季／月的天气与大气状况 → 走 `ptolemy-annual-atmosphere`
- 用户只是想先定大势与个人谁优先 → 走 `ptolemy-general-particular-scope`
- 用户要某个人的本命盘 → 走个人命盘类方法
- 用户要的是某场具体灾难／某地某日会出什么事的预告 → 本 skill 明令不作此类预言

## R：原文锚点

> "The strongest and principal cause of all these events exists in the ecliptical conjunctions of the Sun and Moon, and in the several transits made by the planets during those conjunctions."（BOOK THE SECOND, CH. V）（已据公版原文核）

> "the locality of the event, and points out the cities or countries liable to be influenced by particular eclipses"（BOOK THE SECOND, CH. V）（已据公版原文核）

> "Another branch relates to time, and gives pre-information of the period at which the event will occur"（BOOK THE SECOND, CH. V）（已据公版原文核）

> "The third branch is generic; and points out the classes, or kinds, which the event will affect."（BOOK THE SECOND, CH. V）（已据公版原文核）

> "The last part is specific; and foreshows the actual quality and character of the coming event."（BOOK THE SECOND, CH. V）（已据公版原文核）

> "Whatever countries or cities shall be thus found in familiarity with the ecliptical place, will all be comprehended in the event"（BOOK THE SECOND, CH. VI）（已据公版原文核）

> "the effect will endure as many years as the obscuration lasted hours, provided the eclipse was solar; but if lunar, a like number of months is to be reckoned instead of years."（BOOK THE SECOND, CH. VII）（已据公版原文核）

> "should the zodiacal constellations, and those of the ruling fixed stars out of the zodiac, be of human shape, the effect will fall upon the human race."（BOOK THE SECOND, CH. VIII）（已据公版原文核）

> "those bearing the figure of ferocious beasts denote that the event will affect savage and destructive animals"（BOOK THE SECOND, CH. VIII）（已据公版原文核）

> "when Saturn may be sole governor, he will produce disasters concomitant with cold."（BOOK THE SECOND, CH. IX）（已据公版原文核）

> "Jupiter, if he should be lord alone, will thoroughly improve and benefit all things."（BOOK THE SECOND, CH. IX）（已据公版原文核）

> "Mars, when governing alone, generally causes such mischief and destruction as are concomitant with dryness."（BOOK THE SECOND, CH. IX）（已据公版原文核）

> "if these colours or hues should be black, or greenish, they portend effects similar to those produced by Saturn's nature; if white, to those operated by Jupiter; if reddish, to those by Mars; if yellow, to those by Venus; and if of various colours, to those by Mercury."（BOOK THE SECOND, CH. X）（已据公版原文核）

> "operate effects like those of Mars and Mercury; exciting wars, heated and turbulent dispositions in the atmosphere"（BOOK THE SECOND, CH. X）（已据公版原文核）

## I：核心解释

1. **主因是食相**：全体性事件最强、最主要的原因，存在于日月合朔的食相，以及食相期间行星的过运（transits）中。这是整条线的入口。（R1）
2. **四支框架**：一次通用事件的判读，分四支——地域（哪些城市、国家受影响）、时间（何时起、持续多久）、种类（落在哪一类人／物上）、性质（好还是坏、什么性质）。四支共用同一张盘，必须一起读。（R2–R5）
3. **地域怎么定**：看食相发生在黄道的哪一处，再按先前的地域亲缘规则（象限与三方星座）找出与该处亲缘的国家；城市层面看建城时的上升点与日月位置，或当政者在食相当时的天顶。凡如此找到的国家与城市，都会卷入该事件；其中与食相所在宫最相应、且食相在其上空可见的地方，影响最重。（R6）
4. **时间怎么算**：先按食相发生时刻与该地纬度，像排本命盘一样排角。记下食分持续的赤道小时数——日食：多少小时＝多少年；月食：多少小时＝多少月。起效早晚与最强期看食相点相对角：近东地平→头四个月内起效、最强在全程前三分之一；近天顶→第二四个月起效、中三分之一；近西地平→第三四个月起效、末三分之一。（R7）
5. **强弱如何增损**：行星晨见或留驻→增强增大；夕见、在日光下、或半夜上中天→减弱减小；中间时段的合朔与过运会造成局部的松紧。
6. **种类怎么定**：由食宫与主星所在星座的“形”推断——人形星座→落在人类；陆兽／四足形→相应走兽；蛇形→蛇类；猛兽形→猛恶动物；驯兽形→家畜；北方陆象→地震，南方陆象→暴雨；翼形（如天鹰）→鸟类（尤供人食者）；游水形（如海豚）→海兽与船队；河鱼形（宝瓶、双鱼）→河与淡水动物；南船座→海与河都受影响。再叠加季节（春～藤蔓花果、夏～收成与尼罗河、秋～谷物草药、冬～蔬食与候鸟候鱼）以及角的位置（东→果实、萌芽、少年；天顶→宗教、君王、中年；西→法律、老年、将死者）。（R8、R9）
7. **性质怎么定**：由主星的力量与相互的“调和”（contemperament）决定。土星独主→与寒同来的祸患（久病、痨、风湿、水病、四日热，以及流放、贫困、 grief 与惊恐，死者多在年长者）；木星独主→一切向好（荣誉、幸福、和平、丰收、君主恩泽）；火星独主→与燥同来的祸患（外战内乱、俘杀、暴动、猝死，热病与出血，火灾旱灾）；金星独主→类木星而更柔和（荣华、婚姻、多子、航行顺遂）；水星常随伴并增其力，兼主贸易技艺、宗教、政事、风俗法律，并生多风的天气与雷鸣地动。（R10–R12）
8. **颜色与彗星**：食相颜色黑或青绿→土星性；白→木星性；红→火星性；黄→金星性；杂色→水星性。彗星（梁状、喇叭状、管状等）性质似火星与水星，主战乱与大气中的燥热扰攘。（R13、R14）
9. **谁最受**：本命盘日月或角点与食相当时的配置相同（或正相反）的人，尤以能看见该食相者为甚。

## A1：来源应用 — 书上给的具体做法

- **先取食相**：找到日／月食发生的确切时刻与黄道位置；行星在食相时的过运一并记下。（R1）
- **排四支**：按 R2–R5 依次给出地域、时间、种类、性质，别只答一支。
- **定地域**：按象限／三方星座找亲缘国；城市层面用建城上升点或当政者天顶。（R6）
- **算时间**：食分小时数→日食×年、月食×月；按食相点相对东／中／西的角定起效期与最强期。（R7）
- **定主星**：找对食黄道位置与“食相之后那个角”都有最多主张的行星；若食之主与角之主不是同一颗，两颗都记、以食之主为首，另一颗“同掌”。恒星则以最亮、且在食相时与角有九种相位关系者为要。
- **读种类**：按星座形状读落在人／兽／鱼／鸟／作物哪一类；再看季节与角。（R8、R9）
- **读性质**：按主星的单独性质与混合判吉凶倾向。（R10–R12）
- **看颜色与彗星**：颜色按五色配五星；彗星另作一段。（R13、R14）
- ⚠️ **（补充）** 书里给的全是“倾向”话（如“将会有”“多会”），不是对具体事件的预告。应用时必须保留这层语气，不得改写成“某年某日某地必发生某事”。

## A2：典型触发场景

1. 用户拿着某次日食／月食的时间和落点，问“这意味着什么”
2. 用户问“这次影响持续多久、什么时候开始”
3. 用户问“这次事件会落在人身上，还是牲畜／作物上”
4. 用户问“这次是吉是凶、由哪颗行星主导”
5. 用户问“食相颜色／最近出现的彗星要怎么读”

## E：执行步骤

### 步骤1：锁定食相与相关地区

**输入**：食相时刻、类型（日／月）、黄道落点、相关地区。
**输出**：一张“食相盘”的基本参数 + 候选亲缘国家／城市列表。

🔴 **CHECKPOINT — 触发条件：给不出食相时刻或地点**：先追问；给不出就不推，明确说“前提不足（需大致时空信息）”。

### 步骤2：定地域（第一支）

**输入**：步骤1 的食相黄道位置。
**输出**：卷入该事件的国家／城市，并标出哪一处最相应。

🔴 **CHECKPOINT — 触发条件：用户想据此点名某个具体城市“要出事”**：改述为“按书里的亲缘规则，与该处相应的地方是……”，不作具体预告。

### 步骤3：算时间（第二支）

**输入**：食分持续的赤道小时数 + 食相点相对角的位置。
**输出**：起效期、持续期、最强期。

🔴 **CHECKPOINT — 触发条件：用户把“年数＝小时数”当成精确预言**：标明这是书里的象征换算，只作倾向性的量级参考。

### 步骤4：定种类（第三支）

**输入**：食宫与主星所在星座的形状、季节、角。
**输出**：落在人／陆兽／蛇／猛兽／家畜／鸟／海兽／河鱼／作物哪一类。

🔴 **CHECKPOINT — 触发条件：用户想把它指向某群具体的人**：只给“类别层级”，不点具体人群；避免指向任何现实群体。

### 步骤5：定性质（第四支）

**输入**：掌握食黄道位置与“其后之角”的主星及其混合。
**输出**：一个“偏吉／偏凶 + 由哪颗行星主导 + 什么性质”的倾向。

🔴 **CHECKPOINT — 触发条件：牵出战争、瘟疫、饥荒、死亡等灾难性内容**：明说“这是象征层的倾向性推演，不是对具体事件的预告，也不引起恐慌”；按 B 节安全兜底处理。

### 步骤6：补颜色与彗星，并收束

**输入**：食相颜色／彗星信息。
**输出**：颜色配行星的一笔、彗星按火星·水星性质的一笔 + 总收束。

🔴 **CHECKPOINT — 触发条件：用户要求“给个准话，会不会出事”**：拒绝做确定性预言，回到四支的倾向性表述。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 只答一支 | 只说了吉凶，没给地域／时间／种类 | 🛑 回到四支框架，把缺的三支补齐 |
| 把倾向写成预言 | “某年某地必然发生灾难” | 🛑 保留书里的“倾向／多会”语气，去掉“必然／注定” |
| 缺时空锚点硬算 | 没时刻没地点就给结论 | 🛑 回到步骤1 的 CHECKPOINT，先要大致时空信息 |
| 精确化年数 | 把“小时＝年”当成准数 | 🛑 说明这是象征换算，只作量级参考 |
| 指向现实人群 | 把“种类”落到某个真实的族群体 | 🛑 只给类别层级，不点具体人群 |
| 引发恐慌 | 用战争／瘟疫／死亡渲染 | 🛑 走安全兜底：明说不作预言、不引起恐慌 |
| 越界到地区常态 | 用本 skill 给一片地区定性格 | 🛑 转 `ptolemy-region-familiarity` |

### 边界规则

1. **四支一起给**：地域、时间、种类、性质是一次事件的四个面，缺一不可（R2–R5）。
2. **必须写明前提**：至少要有食相的大致时刻、类型与相关地区；缺则退回追问。
3. **只作倾向**：全程用“倾向／较可能／多会”的措辞，不作确定性预言。
4. **不瞄准现实群体**：“种类”只到类别层级（人类、家畜、作物……），不指向任何具体人群或组织。
5. **与相邻 skill 分工**：层次取舍 → `ptolemy-general-particular-scope`；地区常态 → `ptolemy-region-familiarity`；时令气候 → `ptolemy-annual-atmosphere`；个人命盘 → 个人命盘类方法。
6. **安全兜底**：涉及天灾、灾异、战争、瘟疫等群体性内容时，只作倾向性推演，**不作预言、不引起恐慌**。不借此对任何现实地点、国家或人群发出警报。涉及就医、心理危机时只做提醒与陪伴，指向专业资源，不做诊断。

### 用户自查清单

- [ ] 我给全了四支（地域、时间、种类、性质）
- [ ] 我能说清食相的大致时刻、类型与相关地区（前提齐备）
- [ ] 我的措辞是“倾向／较可能”，没有“必然／注定”
- [ ] 我把“种类”只说到了类别层级，没指向现实人群
- [ ] 我加了“不作预言、不引起恐慌”的边界句

**勾选 4+ 项**：判读到位。**≤ 2 项**：多半是缺支或写成了预言，回到对应步骤。

## 📖 练习手册

**四支拆解**：拿一次公开的日食参数，分别写出地域、时间、种类、性质四支各一句。

**用词练习**：把你写的四支里所有“必然／一定”改成“倾向／较可能”，感受语气的差别。

**颜色配星**：默写五色配五星（黑青绿→土、白→木、红→火、黄→金、杂→水）。

## 🚫 反例与黑名单

1. **把倾向写成灾难预告** → 🛑 违背 R1 的自然理性之界，也违背“不作预言、不引起恐慌”。
2. **只答吉凶、不给其余三支** → 🛑 违背四支框架。
3. **把“种类”指向现实族群** → 🛑 只到类别层级。
4. **没有时空信息也照算** → 🛑 前提不足，先追问。
5. **用小时数下精确年限断言** → 🛑 只作象征量级参考。

### 灰色地带（需谨慎判断）

1. **食相可见与不可见**：书里主张与食相黄道位置亲缘的所有国家都卷入事件，但影响**主要**落在能看见食相的地方。遇到“看不见也算不算”时，按这条分主次（补充）。
2. **多颗行星争夺主导**：若无法选出一颗独主，可记两颗（以食之主为首、另一颗同掌），并说明混合性质，不必硬断一颗。
3. **用户拿现实灾难来印证**：这是回溯性附会。明确说明象征层不做“事后点名”，只谈倾向，不承认对具体事件的预告能力。
