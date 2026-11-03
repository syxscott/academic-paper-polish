# 全文逐字精读实证（v2.15.0 新增）

> **本文件的每一条结论都来自「逐字读完整个正文文件」，不是关键词命中率，也不是段落骨架扫描。**
> 语料：D:\数据集\PDF_Radiolaria 全库 8162 篇 PDF 中按 28 个主子目录**分层随机**抽取 181 篇
> （种子 20261103，**不按文件大小排序**）；其中正文可逐字读取者 164 篇（≥3000 字符、文本层乱码率 ≤30%）。
> 每篇由独立子 Agent 用 read 工具**读到文件末尾**，并在分片末尾的覆盖率表中逐篇声明
> 「文件字符数 / 实际读到的字符数 / 覆盖章节」；主会话另用机器校验器把笔记中的每条引文回源核对。

## 一、阅读口径与可兑现范围（先说清楚）

| 口径 | 数值 | 说明 |
|---|---|---|
| 分层随机抽取 | 181 篇 | 28 个主子目录按篇数比例分配，目录内均匀随机，**不按文件大小排序** |
| 正文可逐字读取 | 164 篇 | ≥3000 字符且文本层乱码率 ≤30% |
| 其中期刊论文（≤60 页） | 约 120 篇 | 逐字读完 Abstract→Conclusion→Acknowledgements |
| 其中专著/图幅（>60 页） | 约 12 篇 | 逐字读完，按章节结构层记录 |
| 无文本层（扫描件） | 12 篇 | 只能渲染页面看图，无法逐字读 |
| 正文合计 | 约 570 万字符（切掉参考文献后） | 参考文献列表不计入正文 |

**🔴 重要更正**：本 skill 早期版本（v2.12.0–v2.14.0）声称"130 篇逐篇读段落骨架"，
该口径作废。原因有二：(1) 旧抽取器用 dict 存章节，遇同名标题会**覆盖前一段正文**；
(2) 旧"130 篇"取自按文件大小升序排列的清单，实为全语料**最小的** 130 篇（中位 0.89 MB），
而其余 216 篇中位 6.88 MB、最大 435 MB——**样本严重偏小**。v2.15.0 已重抽并重跑。

## 二、章节链实测：没有统一模板

164 篇中**没有一篇的章节链与另一篇完全相同**。实测到的骨架可归为五类：

### 2.1 完整 IMRaD + 声明块（高标准地学刊）

刊头(含 Article history 四日期) → 摘要 → 1. INTRODUCTION → 2. Oceanographical settings → 3. METHODS (3.1…) → 4. RESULTS (4.1…) → 5. DISCUSSION (5.1 MIS 6.2 / 5.2 MIS 5e …) → 6. CONCLUSION → Author statement → Data availability → Declaration of competing interest → ACKNOWLEDGEMENTS

（证据：Gorbarenko et al 2020, Quaternary Science Reviews 247:106569）

### 2.2 分类学体系论文（无 Discussion、无 Methods）

刊名头 + УДК → 标题 → 无标题摘要 → Описание видов → Отряд → …

（证据：Mamedov 1973, Известия АН Азербайджанской ССР 1973(2):59–64）

### 2.3 短篇发现报告（3–10 页，无独立 Discussion）

（无标题引言）→ 正文连续散文 → 图注 → 图注

（证据：Deflandre 1946, C.R. Acad. Sci. Paris 223:515–517）

刊头 → 摘要 → 一、火山岩野外观察 → 二、放射虫 → 参考文献 → 图版I

（证据：Yang Wanrong & Jiang Nayan 1980, 地层学杂志 4(1):67–69）

### 2.4 区域生物地层学（无独立 Methods，方法只有一句）

刊名头 + УДК + 标题 → 摘要（无标题）→ Ключевые слова. → 无标题正文 → 逐剖面描述 → 无标题结论段（4 段）→ СПИСОК ЛИТЕРАТУРЫ

（证据：Гольтман и др. 2002, Стратиграфия. Геологическая корреляция 10(5):92–107）

### 2.5 系统描述类（讨论不在 Discussion 段）

SYSTEMATIC → 逐类群块 → 结论

（证据：Baker 1983, J. Paleontology；Afanasieva 2019, Pal J 53(5):435–446）

## 三、中间部分（Methods / Results）的真实写法

### 3.1 Methods 的三种详略档次

| 档次 | 特征 | 证据 |
|---|---|---|
| **完整式** | 公式 + 逐符号定义 + 仪器 + 测量间隔 + 自陈简化 | Gorbarenko 2020: "ARM (individuals cm⁻² kyr⁻¹) = CM × DBD / LSR; where CM is the content of microfossils (individuals per gram of dry sediment), DBD is the dry bulk density (g cm⁻³) and LSR is the linear sedimentation rate (cm kyr⁻¹)" |
| **一句式** | 只说材料类型 | Гольтман 2002: "Материалом для радиоляриевого анализа послужили, главным образом, шлифы." |
| **写进摘要式** | 俄文分类学把绘图方法写进摘要 | Mamedov 1973: "Зарисовки радиолярий выполнялись под микроскопом МБИ-3 при 280-кратном увеличении художником А. А. Захаряном." |

→ **没有"必须写满 Methods"的规则**；但**只要用了指标，就必须给公式与符号定义**。

### 3.2 Results 的两条硬要求

1. **先给总量与采样密度**：
   "The 23 species and 7 genera BF were identified in the 245 samples of the core PC-7R. The BF abundance varies down core from 0 to 916 ind./g"（Gorbarenko 2020）
2. **直接说某组不具信息量**：
   "Therefore, this group is not informative (Fig. 4)."（同上）

### 3.3 结果段里嵌"反常发现"，为讨论埋伏笔

"However, during the HEE 9 of MIS 5c, the ARs of R-surface, A. setosa and R-dichothermal showed sharp increases, which were contrary to the drop in the AR of BF and productivity."（Gorbarenko 2020）

## 四、Discussion 的四拍结构（最值得抄的一条）

**按时间段分节，每节固定四拍**（证据：Gorbarenko 2020 的 5.1 MIS 6.2 / 5.2 MIS 5e）：

