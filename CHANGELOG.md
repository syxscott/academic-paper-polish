# Changelog

本文件记录本仓库（agent skill：学术论文写作、润色、改稿与投稿）的主要变更。

## [2.15.0] — 2026-11-02

### 先更正：上一轮的"全文通读"建立在两个抽样/抽取缺陷之上

本轮对 v2.14.0 的证据链做机器审计，发现**两个独立缺陷叠加**，足以推翻旧样本的代表性：

1. **抽取器用 dict 存章节，遇同名标题会覆盖前一段正文。**
   实测：full151.jsonl 首篇 Afanasieva & Amon 2011c 的 sec_order 出现两个 introduction，
   sections['introduction'] 被第二次标题覆盖，导致正文既丢失又重复计数
   （chars_body 1,326,873 字符 vs 原始 chars 812,199）。
   改为**有序分段列表**后重跑，重复消失（探针串出现次数 2 → 1）。
2. **旧"130 篇"实为全语料最小的 130 篇。**
   skel120.jsonl 按文件大小升序排列，取前 130 行即**最小的 130 篇**
   （中位 0.89 MB，70 篇 ≤1 MB）；而其余 216 篇中位 6.88 MB、最大 435 MB。
   此外旧抽取器的正文中位数仅 198 字符（同文件用全文抽取为 23,561 字符）。

**处理**：重抽**分层随机**样本（28 个主子目录按篇数比例分配、目录内均匀随机、
**不按大小排序**、种子 20261103），得 181 篇；补抽 30 篇使可逐字读者达 **164 篇**。
正文切掉参考文献后合计约 **570 万字符**（旧口径 1120 万为虚高，含重复与文献表）。

### 本轮真正做的：164 篇逐字全文精读 + 449 张图实看

- **精读**：每篇由独立子 Agent 用 read 工具**读到文件末尾**（Abstract → Introduction →
  中间部分 → Discussion → Conclusion → Acknowledgements），分片末尾逐篇声明
  「文件字符数 / 实际读到的字符数 / 覆盖章节」；主会话另用**机器回源校验器**把笔记中
  每条引文拿回源文件核对（含 ≥12 个拉丁/西里尔字符的引文才纳入；纯中文分析文字不计）。
- **图件**：渲染 449 张 PNG，5 组审阅**实际打开看图**（不是只读图注），逐组给出
  「按刊物归纳 / 跨刊通用 / 差异与例外」三分类。

### 新增两个 reference 文件

| 文件 | 内容 |
|---|---|
| references/figure-conventions-evidence.md | 图件制图实证：比例尺 vs 放大倍数**按刊分**的四条路线、图注前缀多语种词汇表（实测 4035 条）、子图标号五体系、图版说明四种制式、表格表注符号体系、Elsevier 彩色图强制话术、图件交稿自查 |
| references/fulltext-reading-evidence.md | 全文精读实证：章节链五类骨架、Methods 三档详略、Results 两条硬要求、**Discussion 四拍结构**、Conclusion 两种形态、**短篇三种讨论形态**、引言六种起手、类群块跨语种模板 |

### 关键新结论（全部附论文名 + 逐字原文）

- **制图惯例按「刊」分，不存在全领域统一规则**：Palaeo 3P / Pal J / QSR / Deep-Sea Res. 用
  **图上比例尺条**；Geologica Carpathica / Micropaleontology / Revue de micropaléontologie 只写
  **× magn.**；Brandt 1885 用物镜/目镜比值 "(320/1)"。
- **图注前缀是多语种的**：Fig.(1219) / Рис.(163) / Таблица(170) / 图 / 图版 /
  Abb.(34) / TEXT-FIGURE（Micropaleontology 系特有）——**不可统一成一种写法**。
- **Discussion 的四拍结构**（Gorbarenko et al 2020）：数据陈述 → 机制解释 →
  **与前人比对（一致 or 矛盾，明确写出）** → 本研究结论 + 不确定性。
  关键句式："Such a pattern … is **consistent with** … **but contradicts** …"。
- **Conclusion 的两种形态**：连续散文式（高标准刊，机制归因用 "rather than" 排除、
  不确定性用 "likely due to"）vs 编号清单式（短篇/区域地层）。
- **短篇（3–10 页）绝大多数没有独立 Discussion 段**，讨论以三种形态出现：
  点名质疑前人（Zheng 1986 点名 Miyashiro/Pearce/Robinson 三个范式）／
  承认局限再修正（Deflandre 1946）／"不能断言但可能"（Yamasaki 1999）。
- **俄文分类学种级块是五拍固定结构**：Описание. → Размеры, мк: → Изменчивость. →
  Сравнение. → Местонахождение и возраст.（Mamedov 1973）；且必写
  "Близкие по морфологии виды не установлены." 与 "…позволяет выделить новый род, так как
  подобный род в семействе … не выделен."
- **Methods 没有"必须写满"的规则**，但**只要用了指标就必须给公式与逐符号定义**
  （Gorbarenko 2020 的 ARM = CM × DBD / LSR 及其全符号说明）。

### 语料与工具

- 语料：D:\数据集\PDF_Radiolaria，8162 篇 / 62 GB / 64 子目录。
- 流水线脚本（临时目录，未入库）：extract_v2.py（分段保序抽取）、export_txt.py、
  cut_refs3.py（切参考文献 + 乱码检测）、caps_multilang.py（多语种图注）、
  render_fill.py（渲染图页）、verify_quotes5.py（引文回源校验）、
  merge_notes.py / cov_stats3.py（合稿与覆盖率统计）。

---

## [2.15.0] — 2026-11-02（补充：覆盖度审计与缺口补齐）

### 一轮诚实的覆盖度审计发现的缺口

对 164 篇精读笔记做字段覆盖率机器审计，发现**模板没要求、因而没分析**的要素：

| 缺口 | 原覆盖率 | 处理 |
|---|---|---|
| 摘要写法 | 1% | 已补：44 篇实测（87% 结果打头 / 29% 目的句 / 被动 87% / 现在时 95% / 中位 2000 字符 13 句） |
| 标题写法 | 0% | 已补：44 篇可抽取标题（中位 6.5 词、冒号 0%、问号 0%、年代词 41%、产地 32%）+ 三个构造公式 |
| 时态/语态 | 0% | 已补：摘要口径（现在时 95% / 被动 87% / we 18%）；引言口径未量化，已标注 |
| 综述口吻 | 27% | 已补：4 篇综述型论文逐字证据（收录标准先行、每节概括句、跨门类类比、零图表可行） |
| 现代期刊声明块 | 1% | 已补：四日期 / CRediT / Data availability / COI / 致谢顺序（逐字） |
| 关键词 | 40% | 半覆盖，维持原状 |

