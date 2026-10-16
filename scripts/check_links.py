#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 Markdown 中的本地链接是否真实存在。

扫描：
  - [text](path) 相对链接
  - `path` 形式的 references/ 引用

跳过（避免假阳性）：
  - http(s)://、#锚点、mailto:
  - 含通配符的路径模式（如 `references/*.md`，是模式不是文件）
  - `CHANGELOG.md` 中的行内代码路径 —— 变更日志按设计要记录"改动前"的
    旧路径与已删除文件，这些路径按定义不存在，不应判为断链。
    （CHANGELOG 里的真实 [text](path) 链接仍然校验。）

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
            for m in LINK_RE.finditer(text):
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