1. **数据陈述**："The high values of IRD during MIS 6.2 indicate that…"
2. **机制解释**："…forced active sea ice formation and caused its expansion into the central OS"
3. **与前人比对（一致 or 矛盾，二选一，明确写出）**：
   "Such a pattern of duration and intensity during interstadial B1 is consistent with the pattern of B1 in the southern Bering Sea according to Gorbarenko et al. (2019) but contradicts its timing and intensity according to Ovsepyan et al. (2017)."
4. **本研究结论 + 不确定性**："Such hypothesized glaciers should have strongly cooled the OS area by geostrophic winds related to the enhancement of the Siberian High."

→ **"consistent with … but contradicts …" 是本领域讨论的标准句式**，把分歧显性化，而不是和稀泥。

## 五、结论（Conclusion）的两种形态

### 5.1 连续散文式（高标准刊）

开头一句**复述研究做了什么**（含时段、方法、指标）：

"The responses of the production of BF and radiolarian ecological groups in the central OS to orbital and millennial-time scale climate and environmental changes over the last 136 kyr were studied on the basis of available productivity, geochemical and lithological records in the sediment core PC-7R. A previously constructed age model of this core was modified to millennial scale resolution."

然后按「代理 → 现象 → 机制」逐条展开，机制归因用 **"rather than" 做排除**：

"Therefore, we suggest that the enlarged production of R-mesopelagic during late MIS 5e was mostly supported by the large lateral transportation of detritus and OM from the subarctic western Pacific into the intermediate water of the central OS, rather than from the northwestern OS shelf and slope."

不确定性用 **"likely due to"** 而非断言：

"the radiolarian production, especially for R-mesopelagic, was significantly suppressed in the central OS, likely due to low primary productivity and weak lateral transport of detritus from the WSAP while ventilation of the OSIW was high."

末尾留**明确的开放问题**：

"The sources of these peaks of mesopelagic radiolarian production may lay in the western North Pacific, including the Okhotsk and Bering Seas and their hinterlands, and they present an important subject for further high-resolution investigation."

### 5.2 编号清单式（短篇/区域地层）

"以下地区情况可资鉴别：1. … 2. … 3. … 4. … 5. …"（Zheng Haixiang et al 1986, Bull. Chengdu Inst. Geol. M.R. 7:85–93）

## 六、短篇（3–10 页）的三种讨论形态

**实测：本领域 3–10 页短篇绝大多数没有独立 Discussion 段**，讨论以三种形态出现：

| 形态 | 证据 |
|---|---|
| **点名质疑前人** | Zheng 1986 点名 Miyashiro(1973)、Pearce et al(1981)、Robinson(1984) 三个既有范式，再逐条给五条反证："以下地区情况可资鉴别：1. … 2. …" |
| **承认局限再修正** | Deflandre 1946: "la première étude des nodules phosphatés donne une idée incomplète et fausse de leur microfaune de Radiolaires. Il en est exactement de même si l'on n'étudie que les spécimens dégagés. Mais, grâce à cette seconde méthode…" |
| **"不能断言但可能"** | Yamasaki & Yamasaki 1999: "Amphipyndax aff. enesseffi および A. aff. tylotus の形態特に diagonal ridge の発達についての時間的変化は検討されていないので…明確なことは言えないが，DK群集帯の中での上位層準であることを示す可能性があると思われる。" |

## 七、引言（Introduction）的起手模式（逐字实证）

| 模式 | 逐字证据 | 出处 |
|---|---|---|
| **区域重要性 + 研究史 + 缺口 + 范围句**（五段式） | "this is why the OS, as the lowest-latitude region with seasonal sea ice cover in the world, plays a leading role in high-latitude paleoceanography" … "Here, we focus on the high-resolution study of radiolarian and BF species…" | Gorbarenko 2020 |
| **孤例价值 + 原因** | "Радиолярии отряда Phaeodaria исключительно редки в ископаемом состоянии. Это обстоятельство объясняется особенностями их скелета…" | Runeva 1974 |
| **承认现状困难 → 引出动作** | "Si l'on ne s'aperçoit qu'un type de sclérite peut se rencontrer dans plusieurs genres… néanmoins les micropaléontologistes… ne peuvent éviter la création de dénominations particulières pour chaque type." | Deflandre 1946 |
| **区域综述 + 缺口 + 本文动作** | "…からの報告であり，…については…が報告しているだけである" | Yamasaki 1999 |
| **时间地点 + 发现 + 自陈局限** | "1983年野外地质调查期间，我们在西藏阿里地区发现了四条蛇绿岩剖面（图1）虽然尚未取得岩石学、岩石地球化学的室内测试资料…但是，在野外这四条剖面上均可追索和鉴别出相对完整的 steimann 三元体系。" | Zheng 1986 |
| **背景 + 目的（无引言段）** | "我国南部长兴阶的层型剖面在浙江长兴煤山藻青采石场。层型剖面经我所二迭—三迭纪地层队研究（1978）…" | Yang 1980 |

## 八、系统描述类（类群块）的标签模板（跨语种汇总）

| 模板 | 标签序列 | 出处 |
|---|---|---|
| **Pal J 英文制式** | Genus X gen. nov. → Etymology. → Type species. → Diagnosis. → Species composition. → Comparison. | Afanasieva 2019 |
| **Pal J 种级** | X sp. nov. → Etymology. → Holotype. → Description. → Measurements in μm and ratios (Fig. 6): → Comparison. → Material. → Remarks. | Afanasieva 2019 |
| **俄文五拍** | 学名 + sp. n. → 图版引用 → Голтип 存放地行 → Оригинал 存放地行 → Описание. → Размеры, мк: → Изменчивость. → Сравнение. → Местонахождение и возраст. | Mamedov 1973 |
| **俄文阶元诊断集** | ОТРЯД → Диагноз. → Состав. → Распространение. | Afanasieva 2002 |
| **附录匿名新种** | species D → Dimensions-(based on 60 specimens…) → Remarks- | Baker 1983 |

→ **俄文必写两句**："Близкие по морфологии виды не установлены."（无近似种时）
和 "…позволяет выделить новый род, так как подобный род в семействе … не выделен."（新属理由）。

## 八之二、摘要（Abstract）写法实证

### 8.2.1 一个必须先说的口径问题

164 篇里**只有 44 篇**（27%）有机器可识别的独立 ABSTRACT 段；
其余 **120 篇（73%）的摘要没有标题标记**，直接嵌在标题页/正文流里
（俄文刊、中文刊、日文刊、老刊尤其如此）。
→ **写摘要时不必纠结"要不要 Abstract 标题"**：老刊常省略标题，新刊（Elsevier/Springer）必有。

