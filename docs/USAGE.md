# 문제 풀이와 학습 기록 사용법

Linux 또는 VS Code Remote WSL 환경을 기준으로 합니다. 모든 터미널 명령은
저장소 루트에서 실행합니다. 풀이 파일은 각 플랫폼 폴더에 그대로 저장합니다.

## 처음 한 번: Python과 워크스페이스

`uv`가 없다면 [공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/)를 따릅니다.

```bash
uv sync --frozen
uv run --frozen python scripts/setup_workspace.py
```

`.python-version`은 CPython 3.12를 선택하며 `.venv`에 개발 도구를 설치합니다.
YAML·Markdown 파서는 기록 검사에만 사용하므로 제출 코드에서 import하지 않습니다.
시스템 Python이나 다른 학습 레포의 가상환경은 사용하지 않습니다.

생성기는 `.local/atcoder.code-workspace`, `.local/codeforces.code-workspace`,
`.local/cses.code-workspace`를 만듭니다.
인터프리터와 템플릿을 먼저 검증하고, 내용이 같으면 파일을 다시 쓰지 않습니다.
풀이·CPH 테스트·`main.py`·`ex.in`은 변경하지 않습니다.
생성한 워크스페이스를 직접 편집한 설정은 재생성 시 교체되므로 공통 변경은 생성기에 반영합니다.
과거 루트의 두 `.code-workspace` 파일은 이 방식으로 대체했습니다.
다른 경로에 clone하거나 이동하면 `uv sync --frozen`부터 다시 실행합니다.

## VS Code와 브라우저 연결

