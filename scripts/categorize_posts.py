#!/usr/bin/env python3
"""Scan content/posts/*.md, infer one category + optional series from title/tags,
then insert categories: and series: fields into each frontmatter (idempotent).

Run from repo root:
    python3 scripts/categorize_posts.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "content" / "posts"

# Category rules: ordered. First match wins.
# Each rule is (category, regex-list-applied-to-title-or-tags).
CATEGORY_RULES: list[tuple[str, list[str]]] = [
    (
        "자동매매시스템",
        [
            r"자동매매",
            r"자동\s*모니터링",
            r"백테스트",
            r"stock[_-]?monitor",
            r"파이썬투자",
            r"코인자동매매",
        ],
    ),
    (
        "종목분석",
        [
            r"종목\s*분석",
            r"투자\s*분석",
            r"주가\s*분석",
            r"\(\d{6}\)",          # (123456) ticker pattern
            r"\b\d{6}\b",
            r"FC-BGA",
            r"\bPCB\b",
            r"공급망",
            r"제시\s*리버모어",
        ],
    ),
    (
        "업무자동화",
        [
            r"SCM\s*자동화",
            r"\bSCM\b",
            r"업무\s*자동화",
            r"대시보드",
            r"사내\s*자동화",
        ],
    ),
    (
        "리뷰",
        [
            r"리뷰",
            r"이세계",
            r"신작\s*애니",
            r"애니리뷰",
            r"정주행",
            r"닥터스톤",
            r"리제로",
            r"무직전생",
            r"스노우볼",
        ],
    ),
    (
        "러닝",
        [
            r"러닝",
            r"달리기",
            r"러닝\s*자세",
            r"러닝\s*폼",
            r"마라톤",
            r"조깅",
        ],
    ),
    (
        "생활후기",
        [
            r"캠핑",
            r"재활용",
            r"휘발유",
            r"남의\s*돈",
            r"생활비",
            r"분리배출",
            r"한\s*달\s*살아",
        ],
    ),
    (
        "여행기술",
        [
            r"파미르",
            r"하이웨이",
            r"실크로드",
            r"여행",
            r"가이드",
            r"AI\s*가짜",
            r"딥페이크",
            r"가짜뉴스",
            r"미디어리터러시",
            r"hantaan",
            r"cruise",
        ],
    ),
    (
        "시사이슈",
        [
            r".*",  # catch-all (last)
        ],
    ),
]

# Series rules: (series_name, regex_list). Multiple series allowed per post.
SERIES_RULES: list[tuple[str, list[str]]] = [
    (
        "AI PCB 시리즈",
        [
            r"코리아써키트",
            r"티엘비",
            r"이수페타시스",
            r"삼성전기.*MLCC",
            r"\bPCB\b",
            r"FC-BGA",
            r"패키지기판",
            r"CCL.*M7",
        ],
    ),
    (
        "자동매매 백테스트",
        [
            r"자동매매",
            r"백테스트",
            r"stock[_-]?monitor",
            r"코인.*단타",
        ],
    ),
    (
        "SCM 자동화",
        [
            r"SCM\s*자동화",
        ],
    ),
    (
        "한국 건설 안전",
        [
            r"GTX\s*철근",
            r"서소문\s*고가",
            r"무량판",
            r"노후\s*인프라",
            r"순살시공",
        ],
    ),
    (
        "스타벅스 5·18 논란",
        [
            r"정용진",
            r"탱크데이",
            r"스타벅스.*5\W*18",
            r"신세계불매",
        ],
    ),
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _split_frontmatter(text: str) -> tuple[str, str] | None:
    """Return (frontmatter_block, body) or None if no frontmatter."""
    if not text.startswith("---"):
        return None
    # Match leading --- ... ---
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return None
    return m.group(1), text[m.end():]


def _match_any(patterns: list[str], haystack: str) -> bool:
    return any(re.search(p, haystack, re.IGNORECASE) for p in patterns)


def infer_category(title: str, tags_line: str) -> str:
    hay = f"{title}\n{tags_line}"
    for cat, patterns in CATEGORY_RULES:
        if _match_any(patterns, hay):
            return cat
    return "시사이슈"


def infer_series(title: str, tags_line: str) -> list[str]:
    hay = f"{title}\n{tags_line}"
    matched = []
    for name, patterns in SERIES_RULES:
        if _match_any(patterns, hay):
            matched.append(name)
    return matched


def _yaml_list_line(key: str, items: list[str]) -> str:
    quoted = ", ".join(f'"{x}"' for x in items)
    return f"{key}: [{quoted}]"


def _upsert_frontmatter_field(fm: str, key: str, line: str) -> str:
    """Replace existing `key:` line, or append after `draft:` (or end)."""
    pattern = re.compile(rf"^{re.escape(key)}\s*:.*$", re.MULTILINE)
    if pattern.search(fm):
        return pattern.sub(line, fm, count=1)
    # Insert after `draft:` line if present, else append.
    draft_re = re.compile(r"(^draft\s*:.*$)", re.MULTILINE)
    if draft_re.search(fm):
        return draft_re.sub(rf"\1\n{line}", fm, count=1)
    return fm.rstrip("\n") + "\n" + line + "\n"


def process(path: Path, dry_run: bool) -> tuple[str, str, list[str]]:
    text = _read(path)
    parts = _split_frontmatter(text)
    if not parts:
        return ("(no frontmatter)", "", [])
    fm, body = parts

    title_m = re.search(r'^title\s*:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
    tags_m = re.search(r"^tags\s*:.*$", fm, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""
    tags_line = tags_m.group(0) if tags_m else ""

    category = infer_category(title, tags_line)
    series = infer_series(title, tags_line)

    new_fm = _upsert_frontmatter_field(fm, "categories", _yaml_list_line("categories", [category]))
    if series:
        new_fm = _upsert_frontmatter_field(new_fm, "series", _yaml_list_line("series", series))

    if new_fm == fm:
        return (category, ", ".join(series), [])

    new_text = f"---\n{new_fm}\n---\n{body}"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return (category, ", ".join(series), ["updated"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", help="Process a single post path (default: all posts)")
    parser.add_argument("--quiet", action="store_true", help="Only print updates")
    args = parser.parse_args()

    if args.file:
        single = Path(args.file).resolve()
        if not single.exists():
            print(f"File not found: {single}", file=sys.stderr)
            return 1
        files = [single]
    else:
        files = sorted(POSTS.glob("*.md"))
        if not files:
            print(f"No posts at {POSTS}", file=sys.stderr)
            return 1

    counts: dict[str, int] = {}
    for p in files:
        cat, ser, status = process(p, args.dry_run)
        counts[cat] = counts.get(cat, 0) + 1
        flag = "[DRY]" if args.dry_run else ("[upd]" if status else "[ok ]")
        ser_disp = f" | series: {ser}" if ser else ""
        if not args.quiet or status or args.dry_run:
            print(f"{flag} {cat:8s} {p.name}{ser_disp}")

    if not args.quiet and not args.file:
        print()
        print("=== Category counts ===")
        for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