### 修掉最严重的可用性问题：新研究进不了主调用路径

审计发现 **10 个 prompt 模块原先 0 个引用新实证** —— 用户说"帮我润色摘要"时加载的
prompts/01-abstract.md 根本不知道 164 篇摘要实证的存在。
现已在 **9/10 个模块**顶部加"🔴 动笔前先读实证"指引（10-reviewer-response 无语料支撑，保持原状）。

### 新增决策树（§八之四）

3 个判断问题（贡献类型 / 老刊新刊 / 篇幅）+ 5 种骨架速查表（A 系统描述 / B 生物地层 /
C 多指标古环境 / D 区域综合 / E 短篇报告）。

### 口径诚实标注

- 引言段的时态/语态**未做同口径统计**，已在文件中标注为待办。
- 44 篇可抽取标题只占 164 篇的 27%，标题结论只适用于能抽出标题的样本。
- 12 篇无文本层扫描件、3 篇文本层乱码，均未计入任何结论。

---

## [2.15.0] — 2026-11-02（再追加 10 篇：中文刊与英文刊的系统性差异）

### 追加精读 10 篇（2021 年新文献，538,220 字符）

从 `D:\文档\编程项目\SKills寻找创新点\2021新放射虫文献` 选取 10 篇：
6 篇中文刊（《微体古生物学报》为主）+ 4 篇英文刊（Pal J / Rev Micropal / Palaeoworld），
覆盖分类学新属、生物地层、综述、现代生态、古海洋。4 个子 Agent 逐字读完，引文均经 grep 逐字校验。

### 🔴 推翻 5 条既有结论（重要）

| 原结论 | 修正 |
|---|---|
| Revue de micropaléontologie 用 × magn. | **不成立**：Bragina & Bragin 2021 用比例尺条 |
| 摘要现在时 95% | **仅限英文刊**（008/009 摘要以过去时被动起手） |
| 引言 we 49% | **仅限英文刊**（009 引言 0 处 we） |
| 标题中位 6.5 词 | 有例外：分类学/古生物长标题可达 10–28 词；中文标题 14–18 字 |
| 关键词中位 8 个 | 有偏差：英文刊 5–10，中文刊 4–6 |

### 新增 §8.11（中文刊 vs 英文刊的系统性差异，16 小节）

核心：**中文刊与英文刊系统性地不同**，许多旧结论只适用于英文刊。

- 中文刊固定骨架：摘要→关键词→编号正文→**系统描述（代替讨论）**→参考文献→英文摘要（＋新种英文描述）
- 中文摘要骨架：**主题句/前人工作起手 → 本文工作 → 结论**（与英文的结果打头相反）
- 中文第一人称三型：「本文」/「我们」/「笔者」；中文无被动标记
- 中文综述组织：构造单元 → 地区 → 剖面 → 时代 → 属种 → 对比（**无收录标准段**）
- 中文类群块：属级「模式种→属征→时代与分布」；种级收尾「产地和层位」；**英文新种描述集中置于文末**
- 中文图注七要素：图号＋中文题名＋英文题名＋分图条目＋比例尺＋标本保存地
- 中文图表引用：（图１）/（表１，点２）/（图３－１，２）；对比表用「√」
- **METHODS 容器化**（007 把结果+讨论装进 METHODS，占全文 45%）
- **无 Discussion 时讨论的四个去处**（METHODS / 引言 / Results / 类群块）
- **结论第三种形态**（混合式 / 单段连排 / 两级编号 / 写在摘要里）
- 长文分节：按剖面 → 按生态区 → 按主题；图版按生态区组织
- **摘要-正文数字矛盾**（001：摘要 23 种 vs 正文 24 种）——三者必须交叉核对

### 其他

- 新增未编号 inline 测量表、延限图、视角键、FAD 事件表、统计门槛写法等制式
- 修正 figure-conventions-evidence.md：补 §1.5 中文图注格式、§1.6 中文对比表「√」
- prompts 01/02/06/09 接线到 §8.11

---

## [2.14.0] — 2026-11-02

### 🔴 先更正：把夸大的"阅读量"表述改成精确口径

v2.12.0 写下的"130 篇逐篇读段落骨架…48 篇有可读 Introduction、22 篇有可读 Discussion，逐段读"，
经本轮自查（对抽取物做字符量统计）**表述夸大**：那一轮的抽取物合计仅 25,844 字符、
每篇中位 0 字符，**引言只摘了首句、目的句、末句三处**，不构成通读。
该说法**已在 `references/micropaleo-paper-patterns.md` §九 就地标注作废**，不再作为任何结论的依据。

### 本轮真正做的：17 篇全文通读（≈21.6 万字符）

从本地语料抽取 20 条完整正文，去重后 **17 篇**读通了 Introduction / Discussion /
Conclusions 的**连续散文全文**：引言 16 篇 12.5 万字符、讨论 7 篇 5.0 万字符、结论 6 篇 4.2 万字符。
另有 1 篇（Dumitrica 1983 *Suttonium*）PDF 文本层抽取失败，**不计入任何结论**。

**新增结论（全部附论文名 + 逐字原文）**：
- 🔴 **引言模式增至八种**：新增 **F 地质背景前置式**（Ohba & Adachi 1995）、
  **G 综述—反例式**（Febvre 1981，用 "But it now clear that…" 提反例）、
  **H 编号问题式**（Danelian & MacLeod 2019，引言末尾用编号问句列研究问题）
- 🔴 **目的句增至十类**：新增 **"Our study focused on …"**（Li et al. 2009），
  通常紧跟"缺口 + 重要性"两句
- 🔴 **引言长度改用正文字符数**：17 篇全文实测 **1,712–12,184 字符**（中位约 7.6k），
  替代原先受排版影响的"2–108 段"
- 🔴 **讨论起手增至十三种**：新增"竞争假说二选一型"（MacLeod et al. 1997）、
  "已知事实 + 从未有人做过型"（Kashiwagi & Isaji 2015）
- 🔴 **讨论收尾增至八种**：新增"方法缺陷自陈 + 反常归因型"（Yoshino et al. 2020）
- 🔴 **新增三种可抄的讨论骨架**：甲 逐项对照 ｜ 乙 反常→可能原因→**坦承未决并指名缺哪类数据**
  （Qu et al. 2020）｜ 丙 已有说法→本文新证据→结论（Kashiwagi & Isaji 2015）
