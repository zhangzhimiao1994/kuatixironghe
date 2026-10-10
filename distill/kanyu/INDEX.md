# 堪舆择日（kanyu）· 技能索引

> 维度：**堪舆择日**（象征层，注册表顺序 16）｜前缀 `kanyu-*`｜入口 `kanyu-hub`｜共 35 个 skill。
> 来源（引文只从这里抄）：`sources/zangshu.txt`（葬書）、`sources/hanlongjing.txt`（撼龍經/疑龍經/葬法倒杖，四庫本）、`sources/yilongjing.txt`（疑龍經，維基文庫本，互校用）、`sources/xieji.txt`（欽定協紀辨方書，三十六卷）。
> 本维度管两件事：**相地**（读一处地、一座宅的形势）与**择日**（读一个日子宜不宜做某件事）。口径见 `kanyu-hub` 的 I/E/B 节。

## 零、入口

| slug | 一句话功能 |
|---|---|
| `kanyu-hub` | 总览与分诊：认出用户问的是相地还是择日、缺什么信息，并路由到下面 34 个子 skill。 |

## 一、相地 · 葬書（9）

| slug | 一句话功能 |
|---|---|
| `kanyu-zangshu-cheng-shengqi` | 葬者乘生气：相地的第一原理（内篇一）。 |
| `kanyu-zangshu-cang-feng-de-shui` | 藏风得水：什么叫「风水」、得水为何为上（内篇二）。 |
| `kanyu-zangshu-zhi-long-bian` | 支垄之辨：平洋与山垄两套体认方式（内篇二～四）。 |
| `kanyu-zangshu-shi-lai-xing-zhi` | 势来形止：千尺为势、百尺为形与全气之地（内篇三）。 |
| `kanyu-zangshu-xing-shi-pin-lei` | 形势品类：势与形的吉凶读法（雜篇）。 |
| `kanyu-zangshu-shen-fei-ze-xiang` | 审其所废、择其所相、避其所害：在废坏之地里辨真伪。 |
| `kanyu-zangshu-zhi-e-long-lu` | 支葬其额、垄葬其麓：支垄各自的下葬位置（外篇）。 |
| `kanyu-zangshu-ze-te` | 择其特：众山之中取哪一个（外篇）。 |
| `kanyu-zangshu-si-fa` | 乘金相水、穴土印木：书上选穴四法（外篇）。 |

## 二、相地 · 楊筠松（10）

| slug | 一句话功能 |
|---|---|
| `kanyu-hanlong-gan-zhi-long` | 干龙枝龙：天下大势怎么分（撼龍經）。 |
| `kanyu-hanlong-jiu-xing` | 九星辨形：贪巨禄文廉武破辅弼与星峰吉凶（撼龍經）。 |
| `kanyu-yilong-shang` | 疑龙经·上篇：干上寻龙、关局水口为主。 |
| `kanyu-yilong-zhong` | 疑龙经·中篇：枝中干、州县都会怎么落。 |
| `kanyu-yilong-xia` | 疑龙经·下篇：真龙落穴与虚穴假穴之辨。 |
| `kanyu-yilong-shi-wen` | 疑龙十问：抱养、公位、阳宅阴宅、真假形等十疑。 |
| `kanyu-wei-long-pian` | 卫龙篇：贴身护卫正龙的山水怎么认。 |
| `kanyu-bian-xing-pian` | 变星篇：一星一星剥换变去的追法。 |
| `kanyu-dao-zhang-shi-er-fa` | 倒杖十二法：认太极、分两仪到倚盖撞黏（葬法倒杖）。 |
| `kanyu-er-shi-si-sha-zang-fa` | 二十四砂葬法：临穴分寸毫釐的穴形辨。 |

## 三、择日 · 協紀辨方書（15）

