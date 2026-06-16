# blog_hugo

**진행 목적**: `https://tomworlds.com/` (PaperMod 테마) Hugo 정적 사이트의 콘텐츠/테마/배포 저장소. GitHub Pages 호스트, GA4 추적.

**데이터 흐름**:
1. `blog_automator` (별도 프로젝트)가 매일 새벽 3시 LLM으로 글 생성
2. 이미지는 imgbb 대신 `static/images/`로 다운로드해 직접 commit ([[blog_automator_image_localization]] — imgbb 사후 삭제 깨짐 회피)
3. `content/posts/<slug>.md` 작성 → `git push` → GitHub Pages 빌드/배포
4. GA4 `G-JHJJN0EHNB`가 hugo.yaml `googleAnalytics:` 한 줄로 PaperMod 자동 주입 ([[tomworld_analytics_ga4]])
5. 매일 09:00 KST `blog-daily-ga-report`이 전일 GA 수치를 Slack #일상에 발송 ([[blog_daily_ga_report]])

**구성요소**:
- `content/posts/` — 발행된 글 44개 (06-16 기준)
- `content/{about,archives,contact,privacy}.md` — AdSense 사전 작업으로 추가한 사이트 페이지
- `themes/PaperMod` — submodule
- `static/images/` — 게시 이미지 (136MB, GitHub Pages가 호스트)
- `hugo.yaml` — baseURL, GA4, PaperMod, 한국어 설정
- git remote: `git@github.com:jungwankim-man/tomworld.git`

**안전장치**:
- 이미지는 글 발행 전 로컬화 → imgbb 외부 의존 제거
- buildDrafts/buildFuture/buildExpired = false (실수 발행 방지)
- 도메인 Cloudflare DNS 관리 ([[blog_automator_hugo_backend]])
- 태그/카테고리 정규화 → 발견성 보호 (아래 06-09 항목)

## 최근 업데이트

### 2026-06-16 — Google AdSense 신청 (저작권 이미지 정리 + 코드 활성화)

신청 전 점검 결과 정책 페이지(privacy/about/contact)는 이미 완비. 실질 리스크는 **저작권 스크랩 이미지**였음.

#### 1) 저작권 스크랩 이미지 전수 제거 (commit `67cfcf7`)
- imgbb 재업로드 뉴스/애니 사진(URL filename `src-*`) 21개 + 로컬 `src-*` 5개 + `_출처:` 캡션 제거
- `*이미지 출처:*` 푸터 36개 글에서 제거, 본문 노출된 미처리 `IMAGE: ...` AI 프롬프트 16줄(3개 글) 제거
- **AI 생성본**(imgbb `gen-*`/`real-*`/`i2i-*` 65개)·**Pexels**(105개)는 유지 — 라이브 200 확인. 저작권 문제 없음
- [[image_gen_minimize_text]] 블로그 저작권 규칙을 발행 콘텐츠에 실제 적용한 셈

#### 2) AdSense 코드 배선 + 활성화 (commit `e3ae3d8`)
- `layouts/_partials/extend_head.html`에 config 기반 주입: `{{ with .Site.Params.adsense.client }}` → `<head>` adsbygoogle 스크립트
- `hugo.yaml` `params.adsense.client = "ca-pub-3724310991533599"` 주입
- `static/ads.txt` 생성: `google.com, pub-3724310991533599, DIRECT, f08c47fec0942fa0`
- 라이브 검증: `<head>` 스크립트 + `/ads.txt` 200 OK

#### 남은 단계
- 사용자가 AdSense 콘솔에서 **"검토 요청"** 클릭 → 심사 대기(수일~수주). 승인 후 자동 광고 on
- 관련 메모리 [[blog_adsense_application]], [[launchd_adsense_reminder]]

### 2026-06-09 — 콘텐츠 발견성 대공사: 카테고리/시리즈 taxonomy + 태그 정규화 + SoT 통합

배경: 한 달 운영으로 37편이 쌓이자 홈 인트로는 추상적이고 about은 정적이며 `/tags/`에는 `[KO`/`KO]`/`AI PCB`/`PCB주`/`PCB투자` 같은 깨진·중복 태그가 산재. 발견성·신뢰감 모두 떨어지는 상태.

