# 微体古生物 / 放射虫论文的写作与制图模式

> **本文件解决什么问题**：`figure-design-system.md` 讲**通用**图件设计（版式、原型、语义色）；
> `multi-journal-style-guides.md` 讲**各刊官方格式条款**。
> 本文件讲第三件事：**这个领域（微体古生物 / 放射虫）的论文实际长什么样** ——
> 章节怎么排、图叫 Fig. 还是 Plate.、图是彩色的还是灰度的、图注怎么写。
>
> **取样口径**：本地语料库 `D:/数据集/PDF_Radiolaria`（**8162 篇 PDF / 62 GB / 33 个子目录**）。
> - 全库按子目录**比例分层抽样 319 篇**（每层 3–14 篇，固定随机种子 20261101）
> - 其中 **272 篇有可用文本层**（**47 篇为纯扫描件**，无文本层，已剔除出统计）
> - 共解析出 **1139 条图注**；另抽 **40 篇的 376 张嵌入图**做配色统计
> - ⚠️ **口径限制（先读这段再用下面的数字）**：
>   「提及 Fig / Plate」是**文本层词频近似**，不等于严格的图件计数；
>   「有摘要 / 关键词 / 参考文献」只统计**前 30 页**文本中是否出现该词，是**下限估计**；
>   配色统计只覆盖**嵌入位图**，纯矢量图（老刊常见）未被计入。
>   **下面每条结论都标注了样本量与口径，不要把它当成全库普查。**

---

## 一、🔴 四种主题的论文骨架

按语料实际写法，**微体古生物论文分成四类，骨架互不相同**。把综述稿写成系统描述稿，
或把系统描述稿写成数据稿，是这个领域最常见的结构性错误。

| 主题 | 语料中的识别特征 | 典型章节序列（按出现频率排序） |
|---|---|---|
| **A 分类 / 系统描述** | 出现 Systematic description / Taxonomy / Holotype / n. sp. / gen. nov. | Geological setting → Material and methods → **Systematic descriptions（每个分类单元一个并列小节）** → Conclusions → References |
| **B 生物地层 / 带对比** | Zonation / biozone / range chart | Introduction → Geological setting → Material and methods → **Regional geology** → **Radiolarian biostratigraphy（对比表 + 图）** → Conclusions |
| **C 定量 / 古生态** | abundance / diversity / isotope / geochemistry | Introduction → Geological setting → Samples and methods → Results → Discussion → Conclusions |
| **D 综述 / 专著** | review / overview / monograph | Introduction → 各专题章节 → Conclusions → References |

**英文章节标题在 272 篇中的出现频度**（逐字统计）：

| 标题 | 出现篇数 | 占比 |
|---|---|---|
| Introduction | 32 | 12% |
| Conclusions | 17 | 6% |
| Discussion | 17 | 6% |
| Results | 12 | 4% |
| Materials and methods | 7 | 3% |
| Geological setting | 5 | 2% |
| Profile descriptions / Systematic descriptions | 4 / 2 | 各 1% |

⚠️ **这些百分比偏低是有原因的**：许多老论文用 "Summary" 代替 "Abstract"、
用 "Paleogeography" / "Geology" 等自定义标题，且部分为扫描件未被计入。
**能读出来的章节标题里，"Introduction / Conclusions / Discussion" 稳居前三** ——
这个排序本身是可靠的；单个标题的绝对占比则不可靠。

### 🔴 A 类（系统描述）的关键结构特征

在语料里反复出现**同一层级的并列小节**，而不是把描述塞进一个大段落：

- 每个分类单元一个独立小节；小节内固定四段式：
  **Holotype（正模）→ Paratype（副模）→ Description（描述）→ Discussion（讨论）**
- 小节标题直接用**分类单元名**（属名 + 种名，斜体），不写"描述"二字
- 分类学记号固定为 `gen. nov.` / `sp. nov.` / `n. sp.` / `aff.` / `cf.` / `ex gr.`

🔴 **可直接照抄的英文骨架（语料原句）**：

> "Material and methods — In accordance with the recommendations of the International Codes of Zoological Nomenclature (ICZN) … all illustrated and described fossils should be deposited in an appropriate museum or collection …"

> "Research Articles — Research Articles present original, analytical results in any area of paleobiology. These should be timely, relevant, and of broad interest."

---

## 二、🔴 图件范式：Fig. 制 vs 图版（Plate）制

