#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agent Skills 规范一致性校验。

校验每个 skills/<name>/SKILL.md：
  1. YAML frontmatter 存在且可解析
  2. name 存在、<=64 字符、只含小写字母/数字/连字符，不以连字符开头或结尾、无连续连字符
  3. name 等于父目录名（否则静默加载失败）
  4. description 存在且 <=1024 字符
  5. 正文 <500 行
  6. 正文中 `references/*.md` 引用文件真实存在
  7. 存在 agents/openai.yaml 且含 interface 段（Codex 接口声明）

用法：
    python3 scripts/check_skill.py            # 校验
    python3 scripts/check_skill.py --strict   # 任何 WARN 也视为失败

退出码：0 全部通过；1 存在 FAIL。
仅依赖 Python 标准库（无 PyYAML 时用内置简易解析器）。
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

NAME_MAX = 64
DESC_MAX = 1024
BODY_MAX_LINES = 500

results = []


def record(skill, level, msg):
    results.append((skill, level, msg))


def parse_frontmatter(text):
    """返回 (frontmatter_str, body)。缺少 frontmatter 时返回 (None, text)。"""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def get_scalar(fm, key):
    """取顶层标量字段，支持 `key: value` 与 `key: >-` 折行块。"""
    lines = fm.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", lines[i])
        if m and m.group(1) == key:
            val = m.group(2).strip()
            if val in (">", ">-", "|", "|-", ">+", "|+"):
                buf = []
                i += 1
                while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                    if lines[i].strip():
                        buf.append(lines[i].strip())
                    i += 1
                return " ".join(buf)
            return val
        i += 1
    return None


def main():
    strict = "--strict" in sys.argv

    if not os.path.isdir(SKILLS_DIR):
        sys.stdout.write("FAIL: 缺少 skills/ 目录\n")
        return 1

    skills = []
    for d in os.listdir(SKILLS_DIR):
        full = os.path.join(SKILLS_DIR, d)
        if os.path.isdir(full) and os.path.isfile(os.path.join(full, "SKILL.md")):
            skills.append(d)
    skills.sort()

    if not skills:
        sys.stdout.write("FAIL: skills/ 下没有找到任何 SKILL.md\n")
        return 1

    for skill in skills:
        sdir = os.path.join(SKILLS_DIR, skill)
        text = open(os.path.join(sdir, "SKILL.md"), encoding="utf-8").read()
        fm, body = parse_frontmatter(text)

        if fm is None:
            record(skill, "FAIL", "SKILL.md 缺少 YAML frontmatter（必须以 --- 开头）")
            continue

        name = get_scalar(fm, "name")
        desc = get_scalar(fm, "description")

        if not name:
            record(skill, "FAIL", "frontmatter 缺少 name")
        else:
            if len(name) > NAME_MAX:
                record(skill, "FAIL", "name 超过 64 字符（%d）" % len(name))
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
                record(skill, "FAIL", "name 含非法字符（仅允许小写字母/数字/连字符）")
            if name != skill:
                record(skill, "FAIL", "name(%s) != 目录名(%s)，会导致静默加载失败" % (name, skill))

        if not desc:
            record(skill, "FAIL", "frontmatter 缺少 description")
        else:
            if len(desc) > DESC_MAX:
                record(skill, "FAIL", "description 超过 1024 字符（%d）" % len(desc))
            elif len(desc) < 80:
                record(skill, "WARN", "description 偏短（%d 字符），触发关键词可能不足" % len(desc))

        body_lines = body.strip("\n").split("\n")
        if len(body_lines) > BODY_MAX_LINES:
            record(skill, "FAIL", "正文 %d 行，超过 500 行上限（深度内容应移入 references/）" % len(body_lines))

        for m in re.finditer(r"`references/([^`\s]+\.md)`", body):
            rel = m.group(1)
            if not os.path.isfile(os.path.join(sdir, "references", rel)):
                record(skill, "FAIL", "正文引用的 references/%s 不存在" % rel)

        yaml_path = os.path.join(sdir, "agents", "openai.yaml")
        if not os.path.isfile(yaml_path):
            record(skill, "WARN", "缺少 agents/openai.yaml，Codex 无法识别")
        else:
            y = open(yaml_path, encoding="utf-8").read()
            if "interface:" not in y or "display_name" not in y:
                record(skill, "WARN", "agents/openai.yaml 缺少 interface.display_name")

        has = any(r[0] == skill and r[1] in ("FAIL", "WARN") for r in results)
        if not has:
            record(skill, "PASS", "全部检查通过")

    out = []
    out.append("=" * 70)
    out.append("Agent Skills 规范一致性校验")
    out.append("=" * 70)
    for skill, level, msg in results:
        out.append("[%s] %-22s %s" % (level, skill, msg))
    out.append("-" * 70)
    n_fail = sum(1 for r in results if r[1] == "FAIL")
    n_warn = sum(1 for r in results if r[1] == "WARN")
    n_pass = sum(1 for r in results if r[1] == "PASS")
    out.append("PASS=%d  WARN=%d  FAIL=%d" % (n_pass, n_warn, n_fail))
    sys.stdout.write("\n".join(out) + "\n")
    if n_fail or (strict and n_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
