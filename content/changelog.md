---
title: "사이트 변경 이력"
date: 2026-06-09
draft: false
ShowToc: true
TocOpen: false
ShowReadingTime: false
ShowBreadCrumbs: false
hidemeta: true
disableShare: true
searchHidden: true
description: "tomworld 블로그 자체의 디자인·기능 변경 이력. 글 본문과는 별개로, 사이트가 어떻게 바뀌어 왔는지 기록합니다."
---

블로그 콘텐츠가 아니라 **사이트 자체**의 변경 이력입니다.
디자인 손질, 새 기능, 성능 개선처럼 글에 직접 드러나지 않는 변화를 모아 둡니다.

---

## 2026-06-09

### SEO·메타데이터
- 모든 글 frontmatter에 `description:` 자동 채움 (35편 일괄) — Google·Naver 검색 카드 본문이 본문 첫 단락 그대로 노출
- Open Graph / Twitter 카드 이미지를 글마다 자동 생성 (1200×630, 카테고리별 색)
- JSON-LD `BlogPosting` 스키마에 `articleSection`(카테고리), `image`(w/h), `keywords` 추가, `articleBody` 제거(페이지 부피 절감)
- IndexNow 통합 — 새 글 발행 시 Bing·Yandex에 즉시 색인 요청

### 발견·탐색
- 사이트 내 **검색** 페이지(`/search/`) + 헤더 검색창
- 글 하단 **관련 글** 추천(같은 카테고리 3편)
- 홈 **자주 찾는 글** 위젯(누적 조회수 Top 5)
- 카테고리별 RSS 발견용 **구독** 페이지
- 본문 내 종목코드 `(011200)` 자동 링크 → 해당 종목 태그 페이지

### 디자인·UX
- 홈/목록 카드에 OG 이미지 cover 자동 표시 (텍스트만 있는 카드 종료)
- 메타 라인에 카테고리 색 chip + 누적 조회수 chip
- 친근한 톤으로 [소개](/about/)·[문의](/contact/) 카피 재작성
- 인용/제목에서 "총정리/완벽 해설/꿀팁" 같은 SEO-스팸 키워드 금지(글 생성 prompt 단)
- 다크 모드 토글·공유 버튼 등 aria-label 한글화

### 운영·자동화
- 매일 09:00 KST GA4 일일 리포트(Slack) + 글별 누적 조회수 자동 갱신
- 사이드 효과 없는 정리: 옛 draft·중복 글·낡은 정규화 태그 일괄 정리
- 모든 외부 링크 자동 `target=_blank rel=noopener` (render hook)
- 모든 이미지 `loading=lazy decoding=async` (Core Web Vitals)

---

## 그 이전

블로그 시작 이후 누적 변경 이력은 GitHub 커밋 로그를 참고해 주세요.
([주요 사이트 변경 커밋](https://github.com/jungwankim-man/tomworld/commits/main))
