# Paleobiology 期刊投稿规范（图件 + 文体）

> **来源**：`PABfigure-guide.pdf`（Electronic Figure Guidelines，最后更新 2026-03-05）+ `PAB-Paleobiology-style-guide.pdf`
> **目标刊**：*Paleobiology*（Cambridge University Press，ScholarOne 投稿系统，paleobiology@cambridge.org）
> **对放射虫化石图像提取论文直接适用** —— 其中「标本照相要求」「比例尺强制」「不可改动照片」三条就是为化石形态学研究写的。

---

## 一、图件规范（Electronic Figure Guidelines）

### 1.1 两套要求：送审 vs 出版

**最容易搞混的一点：送审和终稿的图件要求完全不同。**

| | **Figures for Review**（送审） | **Figures for Production**（录用后终稿） |
|---|---|---|
| DPI | **无要求**，但必须"可供同行审阅" | **按图件类型有硬性下限**（见 1.3） |
| 格式 | 任意（.jpg .tif .eps .pdf 等） | 任意（.jpg .tif .eps .pdf 等），**❌ 不收 .doc 图** |
| 文件大小 | 🔴 **必须 <40 兆像素**（宽×高 < 40,000,000 px）才能生成 PDF proof | 任意大小，**不需要出现在 PDF proof** |
| 文件名 | 至少含图号，如 `Figure_1.tif` | 图号 + **单栏/双栏**，如 `Fig1_2col.tif` |
| 图注 | 所有文件类型都会显示，**但 .pdf 和 .doc 除外** | — |

> ⚠️ 送审阶段 40 MP 上限是硬性的。 ScholarOne 上传后、正式提交前，**务必检查 proof 里的图是否正常转换且可供审阅**。
> 录用后的大文件上传慢、上传后可能"未转换"，这是正常现象，最终会转给 Production。有问题发 paleobiology@cambridge.org。

### 1.2 图件尺寸（Cambridge 生产规范）

| 版面 | 宽度 | 最大高度 |
|---|---|---|
| **单栏 1 column** | **9 cm** | 24 cm |
| **双栏 2 columns** | **18 cm** | 24 cm |
| 横版 landscape | 反向（宽高互换） | 同样上限 |

### 1.3 🔴 DPI 硬性要求（按图件类型分）

| 类型 | 定义 | 色彩模式 | **分辨率** | 范例 |
|---|---|---|---|---|
| **Line Artwork**<br>线条图 | 黑白或彩色图形，**无精细明暗** | 1-bit 黑白 或 CMYK | 🔴 **1200 dpi** | 线图、柱状图、色块地图、点画图 |
| **Combination Artwork**<br>组合图 | 半调（halftone）+ 线绘 + 大量文字 + 阴影图 | Grayscale(8-bit) 或 CMYK | 🔴 **800 dpi** | 照片/艺术图 + 大量标注或线条 |
| **Halftone Artwork**<br>半调图 | 照片或艺术图，**有精细明暗** | Grayscale(8-bit) 或 CMYK | 🔴 **600 dpi** | 彩色/黑白照片、精细明暗艺术图 |

**线宽（Line Artwork）**
- 🔴 **所有线条至少 0.11 mm（0.3 pt）宽**
- **突出线条**（如图表主线）**0.75–1.0 pt（0.25–0.35 mm）**

**栅格 vs 矢量**
- **栅格图**（.tif .png .jpg）→ 有 dpi 要求，且 **dpi 受栏宽影响**，必须在目标栏宽下满足
- **矢量图**（.eps .pdf .ai）→ 无 dpi 要求，任意尺寸无损
- 🔴 **矢量图含字体时必须嵌入字体**

### 1.4 🔴 大图拆分（Split Figures）

图可拆成两个或多个文件，分别在不同页出版（如把大图拆成两半，各按双栏宽出版）。
🔴 **拆分后的每个文件都必须单独满足图件要求。**

### 1.5 🔴 大文件压缩

生产用的全分辨率大图，**保存时用 LZW 压缩** —— 减小文件体积（有时显著）且**不影响质量、可逆**。
操作路径：图形软件（如 Photoshop）→ `Save as` → 选 TIFF → 保存 → 下一窗口选 LZW。
IrfanView 是免费的 PC 端图形程序，可做 LZW 压缩。

### 1.6 🔴 标本照相要求（★ 化石形态学论文直接适用）

