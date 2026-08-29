---
title: "MLCC 견적 거절당하지 않는 법 — Buyers Edition"
date: 2026-08-29
slug: mlcc-buyers-edition-견적-방어-매뉴얼
categories: ["업무자동화"]
tags: [MLCC, 조달, SCM, 리드타임, BOM]
cover:
  image: "/images/posts/2026-08-mlcc-buyers-edition/img1.webp"
  alt: "MLCC 실물 접사"
images:
  - "/images/posts/2026-08-mlcc-buyers-edition/img1.webp"
  - "/images/posts/2026-08-mlcc-buyers-edition/img2.webp"
  - "/images/posts/2026-08-mlcc-buyers-edition/img3.webp"
  - "/images/posts/2026-08-mlcc-buyers-edition/img4.webp"
---
[1편](/posts/mlcc-쇼티지-진짜-원인---ai-서버가-캐파-삼킨-이유/)에서 AI 서버가 MLCC를 얼마나 삼키고 있는지, 왜 0201·고용량 패키지가 먼저 말라붙는지를 봤다. 그 글의 결론은 세 가지였다: **재고를 잡아라, 다변화해라, 스펙을 풀어라.**

이번 편은 그 다음이다. **견적서에 "sorry, no stock"이라고 적혀 돌아왔을 때**, 발주 라인에서 실제로 통하는 것들을 순서대로 펼쳐본다.

![MLCC 실물 접사](/images/posts/2026-08-mlcc-buyers-edition/img1.webp)
*MLCC — 손톱보다 작은 이 칩 하나가 발주서를 24주 묶는다.*

## 1. 거절에는 네 가지 얼굴이 있다

공급사가 "없다"고 할 때, 사실은 네 다른 상황을 한 단어로 뭉갠 것이다. 대응이 완전히 다르다.

| 메일의 문장 | 진짜 뜻 | buyers의 대응 |
|---|---|---|
| "Out of stock, no ETA" | 프랜차이즈 부품—재고가 진짜 0 | **스펙을 풀어라** (아래 §3) |
| "Lead time 16+ weeks" | 생산 슬롯은 있는데 your PO가 줄을 잘못 섰다 | **LTA·forecast로 앞에서 자리 잡아라** (§2) |
| "Allocation only" | 배분제—큰 손, 오래된 거래처부터 나눠준다 | **Tier 2 프랜차이즈로 우회** (§4) |
| "MOQ is 10× your qty" | 소량이라 받아줄 수 없다 | **가상 묶음(broker)·small-volume channel** (§4) |

한 단어로 들리지 않게, 견적 회신을 위 네 칸으로 분류하는 습관부터가 이 게임의 진입장벽이다.

## 2. 리드타임을 "앞에서" 줄이는 것 — LTA와 Forecast

거절당한 다음에 움직이는 사람은 이미 늦었다. 발주 라인에서 통하는 첫 수는 **past-dated demand를 다시 살려내는 것**이다.

- **LTA (Long-Term Agreement):** 12~24개월 물량을 약속하고, 월별 ship schedule을 확정한다. 공급사는 이걸 "locked demand"로 간주해서 capacity를 따로 떼어놓는다. 가격 보호 조항(±%)을 끼우면 인플레분도 함께 방어된다.
- ** Rolling Forecast (13주/26주):** "확정"은 아니지만 rolling forecast를 제출하는 고객에게만 배분하는 홀더 물량이 있다. forecast를 내는 것 자체가 알로케이션 표에 이름을 올리는 행위다.
- **Blanket PO + Release schedule:** PO 총량은 미리 발주해 두고, 월별로만 release한다. 공급사 입장에선 이미 수주물량이라 lead time 계산에서 한 단계를 건너뛴다.

실무 순서: forecast(월간 갱신) → blanket PO(총량锁定) → release schedule(월별). 이 루틴이 도는 구매자와 안 도는 구매자 사이에 "16+ weeks"와 "in stock, 4 weeks"의 차이가 있다.

## 3. 거절당하지 않는 BOM을 먼저 만드는 법

