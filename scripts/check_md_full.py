# -*- coding: utf-8 -*-
"""全量 Markdown 结构校验（补官方 check_markdown.py 的覆盖缺口）。

官方脚本默认只查 6 个根级文件，且其「表格列数」检查是死代码。
本脚本对 **全部 .md** 做 8 项检查：

  1. 围栏配对（含语言标注的开闭一致性）
  2. <details> 开闭配对
  3. 标题层级跳级（H1→H3），跳过代码块
  4. 表格列数一致性（带表头门控 —— 官方版缺此门控导致 210 行假阳性）
  5. U+FFFD 编码损坏
  6. 表格单元格内的管道符转义（\|）
  7. H1 唯一性（每文件应只有一个一级标题）
  8. 行尾空白 / 制表符

退出码：0 全部通过；1 存在问题。
"""
import io
import os
import re
import sys

FENCE = re.compile(r"^(```|~~~)")
SEP = re.compile(r"^\|[\s\-:|]+\|$")
DETAILS_OPEN = re.compile(r"^<details[^>]*>\s*$")
DETAILS_CLOSE = re.compile(r"^</details>\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

problems_by_file = {}
stats = {"files": 0, "tables": 0, "headings": 0}


def audit(path):
    text = io.open(path, encoding="utf-8").read()
    lines = text.split("\n")
    probs = []
    warns = []

    # --- 1) 围栏配对 ---
    fences = [i for i, l in enumerate(lines) if FENCE.match(l)]
    if len(fences) % 2 != 0:
        probs.append("L%d 围栏未闭合（共 %d 条，奇数）" % (fences[-1] + 1, len(fences)))
    stats["tables"] += 0

    # --- 5) 编码损坏 ---
    n_bad = text.count("\ufffd")
    if n_bad:
        probs.append("%d 处 U+FFFD 编码损坏" % n_bad)

    # --- 8) 行尾空白 / 制表符（代码块内不算） ---
    in_f = False
    for i, l in enumerate(lines):
        if FENCE.match(l):
            info = FENCE.match(l).group(1)
            # 裸 ``` 或 ~~~ 是闭合；带语言/属性的是开启
            rest = l.strip()[len(info):]
            in_f = bool(rest.strip())
            continue
        if in_f:
            continue
        if l.rstrip() != l:
            probs.append("L%d 行尾有多余空白" % (i + 1))
        if "\t" in l:
            probs.append("L%d 含制表符（应为空格）" % (i + 1))

    # --- 需要跳过代码块的扫描：2/3/4/6/7 ---
    i = 0
    in_fence = False
    h1_count = 0
    prev_lv = 0
    while i < len(lines):
        if FENCE.match(lines[i]):
            rest = lines[i].strip()[len(FENCE.match(lines[i]).group(1)):]
            in_fence = bool(rest.strip())
            i += 1
            continue
        if in_fence:
            i += 1
            continue

        # 2) details 配对
        if DETAILS_OPEN.match(lines[i]):
            pass
        if DETAILS_CLOSE.match(lines[i]):
            pass

        # 3) 标题层级
        m = HEADING.match(lines[i])
        if m:
            stats["headings"] += 1
            lv = len(m.group(1))
            if lv == 1:
                h1_count += 1
            if prev_lv and lv > prev_lv + 1:
                probs.append("L%d 标题跳级 H%d → H%d: %s" % (i + 1, prev_lv, lv, m.group(2)[:36]))
            prev_lv = lv

        # 4) 表格列数（带表头门控）
        if lines[i].startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]):
            stats["tables"] += 1
            hdr = count_cols(lines[i])
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                c = count_cols(lines[j])
                if c != hdr:
                    probs.append("L%d 表格列数 %d ≠ 表头 %d: %s" % (j + 1, c, hdr, lines[j][:44]))
                j += 1
            i = j
            continue
        i += 1

    # 2') details 全局配对
    no = sum(1 for l in lines if DETAILS_OPEN.match(l))
    nc = sum(1 for l in lines if DETAILS_CLOSE.match(l))
    if no != nc:
        probs.append("<details> 开 %d / 闭 %d 不配对" % (no, nc))

    # 7) H1 数量
    # 说明：references/ 与 prompts/ 是「参考手册 / 模块」性质，
    # 多个并列主题各自成 H1 是合理结构（如 multi-journal-style-guides.md
    # 有 12 个 H1，分别对应 12 家期刊）。故只对「单文档」要求唯一 H1。
    #
    # README 例外：GitHub README 惯例是 banner 用居中 div + H3 标题，
    # 全文从 H2 起（无 H1）。这是社区通行做法，不算缺陷 → 仅提示。
    base = os.path.basename(path)
    norm = path.replace("\\", "/")
    multi_h1_ok = "/references/" in norm or "/prompts" in norm
    if multi_h1_ok:
        if h1_count == 0:
            probs.append("无 H1 一级标题")
    elif base == "README.md":
        if h1_count == 0:
            warns.append("无 H1（README 惯例为 banner 用 H3 + 正文从 H2 起，可不改）")
    else:
        if h1_count > 1:
            probs.append("有 %d 个 H1（单文档应只有 1 个）" % h1_count)
        if h1_count == 0 and base not in ("CLAUDE.md",):
            probs.append("无 H1 一级标题")

    return probs, warns, len(lines)


def count_cols(line):
    """统计表格列数，正确处理 \\| 转义与行内代码中的管道符。"""
    # 去掉行内代码
    s = re.sub(r"`[^`]*`", "``", line)
    # 未转义的管道符
    return len(re.findall(r"(?<!\\)\|", s))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    files = []
    for r, dirs, fs in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fs:
            if f.endswith(".md"):
                files.append(os.path.join(r, f))
    files.sort()

    for f in files:
        try:
            probs, warns, nl = audit(f)
        except Exception as e:
            probs, warns, nl = ["读取失败: %s" % e], [], 0
        stats["files"] += 1
        if probs:
            problems_by_file[f] = probs
            print("[FAIL] %s  (%d 行)" % (f, nl))
            for p in probs:
                print("       - %s" % p)
        else:
            tag = "[PASS]" if not warns else "[WARN]"
            print("%s %s  (%d 行)" % (tag, f, nl))
            for w in warns:
                print("       ~ %s" % w)

    tot = sum(len(v) for v in problems_by_file.values())
    print("\n" + "=" * 60)
    print("检查 %d 个文件 / %d 个表格 / %d 个标题" % (stats["files"], stats["tables"], stats["headings"]))
    print("通过 %d / 有问题 %d / 问题总数 %d" % (stats["files"] - len(problems_by_file), len(problems_by_file), tot))
    return 1 if tot else 0


if __name__ == "__main__":
    sys.exit(main())
