# blog_hugo

**진행 목적**: `https://tomworlds.com/` (PaperMod 테마) Hugo 정적 사이트의 콘텐츠/테마/배포 저장소. GitHub Pages 호스트, GA4 추적.

**데이터 흐름**:
1. `blog_automator` (별도 프로젝트)가 매일 새벽 3시 LLM으로 글 생성
2. 이미지는 imgbb 대신 `static/images/`로 다운로드해 직접 commit ([[blog_automator_image_localization]] — imgbb 사후 삭제 깨짐 회피)
3. `content/posts/<slug>.md` 작성 → `git push` → GitHub Pages 빌드/배포
4. GA4 `G-JHJJN0EHNB`가 hugo.yaml `googleAnalytics:` 한 줄로 PaperMod 자동 주입 ([[tomworld_analytics_ga4]])
5. 매일 09:00 KST `blog-daily-ga-report`이 전일 GA 수치를 Slack #일상에 발송 ([[blog_daily_ga_report]])

**구성요소**:
- `content/posts/` — 발행된 글 33개 (06-05 기준)
- `content/{about,archives,contact,privacy}.md` — AdSense 사전 작업으로 추가한 사이트 페이지
- `themes/PaperMod` — submodule
- `static/images/` — 게시 이미지 (136MB, GitHub Pages가 호스트)
- `hugo.yaml` — baseURL, GA4, PaperMod, 한국어 설정
- git remote: `git@github.com:jungwankim-man/tomworld.git`

**안전장치**:
- 이미지는 글 발행 전 로컬화 → imgbb 외부 의존 제거
- buildDrafts/buildFuture/buildExpired = false (실수 발행 방지)
- 도메인 Cloudflare DNS 관리 ([[blog_automator_hugo_backend]])

## 관련
- [[blog_automator]] — 글 생성 엔진
- [[blog_automator_hugo_backend]] — 도메인/Cloudflare/AdSense
- [[tomworld_analytics_ga4]] — GA4 G-JHJJN0EHNB
- [[blog_automator_image_localization]] — 이미지 로컬화 정책
- [[blog_daily_ga_report]] — 매일 GA 리포트 Slack
- [[blog_investment_judgment_table]] — 투자 분석 글 포맷 룰
- [[image_gen_minimize_text]] — 이미지 안 글자 최소화 룰
