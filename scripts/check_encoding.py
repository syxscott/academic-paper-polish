#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验仓库内 Markdown 文件无编码损坏（U+FFFD 替换字符）。

中文长文档在多次写入后易出现 U+FFFD，本脚本用于 CI 拦截。

用法：
    python3 scripts/check_encoding.py

退出码：0 干净；1 存在损坏。
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
REPLACEMENT_CHAR = "\ufffd"


def main():
    bad = []
    count = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            try:
                text = open(path, encoding="utf-8").read()
            except UnicodeDecodeError as e:
                bad.append("%s (decode error: %s)" % (os.path.relpath(path, REPO_ROOT), e))
                continue
            count += 1
            n = text.count(REPLACEMENT_CHAR)
            if n:
                bad.append("%s (%d U+FFFD)" % (os.path.relpath(path, REPO_ROOT), n))

    print("Encoding check: %d markdown files" % count)
    if bad:
        print("CORRUPTED (%d):" % len(bad))
        for b in bad:
            print("  " + b)
        return 1
    print("No encoding corruption found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
