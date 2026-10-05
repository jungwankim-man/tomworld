---
title: "Dell U3223QE 사용시간 확인하기: 맥에서 DDPM 보고서로 4,193시간 확인"
date: 2026-09-30 16:36:00 +0900
draft: false
slug: dell-u3223qe-usage-hours-ddpm-mac
categories: ["시사이슈"]
tags: ["Dell", "U3223QE", "모니터", "DDPM", "맥", "사용시간"]
description: "조이스틱형 Dell U3223QE의 누적 사용시간을 macOS용 Dell Display and Peripheral Manager 자산 보고서에서 확인한 과정과 주의할 점."
---
모니터의 사용시간을 확인하려고 Dell 서비스 메뉴 진입 영상을 찾아봤다. 그런데 내 U3223QE에는 영상 속 버튼이 없다. 뒤쪽에 조이스틱 하나와 전원 버튼만 있다. DP 케이블로 연결한 상태에서 조이스틱 가운데를 누르고 전원 버튼을 두 번 누르는 방법도 시도했지만, 내 제품에서는 서비스 메뉴가 열리지 않았다.

결국 답은 숨겨진 파란 메뉴가 아니라 Dell의 **Display and Peripheral Manager(DDPM)** 보고서에 있었다. 2026년 9월 30일 내 U3223QE에서 확인한 값은 **4,193시간**이다.

## 맥에서 확인한 순서

1. [Dell의 macOS용 DDPM 안내](https://www.dell.com/support/kbdoc/en-us/000201067/dell-display-and-peripheral-manager-for-macos)에서 U3223QE가 지원 모델인지 확인하고, [Dell 공식 지원 페이지](https://www.dell.com/support/product-details/ko-kr/product/dell-display-peripheral-manager/drivers)에서 DDPM을 설치했다.
2. 모니터를 DP로 연결하고 DDPM에서 **DELL U3223QE**가 인식되는지 확인했다. 인식되지 않으면 모니터 OSD의 **Others → DDC/CI → On**을 확인한다. Dell 안내에는 Apple Silicon 맥에서 USB 업스트림 케이블 연결도 권장되어 있다.
3. DDPM 앱의 왼쪽 메뉴가 아니라 **macOS 화면 맨 위 메뉴 막대의 DDPM 아이콘을 오른쪽 클릭**했다. 여기서 **Save monitor asset report(모니터 자산 보고서 저장)**를 선택했다.
4. 생성된 `.mif` 파일을 Finder에서 **다음으로 열기 → 텍스트 편집기**로 열고, `⌘F`로 `UsageTime`을 찾았다.

내 보고서의 해당 부분은 아래와 같았다. 개인 식별 정보인 일련번호는 옮기지 않았다.

```text
ModelName = "DELL U3223QE"
UsageTime = "4193 hours"
Connection = "DP"
```

**4,193시간은 24시간씩 환산하면 174일 17시간**이다. 보고서에는 별도로 `DateOfManufacture = 2022 ISO week 44`와 `Age = 1422 days`도 있었는데, `Age`는 사용시간이 아니라 제조 이후 경과일이다. 두 숫자를 혼동하면 안 된다.

## 이 숫자를 해석할 때 주의할 점

`UsageTime`은 모니터가 DDPM에 보고한 누적 시간이다. 이 보고서만으로는 **화면이 실제로 켜져 있던 시간만 집계했는지, 대기 상태를 일부 포함하는지** 확인할 수 없었다. 따라서 이를 패널이 정확히 4,193시간 발광했다는 뜻으로 단정하지 않는다. 또 서비스 메뉴와 DDPM 값이 같은 방식으로 집계되는지도 이번 확인에서는 검증하지 않았다.

조이스틱형 U3223QE에서 서비스 메뉴가 열리지 않는다면, 버튼 조합을 계속 반복하기보다 DDPM 자산 보고서를 먼저 확인해볼 만하다. 적어도 내 DP 연결 환경에서는 사용시간 항목이 실제로 기록됐다.

**참고:** [Dell DDPM for macOS 안내](https://www.dell.com/support/kbdoc/en-us/000201067/dell-display-and-peripheral-manager-for-macos) · [Dell Display Manager 자산 보고서의 `UsageTime` 예시](https://www.dell.com/support/kbdoc/en-us/000060112/what-is-dell-display-manager)