#### 1) 홈 + about 페이지 재설계
- `hugo.yaml`의 `homeInfoParams.Content`를 추상 문구("매일 변하는 세상")에서 **실제 콘텐츠 구성**(종목분석/시사/자동매매/캠핑·생활)으로 구체화, `/about/` 링크 동봉
- `content/about.md` 전면 개편: 5개 묶음(종목분석/자동매매·모니터링/시사·이슈/생활·후기/여행·기술)별 설명 + **글 쓰는 원칙 5조** + 종목·자동매매 디스클레이머 + 발행 리듬
- 각 묶음의 대표 글은 **하드코딩이 아니라 shortcode로 자동 노출** (아래 항목 #3)

#### 2) categories + series taxonomy 도입
- `hugo.yaml`에 `taxonomies: { category, series, tag }` 추가, 메뉴에 `카테고리`(weight 15) 노출
- `scripts/categorize_posts.py` 신설: 제목·태그 정규식 기반 5개 카테고리 자동 분류
  - 종목분석 16 / 시사이슈 9 / 생활후기 6 / 자동매매시스템 3 / 여행기술 3
  - idempotent — 새 글 추가 후 재실행하면 신규 글만 업데이트, `--file FILE` 단일 처리 모드
- 시리즈 4종 자동 매칭: AI PCB 시리즈(7편), 자동매매 백테스트(3편), 한국 건설 안전(3편), 스타벅스 5·18 논란(2편)
- 결과: `/categories/<name>/` + `/series/<name>/` 페이지와 각 RSS 피드 자동 생성

#### 3) 자동 갱신 대표 글 shortcode
- `layouts/_shortcodes/category-posts.html`: `{{< category-posts cat="종목분석" count="5" >}}` 한 줄로 카테고리별 최신 N편 자동 노출
- about.md의 하드코딩된 16개 글 링크 제거 → 새 글 발행 즉시 about 페이지가 자동 갱신
- about 하단 구독 섹션: 전체 RSS + 카테고리별 5개 RSS + 시리즈별 3개 RSS

#### 4) 태그 정규화 — root cause 정공법 + 일회성 정리
- 잔재 패턴: `[KO`(13건)·`KO]`·`EN]` 같은 대괄호 잔재 + `KO`(22)·`EN` 언어 마커가 `/tags/` 오염
- 원인: `blog_automator/src/publisher/hugo.py:54`의 `_normalize_tags()`가 Notion이 보낸 `"[KO, FC-BGA, ...]"` 문자열을 `split(",")` 후 strip만 해서 양 끝 대괄호가 첫·마지막 토큰에 남음. 동시 fix 적용
- `scripts/normalize_tags.py`로 기존 37편 정리: 36/37 업데이트, 깨진 태그 36개 순제거
- 동의어 통합: `노후 인프라`→`노후인프라`, `GTX 철근 누락`→`GTX철근누락`, `신세계불매`→`신세계불매운동`
- PCB 5변형(`PCB관련주`/`PCB주`/`PCB투자`/`AI PCB`/`AI서버PCB`) → `PCB` 단일화 (사용자 승인) → `/tags/pcb/`에 5편 통합 노출

#### 5) GHA 안전망 (`.github/workflows/hugo.yml`)
- Checkout 직후 `Auto-label posts` + `Commit auto-label changes` 2단계 추가
- `permissions: contents: write`로 승격
- `GITHUB_TOKEN` 사용 → bot commit이 워크플로 재귀 트리거 안 함(의도된 동작) → 무한 루프 차단
- 수동 git push로 들어온 글도 GHA에서 자동 라벨링 → publish 우회 케이스 보강

#### 6) 단일 source of truth: `data/tag_aliases.json`
- blog_automator와 blog_hugo가 같은 dict를 두 벌 들고 있던 drift 위험 차단
- 스키마: `{ "drop_tags": [...], "aliases": {...} }`
- blog_hugo `normalize_tags.py` + blog_automator `src/publisher/hugo.py`가 모두 이 JSON을 로드 (blog_automator는 `HUGO_REPO_PATH` + 메모리 캐시 + fallback)
- Round-trip 검증: JSON에 임시 `DRIFT_TEST_TAG` 삽입 → 코드 변경 0 → 양쪽 즉시 인지

#### 7) blog_automator 발행 파이프라인 통합
- `src/publisher/hugo.py`의 `publish()`가 md 작성 직후 `_auto_categorize()` 호출 → 단일 파일 모드로 `categorize_posts.py` 실행 → 새 글이 자동으로 카테고리·시리즈 라벨 부여받고 git commit
- best-effort: 라벨링 실패해도 publish는 계속

검증:
- Hugo 빌드 정상 (402 pages, 카테고리/시리즈 인덱스·RSS 모두 생성)
- `/tags/pcb/` 5편 통합 노출, 깨진 태그 잔존 0
- `_normalize_tags()` 단위 테스트 ALL PASS (bracket residue/언어마커/alias/dedupe/None/빈값)
- about 페이지 shortcode 정상 렌더 (각 카테고리별 최신 N편 + 시리즈 링크)
- `normalize_tags.py --dry-run` 0 변경 (= JSON 로더가 기존 하드코딩과 동일 동작)

남은 follow-up:
- categorize 규칙(CATEGORY_RULES/SERIES_RULES)도 JSON 이전 검토 (현재는 코드 하드코딩)
- `tag_aliases.json`에 `_history` 필드로 변경 이력 누적 (6개월 후 "왜 통합했더라" 보험)
- 발견된 중복 글(캠핑짐 06-07/06-08, 남의 돈/others-money-stock) — 사용자가 "개시된 글 기준으로 정리" 하기로

## 관련
- [[blog_automator]] — 글 생성 엔진
- [[blog_automator_hugo_backend]] — 도메인/Cloudflare/AdSense
- [[tomworld_analytics_ga4]] — GA4 G-JHJJN0EHNB
- [[blog_automator_image_localization]] — 이미지 로컬화 정책
- [[blog_daily_ga_report]] — 매일 GA 리포트 Slack
- [[blog_investment_judgment_table]] — 투자 분석 글 포맷 룰
- [[image_gen_minimize_text]] — 이미지 안 글자 최소화 룰
