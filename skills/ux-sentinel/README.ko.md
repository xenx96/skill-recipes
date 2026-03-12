# UX Sentinel (UX 감시자)

프론트엔드 논의 중 반복되는 UI/UX 개념을 지속적으로 감지하고,
대화 전반의 재발 빈도를 추적하며, 반복된 개념을 MCP를 통해
Notion 데이터베이스에 구조화된 지식 자산으로 등록합니다.

이 스킬은:

- 대화 속 UI/UX 개념을 정규화 및 별칭 매핑으로 감지
- 대화 전체에 걸쳐 재발을 추적 (임계값: 2)
- 임계값 도달 시 카테고리, 정의, 의사결정 규칙과 함께 등록을 제안
- Notion `UI/UX Knowledge Base` 데이터베이스에 구조화된 엔트리를 생성
- 수동 명령어 지원: `@ux save`, `@ux skip`, `@ux link`
- Notion 사용 불가 시 로컬 전용 추적으로 폴백

---

## 왜 필요한가

설계 결정은 반복됩니다. 같은 UX 원칙이 다른 기능, 다른 대화,
다른 스프린트에서 계속 등장합니다. 구조화된 추적 없이는
이런 반복 패턴이 머릿속에만 남아 매번 다시 논의됩니다.
UX Sentinel은 반복되는 UI 마찰 신호로부터 의사결정 기억 시스템을 구축합니다.

---

## 동작 방식

이것은 **System Skill**입니다 — 일회성 실행이 아닌
프론트엔드 논의 중 지속적으로 동작합니다.

1. **감지** — 대화에 등장하는 UI/UX 개념을 인식
2. **추적** — 대화 전체에 걸쳐 재발 횟수를 카운트
3. **제안** — 개념이 2회 등장하면 실행 가능한 의사결정 규칙과 함께 등록 제안
4. **등록** — 사용자 승인 시 구조화된 Notion 엔트리 생성

---

## Notion 연동

Notion에 `UI/UX Knowledge Base` 데이터베이스가 필요하며 다음 속성을 포함합니다:
Concept, Category, Recurrence Count, First Seen, Last Seen,
Trigger Context, UI Decision Rule, Product Context, Maturity, Related Concepts.

최초 사용 시 데이터베이스가 없으면 자동으로 부트스트랩됩니다.

---

## 구조

- [SKILL.md](SKILL.md) — 메인 스킬
