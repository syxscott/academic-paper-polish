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

> **本节的依据（三层，逐层加深）**：
> ① **130 篇逐篇读段落骨架**（分层抽样；英文 110、中文 18、俄文 2）；
> ② 其中 **48 篇有可读的 Introduction、22 篇有可读的 Discussion**，逐段读；
> ③ **5 篇 Introduction 全文 + 1 篇 Discussion 全文 + RadSS 全文**通读。
> 🔴 **本节不给出任何"命中率"** —— 词频只能证明"某个词出现过"，
> 不能证明"作者在这里做了什么论证动作"。所有结论都附**逐字原文**供复核。
> ⚠️ **段数用缩进重建**，对无缩进排版（老扫描件、中文刊物）会偏大，故只作量级参考。

### 9.1 Introduction：**没有统一模板，实测九类目的句句式并存**

#### 9.1.1 目的句的九类句式（逐字，语料原句）

| # | 句式 | 逐字例句 |
|---|---|---|
| 1 | **The aim of this … is to** | "The aim of this study is to discuss the geologic age of the radiolarians and the possible origin of the chert pebbles in the Pondaung Formation…" |
| 2 | **The purpose of this … is to** | "The purpose of this paper is to examine skeletal ontogenesis in five species of the genus *Lamprocyrtis* Kling 1973…" |
| 3 | **The goal of this … is to** | "The goal of this paper is to consider this problem." |
| 4 | **Our objective / Our main objective …** | "Our objective in this work is to consider biostratigraphic zonations of Paleocene and Eocene sediments in western regions of Russia…" |
| 5 | **It is the purpose of this paper to**（老式） | "It is the purpose of this paper to report the unusually abundant, widely scattered, yet somewhat depth-restricted occurrences from this area." |
| 6 | **In this work / paper / contribution, we …** | "In this work we provide the first characterization of the sterols of *Z. nutricula*…" ／ "In this contribution, we report Guadalupian radiolarian and sponge spicule assemblages from the Gujingling Section…" |
| 7 | **We present here / Here we present / Here, we give** | "We present here the occurrence and probable mechanism of formation of volcanic magnetite spherules…" ／ "Here, we give the first description of the only known Jurassic hydrothermal vent fossils…" |
| 8 | 🔴 **Therefore, …（由前文推理得出目的）** | "**Therefore, in the present paper we recognize** the Cordevolian and Julian as separate and roughly equal substages of the Carnian stage." ／ "**Therefore, the objective of the present study is to propose a** …" |
| 9 | 🔴 **否定式：用"不做什么"划定边界** | "**The goal of this project has not been to attempt to formally revise the entire corpus of Cenozoic radiolarian taxonomy**, an enormous task for which we are neither fully qualified, nor have the resources to achieve." |

🔴 **可直接套用的三条硬规则**（从 130 篇读出来的）：
1. **目的句一定要带具体对象**（哪个层、哪个区、哪个类群、哪个数据集）——
   语料里没有一条目的句是空泛的 "to study radiolarians"
2. **目的句可以只是推导的落点**（句式 8）：先把推理铺好，再用 "Therefore" 引出本文主张，
   比开头宣告目的更像"论证"而不是"公告"
3. **目的句可以是否定式**（句式 9）：先声明本项目**不**做什么，往往比声明做什么更专业

**双目标 / 编号式目的句**（两类）：
> "**Our two main objectives were 1)** to document in a Caribbean land setting the late Paleocene changes already reported elsewhere …, **and 2)** to evaluate the potential of Cuban sections to serve as a Global Stratotype Section and Point (GSSP)…"（Aubry & Sanfilippo 1999）
> "**The aims of this synthesis are to** recover long-term paleoproductivity patterns and trends … **and to compare these two areas**."（Schumacher & Lazarus 2004）

**"已有工作 + 本文增量"式**（把本文定位成前作的延续）：
> "In addition to geochemical data, we present radiolarian biostratigraphic data, some paleomagnetic data, and Ar-Ar age analyses…"（Osozawa et al. 2012）
> "The purpose of this paper is to comment on the use of Radiolaria in dating deep-sea sediments and **to complement a recent review** of radiolarian palaeoenvironmental applications (Haslett, 2002)."（Haslett 2004）

#### 9.1.2 五种引言结构（每种附逐字原文）

