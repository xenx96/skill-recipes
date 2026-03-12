# Architecture Spec (구현 후 설계 문서)

구현 완료된 코드 변경사항을 기반으로
구조화된 아키텍처/설계 문서를 자동 생성합니다.

이 스킬은:

- Git diff / 변경된 파일을 분석
- 리스크와 영향 범위를 평가
- 문서화 깊이를 자동 선택 (A/B/C)
- Notion-ready Markdown 사양서를 생성
- 다이어그램 (Mermaid), 테이블, 설계 결정, 운영 참고사항 포함

---

## 왜 필요한가

문서화 깊이는 다음에 비례해야 합니다:

- 리스크
- 보안 영향
- 인프라 영향
- 영향 범위 (blast radius)

이 스킬은 CI 강제 없이도 일관된 문서화를 보장합니다.

---

## 출력 레벨

- A — 경량 (Lightweight)
- B — 표준 (Standard)
- C — 아키텍처 수준 (Architecture-Level)

리스크 점수에 따라 레벨이 자동으로 선택됩니다.

---

## 구조

- [SKILL.md](SKILL.md) — 메인 스킬 (진입점)
- [subskills/diff-risk-evaluator.md](subskills/diff-risk-evaluator.md) — 리스크 점수 산정
- [subskills/notion-spec-generator.md](subskills/notion-spec-generator.md) — 문서 생성
- [subskills/adr-generator.md](subskills/adr-generator.md) — ADR 섹션 (Level C)
- [subskills/notion-page-publisher.md](subskills/notion-page-publisher.md) — Notion 게시