1. 브라우저에 [Competitive Companion](https://github.com/jmerle/competitive-companion#install)을 준비합니다.
   호환 확장이 이미 설치되어 있으면 중복 설치 전에 현재 확장으로 연결을 확인합니다.
2. VS Code에서 **WSL에 설치된** CPH와 Python 확장을 확인합니다. 필요하면 다음을 실행합니다.

   ```bash
   code --install-extension divyanshuagrawal.competitive-programming-helper
   code --install-extension ms-python.python
   ```

3. 사용할 플랫폼 워크스페이스 하나를 엽니다.

   ```bash
   code .local/atcoder.code-workspace
   ```

   Codeforces는 `.local/codeforces.code-workspace`, CSES는 `.local/cses.code-workspace`를 엽니다.
4. 첫 폴더가 해당 플랫폼의 `AtCoder (CPH target)`, `Codeforces (CPH target)` 또는
   `CSES (CPH target)`인지 확인합니다.
   CPH 수신 창을 여러 개 열지 않습니다. 일반 레포 창의 수신 서버는 꺼져 있습니다.
5. 종료된 문제 페이지에서 Companion의 `+`를 누릅니다. 문제 파일과 샘플이 열리면 연결된 것입니다.

CPH가 문제 소스를 저장하는 위치는 **첫 워크스페이스 폴더**입니다.
`saveLocation`은 테스트 메타데이터 위치이며, 빈 값이면 소스 옆 `.cph/`를 사용합니다.
템플릿 경로에는 CPH가 직접 처리하지 않는 `${workspaceFolder}`를 넣지 않습니다.
생성기가 검증한 실제 경로를 로컬 워크스페이스에 기록합니다.

문제가 루트에 생기면 첫 폴더와 열린 창을 확인합니다. 연결되지 않으면
CPH의 확장 호스트, 중복 수신 창, 활성 상태를 확인하고 `Developer: Reload Window`를 실행합니다.
Windows 브라우저와 WSL 사이에 연결이 되지 않으면 VS Code Ports에서 CPH 포트 27121 전달 상태도 확인합니다.
이 생성기는 설정 파일만 준비합니다. 브라우저 확장 설치, 로컬 수신 연결, CSES 로그인·제출은
자동으로 수행하거나 검증하지 않습니다. 클라우드에서 생성한 절대경로를 PC로 복사하지 말고
실제로 VS Code를 실행할 체크아웃에서 생성기를 다시 실행합니다.

## 매 문제: 가져오기·테스트·제출

1. Companion으로 문제를 가져오고 생성된 Python 파일에 직접 풀이를 작성합니다.
2. `Ctrl+Alt+B`로 예제를 모두 실행합니다. `Ctrl+Alt+D`로 CPH 화면을 열 수 있습니다.
3. 경계값·반례를 CPH에 추가합니다. 여러 답이 가능한 문제는 출력 문자열 비교만으로
   정답 여부를 판정하지 말고 조건이나 별도 checker를 확인합니다.
4. 사이트에서 Python/PyPy 제출 언어를 선택하고 코드를 직접 제출합니다.
5. 온라인 결과를 확인한 뒤 필요한 문제만 복기합니다. 로컬 샘플 통과는 AC가 아닙니다.

기본 CPH 제한은 5초입니다. 문제별 제한과 머신 성능이 다르므로 로컬 실행 시간을
저지 통과의 보장으로 사용하지 않습니다. RE는 오류 출력, TLE는 루프와 복잡도부터 확인합니다.
디버그 출력은 `sys.stderr`로 보내 제출 출력과 구분합니다.
Interactive 문제는 이 표준 입력·샘플 실행 흐름의 검증 대상이 아닙니다.

### CSES

[CSES 전용 사용법](../cses/README.md)의 URL·파일명 규칙을 사용합니다.
Competitive Companion은 `https://cses.fi/problemset/task/문제번호/`에서 제목·원문 URL·예제를
가져올 수 있습니다. CPH에는 CSES 번호 전용 파일명 옵션이 없어 제목 기반 이름을 그대로
유지합니다. 예를 들어 1651은 `cses/Range_Update_Queries.py`이며 템플릿 상단에 원문 URL이 남습니다.
가져오기는 문제 페이지에서 수행하고, 기존 파일을 테스트할 때는 다시 가져오지 않고 직접 엽니다.
CSES 제출은 사이트에서 직접 하며 CPH의 Codeforces 제출 기능을 사용하지 않습니다.

### 단일·다중 테스트 템플릿

기본은 `templates/python.py`의 `solve()`를 한 번 호출하는 형태입니다.
입력 첫 줄이 테스트 개수 `t`인 문제에는 `templates/python-multi.py`를 사용합니다.
Codeforces라고 모든 문제가 다중 테스트인 것은 아닙니다.

```bash
uv run --frozen python scripts/setup_workspace.py --platform codeforces --template multi
```

워크스페이스를 다시 열거나 Reload Window를 실행한 뒤 **새 문제를 가져올 때** 적용됩니다.
기존 풀이 파일은 템플릿으로 덮어쓰지 않습니다. 이미 작성 중인 파일의 호출 구조는
문제 입력 형식에 맞게 직접 수정합니다.

단일 테스트로 되돌리기:

```bash
uv run --frozen python scripts/setup_workspace.py --platform codeforces --template single
```

### PyPy로 실행하기

개발 도구는 CPython 3.12에 유지하고 풀이 실행용 PyPy를 별도로 준비합니다.

```bash
uv python install pypy@3.10
uv venv --no-project --python pypy@3.10 .venv-pypy
uv run --frozen python scripts/setup_workspace.py --platform codeforces --python .venv-pypy/bin/python
```

워크스페이스를 다시 열면 CPH가 PyPy를 직접 실행합니다. 다중 테스트도 함께 선택하려면
같은 생성 명령에 `--template multi`를 추가합니다. CPython으로 되돌릴 때는 `--python` 없이 생성합니다.
플랫폼별 버전은 [Codeforces](https://codeforces.com/blog/entry/121114)와
[AtCoder](https://img.atcoder.jp/file/language-update/2025-10/language-list.html)의 언어 안내,
실제 제출 화면에서 확인합니다. 로컬 빌드와 저지의 패치 버전·성능은 다를 수 있습니다.

## 연결이 안 될 때와 테스트 보존

CPH에 샘플 입력·출력을 직접 추가하거나 기존 방식으로 실행할 수 있습니다.
아래 명령은 직접 준비한 `main.py`, `ex.in`을 사용하는 예시입니다.

```bash
uv run --frozen python main.py < ex.in
.venv-pypy/bin/python main.py < ex.in
```

`main.py`, `ex.in`, `.cph/`, `.local/`, 두 가상환경은 Git에서 제외됩니다.
기존 로컬 파일을 지우거나 초기화할 필요가 없습니다.

CPH는 소스의 절대경로를 hash한 이름으로 테스트를 저장합니다. 소스를 옮기면 옛 테스트가
화면에서 보이지 않을 수 있습니다. 재가져오면 테스트 목록이 샘플로 교체될 수 있으므로,
**이동·재가져오기 전에 중요한 사용자 반례를 복기 문서에 입력·기대 출력으로 보존**합니다.
이미 이동했다면 기존 `.cph/*.prob`의 내용을 확인해 필요한 사례를 수동 복구합니다.
메타데이터를 자동 삭제하거나 성공 상태를 새로 만들어 채우지 않습니다.
다른 컴퓨터에서는 같은 원문을 한 번 가져온 뒤, 저장해 둔 추가 반례를 CPH에 다시 붙여 넣어
실행합니다. `.cph`를 Git에 올리거나 이전 머신의 절대경로를 그대로 복사해 연결을 가정하지 않습니다.

## LeetCode

LeetCode의 class/API 형식과 `@lc app=leetcode`, `# @lc code=start/end`는 그대로 사용합니다.
CPH의 stdin 템플릿을 LeetCode 파일에 적용하지 않습니다.

```bash
code --install-extension leetcode.vscode-leetcode
```

확장에는 Node.js 실행기가 필요합니다. `LeetCode: Sign In`에서 로그인한 뒤 문제를 열고
`Test`, `Submit`, `Description`을 사용합니다. 인증은 확장·브라우저에서 수행하며
쿠키나 비밀번호를 이 저장소의 설정에 넣지 않습니다.

다른 머신에서는 확장의 **사용자 설정**에서 다음을 확인합니다. LeetCode 설정은
application scope이므로 `.vscode/settings.json`에 넣어 해결되는 것으로 가정하지 않습니다.

- `leetcode.nodePath`: 실제 Node.js 실행 파일.
- `leetcode.workspaceFolder`: 이 저장소의 루트 경로.
- `leetcode.defaultLanguage`: `python3`.
- `leetcode.filePath.default.folder`: `leetcode/${difficulty}`.
- `leetcode.filePath.default.filename`: `${id}.${kebab-case-name}.${ext}`.
- `leetcode.showDescription`: `In Webview`.
- `leetcode.editor.shortcuts`: `submit`, `test`, `description`.

새 Contest 문제는 확장 목록에 바로 없을 수 있으므로 브라우저에서 풀고, 일반 문제로
등록된 뒤 검색합니다. 검색되지 않으면 새로고침과 `LeetCode: Delete Cache`를 확인합니다.
로그인·제출 성공 여부는 실제 온라인 결과로 확인합니다.

## 학습과 기록

`오늘 학습 시작` 또는 `계속`은 [STATE](../STATE.md)의 현재 범위를 재개합니다.
직접 시도한 코드·설명을 바탕으로 힌트와 리뷰를 받고, `정리해줘`라고 요청하면
확인된 이해나 요청한 기초 참고 자료를 함께 기록합니다. 같은 주제는 기존 노트를 보완합니다.
`오늘 학습 종료`는 다음 행동을 제안하며, `STATE 반영해`라고 요청하면 재개 위치를 저장합니다.

### 내장 스킬 사용하기

스킬은 저장소의 `.agents/skills/`에 포함되어 있으며 자연어 요청과 `$스킬명` 모두 지원합니다.

| 평소 요청 | 스킬 |
| --- | --- |
| 오늘 학습 시작 / 계속 / 힌트 줘 | [study-algorithms](../.agents/skills/study-algorithms/SKILL.md) |
| 이 개념 정리해줘 / 배운 지식 저장해줘 | [record-algorithm-knowledge](../.agents/skills/record-algorithm-knowledge/SKILL.md) |
| 이 문제 복기해줘 | [review-algorithm-problem](../.agents/skills/review-algorithm-problem/SKILL.md) |
| 이번 대회 복기해줘 | [review-algorithm-contest](../.agents/skills/review-algorithm-contest/SKILL.md) |

예를 들어 `$record-algorithm-knowledge 이분 탐색의 경계 조건을 정리해줘`라고 요청합니다.
정리 요청은 파일 저장까지 포함하므로 초안 승인을 다시 요구하지 않습니다.
단순 설명, `이해했어`, `오늘 학습 종료`만으로 노트를 작성하지 않습니다.
일상적인 기록 스킬은 커밋·push·배포를 자동 수행하지 않습니다.
새 스킬이 표시되지 않으면 이 저장소에서 새 Codex 세션을 시작합니다.

### 기록 위치

- 문제 복기: `templates/problem-note.md`를 코드 옆 같은 이름의 `.md`에 복사하고 내용을 채웁니다.
  `solution`은 **그 노트 기준** 상대경로입니다. 예: `abc470a.md` 옆 코드는 `abc470a.py`.
- 재사용할 개념: [knowledge 작성법](../knowledge/README.md)을 따릅니다.
- 대회 전체의 시간 배분·미해결 이유: [contests 작성법](../contests/README.md)을 따릅니다.
- 출처 전문을 복제하지 않고 원문 URL과 자신의 설명을 연결합니다.
- 도움 사용 여부, 제출 결과, 독립 재풀이 결과는 관찰한 경우에만 기록합니다.

## 저장소 도구 검사

```bash
uv run --frozen python -m unittest discover -s tests -v
uv run --frozen python scripts/validate_notes.py
uv lock --check
git diff --check
```

검사기는 `knowledge/`, `contests/`, 플랫폼 폴더의 실제 Markdown 기록을 읽습니다.
README와 기록 템플릿은 기본 검사에서 제외합니다. 특정 완성 노트는 경로 인자로 검사할 수 있습니다.
메타데이터·로컬 파일 링크만 검사하며 외부 사이트 로그인, 링크 상태 확인, 정답 판정은 하지 않습니다.
실제 노트가 0개여도 성공할 수 있으며, 그것은 학습 완료를 의미하지 않습니다.

웹의 실행·검색 확인·배포 절차는 [웹 사용법](WEB.md)을 참고합니다.
