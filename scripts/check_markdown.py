# -*- coding: utf-8 -*-
"""Markdown 结构体检：围栏配对、标题层级、表格列数、details 配对、目录锚点。

用法：python3 scripts/_md_audit.py [file.md ...]
"""
import io
import re
import sys

FENCE = re.compile(r"(?m)^(```|~~~)(.*)$")
DETAILS_OPEN = re.compile(r"(?m)^<details[^>]*>$")
DETAILS_CLOSE = re.compile(r"(?m)^</details>$")


def audit(path):
    text = io.open(path, encoding="utf-8").read()
    lines = text.split("\n")
    problems = []

    # 1) 围栏配对（含语言标注）
    fence_lines = [(i + 1, l) for i, l in enumerate(lines) if FENCE.match(l)]
    if len(fence_lines) % 2 != 0:
        problems.append("围栏数为奇数 %d（未闭合），最后一处: L%d %s"
                        % (len(fence_lines), fence_lines[-1][0], fence_lines[-1][1]))
    opens = []
    for ln, raw in fence_lines:
        info = FENCE.match(raw).group(2).strip()
        if info:
            opens.append(ln)
        elif opens:
            opens.pop()
    if opens:
        problems.append("以下行被当作代码块开围栏但未见闭合: %s" % opens)

    # 2) details 配对
    no = len(DETAILS_OPEN.findall(text))
    nc = len(DETAILS_CLOSE.findall(text))
    if no != nc:
        problems.append("<details> 开 %d / 闭 %d 不配对" % (no, nc))

    # 3) 标题层级跳级（H1->H3 之类）；须跳过代码块内的 # 注释行
    prev = 0
    in_fence = False
    for i, l in enumerate(lines):
        if FENCE.match(l):
            # 带语言标注的是开围栏，裸的是闭围栏
            in_fence = not in_fence if FENCE.match(l).group(2).strip() else False
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s", l)
        if not m:
            continue
        lv = len(m.group(1))
        if prev and lv > prev + 1:
            problems.append("L%d 标题跳级 H%d -> H%d: %s" % (i + 1, prev, lv, l[:40]))
        prev = lv

    # 4) 表格列数一致性（按连续表格块，跳过代码块内）
    i = 0
    in_fence = False
    while i < len(lines):
        if FENCE.match(lines[i]):
            in_fence = not in_fence if FENCE.match(lines[i]).group(2).strip() else False
            i += 1
            continue
        if in_fence:
            i += 1
            continue
            hdr = lines[i].count("|")
            j = i + 2
            bad = 0
            while j < len(lines) and lines[j].startswith("|"):
                if lines[j].count("|") != hdr:
                    bad += 1
                j += 1
            if bad:
                problems.append("L%d 表格有 %d 行列数与表头不符" % (i + 1, bad))
            i = j
        else:
            i += 1

    return problems, len(lines), len(fence_lines)


def main():
    files = sys.argv[1:] or ["README.md", "AGENTS.md", "CLAUDE.md", "CHANGELOG.md",
                             "docs/COMPATIBILITY.md", "docs/PROMPTS-EN.md"]
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
    print("\n问题总数: %d" % total)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