| 项 | 要求 |
|---|---|
| **Alterations 改动** | 🔴 **照片不得改动**，除非色调、对比度、以及添加要素标注或轮廓线 |
| **Lighting 光照** | **从左上斜向照射**标本，除非是原位（in situ）拍摄 |
| **Orientation 朝向** | 按该分类群的**标准惯例**摆放标本 |
| **Key Features 关键特征** | 🔴 **确保关键特征清晰可见** |
| **Scale Bars 比例尺** | 🔴 **标本照片必须带比例尺**。野外照可用标尺或已知尺寸物体。**比例尺尺寸的数值说明**须随比例尺或在图注中给出 |

> 🔴 **不可用放大倍数（如 ×40）代替比例尺** —— 因为终版印刷时图可能被缩放。
>
> 🔴 **比例尺粗细须统一。**

**地图与地层柱状图**：必须包含尺度感，如比例尺或纬度/经度。

### 1.7 图内标注、字体、色彩

| 项 | 要求 |
|---|---|
| **Subfigures 子图标签** | **大写字母 A、B、C…**，置于每张图的**左上或右上角** |
| **字体** | **无衬线**（sans serif，如 Arial）；同类型图（如图表）**字号与样式须一致**；须可读 |
| 🔴 **字号下限** | **8 pt（终版尺寸）** |
| 🔴 **线宽下限** | **0.3 pt（0.11 mm）** |
| 大写 | 图内文字用**大小写混排**，不要全大写；**不要用粗体** |
| 🔴 **字体嵌入** | 为确保出版图与提交稿一致，**必须嵌入字体** |

> 🔴 **校对阶段若图内文字不放大就看不清，proof 会被中止并要求重新提交图件。**

### 1.8 🔴 色彩避坑

当色彩差异是理解图的关键因素时（如图表），**避免以下颜色对**：
**红/蓝 · 红/绿 · 蓝/绿 · 蓝/黄**

### 1.9 🔴 图注（Caption）

- **电报体**（telegraphic style）解释图
- 🔴 **所有子图与图中使用的缩写都必须在图注中解释**
- 在多个图中使用的缩写，**须在每张图的图注中解释**，或引用已解释的图注
- 🔴 **生成该图所用的方法必须在图注中说明**（公式、假设、正文引用等）

### 1.10 实用提示

- 🔴 **在原生软件中直接生成/转换为目标 dpi**（Photoshop psd、Illustrator ai、Coreldraw cdr、Corel PhotoPaint cpt）
- 🔴 **不要**把低分辨率图（如 300 dpi）**重采样/升采样**到高分辨率（如 600 dpi）—— 不会提升真实质量
- 检查 proof：上传后、提交前

---

## 二、文体规范（Style Guide）

### 2.1 总纲

- 遵循 **《芝加哥格式手册》**（The Chicago Manual of Style）http://www.chicagomanualofstyle.org/
- 地质年代遵循 **国际地层委员会（ICS）年代表** https://stratigraphy.org/chart
- 地层学术语遵循 **ICS Guide** https://stratigraphy.org/guide

### 2.2 🔴 地质年代与地层单位（★ 最容易错）

| 用法 | 规则 | 示例 |
|---|---|---|
| **upper / middle / lower** | 用于**岩石或时间地层单位** | Navesink Formation，**upper** Navesink Formation |
| **late / early** | 用于**时间单位** | early Miocene |
| **大写规则** | **只有正式承认的 ICS 时间单元**才大写 Early / Middle / Late | **Early** Cretaceous, early Miocene |
| **边界符号** | 用**斜杠 / ** 表示界线；用**短横 – （en-dash）** 表示时间范围 | K/T boundary；Eocene–Oligocene mammals |
| **Ga / Ma / ka** | 🔴 **表示年代**（距今十亿/百万/千年） | — |
| **Gyr / Myr / kyr** | 🔴 **表示时间跨度** | — |

> 🔴 **Ga/Ma/ka = 时间点（dates）；Gyr/Myr/kyr = 时间段（duration）。混用是 Paleobiology 审稿常扣分项。**

### 2.3 斜体与引号

