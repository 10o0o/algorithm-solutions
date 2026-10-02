# Algorithm Learning Lab

Python 풀이, 요청한 개념 정리와 확인한 학습 경험을 쌓는 개인 CP 학습 저장소입니다.

## 실행과 검증

저장소 루트에서 실행합니다. Linux/WSL, uv, CPython 3.12가 기본 환경입니다.

```bash
uv sync --frozen
uv run --frozen python scripts/setup_workspace.py
uv run --frozen python -m unittest discover -s tests -v
uv run --frozen python scripts/validate_notes.py
uv lock --check
git diff --check
```

웹은 `web/`에서 `npm ci`, `npm run check`, `npm test`, `npm run build`를 실행합니다.
배포 경로 검사는 `SITE_BASE=/algorithm-solutions/ npm run build` 후 같은 환경변수로
`npm run test:e2e`를 실행합니다. 검색은 빌드 미리보기에서 확인합니다.

집중 검사: `uv run --frozen python -m unittest discover -s tests -p test_setup_workspace.py -v`.
검사 도구의 의존성은 개발용이며, 제출 코드는 표준 라이브러리 기반 단일 파일입니다.
제출 문법은 PyPy 3.10 호환을 기본으로 하고, 선택한 저지 실행 환경을 확인합니다.

## 학습과 기록 스킬

학습 요청에서는 `STATE.md`와 해당 문제·자료·사용자 코드를 읽고 다음 스킬을 적용합니다.
이름을 직접 호출하거나 자연어로 요청할 수 있습니다.

| 요청 | 읽을 스킬 |
| --- | --- |
| 오늘 학습 시작, 계속, 힌트 줘, 오늘 학습 종료, STATE 반영해 | [study-algorithms](.agents/skills/study-algorithms/SKILL.md) |
| 이 개념 정리해줘, 배운 지식 저장해줘 | [record-algorithm-knowledge](.agents/skills/record-algorithm-knowledge/SKILL.md) |
| 이 문제 복기해줘, 이 풀이 기록해줘 | [review-algorithm-problem](.agents/skills/review-algorithm-problem/SKILL.md) |
| 이번 대회 복기해줘, virtual 결과 정리해줘 | [review-algorithm-contest](.agents/skills/review-algorithm-contest/SKILL.md) |

정리 요청은 해당 노트 작성을 허용하며, 별도 초안 승인을 반복하지 않습니다.
사용자가 요청한 기초 참고 정리도 작성할 수 있습니다. 실제 학습 경험·제출 판정·도움 여부는
확인한 범위만 기록하고 샘플 통과나 파일 존재를 AC·독립 해결·숙달로 바꾸지 않습니다.
일반 설명이나 `이해했어`만으로 저장하지 않습니다. `오늘 학습 종료`는 다음 행동을 제안하고,
`STATE 반영해` 요청 때 재개 위치를 저장합니다. STATE는 진도 DB가 아닙니다.
진행 중인 실전 대회의 풀이·디버깅 도움은 종료 후 복기로 돌립니다.
학습 운영과 출처는 [로드맵](ROADMAP.md), [참고 자료](docs/REFERENCES.md)를 따릅니다.

## 파일과 환경의 주의점

- 기존 플랫폼별 코드 경로와 LeetCode의 `@lc`, `code=start/end`를 보존합니다.
  LeetCode의 class API를 stdin `solve()` 형태로 일괄 변환하지 않습니다.
- 루트 `main.py`, `ex.in`은 Git에서 제외된 사용자 작업 파일입니다.
  환경 설정·정리 과정에서 삭제하거나 템플릿으로 덮어쓰지 않습니다.
- 새 풀이 복기는 코드 옆 같은 이름의 `.md`에 둡니다. `solution`은 노트 기준 상대경로입니다.
  템플릿은 `templates/problem-note.md`, `knowledge/template.md`, `contests/template.md`입니다.
- CPH는 첫 워크스페이스 폴더에 코드를 생성하며 템플릿 경로 변수를 치환하지 않습니다.
  `.local/*.code-workspace`를 생성해 사용하고 기기 절대경로를 추적 파일에 넣지 않습니다.
- CSES는 `--platform cses`와 `.local/cses.code-workspace`를 사용합니다. 제목 기반 CPH 파일명과
  원문 URL을 보존하며 [CSES 사용법](cses/README.md)을 따릅니다. 설정만으로 풀이·AC 기록을 만들지 않습니다.
- CPH `.cph`에는 절대 소스 경로에 연결된 테스트가 있습니다. 파일 이동·문제 재가져오기로
  추가 반례가 인식되지 않거나 교체될 수 있으므로 [사용법](docs/USAGE.md)의 보존 절차를 따릅니다.
- 일반 풀이 검증은 샘플·필요한 반례를 중심으로 합니다. 자동 회귀 테스트는 저장소 도구와
  반복 사용하는 알고리즘 구현에 집중합니다.
- 웹은 공개 노트와 연결된 플랫폼 풀이를 직접 읽습니다. Markdown 원본·코드 경로를 보존하고
  [웹 사용법](docs/WEB.md)에 따라 링크, 검색, 배포 하위 경로를 검증합니다.