**这是本领域最需要先定的一件事**，因为它决定后面所有排版。

| 范式 | 语料中的论文占比（272 篇有文本层） | 适用 |
|---|---|---|
| **Fig. / Figure 常规图** | **194 篇 = 71%** | 绝大多数论文（数据图、地图、示意图） |
| **Plate. / 图版** | **51 篇 = 19%** | 系统描述类（化石照片版） |
| **两者兼有** | **49 篇 = 18%** | 系统描述 + 数据图的完整研究 |

🔴 **判据**：**要展示"某个分类单元长什么样" → 用图版（Plate）**；
**要展示"分布 / 关系 / 趋势" → 用 Fig.**。系统描述论文几乎一定两者都有。

### 2.1 图注前缀的实际分布（1139 条图注，逐字统计）

| 前缀 | 条数 | 占比 |
|---|---|---|
| `Fig.` | 765 | **67%** |
| `Figure` | 227 | 20% |
| `FIG.` | 45 | 4% |
| `Plate` | 40 | 4% |
| `Рис.`（俄文） | 29 | 3% |
| `图`（中文） | 11 | 1% |
| `図`（日文） | 5 | <1% |

🔴 **首选 "Fig."（带点、缩写）**：67% vs 20% 的差距说明这不是风格偏好，而是领域惯例。
写 "Figure 1." 不会错，但若要贴合本领域习惯，用 **"Fig. 1."**。

### 2.2 面板字母体系（语料原句逐字）

> "Figure 1A. Main features of a polycystine spumellarian cell. Slightly modified from Kling …"
> "Figure 2A. Characters used for the identification of spumellarian radiolarians. From Haeckel …"
> "Figure 2F. Characters used for the identification of spumellarian radiolarians. Original."
> "Figure 2N-S. Characters used for the identification of spumellarian radiolarians. M, P, Q: …"
> "Plate 3, figures K and L; plate 4, figures C, D, F, G, K, L; plate 5, …"
> "Figure 1C-E. General view of entire radiolarian colonies. C, D: by courtesy of Neil Swanberg …"

🔴 **可直接复用的四条写法**：
1. **面板用大写字母 + 连字符区间**："Figure 2N-S."（不是 2N–S，也不是 N to S）
2. **每个面板单独成图注**："Figure 1A." / "Figure 1B." / "Figure 1C-E." —— 不是把一整版写成一个长图注
3. **图版跨页引用写成清单**："Plate 3, figures K and L; plate 4, figures C, D, F, G, K, L"
4. **正文用面板级引用**："(Fig. 2C and D)"、"(Fig. 3B)" —— 不是笼统的"Fig. 3"

### 2.3 🔴 图注里的来源声明（本领域特有）

语料中系统描述与示意图图注常带**来源句**，这是版权合规的天然落点：

> "… Slightly modified from Kling …"
> "… From Haeckel …"
> "… Original."
> "Fig. 1. Schematic classification of Radiolaria based on ribosomal genes (18S and 28S rDNA) modified from Sandin (2019). Non-supported nodes are reported by a surrounded question mark."

🔴 **借用的图必须在图注里写来源**："From X"（直接引用）/ "Slightly modified from X"（轻微改动）/
"modified from X (year)"（改造）/ "Original."（自绘）。**这与 skill 的版权红线是同一条规则**，
本领域把它落到了图注里执行。

---

## 三、🔴 色彩风格：灰度优先，形状承担分组

**实测：40 篇抽样的 376 张嵌入图中，349 张（93%）近灰度，仅 7% 为彩色；
图内平均饱和度中位数 = 0.000（即绝大多数图完全没有彩色信息）。**

这不是"做得糙"，而是这个领域的**信息载体不是颜色**：

| 编码任务 | 语料中的实际做法 |
|---|---|
| 区分组别 | **形状**：● / ▲ / ■ / ◆；或**灰度深浅**；或**黑白花纹填充** |
| 区分地质体 | **花纹（hatching）**：点、斜线、实心深灰 |
| 突出某一条线 | **线型**：实线 / 虚线 + 线宽 |
| 范围包络 | **凸包轮廓线**（白色细线，不填色） |

🔴 **所以在微体古生物论文里，"同一颜色 = 同一组"这条规则要改写成**
**"同一形状 + 同一灰度 = 同一组"** —— 这正是 §二 中
`color-system.md` 说的"一通道一变量"：轴和位置已经用掉信息，
形状与灰度才是剩下的通道。