### 8.2.2 摘要长度与句数（44 篇有独立摘要段的样本）

| 指标 | 数值 |
|---|---|
| 字符数 min / p25 / **中位** / p75 / max | 314 / 1089 / **1992** / 2553 / 6340 |
| 句数 min / **中位** / max | 3 / **13** / 150 |

→ 中位 **约 2000 字符 ≈ 300 词**，**约 13 句**。
  比多数期刊的 150–250 词上限**偏长**——说明本领域摘要偏向"小型引言"，不限定字数时容易写长。

### 8.2.3 摘要的五个功能件（38 篇英文摘要，逐字标记）

| 功能件 | 出现率 | 写法 |
|---|---|---|
| **结果** | **87%** | 必写，且常带数据 |
| **方法** | **74%** | 材料 + 产地 + 手段 |
| **背景/现状** | **68%** | 1–2 句，常用 however / remains / poorly known |
| **结论/意义** | **50%** | suggest / indicate / provide / first record |
| **目的** | **29%** | 反而不常见——本领域摘要常**开门见山报结果**，不写"本文旨在" |

→ 🔴 **与通用模板最大的不同：本领域摘要以"结果"打头（87%），"目的句"只占 29%。**
  通用模板要求的"背景→目的→方法→结果→结论"五段式，在本领域**只有约 30% 的摘要**真的写了目的句。

### 8.2.4 时态与语态（38 篇英文摘要）

| 特征 | 出现率 |
|---|---|
| 现在时标记（is/are/shows/indicates/suggests） | **95%** |
| 过去时/完成体标记（was/were/has been） | 68% |
| 被动结构（be + 过去分词） | **87%** |
| 第一人称 "we" | **仅 18%** |
| 含数字/数据 | 84% |
| 含新分类单元声明（gen. nov./sp. nov.） | 3% |

→ 🔴 **摘要用现在时陈述结论（95%），用被动语态（87%），几乎不用 "we"（18%）。**（⚠️ 仅适用于英文刊；见 §8.11）
  这与通用模板"避免被动"的建议**相反**——本领域的规范是**被动 + 现在时**。

### 8.2.5 逐字例句

**开门见山报结果型**（本领域主流）：
> "There appear to be about six shallow-water polycystine radiolarian provinces in the modern ocean. These provinces owe their integrity to the major circulation systems that create packages of water and environments which vary in degrees of oceanographic and temporal stability."
> —— Casey 1989, Palaeogeogr. Palaeoclimatol. Palaeoecol. 74:15–22

**新分类单元摘要型**（注意：标题即新类群名，摘要直接列新属新种）：
> "Based on the structure of microsphere and systems of girdles the author describes a new family — Miropylidae, two new pyloniid subfamilies — Palaeotetrapylinae and Dipylissinae, and three new genera and species — Miropyle mirabilis, Palaeotetrapyle muelleri and Dipylissa bensoni."
> —— Dumitrica 1988, Pylonioidea

**多语摘要型**（德/法刊同一篇附多种语言摘要）：
> "Résumé — ... / Zusammenfassung — ..."
> —— Baumgartner 1985（121 页专著，附三语摘要）

### 8.2.6 可抄的摘要骨架（按体裁选）

| 体裁 | 骨架 |
|---|---|
| **分类学新类群** | 新类群名 + 产地层位 → 鉴别特征 → 与近缘类群差异 → 意义 |
| **生物地层** | 剖面/层位 → 群集特征 → 与已知带的对比 → 时代结论 |
| **古环境重建** | 材料与方法 → 代理指标结果 → 与环境事件的对应 → 结论 |
| **综述** | 领域范围 → 已有共识 → 分歧/空白 → 本文如何处理 |

## 八之三、现代期刊的强制声明块（1% 覆盖率，但属硬性要求）

164 篇里只有极个别论文（主要是 Elsevier/Springer 系）带这些块，但**目标期刊若要求，缺失即退稿**。

### 8.3.1 四日期投稿流程（Elsevier）

> "Received 11 June 2020 / Received in revised form 26 August 2020 / Accepted 27 August 2020 / Available online 13 September 2020"

### 8.3.2 作者贡献（CRediT）

> "Author statement — Sergey A. Gorbarenko: Conceptualization, Methodology, Validation, Investigation, Writing - Original Draft, Writing - Review & Editing. Elena A. Yanchenko: Methodology, Validation, Formal analysis, Investigation."

→ **逐作者列角色**，用 CRediT 词表（Conceptualization / Methodology / Validation / Investigation / Formal analysis / Writing - Original Draft / Writing - Review & Editing）。

### 8.3.3 数据可用性

> "Data availability — All relevant data in this paper have been uploaded to MendeleyData https://data.mendeley.com/datasets/gbr7tprkyd/1."

### 8.3.4 利益冲突

> "Declaration of competing interest — The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."

### 8.3.5 致谢

> "We are grateful to Captain Akamine and the crew of the R/V Mirai for their help with sediment collection in the OS during the MR06-04 cruise."

→ 致谢顺序：**先谢船上/野外协助 → 再谢合作机构 → 最后谢基金号**。

---

## 八之四、决策树：先判断体裁，再选骨架

**写之前先回答三个问题**（依据：164 篇章节链实测）：

**Q1 本文的主要贡献是什么？**
- 新分类单元 / 新类群 → 骨架 A（系统描述类）
- 地层的时代确定 / 对比 → 骨架 B（生物地层类）
- 环境 / 气候重建 → 骨架 C（多指标古环境类）
- 方法 / 理论 / 综述 → 骨架 D（方法或综述类）

**Q2 目标刊是"老刊"还是"新刊"？**
- 老刊（Pal J / 俄文刊 / 中文老刊 / 日文刊）→ 可省独立摘要标题、可省 Discussion、可用图版制、可用 × magn.
- 新刊（Elsevier / Springer / Wiley）→ 必须有独立 Abstract、必须带声明块、必须给比例尺条、彩色图需免责句

**Q3 篇幅多长？**
- ≤10 页 → 短篇骨架（无独立 Discussion，讨论嵌入末段）
- >10 页 → 完整骨架（但仍可能无 Discussion——65% 的论文没有）

### 五种骨架速查

