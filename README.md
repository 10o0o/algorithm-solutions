# Algorithm Learning Lab

Python으로 문제를 직접 풀고, 복기에서 얻은 개념을 쌓는 개인 알고리즘 학습 저장소입니다.
Codeforces Candidate Master(1900)를 중간 목표, Grandmaster(2400)를 장기 목표로 둡니다.

[사용법](docs/USAGE.md) · [현재 학습 위치](STATE.md) · [로드맵](ROADMAP.md) ·
[개념 노트](knowledge/README.md) · [대회 복기](contests/README.md) · [참고 자료](docs/REFERENCES.md)

[공부용 웹사이트](https://10o0o.github.io/algorithm-solutions/)에서 개념과 문제 설명을 검색하고
연결된 Python 코드를 읽을 수 있습니다. 원본 Markdown은 이 저장소에 그대로 둡니다.

## 시작

Linux 또는 VS Code Remote WSL에서 저장소 루트를 열고 실행합니다. `uv`가 필요합니다.

```bash
uv sync --frozen
uv run --frozen python scripts/setup_workspace.py
code .local/atcoder.code-workspace
```

Codeforces는 `.local/codeforces.code-workspace`를 엽니다. 생성한 워크스페이스는
이 체크아웃의 Python과 템플릿 경로를 담는 로컬 파일이며, 이동 후에는 다시 생성합니다.
CPH를 수신하는 VS Code 창은 한 개만 열어 둡니다.

브라우저의 Competitive Companion으로 문제를 가져와 직접 풀고,
CPH의 `Ctrl+Alt+B`로 예제를 테스트한 뒤 사이트에서 제출합니다.
[확장 설치·PyPy·다중 테스트·문제 해결](docs/USAGE.md)을 참고하세요.

## 학습과 기록

```text
직접 풀이 → 필요한 힌트·리뷰 → 대회 후 업솔빙 → 요청 시 복기·개념 정리 → 독립 재풀이
```

- `atcoder/`, `codeforces/`, `leetcode/`: 기존 풀이 코드. 필요한 문제만 같은 이름의 `.md`로 복기합니다.
- `knowledge/`: 여러 문제에 다시 적용할 개념과 관련 풀이 링크.
- `contests/`: 대회 시간 배분, 미해결 이유, 다음 행동.
- `STATE.md`: 현재 범위와 다음 행동을 담는 재개 지점. `계속` 또는 `오늘 학습 시작`으로 학습을 재개합니다.

`이 개념 정리해줘`, `이 문제 복기해줘`, `이번 대회 복기해줘`라고 요청하면
레포 내장 스킬이 해당 기록을 저장합니다. 이미 아는 기초의 참고 정리도 요청할 수 있습니다.
호출할 수 있는 스킬과 기록 절차는 [사용법](docs/USAGE.md#내장-스킬-사용하기)에 있습니다.

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

웹 실행·검색·배포는 [웹 사용법](docs/WEB.md)을 따릅니다. `main`의 검증이 통과하면
GitHub Pages가 갱신됩니다. 일상적인 기록 저장은 커밋·push를 자동 수행하지 않습니다.