### 3.1 彩色出现在哪里

彩色只在两类图里出现，且都是**系统发育 / 现代生态**这类新刊论文：

- **系统发育树**：末端三角按类群分色（见 §三.2 的 Biard 2022 范例）
- **现代生态统计图**：多样性、丰度、nMDS 等

🔴 **因此：写一篇放射虫化石系统描述论文（1990–2020 年代风格），
不要用彩色配色表；写一篇现代海洋放射虫多样性论文，可以。**
**先定体裁，再定色。**

### 3.2 彩色系统树的三个可抄细节（Biard et al. 2022, *Environ Microbiol*）

1. **外群用灰色横条**（"Phaeodaria"），一眼看出哪支是外
2. **类群分组用灰色圆角框**，框右上角写类群名（Taxopodia / Spumellaria / Nassellaria / Orcadiaria / Collodaria）
3. **不支持的节点标 "?"**，并在图注里说明："Non-supported nodes are reported by a surrounded question mark."

🔴 **图注要解释图里的符号约定**，这是现代刊的硬要求：
读者不看方法部分也能读懂"?"、灰条、彩色三角各代表什么。

---

## 四、🔴 地图与地质图：灰度花纹 + 插图 + 比例尺

语料中的标准地质图版式（以 Aitchison et al. 1999, *Micropaleontology* 45(2) 的 TEXT-FIGURE 1 为范例）：

- **图号写成 "TEXT-FIGURE 1."**（Micropaleontology / SEPM 系的刊式，与普通 "Fig." 不同）
- **主图 + 右上角插图定位图**（inset locator map），标注研究区在更大区域中的位置
- **指北针 + 比例尺**（"0 — 50 km"），比例尺放在图内而非图注
- **经纬度刻度**直接标在图框上（30°、31°、32°、151°、152°、153°E）
- **地质体用黑白花纹**：点填充、斜线填充、实心深灰
- **图例按构造单元分块**："TAMWORTH BELT" 和 "HASTINGS BLOCK" 各一块，而非一张大图例
- **样点直接标在图上**（"Significant radiolarian localities are also indicated"）

> **原文（逐字）**："TEXT-FIGURE 1. Simplified tectonostratigraphic map of the southern New England orogen, eastern Australia showing the areal distribution of rocks assigned to the Gamilaroi terrane. Significant radiolarian localities are also indicated."

🔴 **图注的第一句要说明"这张图传达什么"，不是"这张图画了什么"** ——
这是 Micropaleontology 的原文要求，也是 skill 版权/可读性规则在本领域的落地。

---

## 五、🔴 标本图版（Plate）的制图要求

语料中系统描述论文的图版（Plate）遵守：

- **黑底或纯白底**，标本颜色即数据，不加任何色偏（与 `color-system.md` 的化石照片条款一致）
- **每个视图单独编号**（A、A1、A2、A3…），同一标本的多个视图用**同一字母 + 数字下标**
- **比例尺用数字线段**，常与图注里的放大倍数并存
  （语料实测：1139 条图注中"含放大倍数" 1.5%、"含 scale bar" 1.2%、"含 μm/mm 数值" 1.2%，
  但**这 1% 多是数据图**，图版类图注的比例尺信息多以 "Plate N" + 正文说明形式出现）
- **图注必含分类学记号**（语料实测 1139 条图注中 **7.4%** 含 `gen.` / `sp.` / `n. sp.` / `aff.` / `cf.` / `ex gr.`）

> **原文（逐字）**："Letters on figures (A, B, C, etc.) should run consecutively from left to right and from top to bottom. If more than one specimen is illustrated in a figure, label all views of the same specimen with the same letter with numerical subscripts (A1, A2, A3, etc.)."

---

## 六、🔴 前置要素：这个领域的老刊与新刊差别很大

272 篇有文本层中的英文子集（N=179），前 30 页内出现相应字段的篇数：

| 字段 | 出现篇数 | 占比（下限） |
|---|---|---|
| References | 118 | **66%** |
| Abstract | 95 | 53% |
| Acknowledgements | 94 | 53% |
| Keywords | 41 | **23%** |

🔴 **关键判断**：
- **摘要与致谢**在这个领域是**未必有**的（老刊常无 Abstract；俄文/中文刊另有格式），
  **不要按"通用 SCI 模板"硬套**——先查目标刊（见 `multi-journal-style-guides.md`）
