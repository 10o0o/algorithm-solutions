# Algorithm Learning Lab

Python으로 문제를 직접 풀고, 복기에서 얻은 개념을 쌓는 개인 알고리즘 학습 저장소입니다.
Codeforces Candidate Master(1900)를 중간 목표, Grandmaster(2400)를 장기 목표로 둡니다.

[사용법](docs/USAGE.md) · [현재 학습 위치](STATE.md) · [로드맵](ROADMAP.md) ·
[개념 노트](knowledge/README.md) · [대회 복기](contests/README.md) · [참고 자료](docs/REFERENCES.md)

[공부용 웹사이트](https://10o0o.github.io/algorithm-solutions/)에서 개념과 문제 설명을 검색하고
연결된 Python 코드를 읽을 수 있습니다. 원본 Markdown은 이 저장소에 그대로 둡니다.

## 시작: 루트 폴더 하나

Linux 또는 VS Code Remote WSL에서 저장소 루트를 열고 실행합니다. `uv`가 필요합니다.

```bash
uv sync --frozen
code .
```

VS Code에서 `Tasks: Run Task` → **Companion: Start problem router**를 한 번 실행합니다.
터미널에 `Companion router ready`가 보이면 브라우저의 Competitive Companion `+`로
문제를 가져옵니다. 원문 URL에 따라 `atcoder/`, `codeforces/`, `cses/`로 자동 분류합니다.
CPH는 생성된 파일의 `Ctrl+Alt+B` 테스트를 담당합니다.

- 플랫폼별 워크스페이스를 바꿀 필요가 없습니다. 기존 플랫폼 워크스페이스 창은 닫아 둡니다.
- 루트의 CPH 수신 서버는 꺼져 있으며, 27121 포트는 라우터 하나만 사용합니다.
- 같은 문제를 다시 가져와도 기존 코드·CPH 반례를 덮어쓰지 않습니다.
- 사용자 PC에서 Task 시작·확장 연결을 확인해야 합니다. 레포 설정만으로 PC 연결이 완료되지는 않습니다.

[설치·첫 연결·기존 파일 안전 복구](docs/USAGE.md) · [CSES URL·파일명](cses/README.md)

## 학습과 기록

```text
주제 학습: 필요한 설명·대표 문제 → 직접 설계·구현·실행·복습
혼합 연습: 태그 없이 유형 선택 → 직접 풀이 → 필요한 리뷰
```

학습 범위와 주간 운영은 [로드맵](ROADMAP.md)을 따릅니다. 이미 다룬 주제는 대표 통합 문제로
먼저 확인해 필요한 부분만 연습하고, 새 주제는 충분한 설명과 목표를 확인한 뒤 직접 설계하고
구현합니다. 문제를 섞어 유형을 고르는 연습에서는 시도 전에 주제와 태그를 가립니다.

- `atcoder/`, `codeforces/`, `cses/`, `leetcode/`: 플랫폼별 풀이 코드. 필요한 문제만 같은 이름의 `.md`로 복기합니다.
- `knowledge/`: 여러 문제에 다시 적용할 개념과 관련 풀이 링크.
- `contests/`: 대회 시간 배분, 미해결 이유, 다음 행동.
- `STATE.md`: 현재 목표·근거 코드·남은 질문·다음 한 행동을 담는 재개 지점. `계속` 또는 `오늘 학습 시작`으로 학습을 재개합니다.

`이 개념 정리해줘`, `이 문제 복기해줘`, `이번 대회 복기해줘`라고 요청하면
레포 내장 스킬이 해당 기록을 저장합니다. 이미 아는 기초의 참고 정리도 요청할 수 있습니다.
주제 학습은 `그래프 주제부터 시작하자`, `SCC를 대표 문제로 확인하자`처럼 범위를 지정할 수 있습니다.
호출할 수 있는 스킬과 기록 절차는 [사용법](docs/USAGE.md#내장-스킬-사용하기)에 있습니다.

새 에이전트도 [협업 지침](AGENTS.md#새-학습-세션의-시작)을 따라 STATE와 연결 코드·노트부터
읽습니다. 기본은 목표가 분명한 과제를 직접 설계·구현·실행하고 피드백을 받는 흐름이며, 원하면 설명이나 모범풀이를 받을 수 있습니다.
종료할 때는 확인한 결과·남은 질문·다음 행동·저장/원격 상태를 짧게 정리합니다.

파일 존재·샘플 통과와 온라인 저지 AC, 독립 해결은 각각 구분합니다.
기존 코드에서 해결 여부나 이해 수준을 자동 추정하지 않습니다.
루트 `main.py`, `ex.in`은 로컬 작업용으로 유지하며 Git에서 제외합니다.

## 검증

```bash
uv run --frozen python -m unittest discover -s tests -v
uv run --frozen python scripts/validate_notes.py
uv lock --check
```

기록 검사는 메타데이터와 파일 링크를 확인합니다. 학습 내용의 정확성이나 숙달을
판정하지 않으며, 빈 컬렉션에서 `0 note(s)`가 나오는 것도 정상입니다.
같은 검사는 GitHub Actions에서도 수행합니다.
[이번 구축의 검증 결과와 남은 확인](docs/VALIDATION.md)을 기록해 두었습니다.

웹 실행·검색·배포는 [웹 사용법](docs/WEB.md)을 따릅니다. `main`에 push하고 검증이 통과하면
GitHub Pages가 갱신됩니다. 기록 저장과 커밋·push·배포의 승인 범위는
[원격 동기화 규칙](AGENTS.md#저장과-원격-동기화)에 따라 각각 확인합니다.