- **属名与种名必须斜体**（除二级标题等本就需斜体的位置）
- 🔴 **命名作者（authority）如出现，必须进参考文献** —— 如 *Tappania plana* Yin, 1997，则 Yin (1997) 必须列入文献表
- 🔴 **拉丁短语不斜体**：a priori · gen. et sp. nov. · incertae sedis · in vivo · in vitro · nomen dubium · per se · sensu · sensu lato · sensu stricto
- 数学变量、统计检验名（*t*-test; *F*-test）斜体
- 🔴 **希腊字母用正体，不斜体**
- 实际引文及术语/含义用**双引号**："true fossil record" versus sampled fossil record
- 🔴 **引文必须给页码**：…as noted by Wilson (1977: p. 23)
- **数字与缩写后不加撇号**：1920s not 1920's；NALMAs not NALMA's
- 逗号与句号**放引号内**；分号**放引号外**
- *e.g.* 与 *i.e.* 后加逗号
- 正文中不用下划线

### 2.4 数字、统计与公式

| 项 | 规则 |
|---|---|
| 数字拼写 | **1–10 拼写**（与计量单位连用时除外）；>10 及非整数用阿拉伯数字 |
| <0.001 | 用 10⁻⁴、10⁻⁵ 形式 |
| 千分位 | >9999 加逗号 |
| 概率 | 🔴 **小写斜体 *p***：*p* < 0.001 或 *p* = 5 × 10⁻¹⁰ |
| 单位 | 用公制；小数前补零（*p* < 0.05，不写 p < .05） |
| 数值与单位间**空格** | 3.2 m、0.5 g |
| 数学符号前后空格 | CI = 0.63 |
| 单位写法 | m, mm, km, μm（**不是 μ**）, l, ml, g（**不是 gm**）, kg, mg |
| 约数 | `ca.` + 日期；数值约数用 `~30%` 或拼写（approximately ten years） |
| 嵌套括号 | 括号内用方括号，方括号内用花括号 `([{}])`；公式中顺序相反 `{[()]}` |
| 歧义字符标注 | l vs 1、O vs 0、希腊 chi vs x vs 乘号 |
| 分数 | 优先分数指数与斜杠 / |

**公式排版**
- "Equation" 小写拼写；括号引用时缩写为 eq.
- 编号公式**居中**，编号置于**右边界**并用括号括起
- 尽量写成一行可排下的形式

### 2.5 稿件格式

**顺序**：title page → abstract page → text → Acknowledgements → Competing Interests → Literature Cited → appendix → figure captions → table captions

| 项 | 要求 |
|---|---|
| 🔴 **字体与行距** | **全稿双倍行距，12 号 Times New Roman**（含摘要、文献表、图注、附录） |
| 纸张 | **US Letter**（8.5 × 11 in / 21.5 × 28 cm） |
| 页边距 | **四边各 1 英寸** |
| 页码 | 从标题页开始编号 |
| 行号 | 🔴 **从标题页开始编连续行号**（Word: 页面布局 → 行号 → 连续） |
| 对齐 | 🔴 **不用右对齐或两端对齐** |
| 断词 | 🔴 **不在右边界断词或加连字符** |

### 2.6 标题页（Title Page）

- 必须含：**标题、作者列表、通信作者（星号 + 邮箱）、作者单位、左右 running headers**
- **标题加粗**；🔴 **仅首词与专有名词大写**；**结尾不加句号**
- 作者全名大小写混排；姓名后加单位上标编号；通信作者名后加星号
  - 示例：`James E. Smith1*, Toby Jones1,2, and C. Alston Chase2`
- 单位**不使用缩写**（Dept.、Ave.、P.O. 都不行）
- 仅通信作者留邮箱
- 作者近期调换单位 → 加 **present address**
- **Running headers 总长 ≤50 字符（含空格）**，全大写
  - **RRH**（右）= 缩写标题，*斜体*
  - **LRH**（左）= 作者姓名；**超过两位作者用 et al.**
  - 示例：`RRH: Onshore-offshore faunal change` / `LRH: Johann S. Bach` / `LRH: Ronaele M. Novotny et al.`

### 2.7 🔴 非技术摘要 + 摘要（★ Paleobiology 特有要求）

- 🔴 **两者都必须提供，且各自 ≤300 词**
- **Non-technical Summary 在前，Abstract 在后**
- 两者各自独立成页，与标题页分开，彼此之间空一行
- 🔴 **Non-technical Summary 必须让非专业读者读懂** —— 避免复杂术语，用受过教育的非古生物学者能理解的语言
- "Non-technical Summary" 与 "Abstract" 加粗，正文从下一行开始，全部左对齐