**A 缺口→目的式**（新发现、系统描述最常见）—— Little et al. 1999 (*Geology*)，**引言只有一段**：
> "Although more than 50 modern vent fields with flourishing communities are known, the known fossil record of vent fauna is sparse: **only 19 occurrences in the entire Phanerozoic**—three from the Silurian, six from the Devonian, one from the Jurassic (described here)…"
> "**Consequently, the evolutionary history of these novel communities is not well understood.**"
> "**Here, we give the first description of** the only known Jurassic hydrothermal vent fossils… The Figueroa assemblage **fills a 270 m.y. gap** in the vent fossil record…"

🔴 **缺口用数量写出来**，随后用 "Consequently, … is not well understood" 收口，
**目的句 + 贡献句两句连排**（"目的 + 填补了什么 + 提供了什么认识"）。

**B 必要性论证式**（成因、沉积、全球变化类）—— Vashchenkova 2011 (*Marine Geology*)，**一整段无小标题**：
> "The study of the sedimentary processes in the continent–ocean transition zone is **one of the most important tasks of modern marine geology**."
> "…the origin of the pelitomorphic siliceous rocks … is **still debatable**."
> "**All these properties determine the necessity of the investigation of** siliceous sediments and their formation conditions."

🔴 **没有文献回顾段**，用"重要性 + 未决性 + 现实意义"三层把必要性堆出来。
🔴 这类论文常把 **Results 与 Discussion 合并**（段标题直接写 "RESULTS AND DISCUSSION"）。

**C 教科书铺陈式**（综述、术语解释、教科书章）：
> "Polycystine radiolarians are exclusively marine, pelagic, solitary or colonial protists provided with actinopods." → 形态解剖 → 分类 → 生态 → 繁殖，**逐段铺陈，无"缺口→目的"结构**。
> 🔴 这类章节的图引用写 **"(Figure 1A)"**（不带点），与期刊论文的 "(Fig. 1A)" 不同 —— **别照抄别处的格式**。

**D 材料发现式**（老刊、大剖面、地层工作）—— Fortey & Bruton 1973 (*GSA Bull.*)：
> ① "Fossiliferous lower Paleozoic rocks were **discovered in 1965** at the top of the Hecla Hoek Series in north Ny Friesland, Spitsbergen."
> ② "**This paper describes the succession and its field relations and discusses its correlation** within Spitsbergen and adjacent Arctic regions **preliminary to more detailed paleontologic work to be published in the future**."
> ③ 地质背景 + **坦陈材料局限**："The Cambrian rocks are, however, **incompletely exposed**, and are only present in the northern area; complete knowledge of this part of the section is unlikely."

🔴 **模式 D 有两个通用模板没有的好习惯**：预告后续论文；在引言里就写出材料局限。

**E 铺垫 → 目的 → 单独一段新意声明**（Robinson & Haslett 1995）：
> 铺垫三段后："Sponge spicules … are readily fossilized … making them a common component of marine sedimentary rocks throughout the Phanerozoic. **In this study, we report on** a siliceous microsclere assemblage from the mid-Early Miocene Dos Bocas Formation of Ecuador."
> 然后**另起一段**只写一句新意："**This assemblage is of particular interest as it comprises species previously unknown in the fossil record.**"

#### 9.1.3 引言长度的实测（48 篇可读）

| 指标 | 实测 |
|---|---|
| 段数 | **最少 2 段，最多 108 段**（中位约 43 段；⚠️ 缩进重建会偏大，仅作量级） |
| 短引言（2–6 段） | 多见于**数据报告、短通信**（如 ODP Data Report、引言仅 1–5 段） |
| 长引言（60+ 段） | 多见于**系统描述、综述、专著章节** |

🔴 **所以：本领域不存在"引言该写多长"的规范**，别套通用字数。

#### 9.1.4 缺口的四种写法（130 篇读出来的）

| 写法 | 逐字例句 |
|---|---|
| **数量化** | "only 19 occurrences in the entire Phanerozoic" |
| **未决性** | "the origin … is still debatable" ／ "remains one of the most intriguing problems in geology" |
| **具体未研究对象** | "the first attempt of Early Albian successions dating in northeastern Tunisia" |
| **技术/方法空白** | "The use of technology in biological classification has **not yet been given that much attention** by some specialists from different areas such as taxonomy, paleontology and morphological systematics."（RadSS 2016） |