| 骨架 | 章节链 | 典型刊 |
|---|---|---|
| **A 系统描述** | INTRODUCTION → [Repository] → SYSTEMATIC DESCRIPTION（逐类群块）→ [Discussion 常缺省] | Pal J, Pal Zh, 分类学专刊 |
| **B 生物地层** | INTRODUCTION → GEOLOGICAL SETTING → MATERIAL & METHODS → RESULTS（逐剖面/逐层）→ DISCUSSION → CONCLUSION | Palaeo 3P, 地层学杂志 |
| **C 多指标古环境** | INTRODUCTION → OCEANOGRAPHICAL SETTING → METHODS → RESULTS → DISCUSSION（按时间段分节）→ CONCLUSION + 声明块 | QSR, Palaeo 3P, Deep-Sea Res. |
| **D 区域综合/综述** | 无统一链，按主题分节 | 综述刊 |
| **E 短篇报告** | （无标题引言）→ 正文连续散文 → 图注；或 一、二、三 编号小节 | 各类刊的短通讯 |

## 八之五、标题（Title）写法实证

### 8.5.1 统计（44 篇可抽取标题，≥5 词）

| 指标 | 数值 |
|---|---|
| 词数 min / p25 / **中位** / p75 / max | 5 / 5 / **6.5** / 10 / 16 |
| 含**年代词**（Devonian/Stage/Formation/Group…） | **41%** |
| 含**产地/构造词**（Urals/Sea/Basin/Klippen/Suture…） | **32%** |
| 含**类群名**（radiolaria/foraminifera…） | **25%** |
| 含**方法/研究词**（analysis/review/biostratigraphy/fauna…） | 20% |
| 用**破折号** | 23% |
| 用**冒号副标题** | **0%** |
| 用**问号** | **0%** |

→ 🔴 **本领域标题不用冒号副标题、不用问号**；主流是 **6–7 个词的名词短语**。

### 8.5.2 三个可抄的构造公式

1. **「时代 + 类群 + 产地」**（最主流）
   > "Devonian radiolarians of Russia"
   > "Jurassic Sedimentary Evolution and Nappe Emplacement in the Argolis Peninsula (Peloponnesus Greece)"
2. **「新类群名 + 产地 + 时代」**（分类学论文，把新类群名直接写进标题）
   > "New Taxa and New Middle Famennian Natgorella hirsuta–Spinoalius melekessensis Radiolarian Ecozone of the Volga–Ural Basin"
3. **「主题 + 产地」**（区域地层）
   > "Some Devonian radiolarians from chert blocks in the Bentong-Raub Suture Zone in Pahang"
   > "Northern Okinawa Trough"

### 8.5.3 逐字标题（跨刊）

- "Pieniny Klippen Belt"（极短型，4 词）
- "Jurassic and Early Cretaceous Vaamychgyn-Podgornaya Koryak"（时代 + 构造单元）
- "Туронские радиолярии в разрезе горы Ак Крым"（俄文：时代 + 类群 + 剖面）
- "Анализ динамики исчезновения и появления новых видов радиолярий"（俄文：方法词 + 对象）
- "micro L'origine péridienne des Radiolaires et l'interprétation parasitaire de l'anisosporogénèse"（法文：主题 + 理论解释）

---

## 八之六、时态与语态（摘要口径，38 篇英文摘要）

| 特征 | 出现率 | 写法建议 |
|---|---|---|
| 现在时（is/are/shows/indicates/suggests） | **95%** | 陈述结论用现在时 |
| 被动结构（be + 过去分词） | **87%** | 用被动，突出结果而非作者 |
| 第一人称 "we" | **仅 18%** | 少用 "we" |
| 过去时/完成体 | 68% | 描述具体做过的事可用过去时 |
| 含数字/数据 | 84% | 摘要要给具体数据 |

→ 🔴 **本领域摘要规范 = 现在时 + 被动 + 少用 we**。
  这与通用模板"避免被动"的建议**相反**，是本领域最容易被通用建议带偏的一条。

⚠️ **引言段的时态/语态未做同口径统计**（笔记中散见，未量化）——
  需要时按目标刊抽样 10–20 篇引言首段重做。

---

## 八之七、综述口吻（review tone）

语料里识别出 **4 篇综述型论文**（刊眉或体裁自标 "総説" / review / 综述），
其口吻与原创研究**明显不同**：

### 8.7.1 综述型引言 = 「前编回顾 + 本编范围 + 双角色框架」

> 「本論では言及しないことにする。」（前编已述，本编不重复）
> 「石油根源に底生有孔虫が実績をあげてきたが，放散虫化石は潜在のような古生態学的な研究の不足については」
> —— 本山功 1999, J. Japan Assoc. Petrol. Technol. 64(3):269–281（刊眉明写 "総説"）

### 8.7.2 综述方法学的关键动作：**先立收录标准，再列数据**

> 「収録の対象とした文献は，原則として放散虫化石の種名あるいは化石帯名が掲載されていて，かつ試料採取地点あるいは試料採取ルートが明示されている公表論文とした。」
> —— 同上

→ 🔴 **综述不能只罗列文献，必须显式写出"我收录了什么、排除了什么、为什么"。**

### 8.7.3 综述体的骨架钉：**每节收尾给一句可记忆的概括句**

> "Summing up, one might conclude that sinking serves different purposes in the life-history cycles of diatoms."
> —— Smetacek 1985, Marine Biology 84:239–251（综述+假说论文，**零图表**，以文献密度替代图表）

### 8.7.4 用类比跨门类外推

> "The striking similarity of this behaviour with that of bloom diatoms strongly suggests similar life-history patterns amongst species in both groups."
> —— 同上

### 8.7.5 长篇报告的综述放在**章首「概要と研究史」**

> 「本報告では化石の産出が乏しく，詳しい年代の検討が困難なため，手取層群の区分はおおむね河合・野沢（1958）に従い…」
> —— 日文地学报告（先综述研究史与争议，再声明本报告采用方案）

### 8.7.6 综述 vs 原创的五条差异

| 维度 | 原创研究 | 综述 |
|---|---|---|
| 引言 | 缺口 → 目的 → 本文动作 | 前编回顾 → 本编范围 → 双角色框架 |
| 方法 | 材料/采样/仪器 | **收录标准**（收什么、排什么） |
| 图表 | 本文数据图 | 常为零图表，靠文献密度 |
| 收尾 | 结论 + 开放问题 | 每节给可记忆的概括句 |
| 文献 | 支持论证 | **本身就是对象**，需分层评价 |