- 🔴 **引言的编号问题 ↔ 结论的编号答案一一对应**（Danelian & MacLeod 2019；
  Li et al. 2009 的 "5 Conclusions" 是三条编号句）
- 🔴 **类群块模板增至五种**（新增 D 度量短文型、E 目录式），并补出**属 / 目 / 科级块的
  独立标签体系**（目级 definition–range–origin；科级 type genus–diagnosis–occurrence）
- 🔴 **Remarks 三种模板**：四步（吻合→差异→处置→与他人不同）／
  同义五步（判定→原区分点→**差异归因**→模式标本复核→结论）／
  **待观察特征清单**（定种不足时列出还缺哪些形态部件）
- 🔴 **Repository 两种放法**：单列一节，或**写在系统描述段第一句**
- 🔴 **前人引用**：图号可带小数点（figs. 4.1–4.6）也可不带（figs. 8–12），
  且**把前人的度量值搬进 Remarks 做对比**

### §十 的口径一并补齐

22 篇系统描述精读合计 **约 11.96 万字符**（每篇中位 4,139 字符），其中 **15/22 篇**抽出整段讨论、
**11/22 篇**抽出整段系统描述正文 —— 这一轮是**真读**，口径照此写明。

### 同步

- SKILL.md 升到 **2.14.0**：结构对照表按新口径重写，补"讨论骨架""引言 ↔ 结论"两行
- evals/evals.json 升到 **1.9.0**，新增 **R11-fulltext-honesty**（口径诚实性防回归）与
  **R12-fulltext-patterns**（本轮新模式）
- README 徽章同步

## [2.13.0] — 2026-11-02

### 新增：系统描述类论文专章（22 篇精读）

从 346 篇分层抽样中筛出**系统描述类候选 35 篇**，**逐篇精读 22 篇**
（含全文段落、类群块标签顺序、系统描述段正文、讨论段正文），覆盖 J. Micropaleontology、
Palaeontological Research、Revue de micropaléontologie、Micropaleontology、
Palaeontological Journal、USGS Professional Paper 等刊式。

**🔴 最重要的结论**：**系统描述类论文通常没有独立 Discussion 段**，
讨论由**每个类群块的 Remarks（+ Comparison）承担**。

**新增内容**（references/micropaleo-paper-patterns.md 第十章）：
- **Remarks 块四步**：吻合 → 差异点 → 分类处置 → 与他人处理不同（逐字例句）
- **类群块标签三种模板**：完整型 / 标准型 / 度量型
- **章节安排**：Repository 常独立成节；地质背景常分区域地质 + 采样剖面两节；
  属级标题固定写法（Genus X Author, 19xx ＋ Type Species.—）
- **图版说明两制式**：放大倍数制（× 175）与图版引用制（Plate 3.1, figure 7）
- **前人描述引用三要素**：命名人 + 年 + pl.X, figs. Y-Z, p.N
- **跨类群讨论写法**：把本系列新种汇成"数量 + 出处"总结 → 与前人计数对照 → 抬到属级问题
- **形态计量类讨论骨架**：引前人原句标页码 → 指出其局限 → 本文如何扩展 → 承认方法误差
- **13 条系统描述类交稿自查**

### SKILL.md / evals 同步

- SKILL.md 新增「🔴 系统描述类论文（写新种/新属）专章」小节与触发词
- evals/evals.json 升到 1.8.0，新增 **R10-systematic-description**

## [2.12.0] — 2026-11-02

### 精读扩到 130 篇，第九章整章重写

> ⚠️ **v2.14.0 更正**：本节"48 篇有可读 Introduction、22 篇有可读 Discussion，逐段读"**表述夸大** ——
> 那一轮引言**只摘了首句、目的句、末句三处**，不构成通读。该表述已作废，**详见 v2.14.0**。

在 v2.11.0 的 5+1 篇全文基础上，**扩到 130 篇逐篇读段落骨架**
（分层抽样；英文题名 110、中文 18、俄文 2），其中 **48 篇有可读 Introduction、
22 篇有可读 Discussion**，并通读 **RadSS（Apostol et al. 2016，放射虫 SVM 分类）**全文。

**新增结论**：
- 🔴 **目的句实测九类句式**：aim / purpose / goal / objective / It is the purpose of…
  / In this work we… / We present here… / **"Therefore, …"（由前文推理得出）** /
  **否定式划边界**（"The goal of this project has not been to…"）
- 🔴 **引言长度实测 2–108 段**，本领域无统一规范；短引言多见于数据报告与短通信
- 🔴 **讨论起手实测十一种**（比较对象 / 标志性种定年 / 结论先行 / 否定排除 / 让步 /
  复述目的 / 子标题+综述 / 子标题+结合已发表数据 / 数据→推断 / 结果陈述 / 自承不完整）
- 🔴 **讨论收尾实测七种**（让步 / 需进一步研究 / 归因 / 地层陈述 / 审慎推测 /
  否定限定 / 结论重述），**无一是"未来展望"**
- 🔴 **缺口四种写法**：数量化 / 未决性 / 具体未研究对象 / 方法空白
- 🔴 **中文日文章节对应词**：提要、**地質概説（地质概况）**、**考察（Discussion）**、まとめ；
  中文刊**常无引言节**，直接以地质概况起头
- 🔴 **计算机方法类论文骨架**（RadSS）：INTRODUCTION → RELATED WORK →
  RADIOLARIANS / MACHINE LEARNING AND FEATURE EXTRACTION（Training App / Classifier App）→ RESULTS

### SKILL.md 同步

对照表新增：目的句九类句式、引言长度无规范、讨论十一种起手、中日文章节对应词。

## [2.11.0] — 2026-11-01

### 🔴 更正：v2.10.0 用"命中率"下结论的方式作废，改为逐篇精读

v2.10.0 用**关键词出现率**（正则命中 "however"/"because"/"our results" 等）去衡量
Introduction 与 Discussion 的"论证动作"。**这是方法错误**：词频只能证明某个词出现过，
不能证明作者在该处做了什么论证动作。据此得出的两条结论**被精读推翻**：

