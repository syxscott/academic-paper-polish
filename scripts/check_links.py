#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 Markdown 中的本地链接是否真实存在。

扫描：
  - 相对链接：方括号后紧跟圆括号的本地路径
  - 行内代码路径：反引号包裹的 references/ 路径

跳过（避免假阳性）：
  - http(s)://、#锚点、mailto:
  - **代码块与行内代码** —— 其中的链接语法是示例文本，不是真实链接
    （否则文档里写个例子就会被判断链）
  - 含通配符的路径模式（如 references/*.md，是模式不是文件）
  - `CHANGELOG.md` 中的行内代码路径 —— 变更日志按设计要记录"改动前"的
    旧路径与已删除文件，这些路径按定义不存在，不应判为断链。
    （CHANGELOG 里的真实链接仍然校验。）

用法：
    python3 scripts/check_links.py

退出码：0 全部可解析；1 存在断链。
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "skills"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REF_RE = re.compile(r"`(references/[^`\s]+\.md)`")

# 围栏代码块（``` 或 ~~~ 包裹）
FENCE_RE = re.compile(r"^(?:```|~~~).*?^(?:```|~~~)", re.S | re.M)
# 行内代码 `...`
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def strip_code(text):
    """去掉围栏代码块与行内代码后返回。

    反引号里的 [x](y) 是示例文本，不是真实链接，不参与链接校验，
    否则文档里写个例子就会被判成断链（假阳性）。
    """
    return INLINE_CODE_RE.sub(" ", FENCE_RE.sub("\n", text))


def main():
    broken = []
    checked = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            try:
                text = open(path, encoding="utf-8").read()
            except Exception:
                continue
            # 链接扫描基于去掉代码后的文本，避免把示例当成断链
            for m in LINK_RE.finditer(strip_code(text)):
                ref = m.group(1).strip()
                if ref.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = ref.split("#")[0]
                if not target:
                    continue
                checked += 1
                full = os.path.normpath(os.path.join(root, target))
                if not os.path.exists(full):
                    broken.append("%s -> %s" % (os.path.relpath(path, REPO_ROOT), ref))
            # CHANGELOG 记录历史路径（含已删除文件），只校验其真实链接，
            # 不校验行内代码路径，否则必然假阳性。
            if f == "CHANGELOG.md":
                continue
            for m in REF_RE.finditer(text):
                rel = m.group(1)
                if "*" in rel or "?" in rel:
                    continue  # 通配模式，非具体文件
                checked += 1
                full = os.path.normpath(os.path.join(root, rel))
                if not os.path.exists(full):
                    broken.append("%s -> %s" % (os.path.relpath(path, REPO_ROOT), rel))

    print("Markdown link check: %d local references" % checked)
    if broken:
        print("BROKEN LINKS (%d):" % len(broken))
        for b in broken:
            print("  " + b)
        return 1
    print("All local markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