## 八之八、引言（Introduction）时态与语态

**口径**：45 篇有独立 INTRODUCTION 段的**英文**论文（其余 119 篇无独立标题，未纳入）。⚠️ 结论仅适用于英文刊；中文刊见 §8.11。

| 特征 | 引言 | 对比：摘要 |
|---|---|---|
| 现在时标记 | **96%** | 95% |
| 过去时/完成体标记 | **93%** | 68% |
| 被动结构 | **96%** | 87% |
| **第一人称 we** | **49%** | **仅 18%** |

→ 🔴 **最重要的差异：引言可以用 we（49%），摘要几乎不用（18%）。**（⚠️ 仅适用于英文刊；中文刊用「我们」/「本文」/「笔者」，见 §8.11.4）
  写引言时「我们做了什么」是合法的；写摘要时要把主语让给结果。

→ 引言长度：中位 **3786 字符**（min 774 / p75 8177 / max 18955），
  是摘要中位（2000）的约 **1.9 倍**。

**写法建议**：
- 引言：现在时陈述领域现状 + 过去时叙述本文工作 + 可用 we
- 摘要：现在时 + 被动 + 不用 we


## 八之九、关键词（Keywords）写法

**口径**：62/164 篇（38%）能机器识别关键词块（58 篇为行内标记，4 篇为独立段）。

| 指标 | 数值 |
|---|---|
| 个数 min / p25 / **中位** / p75 / max | 0 / 4 / **8** / 12 / 20 |
| 分隔符 | 逗号（英文）/ 逗号或顿号（中文） |
| 大小写 | **全小写为主**（英文刊） |
| 是否加句号 | **不加** |

### 8.9.1 关键词的四个语义层（按出现频次）

1. **类群名**（最高频）：Radiolaria / radiolarians / Polycystine radiolaria
2. **研究主题**：biostratigraphy / paleoecology / paleobiogeography / evolution / biodiversity / taxonomy / stratigraphy
3. **时代**：Devonian / Cretaceous / Jurassic / Paleogene / Famennian / Campanian
4. **产地**：Russia / Polar Urals / Volga-Ural Basin / Western Carpathians / Koryak Highland

→ 🔴 **公式：类群 + 主题 + 时代 + 产地**（各取 1-3 个，共约 8 个）。

### 8.9.2 逐字例子

> "Radiolaria, paleoecology, paleobiogeography, evolution, biodiversity, new species, biostratigraphy, Devonian, Russia."
> —— Afanasieva & Amon 2011c（Pal J）

> "Jurassic, Western Carpathians, Pieniny Klippen Belt, Pruske Unit, stratigraphy, microfacies, radiolarians, sedimentology."
> —— Aubrecht & Ozvoldova 1994（Geol. Carpathica）

> "Polycystine radiolaria  Biodiversity  Eastern Mediterranean  Sediment trap  Ionian Sea  Aegean sea  Cretan sea"
> —— Danelian et al. 2022b（注意：用**双空格**分隔，无逗号）

### 8.9.3 双语关键词是常态（多语种刊）

> "Ключевые слова: РАДИОЛЯРИИ, МЕЛ, ПАЛЕОГЕН, ЭВОЛЮЦИЯ, ВЫМИРАНИЕ ВИДОВ" + "Keywords: RADIOLARIA, CRETACEOUS, PALEOGENE, EVOLUTION, SPECIES EXTINCTION"
> —— Agarkov & Agarkov 2017（俄文刊附英文关键词）

> "Key words : Upper Cretaceous, Dictyomitra koslovae Assemblage Zone, radiolaria.　キーワード：上部白亜系，Dictyomitra koslovae 群集帯，放散虫．"
> —— Yamasaki & Yamasaki 1999（日英并置）

→ **中文/日文/俄文刊常要求双语关键词**；英文刊只给英文。

### 8.9.4 注意一种变体：**双空格代替逗号**

Danelian et al. 2022b 用双空格分隔且无标点——**同一刊物体系内可能两种并存**，
交稿前按目标刊近期论文核对。


## 八之十、适用范围声明（重要）

🔴 **本 skill 的结论只适用于「地学 / 古生物（微体古生物）类的期刊论文写作」**，
具体是放射虫、有孔虫、牙形刺、硅藻等微体古生物方向的**原创研究论文与综述**。

**不要推广到**：
- 其他学科（生物、化学、医学、材料、计算机）——章节惯例、引文密度、图表规范都可能不同
- 非地学的古生物学（脊椎动物大化石、植物化石）——图版制式与描述粒度不同
- 社科 / 人文 —— 完全不适用

**证据基础**：本地语料 D:\数据集\PDF_Radiolaria（8162 篇 / 62 GB / 64 子目录），
分层随机抽取 181 篇，164 篇逐字精读。

**明确不覆盖**：
- 返修信 / 审稿回复（需要另一批语料）
- 基金申请书、学位论文答辩（不在语料里）
- 非英文/俄文/中文/日文/德文的第四语种
## 八之十一、中文刊 vs 英文刊的系统性差异（2021 年 10 篇新增证据）

> ⚠️ **样本偏倚声明**：本节的中文刊结论 4/6 来自《微体古生物学报》一本刊，详见 §12.3。

**证据**：2026-11-02 追加精读 10 篇（6 篇中文刊 + 4 篇英文刊，合计 538,220 字符），
与前述 164 篇（以英文为主）的结论逐条对照。**核心发现：许多结论只适用于英文刊，中文刊系统性地不同。**

### 8.11.1 必须修正的既有结论（5 条）

| 原结论 | 修正 | 反证 |
|---|---|---|
| Revue de micropaléontologie 用 × magn. | **不成立**：至少 Bragina & Bragin 系列（2020a/2021）用比例尺条（100 mm: a – 1–3, 7; b – 4–6; c – 9–12; 50 mm: d – 8.） | 008 |
| 摘要现在时 95% | **仅限英文刊**：008/009 摘要以**过去时被动**起手（were recovered、were studied），随后转现在时 | 008, 009 |
| 引言 we 49% | **仅限英文刊**：009 引言 0 处 we；中文刊用「我们」/「本文」/「笔者」 | 009, 000–005 |
| 标题中位 6.5 词 | **有例外**：分类学/古生物长标题可达 10–28 词；中文标题 14–18 字 | 006(28), 007(10), 008(12), 009(16) |
| 关键词中位 8 个 | **有偏差**：英文刊 5–10 个，中文刊 4–6 个 | 006(10), 007(6), 008(5), 009(5), 000(4), 002(4) |

