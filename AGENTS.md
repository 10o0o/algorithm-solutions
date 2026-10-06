# Algorithm Learning Lab

Python 풀이, 요청한 개념 정리와 확인한 학습 경험을 쌓는 개인 CP 학습 저장소입니다.

## 새 학습 세션의 시작

1. 이 지침 다음에 [STATE.md](STATE.md)를 읽습니다. 현재 목표·미해결 질문·다음 행동부터 재개합니다.
2. STATE가 가리키는 해당 코드와 노트의 최신 부분을 읽고 실제 파일·현재 사용자 설명과 대조합니다.
   오래된 재개 문장만 보고 이미 작성한 구현을 처음부터 가르치지 않습니다.
3. [study-algorithms](.agents/skills/study-algorithms/SKILL.md)를 적용합니다. 로드맵은 범위·우선순위를
   조정할 때만 다시 읽고, 매번 전체 저장소나 모든 기초 노트를 읽지 않습니다.
4. 현재 요청을 우선해 한 번에 학습 목표 하나와 남은 질문 하나를 짧게 잡습니다.
   이미 있는 코드·설명으로 판단할 수 있으면 같은 설명이나 사전 퀴즈를 다시 요구하지 않습니다.

기본은 목표가 분명한 과제의 설계·구현·실행 → 실제 코드·출력 피드백입니다. 새 기법은
필요한 설명 뒤 직접 적용하고, 막힌 부분에는 작은 힌트를 제공합니다. 정답을 원하면 제공하되 도움의 범위를 남깁니다. 요청 없이 사용자 풀이를 완성 코드로 교체하지 않습니다.
학습 운영·증거 구분·종료 절차의 상세 기준은 위 학습 스킬 한 곳에서 관리합니다.

## 실행과 검증

저장소 루트에서 실행합니다. Linux/WSL, uv, CPython 3.12가 기본 환경입니다.

```bash
uv sync --frozen
uv run --frozen python -m unittest discover -s tests -v
uv run --frozen python scripts/validate_notes.py
uv lock --check
git diff --check
```

웹은 `web/`에서 `npm ci`, `npm run check`, `npm test`, `npm run build`를 실행합니다.
배포 경로 검사는 `SITE_BASE=/algorithm-solutions/ npm run build` 후 같은 환경변수로
`npm run test:e2e`를 실행합니다. 검색은 빌드 미리보기에서 확인합니다.

라우터 집중 검사: `uv run --frozen python -m unittest discover -s tests -p test_companion_router.py -v`.
이전 워크스페이스 생성기 검사는 `-p test_setup_workspace.py`로 실행합니다.
검사 도구의 의존성은 개발용이며, 제출 코드는 표준 라이브러리 기반 단일 파일입니다.
제출 문법은 PyPy 3.10 호환을 기본으로 하고, 선택한 저지 실행 환경을 확인합니다.

## 학습과 기록 스킬

학습 요청에서는 `STATE.md`의 재개 위치, `ROADMAP.md`의 주제 순서, 해당 문제·자료·사용자 코드를 확인하고 다음 스킬을 적용합니다.
이름을 직접 호출하거나 자연어로 요청할 수 있습니다.

회차는 구체적인 목표·이유·완료 기준으로 시작하고, 학습자의 실제 풀이와 코드에 맞는 충분한 과제를 둡니다. 새 기법은 필요한 설명 뒤 직접 적용하고, 익숙한 주제와 혼합 연습은 독립 시도부터 시작합니다. 세부 진행 방식과 도움 경계는 해당 스킬을 따릅니다.

| 요청 | 읽을 스킬 |
| --- | --- |
| 오늘 학습 시작, 계속, 힌트 줘, 오늘 학습 종료, STATE 반영해 | [study-algorithms](.agents/skills/study-algorithms/SKILL.md) |
| 이 개념 정리해줘, 배운 지식 저장해줘 | [record-algorithm-knowledge](.agents/skills/record-algorithm-knowledge/SKILL.md) |
| 이 문제 복기해줘, 이 풀이 기록해줘 | [review-algorithm-problem](.agents/skills/review-algorithm-problem/SKILL.md) |
| 이번 대회 복기해줘, virtual 결과 정리해줘 | [review-algorithm-contest](.agents/skills/review-algorithm-contest/SKILL.md) |