BOM을 다시 설계하면 리드타임 자체가 사라지는 경우가 있다.

- ** voltage/temperature 특성 완화:** X7R이(required)인데 현장에서 X5R로 견딜 수 있다면? 용량 tolerance ±10%가 ±20%로 풀리면 재고 Finder는 즉시 다른 리전을 찾는다. **BOM 여유도(derating)를 설계 단계에서** 남겨두는 것이 구매 단계의 재고가 된다.
- **패키지 alt:** 0402가 말라붙었다면 0603 footprint에 0402-compatible land pattern를 준비해두는 설계가 true value다. 기판 리비전 한 번으로 6개월을 산다.
- **AEC-Q200 등급:** 자동차 등급이 아니어도 되는 컨슈머 보드라면, industrial-grade로 풀면Allocation 대상에서 빠진다. 등급이 곧 줄이다.
- **2nd source 지정 방식:** BOM에 "or equivalent"를 넣는 것과, **실제로 cross-ref된 alternate part number**를 두 개 넣는 것은 전혀 다른 의미다. latter만 거절邮件에서 살아남는다.

핵심: "대체 가능"은 구매의 언어가 아니라 **설계의 언어**다. BOM approval 단계에서 alternate를 못 박지 않으면, 거절당했을 때 아무도帮你 대체하지 않는다.

## 4. 프랜차이즈, Allocated 지옥을 우회하는 두 갈래

### Authorized distributor 외의 길
- **Franchise와 broker는 전혀 다른 시장이다.** Authorized는 제조사 allocation을 받지만, broker는现货(재고 풀)을 산다. 리드타임이 필요 없는 대신 **price premium과 counterfeit risk**가 따라온다.
- Broker를 쓸 때의 실전防线: lot code 추적 가능 요구, 출처 documentation (C of C), incoming inspection 샘플抽检, counterfeit-prone 디바이스(MLCC는 RISK 상위군)는 비즈니스 крит적 용도면 broker 사용 자체를 막는 gate.

### 사이즈 때문에 거절당할 때
- **Franchise는 MOQ 10k~100k, broker는 MOQ 1 reel.** 소량proto는 broker가 살 길이다. 단, 그 price는 3~10배.
- 더 좋은 수는 **虚拟 묶음**: 동일 파트를 쓰는 여러 projects/팀 수요를 모아 MOQ를 넘기는 internal aggregation. 구매자之间有配额,部门之间有预算, 합치면 franchise에서 살 수 있는 Volume이 되는 경우가 의외로 많다.

## 5. 에스컬레이션 — "no"라고 말할 수 있는 사람 찾기

- 담당 AE가 "no stock"이라고만 반복하면, 그건 *answer가 아니라 wall*이다. one level up ( regional sales manager)으로 올라가 **locked demand가 실제로 table에 올라가 있는지** 확인해야 한다.
- 공급사 visit이 어려우면 **vendor quarterly review**의 달력에 올라가 있는 게 افت radic of 모든 door opening이다. 분기 review에서 "우리는 이 part에서 supplier risk RED다"라고 문서를 남기면, allocation 표가 움직인다.

## 6. 그 외 실무 체크리스트 (한 장 요약)

- [ ] 월간 rolling forecast를 제출하고 있는가
- [ ] Critical part에 blanket PO + release schedule이 도는가
- [ ] BOM에 cross-ref된 alternate PN이 2개 이상 있는가
- [ ] 설계 derating 여유가 등급을 하나로 조이고 있는가
- [ ] broker counterfeit gate (C of C + inspection)가 있는가
- [ ] Vendor QBR에 risk item을 문서로 남기는가

---

1편에서 다룬 수요 폭증의 구조적 문제는 구매자 개个人的 노력으로 못 바꾼다. AI 서버 캐파를 안 쓰는 방법은 없다. 다만 **"sorry, no stock"을 "4 weeks, ok"로 바꾸는 것은** 위와 같이 구조적으로 미리 해둔 회사에만 Occurs. 마지막 words은 자신을 향해 두고 있다: **여러 회사의 BOM approval에 standing item으로 alternate topic을insert하고 있는가?**
