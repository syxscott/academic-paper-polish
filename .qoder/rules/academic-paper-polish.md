# Qoder / QCode Rule

> 规则来源：[AGENTS.md](https://github.com/syxscott/academic-paper-polish/blob/main/AGENTS.md) —— 单一来源。
> Qoder **原生读取 `AGENTS.md`**，本文件为可选的显式规则层。

## 规则摘要

本仓库提供学术论文写作、润色、改稿与投稿的全流程 AI 辅助，共 10 个 prompt 模块。

### 模块索引

| # | 模块 | 触发场景 |
|---|---|---|
| 1 | 摘要 | 润色 / 压缩摘要 |
| 2 | 引言 | 倒金字塔 · 缺口论证 |
| 3 | 文献综述 | 主题整合 · 批判分析 |
| 4 | 研究方法 | 可复现性审查 |
| 5 | 结果 | 客观性 · 图表规范 |
| 6 | 讨论 | 结果↔文献对话 · 局限 |
| 7 | 结论 | 升华 · 不引入新信息 |
| 8 | 去 AI 化 | 终稿通篇润色 |
| 9 | 期刊匹配与投稿 | 先定期刊再动笔 |
| 10 | 审稿意见回复 | 逐条答复 |

文件路径：`skills/academic-paper-polish/prompts/01-abstract.md` … `skills/academic-paper-polish/prompts/10-reviewer-response.md`

### 🔴 八条硬规则

1. **先定期刊再动笔** —— GCA 要求 Results/Discussion 分离；ES&T 合并且禁用独立结论段
2. **引言 = 倒金字塔**，opening 必须与 resolution 对齐
3. **引文密度** —— Intro 除问题句外都要引文；Results 几乎无引文；Discussion 每段 5–8 句（1 topic + 3–4 带引用 + 2–3 自己数据）；Abstract/Conclusion 不引文
4. **段落 5–8 句**最合理
5. **讨论六步**，含"表明局限性"
6. **结论含局限性 + 未来方向**
7. **文献五误区** —— 知而不引 / 断章取义 / 引而不确 / 来源不实 / 盲目自引

### 🔴 内容红线

不得改数据、改结论、引入未经证实的推测、编造文献、保证过 AI 检测。

**改稿保留原意**：措辞与结构可改，数据与科学主张不可改。遇到越线要求时说明风险并拒绝该部分，继续完成其余部分。

### 🔴 图表硬参数

300 dpi 至少 · 单图 <10 MB · 总 <50 MB · 图宽单栏 <85 mm / 双栏 <180 mm · **Word 中严禁拉对角线缩放** · 图注自明 · 连续行号。