| slug | 一句话功能 |
|---|---|
| `kanyu-xieji-ben-yuan` | 本原：河洛八卦、二十四方位与诸家五行（卷一卷二）。 |
| `kanyu-xieji-yi-li-nian-shen` | 义例·年神：太岁、岁破、大将军一类年神起例（卷三）。 |
| `kanyu-xieji-jian-chu` | 义例·建除十二神：建除满平定执破危成收开闭（卷四）。 |
| `kanyu-xieji-yue-shen` | 义例·月神：天道、天德、月德一类按月起例（卷五）。 |
| `kanyu-xieji-ri-shen` | 义例·日神：三合、临日、驿马、劫煞一类按日起例（卷六）。 |
| `kanyu-xieji-huang-dao-gui-ren` | 义例·黄道黑道与诸贵人：十二神与天乙、喜神等（卷七）。 |
| `kanyu-xieji-lu-ma` | 义例·岁禄、飞天禄马、飞宫贵人（卷八）。 |
| `kanyu-xieji-li-cheng` | 立成：把各类起例汇列成表、查表的办法（卷九）。 |
| `kanyu-xieji-yi-ji` | 宜忌：神煞轻重相胜、趋避取舍（卷十）。 |
| `kanyu-xieji-yong-shi` | 用事：御用六十七事、民用三十七事、选择六十事（卷十一）。 |
| `kanyu-xieji-gong-gui` | 公规：祀典、春牛经、气候、更漏中星（卷十二～十三）。 |
| `kanyu-xieji-li-yong-zao-ming` | 利用·选择要论与杨筠松造命歌（卷三十三）。 |
| `kanyu-xieji-zhi-sha` | 利用·制煞要法：遇煞怎么制、怎么变通（卷三十四）。 |
| `kanyu-xieji-fu-lu` | 附录：世俗相沿的择日条目（卷三十五）。 |
| `kanyu-xieji-bian-e` | 辨讹：辨世俗术家之讹（卷三十六）。 |

## 四、关系

关系标签沿用 zhengliu 约定：`depends-on`（要先有它才好用它）／`contrasts-with`（容易混、要分清）／`composes-with`（常一起用）。

### 入口 → 分组（depends-on）

- `kanyu-hub` **depends-on →** 三组全体：先分诊再分派；子 skill 之间不互相路由。
- 相地两组 **depends-on →** `kanyu-zangshu-cheng-shengqi`：形势之象的读法都以「乘生气」为总纲，其余九个葬書 skill、以及撼龍/疑龍诸篇都建立在这一原理上。
- 择日一组里，`kanyu-xieji-li-cheng` **depends-on →** 卷三～卷八各「义例」子 skill（`kanyu-xieji-yi-li-nian-shen`、`kanyu-xieji-jian-chu`、`kanyu-xieji-yue-shen`、`kanyu-xieji-ri-shen`、`kanyu-xieji-huang-dao-gui-ren`、`kanyu-xieji-lu-ma`）：先有起例，才有表可查。
- `kanyu-xieji-yong-shi` **depends-on →** `kanyu-xieji-li-cheng` 与 `kanyu-xieji-yi-ji`：按事查宜忌，要先能查表、又要会取舍。

### 容易混的成对区分（contrasts-with）