| v2.10.0 的结论 | 精读结果 | 处置 |
|---|---|---|
| "Discussion 首句不是复读摘要（重述结果仅 10%）" | **不成立**。多数讨论首句是**直接进入比较对象**（"directly comparable with …"）或用标志性种锁定时代；"重述结果"少，是因为讨论确实不复读摘要，但**原因不是词频测出来的** | 改写为**四种起手**（逐字列出） |
| "Discussion 主体是机制解释 35% + 启示 35%，与文献逐句对照仅 15%" | **不成立**。词频把"逐项对照"漏掉了 | 改写为**逐项对照 + 显式焊合**（"Because …, we propose that …"） |
| "目的句在引言后半段" | **不成立**。目的句位置随引言模式而变（第 1–3 段都有） | 改为"**独立成句，位置随模式而变**" |
| "remains unclear 仅 14%" | 数字是截断假象；**精读发现本领域确实用这类说辞**（"remains one of the most intriguing problems"） | 删除该数字，改为"具体或数量化的缺口" |

### 新增：五种 Introduction 写法 + Discussion 的四种起手与四种收尾（逐字）

精读 **5 篇 Introduction 全文 + 1 篇 Discussion 全文 + 8 篇 Discussion 首末句**后，
`references/micropaleo-paper-patterns.md` 第九章整章重写：

- **Introduction 五种模式**：A 缺口→目的（目的句 + 贡献句两句连排）｜B 必要性论证（无文献回顾段）
  ｜C 教科书铺陈 ｜D 材料发现（含材料局限坦陈）｜E 铺垫→目的→**单独一段新意声明**
- **Discussion 三段骨架**：给出比较对象 → **按形态类型/属种逐项对照** → 指出差异并收口
- **四种起手**：直接进入比较对象 / 用标志性种锁定时代 / 先摆领域通说 / "Because …, we propose that …"
- **四种收尾**：让步限定 / 需要进一步研究 / 归因 / 地层陈述 —— 无一是"未来展望"

### 方法纪律

SKILL.md 新增方法说明：**结构结论必须来自通读全文，不得用词频命中率代替对论证动作的判断**。
`evals/evals.json` 的 R09 同步加 `must_not`："用词频命中率代替对论证结构的判断"。

## [2.10.0] — 2026-11-01

### 新增：论文整体结构（Introduction 怎么写 / Discussion 怎么讨论）

在同一分层抽样（224 篇）上再抽取 IMRaD 正文：**Introduction 50 篇、Discussion 20 篇、
Conclusions 13 篇**（三者齐备仅 5 篇，老论文常把讨论拆进各小节或与结论合并）。
新增 `references/micropaleo-paper-patterns.md` 第九章。

**实测到的写法（与通用 SCI 模板不同的部分）**：
- **Introduction 首句先给事实**（放射虫是什么 / 材料何时何地发现），不直接说"本文做了什么"
- **目的句在引言后半段**，句式 `The aim/purpose of this …` / `In this paper, we present …`，
  且**必须带具体对象与产地**
- **缺口是具体的**（哪个层 / 哪个区 / 哪个类群没研究过）；`remains unclear` 仅 **14%**
- **Discussion 首句不是复读摘要** —— 先摆领域共识 / 与已有工作对表 / 用数据锁定时代；
  "重述本文结果"仅 **10%**，主体是**机制解释（35%）+ 启示外推（35%）**
- **Discussion 收尾是让步限定 / "需要进一步研究" / 地层结论**，不是"未来展望"
- **Geological setting 几乎必选且排在 Methods 之前**；系统描述类论文**没有独立 Results 段**

**附逐字例句**：Introduction 首句 8 例、目的句 7 例、Discussion 首句 8 例、
Discussion 收尾 8 例、Conclusions 收尾 6 例，全部取自语料原句。

⚠️ **抽取口径**：以"标题样式行"作为段落边界，正文可能被截短 →
"文献回顾/转折词"偏高、"提出目的"偏低；**逐字例句不受影响**。

### 其他

- SKILL.md 新增「本领域的 Introduction / Discussion 写法与通用模板不同」对照表
- 触发词补 `introduction 怎么写` `discussion 怎么写` `论文结构怎么排` `讨论部分怎么写`
- `evals/evals.json` 升到 1.5.0，新增 **R09-paper-structure**

## [2.9.0] — 2026-11-01

### 新增：微体古生物 / 放射虫论文的写作与制图模式（基于 8162 篇本地语料）

新增 `references/micropaleo-paper-patterns.md`。取样口径：本地语料 `D:/数据集/PDF_Radiolaria`
**8162 篇 PDF / 62 GB / 33 个子目录**，按子目录**比例分层抽样 319 篇**（固定种子），
其中 **272 篇有文本层**（47 篇纯扫描件剔除），解析出 **1139 条图注**，
另抽 **40 篇的 376 张嵌入图**做配色统计。

**核心实测结论**：
- 🔴 **93% 的图是灰度**（349/376），图内平均饱和度中位数 = 0.000 —— 分组靠**形状/灰度/花纹**，不靠颜色
- 🔴 图注前缀 **"Fig." 占 67%**，"Figure" 仅 20%
- **71%** 用 Fig. 制、**19%** 用**图版（Plate）**制、**18%** 两者兼有
- 地质体用**黑白花纹**（点/斜线/实心深灰），地图带**比例尺 + 指北针 + 插图定位图**
- Micropaleontology 的图件标签是 **"TEXT-FIGURE"** 而非 "Fig."
- 英文子集（N=179）前置要素覆盖率：References 66% / Abstract 53% / Acknowledgements 53% /
  **Keywords 仅 23%** —— 本领域**不普遍要求摘要与关键词**，不能按通用 SCI 模板硬套

**新增内容**：四类主题的章节骨架（含 A 类系统描述的
**Holotype → Paratype → Description → Discussion** 四段式）、面板字母体系
（"Figure 2N-S."、正文 "(Fig. 2C and D)"）、图注来源声明
（From / Slightly modified from / modified from / Original.）、
地质图制式、图版规则、交稿自查表（13 条）。

⚠️ **口径声明**：所有比例都标注了样本量与测量限制（词频近似、仅前 30 页、纯矢量图未计入配色统计）。

### 其他

- SKILL.md 新增「🔴 微体古生物 / 放射虫论文的写作与制图模式」章节；
  铁律 0 期刊表补 **Micropaleontology** 行；触发词补充微体古生物相关词
- `evals/evals.json` 升到 1.4.0，新增 **R08-micropaleo-patterns**，
  `must_not` 锁死"给分类描述论文配彩色编码表"

## [2.8.0] — 2026-11-01

### 🔴 剩余期刊全部按「官方原文」标准复核

延续 v2.7.0 的原文优先规则，把 `multi-journal-style-guides.md` 里其余各刊逐本过了一遍，
每本都读官方页/官方 author kit，**逐字英文原文**追加为「📌 官方原文速查（verbatim）」小节。

