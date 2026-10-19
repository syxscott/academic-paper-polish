# -*- coding: utf-8 -*-
"""Markdown 结构体检：围栏配对、details 配对、标题层级、表格列数、H1 数量、空白规范。

覆盖 **仓库内全部 .md 文件**（默认递归扫描）。

检查项：
  1. 围栏配对（``` / ~~~）
  2. <details> 开闭配对
  3. 标题层级跳级（H1→H3），跳过代码块内部
  4. 表格列数一致性 —— 🔴 必须带表头门控，否则产生大量假阳性
  5. H1 数量（references/ 与 prompts/ 为分章手册，允许多 H1）
  6. 行尾多余空白 / 制表符

用法：
    python3 scripts/check_markdown.py                 # 扫描全仓库
    python3 scripts/check_markdown.py README.md ...    # 只查指定文件

退出码：0 全部通过；1 存在问题。

⚠️ 维护提醒：第 4 项若改动，**必须保留表头门控**
（`lines[i].startswith("|")` + 次行为分隔行）。
早期版本缺门控，在 31 个真表格上产生 210 行假阳性，把真问题淹没。
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


def count_cols(line):
    """统计表格列数：忽略行内代码中的管道符，识别 \\| 转义。"""
    s = re.sub(r"`[^`]*`", "``", line)
    return len(re.findall(r"(?<!\\)\|", s))


def is_fence_open(line):
    """带语言/属性标注的是开围栏，裸的是闭围栏。"""
    info = FENCE.match(line).group(1)
    return bool(line.strip()[len(info):].strip())


def audit(path):
    text = io.open(path, encoding="utf-8").read()
    lines = text.split("\n")
    problems = []

    # --- 1) 围栏配对 ---
    fence_lines = [(i + 1, l) for i, l in enumerate(lines) if FENCE.match(l)]
    if len(fence_lines) % 2 != 0:
        problems.append("围栏数为奇数 %d（未闭合），最后一处: L%d %s"
                        % (len(fence_lines), fence_lines[-1][0], fence_lines[-1][1]))
    opens = []
    for ln, raw in fence_lines:
        if is_fence_open(raw):
            opens.append(ln)
        elif opens:
            opens.pop()
    if opens:
        problems.append("以下行被当作代码块开围栏但未见闭合: %s" % opens)

    # --- 2) details 配对 ---
    no = sum(1 for l in lines if DETAILS_OPEN.match(l))
    nc = sum(1 for l in lines if DETAILS_CLOSE.match(l))
    if no != nc:
        problems.append("<details> 开 %d / 闭 %d 不配对" % (no, nc))

    # --- 3) 标题层级跳级 / 4) 表格列数 / 5) H1 数量（均需跳过代码块）---
    prev = 0
    h1_count = 0
    in_fence = False
    i = 0
    while i < len(lines):
        if FENCE.match(lines[i]):
            in_fence = is_fence_open(lines[i])
            i += 1
            continue
        if in_fence:
            i += 1
            continue

        m = HEADING.match(lines[i])
        if m:
            lv = len(m.group(1))
            if lv == 1:
                h1_count += 1
            if prev and lv > prev + 1:
                problems.append("L%d 标题跳级 H%d -> H%d: %s" % (i + 1, prev, lv, m.group(2)[:40]))
            prev = lv
            i += 1
            continue

        # 🔴 表头门控：必须是 "|" 开头的行，且次行为分隔行
        if lines[i].startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]):
            hdr = count_cols(lines[i])
            j = i + 2
            bad = 0
            while j < len(lines) and lines[j].startswith("|"):
                if count_cols(lines[j]) != hdr:
                    bad += 1
                j += 1
            if bad:
                problems.append("L%d 表格有 %d 行列数与表头不符" % (i + 1, bad))
            i = j
            continue

        i += 1

    # --- 5) H1 数量 ---
    # references/ 与 prompts/ 是「参考手册 / 模块」性质，
    # 多个并列主题各自成 H1 是合理结构（如 multi-journal-style-guides.md
    # 有 12 个 H1，分别对应 12 家期刊）。故只对「单文档」要求唯一 H1。
    # README 例外：GitHub 惯例是 banner 用居中 div + H3，正文从 H2 起（无 H1）。
    base = os.path.basename(path)
    norm = path.replace("\\", "/")
    if "/references/" in norm or "/prompts" in norm:
        if h1_count == 0:
            problems.append("无 H1 一级标题")
    elif base != "README.md":
        if h1_count > 1:
            problems.append("有 %d 个 H1（单文档应只有 1 个）" % h1_count)
        if h1_count == 0 and base != "CLAUDE.md":
            problems.append("无 H1 一级标题")

    # --- 6) 行尾空白 / 制表符（代码块内不算）---
    in_fence = False
    for i, l in enumerate(lines):
        if FENCE.match(l):
            in_fence = is_fence_open(l)
            continue
        if in_fence:
            continue
        if l.rstrip() != l:
            problems.append("L%d 行尾有多余空白" % (i + 1))
        if "\t" in l:
            problems.append("L%d 含制表符（应为空格）" % (i + 1))

    return problems, len(lines), len(fence_lines)


def collect(root):
    """收集指定路径下的全部 .md；无参数时扫描整个仓库。"""
    if root and os.path.isfile(root):
        return [root]
    files = []
    for r, dirs, fs in os.walk(root or "."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fs:
            if f.endswith(".md"):
                files.append(os.path.join(r, f))
    return sorted(files)


def main():
    args = sys.argv[1:]
    if args:
        files = args
    else:
        files = collect(".")
        if not files:
            print("未找到任何 .md 文件")
            return 1

    total = 0
    for f in files:
        try:
            problems, nl, nf = audit(f)
        except Exception as e:
            print("[FAIL] %s  无法读取: %s" % (f, e))
            total += 1
            continue
        if problems:
            print("[FAIL] %s  (%d 行, %d 围栏)" % (f, nl, nf))
            for p in problems:
                print("       - " + p)
            total += len(problems)
        else:
            print("[PASS] %s  (%d 行, %d 围栏配对, 标题层级连续, 表格列数一致)" % (f, nl, nf))
    print("\n检查 %d 个文件" % len(files))
    print("问题总数: %d" % total)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