### 8.11.2 中文刊的固定骨架（与英文 IMRaD 不同）

```
摘要（提要）→ 关键词 →（引言 / 前言）→ 编号正文（1 / 2 / 3 …）
→ 系统描述（「3 系统分类描述」/「3 系统古生物学」，常是最大章节，**代替讨论**）
→（致谢）→ 参考文献 → 英文摘要（＋新种英文描述）
```

→ 🔴 **中文刊把「系统描述」当主章节，时代讨论放独立编号节**
   （如「1 早白垩世的 Cecrops septemporatus 生物带」「2 凯迪期放射虫化石带及斯堪的纳维亚冰川漂砾来自何方」）。

### 8.11.3 中文摘要的骨架（与英文相反）

英文摘要：**结果打头**（87%）。
中文摘要：**主题句 / 前人工作起手** → 本文工作 → 结论（中文样本 3/3 如此）。

逐字例：
> 「雅鲁藏布江缝合带是青藏高原上最年轻的一条缝合带…」（000，主题句起手）
> 「放射虫 Cecrops septemporatus 带在世界各地的瓦兰今阶广泛分布，中国最早在上世纪八、九十年代发现于…」（001，主题＋前人发现起手）
> 「安太庠等（1985）把金粟山组分成 4 段…」（002，直接以前人工作起手）

### 8.11.4 中文第一人称三型

| 型 | 例子 |
|---|---|
| 「本文」作主语 | 「本文对藏南地区放射虫的相关报道进行了总结」「本文继续报告…」 |
| 「我们」 | 「这次，我们在第 4 段中找到了…」「经我们这次对这个放射虫动物群的重新研究」 |
| 「笔者」 | 005 用「笔者」 |

→ 中文无被动语态标记，**不要按英文的被动 87% 要求改中文稿**。

### 8.11.5 中文综述的组织方式（与收录标准先行不同）

英文综述强调**先立收录标准**（§8.7.2）。中文综述（000）**无收录标准段**，改为：

```
按「构造单元」分节（缝合带南北两侧 → 特提斯喜马拉雅）
→ 按「地区」分节（泽当 / 白朗 / 拉孜 / 仲巴；江孜 / 萨迦 / 萨嘎 / 仲巴）
→ 每节按「剖面 / 地层 → 时代 → 属种 → 对比」写
```

评价他人工作用「但」「仍存在很大争议」「有待做一些新的修订」「并未引起足够重视」，
且**对争议双方并列陈述**（如 Turbocapsula costata 的两种定年都列出）。

### 8.11.6 中文类群块模板（与英文 Pal J 制式不同）

| 层级 | 中文模板 | 英文模板（对照） |
|---|---|---|
| 属级 | 模式种 → **属征** → 时代与分布 | Genus X gen. nov. → Etymology. → Type species. → Diagnosis. → Species composition. → Comparison. |
| 种级 | … → **产地和层位** / **时代分布** | X sp. nov. → Etymology. → Holotype. → Description. → Measurements → Comparison. → Material. → Remarks. |

- 中文新种块以「（新种）」标注；英文用 sp. nov.
- **英文新种描述常集中置于文末**（DESCRIPTION OF NEW SPECIES / Description of New Species），与中文正文分离——**这是中文刊特有的版面安排**。

### 8.11.7 中文图注格式（固定七要素）

```
图号 ＋ 中文题名 ＋ 英文题名 ＋ 分图条目（1,2. 种名：1. 样品号 / SEM 影像编号）＋ 比例尺 ＋ 标本保存地
```

- **同刊内比例尺写法不统一**：001 图 2/图 4 用「比例尺（Scale）＝100μm」，图 3 用「比例尺（scalebar）＝100μm」；002 用「标尺＝100μm」。
- **分图编号两种格式并存**：001 写「（图２ ６）」，002 写「（图３－１，２）」。
- **中文刊全部使用比例尺，不用 × magn.**（与部分英文刊相反）。

### 8.11.8 中文图表引用格式

```
（图１）  （表１，点２）  （图３－１，２）  （详见３．２）
```

→ 图号与表号混排，表注常用「注：位置前的数字编号与图１和图２中的一致」把**图-表-点号绑定**。

### 8.11.9 中文对比表用「√」标记共同种

002 表 1：行＝种名，列＝本文＋5 个地区/文献，**单元格打「√」**。
→ 与英文刊的 X / ♦ / 线条式矩阵不同（§5.3 需补这一条）。

### 8.11.10 中文刊的固定前置 / 后置件

- 首页脚注：**基金号** + 「收稿日期 …，修改稿收到日期 …」
- 「＊＊通讯作者（Corresponding author）E-mail：…」
- 可有「致谢」节，含**献给专辑的献词**（「谨以本文献给盛金章老师诞辰 100 周年专辑…」）
- 文末附**英文摘要 + 新种英文描述**

### 8.11.11 新发现：METHODS 容器化（英文长文）

007（Afanasieva 2021, Pal J, 38 页）把**结果与讨论全部装进 METHODS 标题下**
（53,369 字符，占全文约 **45%**），内部用 **8 个全大写字标题**分节。
→ 已有「章节链五类骨架」未涵盖这种变体。

**无 Discussion 时讨论的去处**（10 篇里 9 篇无独立 Discussion）：
1. 装进 METHODS（007）
2. 嵌在引言（008）
3. 嵌在 Results（009）
4. 用类群块的 Comparison / Remarks 承担（006）

### 8.11.12 结论的第三种形态：混合式

已有「结论两种形态」（编号列表 / 段落）。新证据显示还有：

| 形态 | 特征 | 例 |
|---|---|---|
| 混合式 | 导语句 + 编号列表 + 列表后段落 + 嵌套项目符号 | 007 |
| 单段连排式 | 编号 1–5 但**连排成一个自然段** | 009 |
| 两级编号式 | １）＋ａ） | 004 |
| 写在摘要里 | 正文无结论节，结论式判断放摘要 | 002 |