### 2.8 标题层级

| 层级 | 格式 |
|---|---|
| **Primary 一级** | 居中加粗；首词与重要词大写，冠词/连词/介词小写；**正文另起一行** |
| **Secondary 二级** | 加粗斜体，左对齐顶格；大写规则同一级；**正文另起一行** |
| **Tertiary 三级** | 加粗斜体 + 句点；大写规则同一级；**正文接排在同一行** |

**Boxes（可选）**
- 用途：比正文更深入探讨某概念，或可独立于正文的短案例
- 框标题加粗，≤50 字符
- 🔴 **正文 ≤150 字**（不含框标题）
- 须支撑正文但能独立成篇
- 所有 box 须在正文按序引用
- 🔴 **按录用后图件要求提交**（.eps .tiff .png 等图像文件）

### 2.9 正文引用

- 🔴 **文中引用与文献表必须一一对应**
- 🔴 **作者与年份之间不加逗号**：(Darwin 1859)
- 按**作者姓名字母序 + 发表年**排列
- **三位及以上作者 → 首位作者 + et al.**
- 不同作者之间用**分号**分隔；同一作者多次引用用**逗号**分隔
- 具体页/表/图 → **小写，冒号置于年份后**：(Darwin 1859; McCalpin et al. 1987, 1989: pp. 22–24)
- 个人通讯须给年份 + 姓名首字母缩写 + 姓
- 引文须给页码
- in press 可引，尽量给出预计出版年
- 🔴 **不引未发表或在审稿件**；尽量不引未发表的学位论文
- 作者须为所有引文的准确性负责

### 2.10 图表引用

| 项 | 规则 |
|---|---|
| **Figure** | 正文中**大写拼写**；括号中缩写 `(Fig. 2)`；图的分部大写 `(Fig. 3A)` |
| **Table / Appendix** | 首字母大写，**不缩写**；仅一个 Appendix 时不编号 |
| 🔴 **不用图注排位（no figure call outs）** | 图表会自动排在靠近正文引用的位置 |

### 2.11 Acknowledgments / Competing Interests / Author Contributions

**Acknowledgments**
- 机构与大学名**全称拼写**
- 🔴 **不用尊称**（Dr.、Prof.、Mrs. 等）
- 人名用**带空格的首字母缩写**，缩写在前、姓在后

**Competing Interests（所有作者必须写）**
- 定义：可能被认为对研究内容或发表施加不当影响的情形（财务、专业、合同、个人关系等）
- **不等同于 conflict of interest**
- 须与**所有**贡献作者相关
- 格式：`A. B. Smith is employed at company C, and D. E. Johnson received grant funding from company F.`
- 🔴 **无利益冲突则写 "the author/authors declare none"**

**Author Contributions**
- 简要总结每位作者的具体贡献（分析、数据解读、撰写草稿等）
- 不用尊称，用首字母缩写
- 参考 **CRediT** 分类 https://credit.niso.org

### 2.12 🔴 数据可用性与补充材料（FAIR 原则）

- 过长或格式不适合正文发表的材料（影片、程序、数据库）→ 作为**补充材料**
- 🔴 **须遵循 FAIR 原则**：可获取、可互操作、可复用
- 🔴 **数据与代码必须在同行评审期间可获取**，发表后存入**稳定的公开仓库**
- **Paleobiology 全额承担**投递到 Dryad / Zenodo 的费用（作者零成本）；**Morphobank 对作者始终免费**

**可用仓库**：Dryad · Zenodo · Morphobank · **GitHub**

**Data Availability Statement**
- 🔴 须引用**仓库与 DOI**，且**必须是最终 DOI，不能是审稿专用私有链接**
- 🔴 **DOI 必须在 article proof 就绪前已激活**
- 示例：`Data available from the Dryad Digital Repository: https://doi.org/10.5062/dryad.411hq`

**文件命名**：Supplementary Table 1, 2… / Supplementary Figure 1, 2…

**必需支撑文件（按研究类型）**

