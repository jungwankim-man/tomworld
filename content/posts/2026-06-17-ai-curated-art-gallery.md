---
title: "AI가 직접 고른 오늘의 그림 18선 — 싫어요까지 학습하는 이미지 생성 파이프라인"
description: "50장을 뽑아 AI가 직접 보고 18장을 골랐습니다. 좋아요뿐 아니라 싫어요까지 점수로 학습해 다음 생성에서 제외하는 피드백 루프로 만든 결과물 갤러리입니다. 애니풍 9컷과 사진풍 9컷을 한 번에 모았습니다."
date: 2026-06-17T19:30:00+09:00
draft: false
categories: ["AI 이미지"]
tags: ["AI그림", "이미지생성", "SDXL", "z-image", "피드백루프"]
cover:
  image: "/images/posts/2026-06-17-ai-curated-art-gallery/a02-cherry-blossom-umbrella.png"
  alt: "벚꽃 아래 우산을 든 애니메이션 소녀"
  relative: false
---

오늘은 분석 글 대신 가벼운 갤러리입니다.

로컬 이미지 파이프라인으로 한 번에 50장을 생성한 뒤, 그중 잘 나온 18장을 골라 모았습니다. 단순히 무작위로 뽑은 게 아니라, **사용자가 :star:로 누른 좋아요와 👎로 누른 싫어요를 모두 점수로 학습**해 다음 생성 때 반영하는 피드백 루프를 거친 결과입니다.

이 글에서 볼 수 있는 것:
✅ 애니메이션 스타일 9컷 (SDXL Ri-mix)
✅ 사진 스타일 9컷 (z-image)
✅ 피드백 루프가 결과 품질에 어떻게 작동하는지 짧은 정리

## 어떻게 만들었나 — 좋아요 + 싫어요 피드백 루프

기존에는 마음에 드는 그림에 :star:를 눌러 "다음에 비슷하게" 학습시켰습니다. 여기에 한 가지를 더했습니다. **마음에 안 드는 그림에는 👎를 눌러 음수 점수를 주고, 그 프롬프트를 다음 생성 풀에서 아예 제외**하도록 한 것입니다.

- 좋아요(:star:)는 양수 점수 → 인기 가중치가 높아져 더 자주 등장
- 싫어요(👎)는 음수 점수 → few-shot/샘플링 풀에서 자동 제외 + 생성 차단
- 반복되는 불만(붉은 톤·디테일 부족·단조로움 등)은 부정 프롬프트로 자동 누적 반영

이번 50장도 이 누적 피드백이 적용된 상태에서 생성했고, 최종 18장은 직접 한 장씩 확인하며 골랐습니다.

## 애니메이션 스타일 9선

![벚꽃 아래 우산을 든 소녀](/images/posts/2026-06-17-ai-curated-art-gallery/a02-cherry-blossom-umbrella.png)
벚꽃이 흩날리는 봄날, 투명 우산 너머로 들어오는 분홍빛. 가장 마음에 든 한 컷입니다.

![은빛 머리의 소녀와 따뜻한 커피](/images/posts/2026-06-17-ai-curated-art-gallery/a01-silver-hair-coffee.png)
창가의 아침 햇살과 김이 오르는 머그. 아늑한 분위기.

![은빛 갑옷의 전사](/images/posts/2026-06-17-ai-curated-art-gallery/a03-armored-warrior.png)
푸른 눈빛과 정교한 갑옷, 빛줄기가 만드는 극적인 대비.

![물속의 인어](/images/posts/2026-06-17-ai-curated-art-gallery/a04-mermaid.png)
청록빛 머리카락과 수면을 통과한 빛의 일렁임.

![초승달 아래 뱀파이어](/images/posts/2026-06-17-ai-curated-art-gallery/a05-vampire-crescent.png)
붉은 장미와 초승달, 고딕한 무드의 초상.

![우주비행사](/images/posts/2026-06-17-ai-curated-art-gallery/a06-astronaut.png)
헬멧을 벗은 채 바라보는 먼 성운. 렌즈 플레어가 포인트.

![여우 정령과 기모노](/images/posts/2026-06-17-ai-curated-art-gallery/a07-fox-spirit-kimono.png)
신사의 등불을 배경으로 한 흰 여우 귀, 단정한 기모노.

![앵무새를 어깨에 올린 해적 선장](/images/posts/2026-06-17-ai-curated-art-gallery/a08-pirate-parrot.png)
삼각모와 알록달록한 앵무새, 장난기 있는 미소.

![장미에 둘러싸인 플로리스트](/images/posts/2026-06-17-ai-curated-art-gallery/a09-florist-roses.png)
창가의 따뜻한 빛과 장미, 부드러운 옆모습.

## 사진 스타일 9선

![비 오는 카페의 빨강 머리](/images/posts/2026-06-17-ai-curated-art-gallery/r01-redhead-cafe.png)
빗방울 맺힌 창가, 크림색 스웨터와 커피 한 잔.

![토스카나의 포도밭 일몰](/images/posts/2026-06-17-ai-curated-art-gallery/r02-tuscan-vineyard.png)
황금빛 노을이 굽이치는 언덕과 사이프러스 가로수.

![비 내린 도쿄 횡단보도](/images/posts/2026-06-17-ai-curated-art-gallery/r03-tokyo-crosswalk.png)
젖은 노면에 번지는 네온, 코트 차림의 실루엣.

![공원 벤치의 두 친구](/images/posts/2026-06-17-ai-curated-art-gallery/r04-friends-bench.png)
함께 웃는 자연스러운 순간. 따뜻한 가을 햇살.

![설산과 얼어붙은 호수의 반영](/images/posts/2026-06-17-ai-curated-art-gallery/r05-alpine-lake.png)
분홍빛 알펜글로가 물든 봉우리, 거울 같은 호수면.

![해질녘 아말피 해안](/images/posts/2026-06-17-ai-curated-art-gallery/r06-amalfi-coast.png)
절벽을 따라 켜지는 파스텔빛 집들과 작은 배들.

![갓 구운 사워도우](/images/posts/2026-06-17-ai-curated-art-gallery/r07-sourdough.png)
바삭한 크러스트와 로즈마리, 김이 오르는 정물.

![해안 도로의 모터사이클](/images/posts/2026-06-17-ai-curated-art-gallery/r08-coastal-motorcycle.png)
황금빛 해안선을 달리는 라이더. 속도감이 담긴 한 컷.

![뜨개질을 가르치는 할머니](/images/posts/2026-06-17-ai-curated-art-gallery/r09-grandmother-knitting.png)
포치 그네에 앉아 손녀에게 뜨개질을 가르치는 장면. 가장 따뜻했던 사진풍 컷.

## 마무리

같은 파이프라인이라도 "좋아요만" 학습할 때와 "싫어요까지" 학습할 때의 결과는 시간이 갈수록 벌어집니다. 마음에 안 드는 컷을 한 번 눌러두면 비슷한 실패가 다음 배치에서 줄어드는 구조라, 쌓일수록 골라낼 게 적어집니다.

다음에는 이 18장 중 반응이 좋은 컷을 다시 시드로 삼아 한 단계 더 다듬어 볼 생각입니다.