- `kanyu-zangshu-cheng-shengqi` **contrasts-with** `kanyu-zangshu-cang-feng-de-shui`：前者是总原理（为什么要乘生气），后者是取用条件（什么形势才存得住生气）。问「为什么」落前者，问「怎么看风水」落后者。
- `kanyu-zangshu-shi-lai-xing-zhi` **contrasts-with** `kanyu-zangshu-xing-shi-pin-lei`：前者讲「势」「形」的尺度与止处（千尺百尺、势来形止），后者讲形势品类的吉凶读法。一个定尺度，一个分品类。
- `kanyu-zangshu-zhi-long-bian` **contrasts-with** `kanyu-zangshu-zhi-e-long-lu`：前者是支垄两套体认的分辨，后者是分出支垄之后各自葬法的落点。
- `kanyu-hanlong-jiu-xing` **contrasts-with** `kanyu-bian-xing-pian`：前者静看九星各形与吉凶，后者看龙行一路剥换、一星变一星的动态追法。
- `kanyu-yilong-shang/zhong/xia`（`kanyu-yilong-shang`、`kanyu-yilong-zhong`、`kanyu-yilong-xia`）互 **contrasts-with**：上篇干上寻龙（关局水口），中篇枝中干与州县都会，下篇落穴真假与虚穴。按用户问的是「主干」「都会」还是「到底是不是穴」来分。
- `kanyu-xieji-yi-li-nian-shen` **contrasts-with** `kanyu-xieji-yue-shen` **contrasts-with** `kanyu-xieji-ri-shen`：同是起例，起例的周期不同（年/月/日）。问「一年一换」落年神，问「按月」落月神，问「按干支日」落日神。
- `kanyu-xieji-li-cheng` **contrasts-with** `kanyu-xieji-yi-ji`：前者是「照起例查表」（得到有哪些神煞），后者是「轻重相胜、趋避取舍」（得到该听哪个）。查得到不等于判得出。
- `kanyu-xieji-li-yong-zao-ming` **contrasts-with** `kanyu-xieji-zhi-sha`：前者是选择要论与造命歌（怎么定体用、补龙扶山），后者专讲遇煞怎么制、怎么变通。
- `kanyu-xieji-yong-shi` **contrasts-with** `kanyu-xieji-yi-ji`：一个以「事」为纲（做什么事宜忌什么），一个以「神」为纲（神煞轻重如何取舍）。用户按事来问落前者，按神煞来问落后者。
- `kanyu-xieji-fu-lu` **contrasts-with** `kanyu-xieji-bian-e`：前者照录世俗相沿的条目（如洗头日、嫁娶周堂），后者专辨世俗术家之讹。一个收录、一个纠错。
- `kanyu-xieji-ben-yuan` **contrasts-with** 各义例子 skill：前者是原理地基（河洛八卦、方位五行），后者是原理之上的一道道起例。

### 常一起用（composes-with）

- `kanyu-zangshu-cheng-shengqi` **composes-with** `kanyu-zangshu-shi-lai-xing-zhi`：总纲 + 尺度，是读一处形势的最小组合。
- `kanyu-zangshu-cang-feng-de-shui` **composes-with** `kanyu-zangshu-zhi-long-bian`：支垄取用不同，藏风得水的判法也随之不同。
- `kanyu-hanlong-gan-zhi-long` **composes-with** `kanyu-hanlong-jiu-xing`：先分干枝大势，再辨星峰。
- `kanyu-yilong-xia` **composes-with** `kanyu-dao-zhang-shi-er-fa`：判出真龙落穴后，再谈倚盖撞黏的落穴做法。
- `kanyu-hanlong-jiu-xing` **composes-with** `kanyu-yilong-xia`：九星辨形为疑龙的真假落穴提供星峰依据。
- `kanyu-xieji-ben-yuan` **composes-with** 各义例子 skill：原理与起例配套读。
- `kanyu-xieji-li-cheng` **composes-with** `kanyu-xieji-yong-shi`：查表得到神煞，再按用事定宜忌。
- `kanyu-xieji-yi-ji` **composes-with** `kanyu-xieji-zhi-sha`：取舍与制煞常连用（宜从则从，不宜则制）。
- `kanyu-xieji-bian-e` **composes-with** `kanyu-xieji-fu-lu`：附录里世俗条目的来历，多由辨讹一节来分辨。
- 相地与择日两支整体 **composes-with**：遇到「先找地、再挑日子」的问题，按「先形势、后日子」组合，由 `kanyu-hub` 分别分派。

## 五、计数

- 相地·葬書 9 + 相地·楊筠松 10 + 择日·協紀辨方書 15 + 入口 1 = **35**。
- 数量由原书结构定（葬書三篇＋撼龍經/疑龍經/葬法倒杖；協紀辨方書三十六卷），不预设、不为凑数硬拆。