| 刊 | 官方来源 | 取到的原文要点 |
|---|---|---|
| **Nature** | nature.com formatting-guide | 印刷页数、summary paragraph 200 词、Title 75 字符、Refs ≤50、Methods ≤3,000 词、90/180/170 mm、lower-case 标注、scale bars、12-pt TNR、line numbers、Reporting Summary |
| **PNAS** | pnas.org authors/submitting-your-manuscript | 体裁页数与字数、Significance Statement ≤120 词、Abstract ≤250 词、Title <135 字符、稿件顺序、图件 dpi（300 / 600–900 / 1000–1200）、图注写法 |
| **CVPR/ICCV/3DV** | cvpr.thecvf.com + 官方 author kit `sec/2_formatting.tex` | 8 页上限、模板与匿名硬拒、版面尺寸与边距、Times 字号体系、图注位置、**色觉友好条款** |
| **Palaeoworld** | elsevier.com Palaeoworld guide | 期刊定位、接受体裁、学科范围 |
| **APP** | app.pan.pl/instruction.html | 稿件构成、Brief report 篇幅、183/89/237 mm、图注与面板字母、400 dpi、照片黑底、ZooBank/IPNI、标本存放、版面费 |
| **PE** | palaeo-electronica.org contributor instructions | PDF 单文件投稿、175/84 mm @300 ppi（首投可 150）、8 pt 字号下限、对比度、编号与面板字母 |
| **PalZ** | link.springer.com/journal/12542 | 三种体裁与各自篇幅、single-blind、Abstract 150–250 词、author-year 引注、EPS/TIFF 图件与字体嵌入 |
| **Elsevier 微体古生物系** | 同 ESR 模板 | 改为**指针**：直接引用 §一 ESR 原句，不重复抄录 |
| **JM / Copernicus** | Copernicus 平台投稿说明 | v2.7.0 已逐字核对 |

### 🔴 又修正一处过度断言：PNAS 摘要「单一段落」

本次逐字核对 PNAS 官方页时发现：**该页全文没有出现 "paragraph" 一词**。
官方只要求 "Explain to the general reader the major contributions of the article /
Include no more than 250 words / Cite all references in the abstract in full within
the abstract itself AND in the text"。
v2.6.0 的「🔴 ≤250 词，单一段落」**同样是无依据的断言**，已删除。

### 目录状态与文件头同步

- 目录「状态」列逐刊标注复核日期与获取状态
- **Paleobiology 标 🟡**：Cambridge 官方页被 cookie 墙拦截，本次**未取到英文原句**，
  其内容仍为 2026-10-16 核验版，引用前请回官方页确认（不拿转述冒充原文）

## [2.7.0] — 2026-11-01

### 🔴 新规则：期刊硬规则一律用官方原文

转述会丢限定词与强度词（required / encouraged / must / may），还会凭空造出原文没有的要求。
本仓库因此立规矩：**`references/` 里每条期刊硬约束都附官方英文原句（verbatim）**，
中文只作定位标注，**转述不算数**；AI 回答时直接引原句。

- `AGENTS.md`「维护约定」新增该条，并说明来源可回查
- `SKILL.md` 铁律 0 之后新增同款提示
- `multi-journal-style-guides.md` 文件头新增写法约定

### ESR / JM 两节改为逐字英文原文

- **ESR（第一章）**：1.1 收录边界、1.2 文章类型与字数、1.3 前置要素、1.4 文件格式与行号、
  1.5 结构、1.6 图表、1.7 其他 —— 全部改为「中文要点 + 官方原文（verbatim）」两列结构
- **ESR 新增 1.8 参考文献（author-date 制）**：13 条官方原文，覆盖文末排序、
  摘要引用须完整给出、DOI、数据集引用六要素、预印本标注等
- **JM（第十章）**：图件硬参数、色觉无障碍、表格/地图/日期/附录条款改为逐字原文

### 图件设计体系补蓝本原文锚点

`references/figure-design-system.md` 新增「🔖 蓝本原文锚点（verbatim）」：
Fig 1/3/4/6/7/8/9/10/12/13/14 的**图注原句**、正文中「manual (red) versus
automated (purple)」的**颜色声明原句**、Fig 2 与 Fig 5 的**图注诚实性写法原句**，
并声明"颜色语义要写进正文"这条规则的原文依据。

### 回归测试

- `evals/evals.json` 的 R07 改为**必须引用官方英文原句**
  （"without any limitation on the number of words used"、"does not exceed 250 words"、
  "encouraged"、"Bibliometric studies will not be considered"），
  `must_not` 增加"用中文转述代替官方英文原句"

## [2.6.0] — 2026-11-01

### 🔴 修正：两条在官方原文中查无依据的断言（ESR 复核发现）

重新逐字核对 ESR 官方 guide-for-authors 后，发现两处过度断言：

- 🔴 **「摘要必须写成单一段落」→ 删除**。官方摘要段原文只要求
  "concise and factual abstract that does not exceed 250 words" + 能独立成篇
  （stand alone）+ 避免引用 + 避免非常用缩写，**通篇没有 single paragraph 要求**。
  已同步修正 4 处：`multi-journal-style-guides.md`、`prompts-en/01-abstract.md`、
  `prompts-en/03-literature-review.md`、`prompts-en/09-journal-submission.md`。
- 🔴 **「Highlights 是硬性要求」→ 降级为「鼓励提供」**。官方措辞是
  "You are **encouraged** to provide article highlights at submission"，
  并非 required。格式数字（3–5 条、每条 ≤85 字符、单独可编辑文件）不变。

### 新增：ESR 章节按官方原文重写并扩充

`references/multi-journal-style-guides.md` 第一章（ESR）于 **2026-11-01 逐字复核**：

- 新增 **1.2 文章类型与字数**：Review paper 无字数上限（官方原话
  "without any limitation on the number of words used"）；>20,000 词须先邮件
  + 抄送 Tim Horscroft；**Discussion / Reply 各 ≤3,000 词、各限 1 次、6 个月 / 1 个月时限**；
  🔴 **Invited Review Article 仅限受邀**
- 新增 **1.3 前置要素**：Abstract 为 **required**（含 4 项内容要求）、
  Keywords 1–7、Highlights 为 **encouraged**、Data statement **required at submission**、
  生成式 AI 声明、🔴 **Covering letter 须附「近期该主题论文清单」**
- **1.6 图表**补官方 "Do not submit" 三条（分辨率过低 / 文字相对过小 /
  多图合并——仅比较用图组例外）与 Captions 写法、Text graphics 规则