- **Keywords 出现率最低（23%）**：放射虫系统描述类论文普遍不列关键词
  （因为检索靠分类单元名与图版），**加关键词不是硬性要求，但加了不违规**
- 🔴 **因此本领域的"摘要/关键词缺失"不能一律判为格式错误** ——
  这与 `journal-constraints.md` 的通用规则存在张力，**以目标刊官方要求为准**

---

## 七、交稿前自查（微体古生物 / 放射虫专用）

- [ ] 图号用的是 **"Fig."** 而不是 "Figure"？（本领域 67% 用前者）
- [ ] 展示分类单元形态 → 用 **图版 Plate**；展示分布/关系 → 用 **Fig.**（两者可兼有）
- [ ] 图是**灰度**的吗？分组用**形状/灰度/花纹**而不是颜色？（语料 93% 灰度）
- [ ] 每个面板单独一条图注，用 **"Figure 1A." / "Figure 2N-S."** 的写法？
- [ ] 正文用**面板级引用**："(Fig. 2C and D)"？
- [ ] 借用/改造的图，在**图注里写了来源**（From X / modified from X (year) / Original.）？
- [ ] 图版里同一标本的多个视图用**同一字母 + 数字下标**？
- [ ] 地质图有**比例尺 + 指北针 + 插图定位图**，地质体用**黑白花纹**？
- [ ] 图注第一句讲**这张图传达什么**（the message），不是只描述内容？
- [ ] 系统描述是 **Holotype → Paratype → Description → Discussion** 四段式？
- [ ] 分类单元名用**斜体**，新分类单元带 `gen. nov.` / `sp. nov.` 记号？
- [ ] 标本已按 **ICZN** 存入公开藏馆，收藏号已写明？
- [ ] 目标刊是否真的要求 Abstract / Keywords？（本领域 23%–53% 的实际情况）

---

## 九、🔴 论文整体结构：Introduction 怎么写、Discussion 怎么讨论

> **取样口径**：同一分层抽样（224 篇）里，**Introduction 抽到 50 篇、Discussion 20 篇、Conclusions 13 篇**，
> 三者齐备仅 5 篇 —— 因为老论文常把 Discussion 与 Conclusions 合并，或把讨论拆进各小节。
> ⚠️ **抽取用"标题样式行"作为段落边界**，遇到下一个标题样式行即停止，
> 因此**正文可能被截短** → 下表中"文献回顾"与"转折词"偏高、**"提出目的"偏低**。
> **逐字例句不受此影响**，可直接引用。

### 9.1 Introduction 的实际写法：**先事实，后目的**

**首句几乎从不直接说"本文做了什么"**，而是先给一个领域事实或材料事实：

> "Modern hydrothermal vent sites support communities of animals whose primary producers are chemoautotrophic bacteria that oxidize reduced sulfur compounds from the vent fluid as the primary energy source (e.g., Van Dover, 1995; Grassle, 1986)."
> "The study of the sedimentary processes in the continent–ocean transition zone is one of the most important tasks of modern marine geology."
> "Polycystine radiolarians are exclusively marine, pelagic, solitary or colonial protists provided with actinopods."
> "Fossiliferous lower Paleozoic rocks were discovered in 1965 at the top of the Hecla Hoek Series in north Ny Friesland, Spitsbergen."

**只有少数论文首句即目的句**：
> "This study examines the radiolarian assemblages from cherts intercalated in two carbonate successions exposed in the Karma and Fushe Lura areas (Fig. 1), Northern Albania."

🔴 **本领域的 Introduction 实际骨架（四段）**：
① **领域事实 / 材料事实**（"放射虫是什么"、"这些岩层何时何地发现"）
→ ② **已有研究的状况**（含引用密集段）
→ ③ **缺口 / 转折**（"however…"）
→ ④ **本文目的句**（目的句**通常在 Introduction 的后半段**，不是第一句）

**各动作命中率（Introduction, N=50）**：

| 论证动作 | 命中率 | 解读 |
|---|---|---|
| 文献回顾 | 52% | 引言主体是文献，不是我 |
| 转折词（however/but/yet） | 54% | 转折句几乎必有一处 —— 缺口靠转折句点出 |
| 提出目的 / 研究动作 | 26%（**偏低，因抽取截断**） | 目的句用固定句式，见下 |
| 知识缺口（remains unclear 等） | 14% | 本领域**不用**"remains unclear"这套说辞，改用**具体地层/材料的未知性** |
| 范围限定（here / this study…） | 16% | 同上 |