### 8.11.13 长文分节方式（英文 38 页）

007 的分节逻辑：**按剖面 → 按生态区 → 按主题**（不是按时代、不是按带）。
生态区名用**双名式索引种组合**，并引用《俄罗斯地层规范》定义。
→ 图版也**按生态区组织**（Plate 1–10 对应 4 个 ecozone），而非按种。

### 8.11.14 其他新制式

- **未编号 inline 测量表 + 脚注参数定义**（006：列 Specimen no./H/W/D/Lw/L/dp/wp/dc/wc）
- **出现/缺失矩阵表**、**延限图（range chart）**、**视角键（dorsal/edge/umbilical）**（009）
- **方法段写死统计门槛**（003/005：「鉴定至 400 枚」「仅对 >300 枚样品做相对含量」「至少统计 400 个个体，不足则对全部薄片统计」）
- **类群块四段式**（004：形态 → 命名史 → 分子证据 → 归类决议，并明确表态「暂时将其降为目阶」）
- **FAD 生物事件表**（005：4 个年龄点）
- **图例标签不统一**（Pal J 同刊内 Legend: / Expanations:（拼写错误）/ Explanation: / Designations: / Explanations: 并存）

### 8.11.15 摘要-正文数字矛盾（新警示）

001 摘要写「描述放射虫 18 属 23 种，包括 3 个新种」，正文写「80 141 组合有 20 属 24 种，包括 4 个新种」，
实际系统描述只有 3 个新种。
→ 🔴 **中文刊的「摘要-正文-英文摘要」三者数字必须交叉核对，不能只信摘要。**

### 8.11.16 本批样本的抽取缺陷（使用结论时注意）

- 中文双栏 PDF 抽取**左右栏交错**，页眉页脚混入正文流
- 000 文件头 FIG/TAB 计数为 0，但实有图 1–2、表 1–2（表体未抽取出）
- 002 表 1 仅部分抽取出
- 003、004 实为 **2020 年**论文（仅 005 为 2021），选刊时注意年份

## 九、横切统计（164 篇精读笔记，机器计数）

对 164 篇精读笔记做关键词计数（**仅作覆盖率参考，不作论证动作判断；强度等级见 §12**）：

| 现象 | 篇数 | 占比 |
|---|---|---|
| 提到图版 / Plate / 図版 | 164 | 100% |
| 提到引言 / Introduction / はじめに | 162 | 99% |
| **没有独立 Discussion 段** | **106** | **65%** |
| 有摘要 | 122 | 74% |
| 提到表格 / Table / Таблица | 83 | 51% |
| 提到比例尺 | 71 | 43% |
| 提到放大倍数 | 50 | 30% |
| 提到标本号 / Holotype / PIN | 15 | 10% |

→ 🔴 **最重要的一条：65%（106/164）的论文没有独立 Discussion 段。**
   这与"短篇没有 Discussion"的旧印象不同——**在 10 页以上的论文里同样普遍**。
   因此 skill 不应假设"一定有 Discussion 段可写"，而应先判断本文属于哪一种骨架。

## 十、引文回源校验（机器口径）

主会话用校验器把笔记中的每条引文拿回源文件核对，结果：

| 类别 | 条数 | 说明 |
|---|---|---|
| 完全精确命中 | 6,448 | 引文逐字出现在源文件 |
| 部分命中（跨排版断行） | 618 | 引文被 PDF 断行/分栏拆开 |
| 图内文字（无文本层） | 282 | 引文来自图片 artwork，只能靠看图获得 |
| 无法核对 | 932 | 多为 OCR 噪声或笔记转述 |
| **合计** | **8,280** | **有据率 88.7%** |

→ 🔴 **88.7% 的引文能在源文件中找到证据**；无法核对的 11.3% 主要是 OCR 噪声，
   笔记中已逐条标注 ⚠️。

## 十一、本文件的局限（必须如实说明）

1. **每刊通常只有 1–2 篇样本**，"按刊"结论只能视为该刊该篇的观察。
2. 12 篇为无文本层扫描件，**无法逐字读**，只能渲染页面看图。
3. 中文 PDF 文本层有损（部分数字与拉丁字符整体丢失），需靠渲染页核对。
4. 章节自动切分对俄文/老刊失效（sec_order 常为 _full），结构靠通读判断。
5. 引文回源校验的机器口径：**含 ≥12 个拉丁/西里尔字符的引文**才纳入核对；
   纯中文分析性描述不计入（避免把分析文字误当原文引文）。

## 十二、结论强度分级（诚实标注，重要）

不同结论的证据强度**差别很大**。为避免以偏概全，本文件所有结论按样本强度分三级：

| 级别 | 定义 | 用法 | 例子 |
|---|---|---|---|
| **A 级** | ≥30 篇样本，或跨 ≥10 个刊 | 可作为规律陈述 | 章节链五类骨架（164 篇）、摘要结构件出现率（38 篇英文摘要，跨多刊）、中文刊骨架（16+6 篇，跨 15+ 刊） |
| **B 级** | 10–29 篇样本 | 可作为倾向陈述，需注明样本量 | 引言 we 49%（45 篇）、关键词中位 8（62 篇）、标题中位 6.5 词（44 篇）、无独立 Discussion 65%（164 篇笔记计数） |
| **C 级** | **<10 篇样本，或单一刊系** | **只能作为「本样本中观察到」，不可写成刊规或领域规律** | 「Pal J 用 scale bar」（2–3 篇）、「Geol Carpathica 用 × magn.」（1 篇）、「Revue de micropaléontologie 用比例尺」（1 篇） |

### 12.1 样本的刊分布实况（机器审计）

- 主样本 174 篇笔记块中，可提取刊名 165 篇，**不同刊名 152 个**
- **只出现 1 次的刊名：143 个（94%）**；出现 ≥3 次的刊名仅 3 个
- → 🔴 **「某刊用 X」类的结论绝大多数只有 1 个样本支撑，属 C 级，不得写成该刊的规范。**

### 12.2 百分比结论的分母必须写明

本文件中所有百分比的分母都**远小于总样本 164 篇**：

