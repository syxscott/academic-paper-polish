# 图件制图实证（v2.15.0 新增）

> **本文件的证据来自「实际打开渲染出的 PNG 看图」，不是只看图注文字。**
> 语料：D:\数据集\PDF_Radiolaria 全库 8162 篇 PDF 中按 28 个主子目录**分层随机**抽取 181 篇
> （种子 20261103，**不按文件大小排序**），渲染图页 449 张 PNG；5 组审阅共实看约 150 篇 / 300+ 张图。
> 每条惯例都注明出自哪一篇/哪一刊；凡属**单刊现象**一律显式标注，不得推广成全领域规则。

## 一、核心结论：制图惯例按「刊」分，不存在全领域统一规则

### 1.1 比例尺 vs 放大倍数（最强的按刊分界）

| 路线 | 采用者 | 逐字证据 |
|---|---|---|
| **图上画比例尺条 + 数值** | Palaeo 3P / Pal J / Elsevier(QSR) / Deep-Sea Res. / NOM | "Fig. 43. ... Scale bar in the upper left represents 133 µm for × 150 and 100 µm for × 200." |
| **只写放大倍数，图内无条** | Geologica Carpathica / Micropaleontology / 福井大学 / 现代地质 / 西语刊 | "Fig. 1 - Emililia sp. 0897, 130x magn., HS-1a." |
| **两者并列给出对照值** | Baumgartner 1985 | "Scale bar in the upper left represents 133 µm for × 150 and 100 µm for × 200." |
| **物镜/目镜比值** | Brandt 1885 | "(320/1)" |

→ **同一篇论文内部可能两制并存**（如 QSR 正文插图用 ×N、图版用比例尺条），因此规则必须写成「本文的图版/照片用什么制」，不能写「本领域用什么制」。

🔴 **v2.15.0 修正（2021 年追加 10 篇）**：先前把 **Revue de micropaléontologie** 归入「只写 × magn.」一类，
被 Bragina & Bragin 2021（该刊）推翻——该篇图版**全部用比例尺条**（"100 mm: a – 1–3, 7; b – 4–6; c – 9–12; 50 mm: d – 8."，实为 μm），
全文无放大倍数标记。→ **「按刊分」必须按刊的具体 series/作者群核对，不能按刊名一概而论。**

🔴 **中文刊（《微体古生物学报》等）全部使用比例尺，不用 × magn.**，但**同刊内写法不统一**：
「比例尺（Scale）＝100μm」/「比例尺（scalebar）＝100μm」/「标尺＝100μm」并存。

### 1.2 图注前缀的多语种词汇表（实测 4035 条图注）

| 语种/刊系 | 图号写法 | 占比特征 |
|---|---|---|
| 英文主流刊 | Fig. N. / Figure N. / Fig. N | Fig. 1219 条、Figure 257 条 |
| 俄文刊 | Рис. N. / рис. N | Рис. 163 条 |
| 俄文老刊 | 把 SEM 图版编成「表」 | Табл. I, рис. 1, 2 |
| 中文刊 | 图N / 图版I / 圖版 | 与 Fig./Table 并存 |
| 日文刊 | 図N / 図版 / 表N | |
| 德文刊 | Abb. N / Taf. N | 34 条 |
| 法文刊 | Fig. N à M 合并式 | |
| 特殊 | TEXT-FIGURE N（Micropaleontology 系）、PLATE N、Plates I-XXI | |

→ **TEXT-FIGURE 是 Micropaleontology / DSDP 系列的特有写法**，其余刊不用。

### 1.3 图注位置分两派（按刊）

- **图下方**：Alcheringa、MEPS、Deep-Sea Research、Palaeo 3P、地层学杂志、Geologica Carpathica
- **图上方**：Pal J、NOM、Protist、J Pal Soc India
- **Elsevier 排文末**："(see on page 6)"
- **BMR 图版页兼目录**

### 1.4 图例（Legend）放哪：三选一，按刊分

1. 做进**图内**（最常见）：符号行、图例框、图内右列
2. 做进**图注内**：Abbreviations:（Geol. Mag.、PALAIOS、NOM）/ explanations:（PalZ）/ 行内冒号式（JGSJ）
3. 做进**正文专章**：Ofioliti 的 NOMENCLATURE、DSDP 的方法段
4. **另排一页**：N. Jb. GP（"Fig. 4 (Legend see p. 59)"）

→ **本领域 30 篇（第 4/6 组）没有一篇用 Legend:/Explanations:/Abbreviations: 小标题**——这是刊级差异，不是缺失。

### 1.5 中文刊的图注格式（固定七要素）

　　图号 ＋ 中文题名 ＋ 英文题名 ＋ 分图条目（1,2. 种名：1. 样品号 / SEM 影像编号）＋ 比例尺 ＋ 标本保存地

- 中文图注**中英双语并列**，与英文刊的纯英文图注不同。
- **分图编号两种格式并存**：001 写「（图２ ６）」，002 写「（图３－１，２）」。
- **中文图表引用**：正文用「（图１）」「（表１，点２）」「（图３－１，２）」「（详见３．２）」，图号与表号混排。

### 1.6 中文对比表用「√」标记共同种

002 表 1：行＝种名，列＝本文＋5 个地区/文献，**单元格打「√」**。
→ 与英文刊的 X / ♦ / 线条式矩阵不同。

## 二、子图标号体系（逐字实测）