| 研究类型 | 要求 |
|---|---|
| **Occurrence-based data** | ① 文献/自建数据库编译的数据**须完整提供**，不能只给来源引用；② 用公开数据库（如 Paleobiology Database）须给出**详细检索参数与下载日期** |
| **Phenotypic trait data** | 🔴 **即使分析用的是衍生变量（如比值），原始数据仍须提供** |
| — 长度测量 | 统一表格格式（.xlsx .txt .csv），含单位信息 |
| — Landmark 数据 | .txt 或 .tps 格式；须附**元数据文件**关联标本信息，含缩放信息 |
| — 离散性状数据 | 通用表格格式或 Morphobank；须含性状描述 |
| — "Landmark-free" | 须归档**处理后、对齐前**的 3D 模型，以及点云/距离矩阵提取 |
| **所有类型** | 🔴 **所有处理数据的代码（含后处理）都须提交**；分析软件详细描述或分析代码（纯制图除外）须提交 |

> ⚠️ **Supplementary Material 内的参考文献不得计入主 Literature Cited。**

### 2.13 🔴 Literature Cited（格式极严）

**EndNote 有 Paleobiology 专用 output style**（endnote.com/support/enstyles.asp）。
🔴 **最终提交稿不要用 Cite-While-You-Write。**

| 项 | 规则 |
|---|---|
| 收录范围 | 正文、表格、图注、附录中引用的**所有**文献 |
| 排序 | 🔴 **严格字母序**（含 Mac 与 Mc），但**三位及以上作者**的条目例外（见下） |
| 同首位作者 | ① 单作者按**年代**排 → ② 双作者**先字母序再年代** → ③ 三位及以上作者**仅按年代**排 |
| 同年同作者 | 按字母序或明显日期序；用**小写字母**区分（1989a, 1989b） |
| 缩进 | 🔴 **不用制表符缩进，用 Hanging Indent** |
| 作者名 | 🔴 **粗体**，大小写混排；首字母间**有空格**；除第一作者外**缩写在姓前** |
| 期刊名 | 🔴 **斜体且不缩写** |
| 卷号 | 🔴 **粗体** |
| In / in | 书中引用时 **italicize** |
| 冒号后 | 文章或书的副标题在冒号后**不大写** |
| 一书三章以上 | 单独引该书，各章引用时用该书的缩写形式 |

**范例**
```
Storm, E. C. 1974. Omnology at the crossroads. Journal of Omnology 22:1–44.

Foote, M. 2001. Origination and extinction components of taxonomic diversity:
  general problems. In D. H. Erwin and S. L. Wing, eds. Deep time:
  Paleobiology's perspective. Paleobiology 26 (Suppl. to No. 4):12–26.

Smithson, A. B. 1995. Gymnosperm envy. Pp. 23–45 in C. D. Jones, ed. Advances in
  angiosperm psychology. Proceedings of the 24th international symposium on
  fossil plants. Geological Society of America, Boulder, Colo.
```

**出版商缩写**：Blackwell Scientific（非 Blackwell Publishing）· **Springer**（非 Springer-Verlag）· 一般删去 "Press"（大学出版社与 Academic Press 除外）· 必要时保留首字母区分（W. H. Freeman; J. Murray）· 知名城市可省州名，用传统缩写而非邮编（Springfield, Mass.）· 需要时加国名（Wiley, Chichester, U.K.）

### 2.14 表格

- 用**可编辑格式**（Excel 或 Word）；Word 须用"创建表格"功能，**不用制表符+空格**
- 可用彩色或灰阶
- 🔴 **表题置于表格正上方，且与表格同页**
- 🔴 表体中**引用年份不加括号**
- 🔴 **不用竖排标题或竖边框**

### 2.15 图件提交

- 🔴 **不要把图嵌入正文文件**
- 🔴 **所有图作为独立文件提交**
- 图的分部用**大写字母**标注
- 🔴 图注中子图引用**加粗**：句首加逗号 `B, scatter plot of the data…`；句中用括号 `Scatter plot of the data (B) shows…`
- 单张图的各部分**排在同一页**；分部很多时可排在**两个对开页**
- 图内文字：**大小写混排 + 无衬线 + 不用粗体**；终版字号 **≥8**
- 🔴 **必须嵌入字体**
- 录用后：**文件名须标明单栏/双栏/整页/横版**

### 2.16 最终提交（Final Submission for Production）

- 提交物会被检查是否可投产
- 转入 Production 后、进入队列前：完成 **Author Information form** + **author agreement**
- 提交前确认：**ScholarOne 个人资料中的邮箱是最新的**；**有 ORCID 的所有合著者已把 ORCID 加进个人资料**
- 有补充材料的，**DOI 必须可用**且写在 Data Availability Statement 中；**不要用私有/审稿 DOI**