### 9.2 Discussion：**起手与收尾各有多种，逐字给出**

#### 9.2.1 十一种起手（语料逐字）

| 起手 | 逐字例句 |
|---|---|
| ① **比较对象型** | "The sponge microsclere assemblages encountered in this study are **directly comparable with** Holocene reef sponge communities off the coast of Belize and in the Gulf of Mexico…" |
| ② **标志性种定年型** | "The occurrence of well-known species such as *Dictyomitra formosa*, *Diacanthocapsa euganea* … undoubtedly determine the Noni Formation as having an early Late Cretaceous age (Cenomanian–Turonian)." |
| ③ **结论先行型** | "Cretaceous accretionary–collision complexes in central Indonesia **were the products of the interaction of** a continent and an ocean." ／ "**Radiolaria were very strongly affected by the** Permian-Triassic biotic crisis." ／ "**We can identify two principal transitions** in the facies distribution of chert during the past 1000 Ma (Table 3)." |
| ④ **否定排除型** | "The cause of the Middle Carnian Wet Intermezzo **cannot be explained simply by** local changes in the climate in the Germanic Basin …, because tectonic changes …" |
| ⑤ **让步型** | "**Although** the unit origami system was for regular polyhedrons, **it could be used for** the modeling of cortical shell structures." |
| ⑥ **复述目的型**（现代刊常见） | "**This research aimed to** identify the sterols of *Z. nutricula* and to use these sterols to clarify the chemotaxonomic relatedness…" |
| ⑦ **子标题 + 综述铺陈型** | "Palaeogeographical settings and chronostratigraphical correlation of Chaohu, Meishan and Dongpan sections / The late Changxsingian rocks of South China can be subdivided into continental clastic facies …, carbonate platform …" |
| ⑧ **子标题 + "结合已发表数据"型** | "**Our assessment of the chemostratigraphy**, described in the geochemistry sections, **combines our data with previously published data sets to arrive at the conclusion that** our suite…" |
| ⑨ **数据 → 推断一句式** | "The studied radiolarian assemblage is early or early middle Albian in age and was collected approximately 15 m below the occurrence of keeled globotruncanids indicating a late middle Albian, or younger, age." |
| ⑩ **结果陈述型（最朴素）** | "Acantharian abundances were relatively low at the VERTEX seasonal station (33°N, 139°W)." |
| ⑪ **自承不完整型** | "The San Agustine and San Franciso de Paula sections **complement each other for a better -yet incomplete-** representation of the uppermost Paleocene-lower Eocene interval." |

🔴 **最值得抄的两种**：② **用标志性种把时代/环境钉死**（地层学论文的看家本领）；
④ **"cannot be explained simply by …, because …"**（先排除简单解释，再给机制）。

#### 9.2.2 Discussion 的核心动作：**逐项对照**，不是逐条罗列文献

Robinson & Haslett 1995 全文的骨架：
> ① 给比较对象 → ② 引已有工作并**按形态类型一项一项对**：
> "Haslett (1992) describes a microsclere assemblage from the Portlandian of southern England in which **reniform** microscleres … occur in association with **spherical** and **oval-cylindrical** microscleres … This Portlandian assemblage is very similar in composition with that of JW 199, in which reniform microscleres are represented by *Placospongia carinata*, **spherical microscleres by** *Geodia neptuni* and **the oval-cylindrical microscleres by** *Conciliaspongia rarus* Gen. et sp. nov."
> ③ 指出差异并收口："The assemblages **only differ by the absence** in the Jurassic assemblage of a stellate microsclere, such as *Chondrilla nucula* Schmidt."

🔴 **写法模板**：把本文的组合**按形态类型 / 属种逐项列出**，逐项对应已有组合，
最后用"只差 X"收口。**这是本领域讨论与通用 SCI 模板最大的差别。**

#### 9.2.3 七种收尾（语料逐字）