🔴 **"知识缺口"只有 14%**：这个领域不写"X 至今仍不清楚"，而写
**"某个地层单元的放射虫组合还没有被系统研究过"** —— 缺口是**具体的**（哪个层、哪个区、哪个类群）。

**目的句的标准句式（逐字，语料原句）**：

> "The aim of this note is to present new biostratigraphical data that define a more precise age of the Simoni Mélange, dating a cherty-silty level found at the top of the Kalur Cherts near the Lumi i Zi (northern Albania)."
> "The purpose of this paper is to examine skeletal ontogenesis in five species of the genus *Lamprocyrtis* Kling 1973, and the latter is present."
> "In the present paper we describe another structurally intermediate group between Nassellaria and Entactinaria."
> "The purpose of this project was to better constrain the early history of the WPWP and to consider this history in the context of the equatorial current system and tropical climate during the late Miocene."
> "The aim of this study is to discuss the geologic age of the radiolarians and the possible origin of the chert pebbles in the Pondaung Formation, in addition to the systematic …"
> "In this paper, we present some newly discovered Early Jurassic (late Pliensbachian) radiolarian data from the Luoqu Section near Luoqu Village, Xigaze, in southern Tibet (Fig. 2)."

🔴 **可直接套用的三种目的句模板**：
- `The aim of this study is to <动词> …`
- `The purpose of this paper is to <动词> …`
- `In this paper, we present <新数据/新类群> from <具体产地> (Fig. N).`

**注意**：目的句里**必须带具体对象**（哪个地层、哪个区、哪个类群），
不能写 "to study radiolarians" 这种空话 —— 这是本领域目的句的硬特征。

### 9.2 Discussion 的实际写法：**不是摘要复读，是"用文献校准自己的解释"**

**Discussion 首句的三种常见起手（逐字）**：

| 起手类型 | 逐字例句 |
|---|---|
| **A 直接与已有工作对表** | "The sponge microsclere assemblages encountered in this study are directly comparable with Holocene reef sponge communities off the coast of Belize and in the Gulf of Mexico, and with an Upper Jurassic microsclere assemblage." |
| **B 用结果锁定时代/环境** | "The occurrence of well-known species such as *Dictyomitra formosa*, *Diacanthocapsa euganea*, *Stichomitra communis*, *Cryptamphorella conara*, together with *Guttacapsa biacuta* and *Praeconoaryomma lipmanea* undoubtedly determine the Noni Formation as having an early Late Cretaceous age (Cenomanian–Turonian)." |
| **C 先摆领域通说，再切入本文** | "The isotopic paleoecologics of planktonic foraminifera can be used to gain insight into the dynamics of stratification in the upper water column." |

🔴 **Discussion 首句不是"本文发现…"** —— 这是与通用 SCI 模板最大的差别。
通用模板教你在 Discussion 开头重述结果；**本领域的老论文不这么做**，
而是**先把领域共识摆出来，再让本文数据进入这个框架**。

**各论证动作命中率（Discussion, N=20）**：

| 论证动作 | 命中率 | 解读 |
|---|---|---|
| 机制解释（because / due to / likely） | 35% | 讨论的主体是**因果解释** |
| 启示 / 外推（suggest / may explain） | 35% | 与机制解释并列，构成讨论主体 |
| 与文献比较（in contrast / consistent with） | 15% | 有比较，但**不是逐句对照** |
| 重述本文结果（our results / we show） | 10% | **很低** —— 讨论不复读摘要 |
| 局限 / 不确定（limitation / further work） | 10% | 老论文常以"需要进一步研究"收尾 |

🔴 **Discussion 的三段式（语料实际形态）**：
① **本文数据落到哪个已知解释上**（年代 / 沉积环境 / 演化压力）
② **这个解释为什么成立**（机制、证据、与某某文献一致或不一致）
③ **还剩什么问题没解决**（以"需要进一步研究"或"某某研究不足"收尾）

**三种收尾句式（逐字）**：

| 收尾类型 | 逐字例句 |
|---|---|
| **A 让步 + 限定结论** | "However, some of these species occur in high latitudes where silica depletion is less pronounced than other regions of the oceans thus lessening the strength of the silica-depletion hypothesis as a major driving force in their evolution." |
| **B 明确指出后续工作** | "More detailed research of the Gufeng Formation is needed for the proper understanding of rocks from the oceanic and platformal facies." |
| **C 以地层/类群结论收尾** | "The lower part of the Formation includes radiolarians belonging to the *Pseudoalbaillella longtanensis-Ps. fusiformis* Assemblage, and the upper part of the Formation includes radiolarians belonging to the *Follicucullus scholasticus* …" |