| 结论 | 分母 | 说明 |
|---|---|---|
| 摘要结果打头 87% | **38 篇**英文摘要 | 中文刊是另一种骨架（§8.11.3） |
| 摘要被动 87% / 现在时 95% | **38 篇**英文摘要 | 同上 |
| 引言 we 49% | **45 篇**英文引言 | 119 篇无独立 INTRODUCTION 标题，未纳入 |
| 标题中位 6.5 词 | **44 篇** | 只占 164 篇的 27% |
| 关键词中位 8 | **62 篇** | 占 38% |
| 无独立 Discussion 65% | **164 篇笔记** | ⚠️ 关键词计数，非重读验证 |

→ 🔴 **引用这些百分比时，必须同时给出分母与语种/刊系限定。**

### 12.3 追加 10 篇的偏倚（必须声明）

§8.11 的中文刊结论基于追加的 6 篇中文论文，其中 **4 篇来自《微体古生物学报》同一本刊**
（李鑫 2020、吴浩若 2021、王玉净 2020、张杰 2020），另 2 篇分别来自《地学前缘》《地球科学》。
→ **§8.11 的「中文刊」结论实际是「以《微体古生物学报》为主、参校两刊」**，
  不能代表所有中文刊。主样本的中文刊分布较广（16 篇分散在十几个刊），可部分对冲这一偏倚，但仍需按刊定向补样。

### 12.4 追加样本非随机（必须声明）

追加 10 篇由人选定（非随机抽样），选择标准是「覆盖不同体裁」而非概率抽样。
→ 这 10 篇的价值在于**纠错与发现新模式**，**不能用于频率估计**。

### 12.5 哪些结论是站得住的

**A 级（可放心用）**：
- 章节链五类骨架（164 篇，152 刊）
- 中文刊与英文刊系统性地不同（主样本中文刊分散在多刊 + 追加样本双重证据）
- 图件按刊系分化（10 篇图件实看，跨 6 个刊系）

**C 级（必须限定后用）**：
- 任何「某刊用 X」的表述 → 改成「在本样本的 N 篇中观察到」或「某作者群/某 series 用 X」
- 所有百分比 → 必须带分母与语种限定



---

## 十三、第二批语料：AI/方法类地学论文（2026-11 新增，77 篇逐字精读）

> **本节是增量，不修改 §一~§十二 的任何内容。**
> 语料来源：`D:\文档\硕士\论文\artificial intelligence in taxonomical classification\参考文献`
> 共 225 篇 PDF（AI × 分类学专题），225/225 抽取成功，正文约 1650 万字符，**全英文**。
> 其中 **A 组 50 篇（化石/微体化石 + AI/ML）与 B 组 29 篇**逐字精读（77 篇，408 万字符，25 个分片，
> 每篇由独立子 Agent 用 read 读到文件末尾）；另 225 篇全部做机器层统计。
> **完整内容见新文件 `ai-ml-paper-patterns.md`。** 本节只给与 §一~§十二 的交叉点。

### 13.1 为什么要有第二批语料

§一~§十二 的 164 篇语料**全部是描述类系统学论文**（新种描述、属级修订），
**没有一篇是「用机器学习/深度学习做一项地学研究」的论文**。
因此 §二 的「章节链五类骨架」、§3.1 的「Methods 三档详略」、§八之十 的系统描述类专章
**都不能直接套到方法类论文上**。

### 13.2 跨语料的核心差异（同口径机器统计）

| 骨架件 | 描述类（n=164） | 方法类 A 组（n=50） |
|---|---|---|
| 有独立 Discussion 段 | 约 35%（65% 无） | **48%**（24/50） |
| 有独立 Conclusion 段 | 有（两种形态） | **52%**（26/50） |
| 有独立 Results 段 | 描述类**没有** | **46%**（23/50） |
| 有独立 Methods 段 | 三档详略 | **62%**（31/50） |
| 有独立 Systematic 段 | **描述类的核心** | **0%**（0/50） |
| 有 Repository 段 | 描述类必备 | **0%**（0/50） |
| 有 Geological setting 段 | 描述类几乎必选 | **0%**（0/50） |
| Data availability 段 | 未单列 | **54%**（27/50） |
| Code availability 段 | 无 | **24%**（12/50） |

→ 🔴 **两类骨架不可混用**：写「微体古生物 + AI」论文时不要套描述类的
「无独立 Results/Discussion、有 Repository/Geological setting」那套。

### 13.3 补上的空白：现代声明块（§八之三 的扩展）

§八之三 记录的现代期刊声明块来自 Elsevier 系样本。本批 225 篇给出了**跨刊系的实测频率**：

| 声明块 | A 组（n=50） | C 组（纯 AI, n=113） |
|---|---|---|
| Data availability | **54%**（27/50） | 28%（32/113） |
| Competing interest | 52%（26/50） | 21%（24/113） |
| Author contributions | 46%（23/50） | 23%（26/113） |
| Funding | 38%（19/50） | 27%（30/113） |
| Code availability | **24%**（12/50） | 5%（6/113） |
| AI 使用声明 | **0%**（0/50） | 1.8%（2/113） |

→ **化石类论文的 Code availability 出现率是纯 AI 论文的 4.5 倍**。
→ **AI 使用声明在 225 篇中几乎不存在**（仅 2 篇命中）——
  这批以 2024–2026 为主的论文**尚未普遍声明 AI 使用情况**。

### 13.4 本批语料的已知缺陷（随结论一起声明）

1. **文件名不可信**：`Beaufort_2004_coccolith_neural_net.pdf` 的正文实际是
   Boeckel & Baumann 2004（*Marine Micropaleontology* 51:301–320），
   全文**既无 Beaufort 也无 neural network**，用的是经典多元统计（DCA/CCA/聚类）。
   → **所有结论以正文实际作者/期刊为准，不以文件名为准。**
2. **全英文，零中文/俄文对照** → 不能直接套到中文刊（对照 §8.11）。
3. **专题偏倚**：225 篇由人选收集 → **不能用于任何频率推断**。
4. **A 组仅 50 篇** → 按 §12 分级，本批多数结论属 **B 级**；
   涉及单一刊/单一作者群的具体写法属 **C 级**。
5. **未开图**：本批只到「图注写了什么」，**不到「图画成什么样」**
   （与 `figure-conventions-evidence.md` 的 449 张实看不同）。
6. **引文回源用词袋判据**（双栏 PDF 抽取会打断行序，字符级连续匹配不可用）：
   661 条引文中 **0 条真实缺失**，99.70% 可验证。
   「逐字」指**词完整**，非字符级一致。