- 刊页指标更新：**IF 11.3 / CiteScore 20.8**（官方刊页 2026-11），
  替换原来的模糊阈值 "IF > 10"

### 回归测试

- `evals/evals.json` 升到 1.3.0，新增 **R07-esr-guide**，
  `must_not` 直接锁死上面两条过度断言（防回归）

## [2.5.0] — 2026-11-01

### 新增：图件设计体系（第三层参考）

以 **Hayat et al. 2026, *J. Micropalaeontology* 45: 95–116**（DOI 10.5194/jm-45-95-2026）
为蓝本，逐像素拆解其 **14 张图**，新增 `references/figure-design-system.md`：

- **图序即论证顺序**：方法 → 数据/对象 → 模型性能 → 误差案例 → 一致性（换 3 种量纲）
  → 生态/业务意义 → 成本/效率
- **五种图件原型**：A 流程图 / B 图像对照版 / C 性能矩阵 / D 成对比较 / E 回归排序，
  每种给出「必备元素」
- **实测语义色字典**（逐像素统计，非目测）：人工 `#D30203`、AI `#75489A`、
  单系列 `#F6A100`、环境量 `#308E2C`、单色阶 `#093576` → `#00509D`；
  背景语义带与凸包浅填充单列
- **版式规范**：面板字母、物种名斜体、R² 位置、1:1 虚线、图例一次讲完
- **图注模板** + **交稿自查表**

### 新增：J. Micropalaeontology / Copernicus 平台口径

- `references/multi-journal-style-guides.md` 新增第十章（横向对比顺延为十一、十二）
- 已核实的图件硬参数：**300 dpi**、**单图 <5 MB / 全文件 <30 MB**、**图宽 ≥8 cm**、
  **复合图合并成单文件**、**图例必须画在图里**、**须过 Coblis 色觉模拟器**、
  矢量优先且字体须嵌入
- `references/journal-constraints.md` 对照表 + 期刊梯队表补 JM 行
- 🔴 **口径声明**：图件条款取自 Copernicus 平台官方投稿说明页（JM 同用
  `copernicus.cls` 与同一份条款，并已由该刊已刊论文 PDF 交叉印证单栏版心 177 mm）；
  **JM 专属字数 / 篇幅 / 摘要长度不复述**，以官网 Author guidelines 为准

### 新增：SKILL.md 的图件设计体系入口

- 新增「🔴 图件设计体系（图序 → 原型 → 语义色）」章节
- 铁律 0 期刊表补 **J. Micropalaeontology** 行
- 描述补触发词：配色方案 / 图序怎么排 / 图注怎么写 / J. Micropalaeontology / JM / 混淆矩阵画法

### 回归测试

- `evals/evals.json` 升到 1.2.0，新增 **R04 / R05 / R06** 三条用例，
  覆盖「图序与原型」「语义色字典」「JM 图件硬参数」
- `evals/README.md` 覆盖模块表同步更新

## [2.4.1] — 2026-10-19

### 🔴 修复（`check_markdown.py` 死代码已修）

- **`scripts/check_markdown.py` 表格列数检查死代码已修复**：
  第 4 项的 `hdr = ...` 缩进与 `if in_fence:` 块的 `continue` 同级，整段永不可达。
  修复方式 = **加表头门控**（`lines[i].startswith("|")` + 次行为分隔行）
  **而非仅删 `continue`** —— 后者会在 31 个真表格上产生 210 行假阳性。
- **默认改为扫描全仓库**（原只检查 6 个根级文件），
  **33 个 references/prompts 文件从此纳入结构检查**
- 新增检查项：`<details>` 配对、H1 数量、行尾空白、制表符；
  管道符计数改为忽略行内代码与 `\|` 转义
- **删除 `scripts/check_md_full.py`** —— v2.4.0 为补缺口临时新增，
  现已合并进 `check_markdown.py`，两套规则并存会导致结论漂移。
  U+FFFD 检查仍由 `check_encoding.py` 专门负责，不重复。

### 校验脚本自检

新 `check_markdown.py` 用**已知坏样本**验证过（先证明工具是对的）：
- 坏样本 6/6 全部抓到（未闭合围栏 / details 不配对 / 标题跳级 /
  表格列数错 / 多 H1 / 行尾空白+制表符）
- 好样本 5/5 无假阳性（正常表格 / 正常围栏 / `\|` 转义 /
  references 下多 H1 / prompts 下多 H1）
- 全仓库扫描 0 误报

### 修正（读全 26 张顶刊 Figure 后发现 v2.4.0 的过度概括）

- **「对照冷色 / 处理暖色」从铁律降级为「目标期刊惯例」**
  🔴 原表述有实证反例：Cell 系列用对照=蓝灰、处理=粉；
  但 **Cell Metabolism 的 WW（对照）用红、KK（处理）用蓝，与之相反**。
  唯一硬标准改为**色相全图可追溯**。

### 新增

- **形状维度**：阴性对照 / 无显著差异用**空心 ○**，不必另配第三种颜色。
  空心 = 「预期中的无效应」，读者一眼知道"这组本该没反应"
- **气泡图三通道编码**：颜色深浅=−log₁₀(p)、大小=Gene Count、X=GeneRatio。
  这不违反「一通道一变量」——轴已表达 GeneRatio，颜色才被腾出来表达显著性
- **背景色块只表类别**，不参与数值编码（判断标准：去掉色块应减少类别信息，而非改变数值解读）
- **热图必须带色标条 + 两端数值 + 变量名**。
  实证：同一篇论文里两张热图色标方向**相反**（蓝-白-红 vs 橙-白-蓝），读者无法靠猜
- **图内符号矩阵**标注组别（`VIDA: + + -` / `NS2B3: - + +`），比图例框省空间
- **小倍数图共用一个图例**，各图上方标 `ns` / `****`
- **图像阵列组别顺序必须与图例一致**（IHC：组名在上、标记名在左）
- **多系列堆叠柱须说明色块排序依据**（如按 Pre→Post 变化量降序）
- **log 轴 + 阈值线 + 个体散点**：浓度/时间序列的标准做法

### 修正

- 检查清单从 12 条扩到 **19 条**
- 地学适配表更新：移除「对照冷/处理暖 直接用」，
  新增「图内符号矩阵（地学少用）」「小倍数图共用图例（直接用）」
- 来源声明补第三篇 **Cancer Cell 2026;44:1549-1567.e12**
- README 配色章节摘要同步修正

### 维护说明