| 收尾 | 逐字例句 |
|---|---|
| ① **让步限定** | "However, some of these species occur in high latitudes where silica depletion is less pronounced than other regions of the oceans thus lessening the strength of the silica-depletion hypothesis as a major driving force in their evolution." |
| ② **需要进一步研究** | "More detailed research of the Gufeng Formation is needed for the proper understanding of rocks from the oceanic and platformal facies." ／ "To discuss this issue, further study is required to correct the fossil data…" |
| ③ **归因** | "The latter result is likely due to the high factor scores of *C. d. davisiana*, a species …" |
| ④ **地层 / 演化陈述** | "Arc magmatism continued well into Late Triassic time along the Sukhothai Terrane in Thailand until its collision with the Loei Terrane during Norian time." |
| ⑤ **审慎推测** | "**One might indeed speculate that** the decline of siliceous sponges in platform environments was a consequence of decreasing silica concentrations in surface ocean waters concomitant with the ecological expansion of planktonic diatoms…" |
| ⑥ **否定 / 限定收口** | "**Not all areas changed their tectonic setting, however,** as the oceanic plate stratigraphy indicates continuous subduction throughout the …" |
| ⑦ **结论重述** | "We conclude that the ability to deposit SrSO4 is a less reliable phylogenetic marker than the ability to construct elaborate skeletal architecture using SrSO4." |

🔴 **七种收尾没有一种是"未来展望 / future research will…"** ——
本领域讨论段的尾声是**限定、归因、推测或地质陈述**。

### 9.3 章节顺序与**中日文论文的章节对应词**

从 PDF 书签与 130 篇通读看到的顺序：

| 主题 | 典型顺序 |
|---|---|
| 系统描述 / 新类群 | INTRO → **GEO** → METH → **SYS**（逐类群并列小节）→ CONC（**无独立 Results 段**） |
| 地层 / 生物地层 | INTRO → **GEO** → METH → **对比** → CONC |
| 成因 / 定量 | INTRO → **GEO** → METH → **RES+DISC 合并** → CONC |
| 综述 / 教科书 | INTRO → 逐知识点铺陈 → CONC |
| **计算机方法类（RadSS 2016）** | **I. INTRODUCTION → II. RELATED WORK → III. RADIOLARIANS / MACHINE LEARNING AND FEATURE EXTRACTION（A. RaDSS Training App｜B. RaDSS Classifier App）→ RESULTS** |

🔴 **中文 / 日文论文的章节对应词**（语料里高频出现，写中文稿时别用错词）：

| 中文 / 日文 | 英文对应 | 说明 |
|---|---|---|
| 提要 | Abstract | 中文期刊摘要叫"提要" |
| 关键词 | Keywords | |
| はじめに / 引言 | Introduction | |
| **地質概説 / 地质概况** | **Geological setting** | 🔴 中文常叫"地质概况"，不是"地质背景" |
| 地层 | Stratigraphy | |
| 放散虫化石 / 放射虫化石 | Systematic description | 中文多直接写"放射虫化石" |
| **考察 / 討論** | **Discussion** | 🔴 中文用"考察" |
| まとめ / 結論 | Conclusions | |
| 参考文献 | References | |

🔴 **中文期刊论文常常没有"引言"这一节**——直接以"地质概况"起头，
写中文稿时不要硬套英文的 Introduction/Geological setting 两段式。

### 9.4 交稿前自查（结构部分）

- [ ] 引言首句是**事实**，不是"本文要研究 X"？
- [ ] 有**明确的目的句**，且带具体对象与产地？句式是否属于 §9.1.1 的九类之一？
- [ ] 目的句**独立成句**，且后面另有段落说明"为什么值得看"？
- [ ] 缺口是**数量化 / 未决性 / 具体未研究对象 / 方法空白**四种之一？
- [ ] 有 **Geological setting（地质概况）**，且排在 **Methods 之前**？
- [ ] 系统描述类：每个类群一个**并列小节**（Holotype→Paratype→Description→Discussion），**且没有独立 Results 段**？
- [ ] 讨论是**逐项对照**（按形态类型/属种一项一项比），而不是逐条罗列文献？
- [ ] 讨论里**标志性种**用来锁定时代/环境？
- [ ] 推论与证据之间是 **"Because …, we propose that …"** 的显式焊合？
- [ ] 讨论收尾是**让步 / 需进一步研究 / 归因 / 审慎推测 / 地层陈述 / 否定限定 / 结论重述**之一，而不是"未来展望"？
- [ ] 材料或数据局限**在引言里就坦陈**？
- [ ] **中文稿**：章节名用"提要 / 地质概况 / 放射虫化石 / 考察"这些对应词了吗？
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
