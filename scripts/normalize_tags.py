#!/usr/bin/env python3
"""Clean up frontmatter `tags:` in every post.

Fixes:
  - Strip stray `[` and `]` characters (bracket residue from old YAML).
  - Remove language marker tags (KO, EN, KO], EN]) — they pollute /tags/.
  - Apply a small alias map to merge whitespace/synonym variants.
  - Trim whitespace and dedupe within each post (preserving order).

Run from repo root:
    python3 scripts/normalize_tags.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "content" / "posts"
ALIAS_FILE = REPO / "data" / "tag_aliases.json"


def _load_aliases() -> tuple[set[str], dict[str, str]]:
    """Single source of truth lives at data/tag_aliases.json.
    Falls back to a minimal default if the file is missing so existing
    posts aren't accidentally polluted by a broken deploy."""
    fallback_drop = {"KO", "EN"}
    fallback_aliases: dict[str, str] = {}
    if not ALIAS_FILE.exists():
        print(f"[normalize_tags] WARN: {ALIAS_FILE.relative_to(REPO)} not found — using minimal fallback")
        return fallback_drop, fallback_aliases
    try:
        data = json.loads(ALIAS_FILE.read_text(encoding="utf-8"))
        return set(data.get("drop_tags", [])), dict(data.get("aliases", {}))
    except Exception as e:
        print(f"[normalize_tags] WARN: failed to parse {ALIAS_FILE.name}: {e} — using fallback")
        return fallback_drop, fallback_aliases


DROP_TAGS, ALIASES = _load_aliases()


def _yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _clean_tag(raw: str) -> str:
    t = raw.strip()
    # Strip any stray brackets that leaked from old YAML.
    t = t.lstrip("[").rstrip("]").strip()
    return ALIASES.get(t, t)


def _normalize_tag_list(tag_strs: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in tag_strs:
        clean = _clean_tag(raw)
        if not clean or clean in DROP_TAGS:
            continue
        if clean in seen:
            continue
        seen.add(clean)
        out.append(clean)
    return out


def _format_tags_line(tags: list[str]) -> str:
    quoted = ", ".join(f'"{_yaml_escape(t)}"' for t in tags)
    return f"tags: [{quoted}]"


_TAGS_LINE_RE = re.compile(r"^tags\s*:\s*(\[.*?\])\s*$", re.MULTILINE | re.DOTALL)
_TAG_VALUE_RE = re.compile(r'"([^"]*)"')


def process(path: Path, dry_run: bool) -> tuple[list[str], list[str], bool]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ([], [], False)
    fm_end = text.find("\n---", 4)
    if fm_end == -1:
        return ([], [], False)
    fm = text[: fm_end + 4]
    body = text[fm_end + 4 :]

    m = _TAGS_LINE_RE.search(fm)
    if not m:
        return ([], [], False)

    raw_tags = _TAG_VALUE_RE.findall(m.group(1))
    new_tags = _normalize_tag_list(raw_tags)

    if raw_tags == new_tags:
        return (raw_tags, new_tags, False)

    new_line = _format_tags_line(new_tags) if new_tags else None
    if new_line is None:
        # All tags dropped — remove the line entirely.
        new_fm = _TAGS_LINE_RE.sub("", fm).rstrip() + "\n"
    else:
        new_fm = _TAGS_LINE_RE.sub(new_line, fm, count=1)

    if not dry_run:
        path.write_text(new_fm + body, encoding="utf-8")
    return (raw_tags, new_tags, True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = sorted(POSTS.glob("*.md"))
    if not files:
        print(f"No posts at {POSTS}", file=sys.stderr)
        return 1

    changed_files = 0
    dropped_total = 0
    for p in files:
        before, after, changed = process(p, args.dry_run)
        if not changed:
            continue
        changed_files += 1
        dropped = [t for t in before if t.strip().lstrip("[").rstrip("]").strip() not in after
                   and _clean_tag(t) not in after]
        dropped_total += len(before) - len(after)
        flag = "[DRY]" if args.dry_run else "[upd]"
        print(f"{flag} {p.name}")
        print(f"       before: {before}")
        print(f"       after : {after}")

    print()
    print(f"=== Summary ===")
    print(f"  files changed: {changed_files} / {len(files)}")
    print(f"  tags removed (net): {dropped_total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
