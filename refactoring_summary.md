
# 📘 리팩토링 학습 자료 정리 (민코딩)

---

## 🧭 개요

- **리팩토링이란?**  
  기능은 유지하면서 코드의 내부 구조를 개선하는 작업입니다.
  ```text
  입력과 출력이 동일하게 유지되면서, 내부 구조만 정리됩니다.
  ```

- **리팩토링의 목적**
  - 가독성 향상
  - 유지보수성 향상
  - 기능 추가 전 구조 정비
  - 장기적 프로젝트 속도 유지

- **단계별 과정**
  1. Unit Test 기반 확보
  2. 리팩토링 시작 (작은 단위)
  3. 코드 스멜 탐지 → 리팩토링 기법 적용
  4. 디자인 패턴과 SOLID 원칙 학습 적용

---

## 🧪 Unit Test

- **pytest 사용 가이드**
  - 설치: `pip install pytest`
  - 테스트 디렉토리 권장 구조: `tests/`
  - 테스트 함수는 `test_` 로 시작
  - Assertion: `assert a == b`

- **Fixture 및 AAA 패턴 활용**
  ```python
  @pytest.fixture
  def my_fixture():
      return setup_resource()

  def test_sample(my_fixture):
      # Arrange - Act - Assert
      assert my_fixture.do_something() == expected
  ```

- **예외 처리 테스트**
  ```python
  with pytest.raises(ValueError):
      function_that_raises()
  ```

---

## 📈 코드 커버리지

- **도구**: `pytest-cov`
  - 설치: `pip install pytest-cov`
  - 실행: `pytest --cov`
  - 결과: `htmlcov/index.html`

- **설정 파일 예시 (`pytest.ini`)**
  ```ini
  [pytest]
  pythonpath = src
  addopts = -s --cov-report=html
  ```

---

## 🛠️ 자주 사용하는 리팩토링 기법

| 기법 | 설명 |
|------|------|
| Extract Function | 긴 함수에서 일부 코드를 함수로 추출 |
| Inline Function | 너무 얕은 함수는 인라인 처리 |
| Rename Variable | 의미 있는 이름으로 변경 |
| Replace Magic Literal | 매직 넘버 → 상수로 치환 |
| Parameterize Function | 중복 함수 → 매개변수화 |

> 더 많은 기법은: [https://refactoring.com/catalog](https://refactoring.com/catalog)

---

## 💀 Code Smell과 대응 기법

| Code Smell | 리팩토링 제안 |
|------------|----------------|
| Long Method | Extract Method |
| Large Class | Extract Class |
| Shotgun Surgery | Move Method |
| Data Clumps | Introduce Class |
| Message Chains | Hide Delegate |
| Primitive Obsession | Replace Primitive with Object |

---

## 🧱 객체지향 원칙 (SOLID)

| 원칙 | 설명 |
|------|------|
| SRP | 단일 책임 원칙 |
| OCP | 확장엔 열려있고 변경엔 닫혀 있어야 |
| LSP | 하위 클래스는 부모 클래스와 호환돼야 함 |
| ISP | 클라이언트에 꼭 필요한 인터페이스만 제공 |
| DIP | 고수준 모듈은 저수준 모듈에 의존하면 안 됨 |

> 실습 코드: [github.com/mincoding1/SOLID](https://github.com/mincoding1/SOLID)

---

## 🧱 디자인 패턴 (GoF)

| 패턴 | 설명 | 실습 |
|------|------|------|
| Factory Method | 객체 생성을 서브클래스에 위임 | 인형 공장 만들기 |
| Singleton | 하나의 인스턴스만 허용 | DeviceState 구현 |
| Adapter | 기존 인터페이스 유지하면서 새 객체 연결 | AWS → Azure 래퍼 |
| Command | 명령을 객체로 캡슐화 | TextEditor 명령 구현 |

---

## 📂 Kata 실습 예시

- **Gilded Rose**
  - 품질과 판매일을 자동 관리하는 시스템 리팩토링
  - 단계: 테스트 → Method 리팩토링 → 클래스 리팩토링

- **Video Rental**
  - 마틴 파울러의 공식 리팩토링 예제
  - 단계:
    1. Unit Test
    2. Test Case 리팩토링
    3. Pythonic 리팩토링
    4. Legacy 코드 리팩토링
    5. 다형성 적용

- **Trivia / ALU / Wheel of Fortune**
  - 레거시 게임 로직을 리팩토링하며,
  - 테스트 가능 구조로 바꾸는 경험 중심 실습

---

## 📎 참고 링크

- GitHub 실습소스
  - https://github.com/mincoding1/
- 리팩토링 예시 모음
  - https://github.com/jeonghwan-seo/Python-CRA-Example
