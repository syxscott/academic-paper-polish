# -*- coding: utf-8 -*-
"""校验 README 内部锚点链接是否指向真实存在的标题。

GitHub 锚点规则：标题文本转小写 -> 去掉标点 -> 空格转连字符；
emoji 被当作标点删除（但其后若原以空格分隔，会留下该空格转成的连字符）。

用法：python3 scripts/_check_anchors.py [file.md]
"""
import io
import re
import sys
import unicodedata

HEADING = re.compile(r"(?m)^(#{1,6})\s+(.*?)\s*#*\s*$")
ANCHOR_LINK = re.compile(r"\[([^\]]*)\]\(#([^)]+)\)")


def slug(text):
    s = text.strip().lower()
    out = []
    for ch in s:
        if ch in " \t":
            out.append("-")
        elif unicodedata.category(ch)[0] in ("L", "N"):
            out.append(ch)
        elif ch == "-":
            out.append("-")
        # 其余标点/emoji 丢弃
    slug_text = "".join(out)
    return re.sub(r"-+", "-", slug_text).strip("-")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    text = io.open(path, encoding="utf-8").read()

    # 去掉代码块，避免把示例里的 # 当标题
    stripped = re.sub(r"(?ms)^(```|~~~).*?^\1", "\n", text)

    anchors = set()
    for m in HEADING.finditer(stripped):
        anchors.add(slug(m.group(2)))

    bad = []
    total = 0
    for m in ANCHOR_LINK.finditer(stripped):
        total += 1
        target = m.group(2).strip().lower()
        if target not in anchors:
            bad.append((m.group(1), target))

    print("锚点检查: %d 个内部锚点链接 / %d 个标题" % (total, len(anchors)))
    if bad:
        print("失效锚点 (%d):" % len(bad))
        for label, t in bad:
            print("  [%s](#%s)" % (label, t))
        return 1
    print("全部锚点指向真实标题 ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