🔴 **Conclusions 的收尾**也常是 **B 或 C**，而不是"未来展望"——
**本领域的结论段常以"地层归属 / 组合归属 / 需要进一步研究"结束**。

### 9.3 章节顺序（按 PDF 书签统计，224 篇）

高频序列（前 12 条中占比最高者）：

| 序列 | 出现 |
|---|---|
| INTRO → GEO → METH → SYS | 2 |
| INTRO → GEO → METH → DISC → CONC | 1 |
| INTRO → METH → RES → RES | 1 |
| INTRO → GEO → METH → GEO → CONC | 1 |

🔴 **本领域的四类骨架**（与 §一 一致，此处给出**顺序**）：

| 主题 | 章节顺序 |
|---|---|
| 分类 / 系统描述 | INTRO → GEO → METH → **SYS（每个类群一个并列小节）** → CONC |
| 生物地层 | INTRO → GEO → METH → **GEO（地层与对比）** → CONC |
| 定量 / 古生态 | INTRO → GEO → METH → **RES** → DISC → CONC |
| 综述 / 专著 | INTRO → 各专题章节 → CONC |

🔴 **两条与通用 SCI 模板不同的硬事实**：
1. **"Geological setting" 几乎是必选项**（INTRO → GEO 出现最频繁）——
   地层/区域背景**放在方法之前**，因为"这套放射虫来自哪个层、哪个区"决定了后面一切
2. **系统描述类论文没有独立的 "Results" 段** —— 结果直接以
   "Systematic descriptions" 里的**逐类群描述**呈现

### 9.4 交稿前自查（结构部分）

- [ ] Introduction **首句是事实，不是"本文做了什么"**？
- [ ] Introduction 里**有明确的转折句**点出缺口（however / but / yet）？
- [ ] 缺口是**具体的**（哪个地层 / 哪个区 / 哪个类群），不是 "remains unclear"？
- [ ] **目的句在引言后半段**，且用 "The aim/purpose of this …" / "In this paper, we present …"？
- [ ] 目的句里**带具体对象与产地**（可带 Fig. 交叉引用）？
- [ ] 有 **Geological setting** 段，且排在 **Methods 之前**？
- [ ] 系统描述类：每个类群一个**并列小节**，四段式（Holotype→Paratype→Description→Discussion）？
- [ ] 系统描述类：**没有独立的 Results 段**？
- [ ] Discussion **首句不是复读摘要**，而是领域共识 / 对表 / 结果定年？
- [ ] Discussion 主体是**机制解释 + 启示**（各约 35%），不是逐句文献对照？
- [ ] Discussion 收尾是**让步限定 / 需要进一步研究 / 地层结论**三者之一？
- [ ] Introduction 与 Discussion 之间**没有重复的句子**？

## 八、来源与可回查

| 来源 | 提供什么 |
|---|---|
| 本地语料 `D:/数据集/PDF_Radiolaria`（8162 篇） | 全部比例数字、1139 条图注、376 张图的配色统计 |
| Aitchison et al. 1999, *Micropaleontology* 45(2): 138–162 | TEXT-FIGURE 制式、黑白花纹地质图、插图定位图、图例分块 |
| Basílio-Dantas et al. 2019 | 灰度环形图与 nMDS：形状编码 + 凸包轮廓 + 图例框 |
| Biard et al. 2022, *Environ Microbiol* | 彩色系统树（灰条外群 / 灰色分组框 / "?" 不支持节点）、Box 1 侧栏、面板级引用 |
| Adl et al. 2019, *J. Eukaryot Microbiol.* | 分类学论文把"分类"写成**编号命题**（(1)…(7)）的写法 |
| APP `instruction.html`、PE `contributor instructions`（见 `multi-journal-style-guides.md`） | 图注必含 authority/date/age/locality；文件名 ISO 9660 |

⚠️ **Micropaleontology 的官方作者指南页受 cookie 墙拦截**，本文件关于该刊的证据
全部来自**已刊论文本身**（属一手出版物证据），**不是官方指南原文**；
引用其格式条款前请回官方页确认。
