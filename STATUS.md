---
name: tomworlds.com 블로그
status: 보류
updated: 2026-09-30
goal: Hugo 블로그로 애드센스 승인받고 수익화
done_when: 애드센스 승인
---

NEXT: 다음 글 주제를 정하고, 이미지는 Krea 2로(사용자 결정) — 58편 기준 애드센스 보완 계획 재평가
BLOCKED: (없음)

## 로그
- 2026-10-31 개선(1bdab33, Flash 미사용): NRPL 글에 LPDDR4 사례+FAQ, Dell 글에 해석·중고거래 단락, SCM 3편 낡은 예고를 "넉 달 뒤" 덧붙임+4편 링크로 교체. categorize_posts.py에 categoryLock 지원(배포 때 자동 분류가 수동 카테고리 덮어쓰던 문제) — Dell=여행기술, 10/31 2편=구매실무 고정. 불용재고 편 초안(/posts/obsolete-inventory-concept/, draft, 11/3 예정). 라이브 확인 완료
- 2026-10-31 애드센스 대비 정리(9c5282c): 영어 시사 3편·그림 18선 robotsNoIndex+sitemap 제외+목록 제외(build.list never), Dell 글 카테고리 시사이슈→여행기술, Pexels 12장 제거(스노우볼 2·SCM 1편 5·2편 5). 파미르 글 Pexels 40장은 사진 위주 글이라 보류. 대표 이미지 3장 추가(4fb1d2d, yogi v3 GGUF — Krea2 bf16 파일이 디스크에서 사라져 대체, 장당 약 6분). 라이브 200·noindex 확인. 육안 검수 미완(vision 400). oMLX(ai.omlx.qwen38) bootout 후 bootstrap이 게이트웨이 가드로 막혀 복구 대기
- 2026-10-31 2편 발행(0b0fa71, Pages 41171978740 성공, 둘 다 200): 「구매 담당자가 AI에게 일을 맡겨본 6가지 사례」(/posts/procurement-ai-6-cases/, SCM 자동화 4편)·「LPDDR4가 사라진다 — 2027 메모리 구매 방향」(/posts/legacy-memory-buying-direction-2027/, 대응 8가지·⑧ 메모리 모듈 업체). 사명·거래처·품번·사내 금액 제외 확인. 이미지 없음. 같은 날 애드센스 검토: 신청 보류 권고(5~6월 몰아쓰기·영어 글 3편·짧은 글 11편·Pexels 32장), noindex 정리 승인 대기
- 2026-10-31 「부품이 사라지기 전에 오는 신호 — NRPL과 EOL 개념 정리」 발행(9a60d1e, Pages 41170203352 성공, /posts/nrpl-eol-parts-concept/ 200). 새 시리즈 '구매·자재 실무 개념' 1편, 이미지 없음(대표 이미지 기본값). 2편 불용재고 대기
- 2026-09-30 홈·목록 매거진 레이아웃 게시(102d2aa, Pages 36649473066 성공): 박스 없는 인트로 → [대표 글 | 자주 찾는 글] → 3/2/1열 카드 그리드, pagerSize 13(대표 1+12), 2쪽 이후는 가로형 대표 카드. 390px에서 가로 스크롤 없음 확인
- 2026-09-29 「주식 20년, AI 1년」 발행(dbcdccc 이후 rebase·push, Pages 성공, 글·이미지 200)
- 2026-09-29 초안 이미지 6장 완료(Hermes, Z-Image, 검수 PASS·빌드 확인); 미커밋
- 2026-09-29 회고 글 '주식 20년, AI 1년' 초안 추가(draft:true, slug stock-20-years-ai-1-year); 이미지 6장 생성은 Hermes에 위임 중(static/images/posts/2026-09-stock20-ai1/)
- 2026-09-29 블로그 복구 수정 9f8aa08을 GitHub main에 게시, Pages 실행 36472281112 빌드·배포 성공. 공개 favicon 5종·기본 대표 이미지·MLCC 1편 링크 200, 본문 수정 링크 반영, HTTP→HTTPS 301 확인.
- 2026-09-28 공개 사이트 핵심 11경로·GitHub Pages 배포 정상 확인. HTTPS 강제 설정 활성화. 로컬에서 404 파비콘·대표 이미지·MLCC 링크와 시리즈 경로 중복 수정, Hugo 빌드 및 내부 참조 15,699건 누락 0 검증. 공개 반영은 아직 전.
- 2026-09-14 Hugo PaperMod 51편. 2026-06-26 애드센스 반려(Low value content) — 반려 원인은 편당 품질이 아니라 사이트 전체 패턴이라는 진단과 보완 계획을 adsense_remediation_plan.md에 정리. 최근 글은 08-30
- 2026-09-14 원장 생성