⚠️ 本次修订源于一次**方法论错误**：初版结论基于 26 张图中的 5 张（抽样），
复核时又误把「已下载 26 张」当作「已阅读 26 张」，实际分三批才读完。
新增的规则全部来自**补读的 21 张**。
**教训：说"读完了"之前必须核对清单，不能把下载量当阅读量。**

## [2.4.0] — 2026-10-19

### 新增

- **`references/color-system.md`** —— 配色系统与视觉编码（11 节）。此前
  `figure-specs.md` 只给色号表，没有配色**决策逻辑**。新增内容：
  - 铁律：配色是**语义系统**不是审美选择（判据：拿掉图例能否判断组别）
  - 🔴 对照冷色 / 处理暖色，**色相在全图所有面板必须固定**
  - 🔴 一个颜色只能承载一个含义（柱状图颜色深浅不能重复表达数值）
  - 🔴 色相编码主变量、明度编码次变量
  - 🔴 基因型用**色温编码版面**（冷暖分屏底色），省去反复对照图例
  - 🔴 连续数据用**感知均匀色阶**（禁 jet / 红绿渐变），发散色阶以 0 为中心
  - 🔴 荧光通道固定色 + 红绿并置必配第二重线索
  - 显著性星号保持中性色（染色会被误读为组别）
  - **12 条配色一致性检查清单**（含灰度/打印检验）
  - **地学场景适配表**：荧光规则不适用；地层柱状图颜色只编码时代不编码岩性
- **`scripts/check_md_full.py`** —— 全量 Markdown 结构体检（8 项检查）。
  🔴 **原 `check_markdown.py` 只检查 6 个根级文件，33 个 references/prompts
  从未被结构检查过**；且其表格列数检查是死代码，从未执行。
  新脚本覆盖全部 39 个文件：围栏配对 / details 配对 / 标题跳级 /
  表格列数（**带表头门控**）/ U+FFFD / `\|` 转义计数 / H1 数量 / 行尾空白+制表符。

### 修复

- 🔴 **`references/论文写作方法论骨架.md` L633 表格列数错误**：
  行首为 `| | **write draft** | 8 | ... |`，比表头 `| Stage | # | Step |`
  多一个管道符（Stage 列后多出空单元格），GitHub 渲染时该行错位。
  已修为 `| **write draft** | 8 | ... |`，与同表 `develop structure` 行同构。
  ⚠️ **此 bug 逃过了 CI** —— `check_markdown.py` 对它报 PASS，正是死代码所致。
- 🔴 **`check_markdown.py` 表格检查死代码**：第 4 项的 `hdr = ...` 缩进与
  `if in_fence:` 块的 `continue` 同级，整段永不可达。
  实测：仓库 6 个文件全 PASS；把该逻辑抽出单独跑，因缺少 `|` 开头门控，
  在 31 个真表格上产生 **210 行假阳性**。
  **注意**：仅删除 `continue` 是错的 —— 会立刻产生 210 行假阳性淹没真问题。
  正确修法是加表头门控。本版暂未改此脚本，改由 `check_md_full.py` 补齐检查。
  > 📌 **后续**：v2.4.1 已按正确方式修复 `check_markdown.py` 本身，
  > 并删除临时脚本 `check_md_full.py`（功能已合并）。

### 重构

- **README 全面重构**：
  - 新增 **🎨 配色系统**章节（首次在前台呈现配色方法论）
  - TL;DR 改为 **v1.0 vs v2.4 对比表**，取代原来的「v2.x 新增」清单
  - 十模块表格改为**可点击链接**（原来只有行内代码，不可点）
  - 期刊硬约束表补入 PPP / APP / PE 的关键约束（原来只有 GCA / ES&T / Paleobiology / PalZ）
  - 兼容性表补齐 Windsurf / Roo / Cline / VS Code / Zed / Warp（原表 12 行，COMPATIBILITY.md 有 14 条）
  - 徽章补 `📚 10 References`，工具数 10 → 12，版本 → v2.4.0
  - FAQ 合并 v1/v2 对比（原占一整节），新增「贡献代码前要跑什么」
  - 删除 L214-216 的**重复分隔符**（`---` 连续出现两次）
- 修正结构树 `03-literature-review.md` 缩进不齐

### 维护约定更新

- 跑校验脚本时，AGENTS.md 的清单需补上 `python3 scripts/check_md_full.py`

## [2.3.2] — 2026-10-17

### 新增
- **`opencode.json`** —— 对齐同类仓库做法，把 `AGENTS.md` 与 `skills/academic-paper-polish/SKILL.md`
  注册进 `instructions`。此前 README 只教用户「自己写一个」，仓库本身并没有该文件，
  是当初借鉴清单里唯一漏落地的一项。

### 文档
- README「方式四」改为「仓库已自带 opencode.json」，并说明已有配置时如何合并
- `docs/COMPATIBILITY.md` opencode 行的「专属规则文件」列补上 `opencode.json`
- `AGENTS.md` 仓库结构树补 `opencode.json`

### 核查结论（未改动）
逐条复核借鉴清单 6 项，全部已落地；另核实两项曾被我误判为「差距」的：
- **description 437 字符不算冗余** —— 官方 Agent Skills 规范明确鼓励 description
  包含具体关键词以帮助 agent 识别任务，本 skill 含 160 字符触发词，符合推荐做法。
- **`check_skill.py` 已完整覆盖 name 全部约束** —— 实测 7 个样本（含 `-pdf`、`pdf-`、
  `pdf--processing`、`PDF-Processing` 等官方明令非法者）全部正确拒绝。

## [2.3.1] — 2026-10-17

### 🔴 修复
- **README 整段内容丢失**：先前用脚本重建「仓库结构」代码块时，正则跨度过大，
  把从树开头到下一个围栏之间的内容一并替换掉，导致
  「🧩 十模块」模块表尾与整个「🔴 八条硬规则」章节（1️⃣–5️⃣）被误删，
  并使围栏数变成奇数（21）→「讨论六步」代码块被提前闭合、后续内容渲染错乱。
  已从损坏前的提交取回原文并更新其中路径，现围栏 22 个全部配对。
  ⚠️ 该损坏曾随 `bcb542d` 推送到 GitHub。

### 新增
- `scripts/check_markdown.py` —— Markdown 结构体检：围栏配对、`<details>` 配对、
  标题层级跳级、表格列数一致性（均跳过代码块内部，避免把 `# shell 注释` 当标题）。
- `scripts/check_anchors.py` —— 校验 README 内部锚点是否指向真实标题
  （按 GitHub slug 规则生成锚点集合）。
- CI 增跑上述两项，README 结构问题今后不会再漏到 main。