| 体系 | 采用者 | 例子 |
|---|---|---|
| 小写字母 | 欧美系主流 | (a)(b)(c)、(a–c) |
| 大写字母 | Stratigraphy、Marine Biology | (A)(B)、(A)–(F) |
| 数字 | SEM 拼版图 | 1–12 + 细节 8a/8b |
| 罗马数字 | **只用于图版号**，不用作子面板号 | Plate I、图版I |
| 冒号式 | N. Jb. GP | Fig. 3:4 |

## 三、图版（Plate）说明的四种制式

### 3.1 罗马数字图版号 + 放大倍数（Geologica Carpathica / QJGS / 成都地矿所刊）

"PLATE II: Fig. 1 - Emililia sp. 0897, 130x magn., HS-1a."

条目格式：Fig. N - 学名 标本号, NNNx magn., 样品号.

### 3.2 阿拉伯数字图版号 + 比例尺（DSDP / Rev Micropal / NOM）

"PLATE 73, fig. 8"、"Plate 122, fig. 26"

图版索引：斜体粗体学名单独一行，下一行给 Plate N, fig. M。

### 3.3 独立「图版说明」节（Pal J / 日文刊）

Explanation of Plate N / 図版説明 —— 逐图给标本号 + scale bar + 地层 + 样品。
日文刊的比例尺写在图版标题行：図版I スケールは100μm.（不是每张照片各标一次）。

### 3.4 图版页兼目录（BMR）

## 四、化石照片/SEM 图的必带要素（跨刊通用）

- **标本号**：PIN no. / CPC / GSCU / F2489(#61) / (HB07, sl.1, DS1/0) —— 无一例外
- **放大倍数或比例尺**：二选一，且必须在图注或图内可见
- **比例尺条写全句**："All scale bars equal 1 μm"、"All scale bars indicate 100 µm"

## 五、表格（Table）的做法

### 5.1 表头单位写法

"Event | depth, cm | age, kyr | sed. rate cm kyr⁻¹"（逗号简写单位）

→ **表头用逗号简写单位**是高标准期刊表头的通用写法。

### 5.2 表注位置与符号体系

- **表注一律在表上方**（MEPS、Deep-Sea Res、NM Museum、NOM）
- **丰度符号按刊**：
  - 英文刊：X（对位矩阵）、♦、?
  - 俄文刊：Р / Ч / О（仅 Стратиграфия）
  - "+ (single specimen), R (rare), F (few), C (common), A (abundant)"
- **星号系统**：* / ** 本组 30 篇零出现

### 5.3 「物种 × 地点」对位矩阵表

"表1 放散虫化石リスト" / "Таблица 1. Распределение радиоляриевой фауны..."

行=属种名（按属名字母序，含 cf./ex gr./aff. 与开放命名 sp. 1），列=层号或采样点，单元格用符号标丰度。

→ **俄文用 X，Afanasieva 2002 用线条表示分布区间**——同为矩阵表，标记法不同。

## 六、地理图与剖面图的三件套

**主图 + 插图定位小图（inset）+ km 比例尺**；采样点在图注里编号对应。

- 图例框名按刊而异：LEGEND / INDEX / Legend / 位置図
- **靠经纬网而非指北针**（仅 6 篇有指北针、11 张有比例尺）
- 改绘必注出处：Modified after / Simplified after / after Petrushevskaya, 1986
- **QSR 型位置图**："Fig. 1. The location of core PC-7R (white circle), surface water circulation around the Okhotsk Sea according to Chernyavsky (1981) and early studied cores (yellow stars) (Okazaki et al., 2003a)."
  → **图注逐个说明每个视觉元素的含义**（white circle / yellow stars），并给洋流图的引用来源。

## 七、Elsevier 彩色图的强制话术

"(For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)"

→ 该句在 QSR 论文里**每张彩色图注末尾都出现**。彩色图注还必须写明：

- 每个元素的颜色（black lines / Blue bars / Gray bar / Magenta bar / purple line / red line）
- 堆叠顺序（"from top to bottom"）
- 双 Y 轴读法（"values of the thick curves are shown at the right side and values of the thin ones are shown on the left side"）

## 八、交稿前自查（图件部分）

- [ ] 本文的**图版/照片**用的是比例尺还是放大倍数？与目标刊一致吗？
- [ ] 图注前缀用的是目标刊的写法吗（Fig. / TEXT-FIGURE / Рис. / 图版）？
- [ ] 每个视觉元素（颜色/线型/条带/符号）都在图注里有对应说明吗？
- [ ] 双 Y 轴图是否写明哪条线读哪个轴？
- [ ] 地图是否给了比例尺 + 指北针或经纬网 + 底图来源？
- [ ] 改绘图是否注明 after X？
- [ ] 每个标本是否都有标本号？
- [ ] 表格单位是否写进表头/行头？表注是否在表上方？
- [ ] 彩色图是否带 Elsevier 彩色免责句？

## 九、本文件的局限（必须如实说明）

1. 每刊通常只有 1–2 篇样本，**"按刊"结论只能视为该刊该篇的观察**，不能当作该刊完整规范。
2. 图内文字（符号、缩写）常存在于矢量/位图 artwork 中，**PDF 文本层不含**，只能靠看图获得。
3. 本文件结论以**实际看图**为主、图注原文为辅；个别 OCR 噪声已在图件审阅笔记中标注。
