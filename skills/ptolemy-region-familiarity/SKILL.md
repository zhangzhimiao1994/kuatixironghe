---
name: ptolemy-region-familiarity
description: 地域与民族的星象亲缘。当用户问“这个地方的人什么气质”“某个国家或民族的文化性格”“按气候带和星座给一个地区定调”时使用。用气候平行圈（南／北／温带）、四组三方星座与四大象限、行星与恒星亲缘，给一个地区做倾向性画像。这是象征层的地区描述，不是对真实人群的事实断言。
input_schema:
  required: [region_name, climate_band]
  optional: [quadrant, founding_date, ruler_birth]
output_schema:
  primary: {climate_temperament: string, triplicity_reading: string, region_character: string}
  secondary: [fixed_star_link, metropolis_link, caveat]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 地域亲缘：给一个地区做倾向性画像

**来源**：《Tetrabiblos》BOOK THE SECOND, CH. II（PECULIARITIES OBSERVABLE THROUGHOUT EVERY ENTIRE CLIMATE）、CH. III（THE FAMILIARITY OF THE REGIONS OF THE EARTH WITH THE TRIPLICITIES AND THE PLANETS）、CH. IV（THE FAMILIARITY OF THE REGIONS OF THE EARTH WITH THE FIXED STARS）（Ashmand 译本）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户问“某地／某国的人大概是什么气质、什么文化性格”
- 用户想按气候带（南方／北方／温带）给一个地区定调
- 用户要按四方象限与三方星座，把某片国土对应到某一个象限
- 用户手里有一个城市的建城日期，想找它与黄道哪一处相应
- 用户问“这个民族是不是天生就如何如何”

**不应触发**：
- 用户问的是某个具体个人的性格 → 走个人命盘类方法，不是地区画像
- 用户问的是日月食／彗星落在一片区域意味着什么 → 走 `ptolemy-general-event-eclipse`
- 用户问的是某个地区年／季的天气收成 → 走 `ptolemy-annual-atmosphere`
- 用户只是想知道该层次先看大势还是先看个人 → 走 `ptolemy-general-particular-scope`
- 用户想要真实的人口学／民族学结论 → 不是本 skill；这是象征素材，不是事实调查

## R：原文锚点

> "The peculiarities of all nations are distinguished according to entire parallels and entire angles, and by their situation with regard to the Sun and the Ecliptic."（BOOK THE SECOND, CH. II）（已据公版原文核）

> "The climate which we inhabit is situated in one of the Northern Quadrants"（BOOK THE SECOND, CH. II）（已据公版原文核）

> "the natives of those countries which lie towards the east excel in courage"（BOOK THE SECOND, CH. II）（已据公版原文核）

> "the inhabitants of the west are milder, more effeminate and reserved."（BOOK THE SECOND, CH. II）（已据公版原文核）

> "in each particular climate, certain peculiar qualities are to be found, arising from the natural familiarity which it holds with the stars and the twelve signs."（BOOK THE SECOND, CH. II）（已据公版原文核）

> "although these qualities do not pervade it, in such a manner as to be necessarily exhibited by every individual native, yet they are so far generally distributed as to be of much utility in investigating particular events"（BOOK THE SECOND, CH. II）（已据公版原文核）

> "there are four triplicities distinguishable in the zodiac"（BOOK THE SECOND, CH. III）（已据公版原文核）

> "The whole inhabited earth is accordingly divided into four parts, agreeing with the number of the triplicities."（BOOK THE SECOND, CH. III）（已据公版原文核）

> "each quadrant is in familiarity with two oppositely-placed triplicities"（BOOK THE SECOND, CH. III）（已据公版原文核）

> "all fixed stars which may be posited on any line, drawn from one zodiacal pole to the other, through such parts of the zodiac as may be connected with any particular country, are also in familiarity with that particular country."（BOOK THE SECOND, CH. IV）（已据公版原文核）

> "those points or degrees of the zodiac, over which the Sun and Moon were in transit, at the time when the construction of any such city was first undertaken and commenced, are to be considered as sympathizing with that city in an especial manner"（BOOK THE SECOND, CH. IV）（已据公版原文核）

> "the mid-heaven in the nativity of the reigning king, or other actual chief magistrate, is to be substituted"（BOOK THE SECOND, CH. IV）（已据公版原文核）

## I：核心解释