정리 요청은 해당 노트 작성을 허용하며, 별도 초안 승인을 반복하지 않습니다.
사용자가 요청한 기초 참고 정리도 작성할 수 있습니다. 실제 학습 경험·제출 판정·도움 여부는
확인한 범위만 기록하고 샘플 통과나 파일 존재를 AC·독립 해결·숙달로 바꾸지 않습니다.
일반 설명이나 `이해했어`만으로 저장하지 않습니다. `오늘 학습 종료`에는 확인된 결과와
다음 행동을 정리합니다. STATE·학습 노트 갱신은 현재 요청 또는 현재 대화에서 확인된 기존
위임 범위에서 수행하고, 권한이 없으면 저장할 내용만 제안합니다. STATE는 짧은 재개 지점이며
전체 학습 이력·진도 DB를 복제하지 않습니다.
진행 중인 실전 대회의 풀이·디버깅 도움은 종료 후 복기로 돌립니다.
학습 운영과 출처는 [로드맵](ROADMAP.md), [참고 자료](docs/REFERENCES.md)를 따릅니다.

## 저장과 원격 동기화

- 학습 기록 저장, 사용자 풀이 수정, 커밋·push, 온라인 제출·배포는 별도 범위입니다.
  현재 요청이나 확인된 위임이 허용하는 범위만 수행하며, 이 문서 자체를 사용자 승인으로 삼지 않습니다.
- 저장 전 `git status`와 관련 diff를 확인하고 사용자 작업·기존 기록을 보존합니다. 허가되지 않은
  변경까지 묶어 커밋하거나 reset·clean·force push하지 않습니다.
- push가 승인됐으면 최신 원격과 비교하고 필요한 검증 후 반영합니다. 충돌은 덮어쓰지 말고 보고합니다.
  이 저장소의 main push는 기존 워크플로를 통해 Pages를 자동 갱신하므로 그 영향까지 승인됐는지 확인합니다.
- 완료 보고에서 로컬 저장·커밋·원격 SHA·CI·Pages 상태를 구분합니다. 원격 확인 전에는
  동기화 완료라고 하지 않으며, 접근 불가·미실행 검사는 그대로 밝힙니다.
- 공개 저장소에는 이 학습에 필요한 내용만 기록합니다. 계정 비밀·사생활·기기 절대경로를 넣지 않습니다.

## 파일과 환경의 주의점

- 기존 플랫폼별 코드 경로와 LeetCode의 `@lc`, `code=start/end`를 보존합니다.
  LeetCode의 class API를 stdin `solve()` 형태로 일괄 변환하지 않습니다.
- 루트 `main.py`, `ex.in`은 Git에서 제외된 사용자 작업 파일입니다.
  환경 설정·정리 과정에서 삭제하거나 템플릿으로 덮어쓰지 않습니다.
- 새 풀이 복기는 코드 옆 같은 이름의 `.md`에 둡니다. `solution`은 노트 기준 상대경로입니다.
  템플릿은 `templates/problem-note.md`, `knowledge/template.md`, `contests/template.md`입니다.
- 기본 편집 환경은 레포 루트 폴더 하나입니다. `Companion: Start problem router` Task가
  공식 Companion JSON을 URL별로 분류하고 CPH는 테스트만 실행합니다. CPH 수신 서버를 동시에 켜지 않습니다.
- 라우터는 localhost 전용이며 코드·기존 반례를 덮어쓰거나 문제 코드를 실행하지 않습니다.
  `--recover`는 원본 코드·`.cph`를 보존한 복사만 수행합니다. 미확인 사용자 파일을 임의 이동하지 않습니다.
- 예전 `scripts/setup_workspace.py`, `.local/*.code-workspace`는 호환용입니다. 첫 폴더 저장 방식이므로
  자동 분류와 혼용하지 않습니다. 기기 절대경로는 추적 파일에 넣지 않습니다.
- CSES 파일명·URL·복구 절차는 [CSES 사용법](cses/README.md), 공통 흐름은 [사용법](docs/USAGE.md)을 따릅니다.
  설정만으로 풀이·AC 기록을 만들지 않습니다. `.cph`는 로컬 메타데이터이며 보존할 반례는 복기에 남깁니다.
- 일반 풀이 검증은 샘플·필요한 반례를 중심으로 합니다. 자동 회귀 테스트는 저장소 도구와
  반복 사용하는 알고리즘 구현에 집중합니다.
- 웹은 공개 노트와 연결된 플랫폼 풀이를 직접 읽습니다. Markdown 원본·코드 경로를 보존하고
  [웹 사용법](docs/WEB.md)에 따라 링크, 검색, 배포 하위 경로를 검증합니다.
