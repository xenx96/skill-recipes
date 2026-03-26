# Notion Format (노션 문서 포맷터)

콘텐츠 타입을 자동 감지해 풍부한 구조의 Notion 문서로 변환합니다.

이 스킬은:

- 콘텐츠 타입 자동 분류 (tech-doc, meeting-notes, analysis, tutorial, bug-report)
- 타입별 포맷 템플릿 적용 (섹션, 코드 블록, 테이블, callout, quote, mermaid 다이어그램, 이모지)
- 콘텐츠 길이에 따라 포맷 깊이 조정 (짧으면 callout 위주, 길면 toggle 접기)
- Notion 친화적 문서 초안 출력
- 선택적으로 Notion MCP를 통해 페이지 저장 (API-post-page / API-patch-block-children)

---

## 왜 필요한가

"notion에 정리해줘"라고만 하면 형식 지정 없이 밋밋한 텍스트로만 이루어진
문서가 생성됩니다. 이 스킬은 콘텐츠 성격에 맞는 요소를 자동으로 선택해,
매번 잘 구조화된 Notion 문서를 생성합니다.

---

## 지원 콘텐츠 타입

| 타입 | 주요 포맷 요소 |
|---|---|
| `bug-report` 🐛 | 타임라인 테이블, 에러 코드 블록, 심각도 callout |
| `meeting-notes` 📋 | 안건 목록, 액션아이템 테이블, quote |
| `tutorial` 📖 | 번호 목록, 코드 블록, 팁 callout, FAQ 테이블 |
| `tech-doc` 🏗️ | mermaid 다이어그램, 코드 블록, 스펙 테이블 |
| `analysis` 📊 | 요약 callout, 데이터 테이블, 결론 |
| `general` 📝 | 섹션 헤딩, 불릿 목록, callout |

타입은 감지 우선순위 순서로 나열됨 (첫 매칭 적용).

---

## 구조

- [SKILL.md](SKILL.md) — 메인 스킬