1. **地区性格由气候位置定，不由血统定**：全民族的特性，是按“整个平行圈与整个角（parallels and angles）”，以及相对太阳与黄道的位置来区分的。换句话说，先看这个地区在北半球哪一带。（R1、R2）
2. **南北三分**：赤道到北回归线之间的地带，太阳直射，被描述为肤黑卷发、身材矮小、性急彪悍（书里名之曰埃塞俄比亚人）；北极圈及以北，太阳热力远，体质寒湿、肤色白皙直发、身材高大、性冷而野（斯基泰人）；北回归线与北极圈之间，温度适中、寒暑交替但不剧烈，于是体态匀称、性情良好、聚居于社会、有文明习惯。（R2）
3. **东西二分**：东方属太阳（东方、日间、阳性、右），故东方人勇敢、行事公开磊落（书里也点明动物的右侧普遍更强）；月亮合朔后总在西方出现，故西方属月亮（阴性、左），于是西方人更温和、阴柔、内敛。（R3、R4）
4. **气候给的只是“一般倾向”**：每个地区都带有与某星座的亲缘，因而有某些特质；但这些特质**不必然**在每个当地人身上显现，只是大体分布，用来辅助调查特定事件。这是全书反对命定论最直白的一句。（R5、R6）
5. **四组三方星座→四大象限**：黄道有四个三方星座（三角），书里把它们配到地球的四个象限。第一组白羊·狮子·人马＝西北，木星为主（因），火星同掌（西）；第二组金牛·处女·摩羯＝东南，金星为主（南），土星同掌（东）；第三组双子·天秤·宝瓶＝东北，土星为主（东），木星同掌（北）；第四组巨蟹·天蝎·双鱼＝西南，火星为主（西），金星同掌（南）。（R7、R8）
6. **双向亲缘**：整个象限归一组三方星座，但靠近“地球中央”的那部分，方向与整个象限相反，于是又与对面那组三方星座亲缘；这些中央地带还加进水星（因其“思虑的、共通的本性”）。（R9）
7. **恒星亲缘**：凡与某国相关的黄道部位，沿同一条“黄道极线”（from one zodiacal pole to the other）排布的恒星，也与该国亲缘——书里用这个办法把黄道以外的恒星分派给地区。（R10）
8. **城市级锚点**：对都会城市，看建城时日月经过的黄道度数，那处与城市特别同情，其中上升点（ascendant）最相应；若查不到建城日期，就以当政君主／长官命盘的天顶（mid-heaven）替代。（R11、R12）
9. **书里给了整张地区表**：正文逐一列举各国，并直接给出性格断语（如与白羊·火星亲缘者有“更野、更大胆、更凶悍”，与狮子·太阳亲缘者“更专横却仁慈、关心公共事务”，与宝瓶·土星亲缘者“更不精致、更严峻粗拙”）。表格见 CH. III 结尾的 TABLE SHOWING ALL THE COUNTRIES BELONGING TO EACH SIGN RESPECTIVELY。（补充：对 CH. III 正文与表格的归纳）

## A1：来源应用 — 书上给的具体做法

- **先定气候带**：判断该地在南（赤道—北回归线）、北（北极圈及以北）、还是中间温带，照 R2 读性情（黑肤性急／白肤冷野／匀称文明）。
- **再过东西轴**：东方（太阳性）→勇敢磊落；西方（月亮性）→温和阴柔内敛。（R3、R4）
- **套四方象限**：按 R7、R8 的四组三方星座，把国土落到某一个象限，取其主星与同掌星的性质；靠近中央的地区再叠加对面三方星座与水星。（R9）
- **查恒星**：沿黄道极线找该地区对应的黄道部位，取同线上的恒星，并把它们也纳入。（R10）
- **查城市锚点**：有建城日期就用建城盘日月度数（尤其上升点）；没有就用当政者的天顶。（R11、R12）
- **照表读断语**：书里为每片国土直接给了性格词（参见 CH. III 的表格与其正文断语）。
- ⚠️ **必须并读的一条**：书里明说这些特质“不必然在每个个体身上显现”（R6）。**（补充）** 书里 CH. II–III 对各族群的具体描写（肤色、习俗、甚至“吃人”“无神”等）是公元二世纪的民族志与地志成见，只可作为象征层的素材，**不得当作对真实人群的事实断言，更不得用于贬低任何民族或地域**。

## A2：典型触发场景

1. 用户拿着一份关于某国家／地区的材料，问“这地方的人大体是什么调性”
2. 用户想把一个古代城市对应到黄道的某一处（给了建城年代或君主生年）
3. 用户问“为什么书里说东方人勇敢、西方人内敛，这是什么机制”
4. 用户把“某个民族天生成什么样”当成事实来问
5. 用户在拼一份跨体系分析，需要给一个地区填一笔象征层的画像

## E：执行步骤

### 步骤1：定气候带

**输入**：地区名 + 大致纬度／气候带。
**输出**：一句气候性情判定（偏南／偏北／温带）。

🔴 **CHECKPOINT — 触发条件：用户给不出地区或纬度**：先追问；给不出就只做“宽泛气候带”的粗略倾向，并说明前提不足。

### 步骤2：叠加东西轴

**输入**：步骤1 的地区。
**输出**：东方（勇敢磊落）或西方（温和阴柔）的一笔。

🔴 **CHECKPOINT — 触发条件：用户把东西描述当成对真实民族的评价**：立刻标注“这是书里的象征分类，不是事实”，并说明这是象征层用法。

### 步骤3：套四方象限与三方星座

