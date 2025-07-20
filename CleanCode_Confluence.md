# 클린 코드 정리 (민코딩 Python 버전)

> 이 문서는 [클린코드]_ 시리즈 자료를 기반으로 작성된 내용을 정리한 것입니다. Confluence 공유용 마크다운 형식입니다.

---


## 클린코드 개요

- **클린코드란?**  
  유지보수가 쉬운 코드. 로버트 C. 마틴의 원칙에 기반하지만 팀의 동의를 기반으로 조율 가능.

- **중요 마인드**
  - 저자 마인드: 코드는 독자(동료 개발자)를 위한 글이다.
  - 보이스카우트 규칙: 들어오기 전보다 더 깨끗하게 떠나라.

- **클린코드가 중요한 이유**
  - SW는 제작보다 유지보수가 더 많음
  - 기한을 맞추기 위해 나쁜 코드가 유지되고 점점 나빠짐




## 실습 준비

- **도구**
  - Python 3.11
  - PyCharm 2025 Community
  - GitHub, Discord, pytest, coverage

- **코딩 환경 팁**
  - 리팩토링: `Ctrl + Alt + Shift + T`
  - 이름 변경: `Shift + F6`
  - 자동 포맷: `Ctrl + Alt + L`
  - 단축키 숙지: `Shift + Shift`




## 클린코드 1부

### 가독성을 위한 Naming

- **Bad Naming**
  - 의미 없는 약어, 시각적 혼란, 너무 일반적인 단어 (Info, Manager 등)

- **Good Naming**
  - 의도를 명확히 드러냄 (ex: `email_notification_enabled`)
  - 일관성 있게 (ex: fetch/get/retrieve 중 하나 선택)

- **PEP8 네이밍**
  - 함수/변수: `snake_case`
  - 클래스/예외: `CamelCase`
  - 상수: `ALL_CAPS`

### 추상화와 함수

- 표현식을 변수로 치환
- 긴 함수는 쪼개기 (함수 하나는 한 가지 일만!)
- Sub 함수로 나눌 때 추상화 수준(Level) 맞추기

### 함수 작성 규칙

- 동사 + 목적어 (`calculate_price`)
- 인자는 적을수록 좋음
- 플래그 인자는 피할 것

### 명시적 코드

- `if x is not None` 처럼 명확하게
- `dict.get(key, default)` 사용
- Type hint, @property 적극 활용




## Tennis KATA

- **기능 설명**
  - 두 플레이어가 점수를 주고받고, 점수를 텍스트로 반환하는 클래스

- **규칙 요약**
  - 0~3점: Love, Fifteen, Thirty, Forty
  - 동일 점수: `X-All`, 3-3 이상 동점은 `Deuce`
  - `Advantage Player`, `Win for Player` 규칙 존재

- **리팩토링 가이드**
  - 의도가 명확한 네이밍 사용
  - 관심사 분리 및 메서드 추상화
  - 지속적인 테스트 유지

- [소스 코드 링크](https://github.com/mincoding1/Tennis)



## 클린코드 2부

### 주석
- 주석보다 코드로 설명하자
- 잘못된 주석은 혼란만 줌
- docstring 활용 권장 (module/class/function)

### 코드 포맷팅
- 파일 크기 제한, 80자 줄 길이
- 관련 함수는 인접하게 배치

### 유닛 테스트
- **원칙: FIRST**
  - Fast, Independent, Repeatable, Self-validating, Timely
- **패턴: AAA**
  - Arrange, Act, Assert
- assertEqual, assertRaises 등 사용
- 테스트도 클린 코드로 관리해야 함