### 修复
- **README 顶部导航锚点全部失效**：GitHub 对 emoji 是删除后留下其后的空格转为的连字符，
  正确锚点形如 `#快速开始-quick-start`（无前导连字符），
  原写作 `#-快速开始-quick-start` 双连字符 → 六个链接全部点不动。已按实测规则改正。
- 补全顶部导航遗漏的两节（`🔴 八条硬规则`、`📐 技术检查卡口`）；
  移除不存在的 `#-安装-install`（无对应标题）。

### 内容校正（与仓库实际状态对齐）
- 版本号徽章 `v2.0.0` → `v2.3.0`（原与 SKILL.md 的 version 不一致）
- 「6 份深度参考」→ **9 份**（实际 references 为 9 个文件）
- 「11 个 AI 工具」→ **10 个**（兼容性表实际 10 条；Codex/Cursor/Copilot/opencode/
  Qoder/ZCode/MiniMax Code/Gemini CLI/Aider/Claude Code），徽章同步改为 `10_AI_Tools`
- 正文与 FAQ 中的「v2.0」表述改为「v2.x」，避免每次升版都要改

## [2.3.0] — 2026-10-17

### 修复
- 🔴 **修正安装说明在嵌套布局下失效**：README「方式二」原为把整个仓库 clone 成
  `~/.claude/skills/academic-paper-polish`，重构后 SKILL.md 已下沉到
  `skills/academic-paper-polish/`，照旧安装会多套一层目录，**客户端发现不了入口、静默不生效**。
  现改为整目录拷贝 `cp -R /tmp/app/skills/academic-paper-polish <skills 目录>/`，
  并列出 Claude Code / WorkBuddy / Codex / opencode / Cursor 五个目标路径 + 一行安装验证命令。

### 改动
- `AGENTS.md` 仓库结构树重建（补 `scripts/`、`evals/`、`agents/`、两个中文 references 文件，修正缩进）
- `README.md` 仓库结构树重建，与 `AGENTS.md` 对齐
- `SKILL.md` metadata：`version` 2.0.0 → 2.3.0；字段 `source_courses` → `source_material`，
  去掉"课件"表述，与「这是 agent skill、不是课件总结」的定位一致
- `scripts/check_links.py` 消除假阳性：扫描链接前先剥离围栏代码块与行内代码
  （其中的链接语法是示例文本，不是真实链接 —— 首版 CI 就因此把文档里的
  `[x](y)` 示例误判成断链而失败）；另跳过含通配符的路径模式；
  `CHANGELOG.md` 中的行内代码路径不再按当前链接校验（变更日志按设计要记录
  "改动前"的旧路径与已删除文件），但其中的真实链接仍然校验

## [2.2.0] — 2026-10-17

### 改动
- **目录布局对齐 Agent Skills 官方规范**：`SKILL.md`、`references/`、`prompts/`、`prompts-en/` 全部移入
  `skills/academic-paper-polish/`，使 skill 自包含、支持整目录拷贝安装。
- **新增 Codex 接口声明**：`skills/academic-paper-polish/agents/openai.yaml`
  （`interface.display_name` / `short_description` / `default_prompt`）。
- **新增可执行校验脚本** `scripts/`：
  - `check_skill.py` —— 校验 frontmatter（`name` 与目录名一致、长度与字符集）、
    description 长度、正文行数上限、`references/*.md` 引用存在性。
  - `check_links.py` —— 校验根级 Markdown 本地链接可解析。
  - `check_encoding.py` —— 拦截 U+FFFD 编码损坏。
- **新增 CI**：`.github/workflows/spec-consistency.yml`，push / PR 时自动跑上述三脚本。
- **新增学术引用文件** `CITATION.cff`。
- **新增评测集** `evals/`（`evals.json` + `README.md`）。

### 内容补录（此前遗漏的图内文字）
- 学位论文写作整节：高校写作规范结构、**GB/T 7714-2015** 引用标准、CNKI 学位论文范例检索、
  **硕士同行评议评分表（A1–A5 + 规范性 20 分）**。
- Review 版式四页完整范例（Nature 栏目横幅 → 图注竖线格式 → References → back-matter 结构）。
- PPP 图表硬参数细化：**dpi 三档（照片 300 / 线条图 1000 / 混合图 500）**、面板标签规范、
  **Palaeo-3 不允许 Plates**、地图禁止政治争议边界、Graphical Abstract 最小 531×1328 px。
- 行号连续编号规则、Introduction/Discussion 禁四级标题、研究点位坐标规则。
- 时间单位精确规则：**Ma/ka/Ga vs Myr/kyr/Gyr**、>2500 Ma 用 m.y.、**cal. B.P.** 近 5 万年强制校准。
- 引用格式细节（a/b/c 区分、同姓同年加首字母）、文献三层排序算法。
- 检索实操：中英双语关键词、**「作者+主题词+期刊+年份」混合检索串**、被引次数二次查询（滚雪球）。
- 素材库方法：批注式参考库（英文原文 + 中文逐段批注）、辨证阅读笔记模板。
- **TREE 综述提案真实要求**：300–600 词 point-by-point + 10–20 篇近 2–4 年关键文献 + 与近 3 年已有综述的差异化说明。

### 规范清理
- 删除纯出处索引文件 `references/course-sources.md`
- 剥离全部幻灯片页码引用与提取过程标注，改为中性技能表述

## [2.1.0] — 2026-10-16

### 新增
- `prompts-en/`：10 个英文 prompt 模块，**每文件自包含**（单文件复制进任意 LLM 即可用，不依赖仓库其他文件）
- `docs/PROMPTS-EN.md` 重写为英文入口

### 改动
- `SKILL.md`、`AGENTS.md`、`README.md`、`COMPATIBILITY.md` 模块表改为**中英双列**

## [2.0.0] — 2026-10-16

### 新增
- 跨平台兼容层：`AGENTS.md`（单一事实源）、`CLAUDE.md`（`@AGENTS.md` shim）、
  `.cursor/rules/*.mdc`、`.qoder/rules/*.md`、`docs/COMPATIBILITY.md`
- `references/multi-journal-style-guides.md`：9 份官方 style guide 汇总
- `references/journal-constraints.md` 新增地质年代硬规则

### 修复
- 🔴 **修正 `SKILL.md` 的 `name` 与目录名不一致**（原 `paper-polish-prompts` ≠ 目录
  `academic-paper-polish`）——该不一致会导致技能**静默加载失败**

## [1.0.0] — 初始版本

- 10 个中文 prompt 模块 + 8 个 references 文件