**输入**：地区的四方归属。
**输出**：该象限的两组三方星座、主星与同掌星，及其性质词；近中央者加对面三方星座与水星。

🔴 **CHECKPOINT — 触发条件：地区跨在象限边界、两套说法都能套**：按书里“愈接近地球中央者、与对面三方星座亲缘”的规则分主次，把两套都写出并标出主从（补充）。

### 步骤4：补恒星与城市锚点

**输入**：可选——相关恒星信息、建城日期或当政者生年。
**输出**：恒星亲缘一笔；有城市数据时补上升点／天顶锚点。

🔴 **CHECKPOINT — 触发条件：只有含糊的“某古城”而没有任何日期**：不虚构锚点，说明“无建城信息时不做城市级判断”。

### 步骤5：收束为倾向性画像并加安全边界

**输入**：前面各步。
**输出**：一段“该地区在象征层的倾向”画像 + caveat。

🔴 **CHECKPOINT — 触发条件：用户要把它当成对当地人的真实判断，或用来歧视某群体**：停用该结论，改述为“象征层素材”，并引 R6 说明“不必然在每个个体身上显现”。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 把象征画像当事实 | 用“某地的人天生如何”下判断 | 🛑 引 R6：只做倾向，不必然；这是象征层，不是人口学 |
| 用古代成见贬低族群 | 复述书里“吃人”“无神”“野蛮”等断语当作真 | 🛑 标注这是公元二世纪的民族志成见，禁止用于歧视 |
| 缺地区／纬度硬推 | 只有一句“看看这个地方” | 🛑 回到步骤1 的 CHECKPOINT，先问清地区与纬度 |
| 象限边界含糊不清 | 两套说法混着给、不分主从 | 🛑 按“近中央叠加对面三方星座”的规则分主次 |
| 虚构城市锚点 | 无日期也给上升点／天顶 | 🛑 无建城信息就不做城市级判断 |
| 越界去做天象事件 | 用本 skill 判日月食吉凶 | 🛑 转 `ptolemy-general-event-eclipse` |

### 边界规则

1. **本 skill 只做“地区的倾向性画像”**，不判具体事件、不判具体人。
2. **必须写明前提**：至少要有地区名与大致气候带；城市级判断须有建城日期或当政者生年。
3. **一切皆为倾向**：书里自己就强调这些特质不必然在个体身上出现（R6），不得写成命定论。
4. **反歧视硬线**：书里的民族／族裔断语是古代材料，只能作象征素材，不得用于支持对真实群体的贬低或刻板印象。
5. **与相邻 skill 分工**：层次取舍 → `ptolemy-general-particular-scope`；天象事件 → `ptolemy-general-event-eclipse`；时令气候 → `ptolemy-annual-atmosphere`。
6. **安全兜底**：本层是象征层推演，不替代事实研究或专业判断。涉及就医、心理危机时只做提醒与陪伴，不做诊断；涉及群体、民族、地域议题时，只作倾向性描述，不作断言、不制造对立。

### 用户自查清单

- [ ] 我能说出这个地区大致落在哪个气候带
- [ ] 我过了东西轴（东方／西方），并说明它只是象征分类
- [ ] 我把地区落到了某一组三方星座，并说明了主星与同掌星
- [ ] 我没有把书里的民族断语当成对真实人群的事实
- [ ] 我给的每一句都是“倾向”，没有用“注定／必然”

**勾选 4+ 项**：画像到位。**≤ 2 项**：多半是把象征当事实，或漏了气候带前提，回到对应步骤。

## 📖 练习手册

**气候带速记**：在地图上挑三个纬度不同的地区，各写一句“偏南／偏北／温带”的性情倾向。

**象限归类**：把书里 CH. III 的四方象限表抄一遍，随便点一个国家说出它归属的象限与两组三方星座。

**边界重写**：挑一句书里最刺眼的族群断语，把它改写成“象征层的倾向表述”，并加一句“不必然在每个个体身上显现”。

## 🚫 反例与黑名单

1. **把象征画像当事实说出** → 🛑 违背 R6，书里自己就说是倾向。
2. **拿古代民族志断语贬低真实族群** → 🛑 反歧视硬线，禁止。
3. **无纬度、无地区也给结论** → 🛑 前提不足，先追问。
4. **用本 skill 判天象事件** → 🛑 转 `ptolemy-general-event-eclipse`。
5. **把地区画像直接安到某个具体人头上** → 🛑 群体倾向 ≠ 个人。

### 灰色地带（需谨慎判断）

1. **地区跨气候带或跨象限**：书里承认同一气候内还有局部差异（临海成航海者、平原成骑手、土壤肥沃定居）。遇到跨界，写两套倾向并标主从，别硬选一个。
2. **现代国家与古代地名的对应**：书里的地名多已消失或改名，对应关系不确定。只做“大致方位／气候带”的落位，别硬套现代国界（补充）。
3. **用户执着于“我们这个地方的人到底怎么样”**：把话题从“事实断定”转到“象征素材怎么看”，并始终带上 R6 的限定。
