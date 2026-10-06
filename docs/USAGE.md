# 문제 풀이와 학습 기록 사용법

Linux 또는 VS Code Remote WSL 환경을 기준으로 합니다. 모든 터미널 명령은
저장소 루트에서 실행합니다. 풀이 파일은 각 플랫폼 폴더에 그대로 저장합니다.

## 처음 한 번: 루트 폴더와 수신 작업

`uv`가 없다면 [공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/)를 따릅니다.

```bash
uv sync --frozen
code .
```

`.python-version`은 CPython 3.12를 선택하며 `.venv`에 저장소 도구를 설치합니다.
YAML·Markdown 파서는 기록 검사에만 사용하므로 제출 코드에서 import하지 않습니다.
기기별 절대경로는 추적 파일에 넣지 않습니다. VS Code Task의 `${workspaceFolder}`는
VS Code가 현재 체크아웃 경로로 바꾸며, 수신기는 자기 위치에서 저장소 루트를 찾습니다.

1. 브라우저의 [Competitive Companion](https://github.com/jmerle/competitive-companion#install)과
   VS Code 추천 확장 CPH·Python을 준비합니다. WSL이라면 해당 WSL에 설치된 확장인지 확인합니다.
2. 예전 `.local/atcoder.code-workspace`, `codeforces.code-workspace`, `cses.code-workspace`
   수신 창을 모두 닫고 **저장소 루트 폴더 하나**를 엽니다. `.local` 파일 자체는 지우지 않아도 됩니다.
3. `Tasks: Run Task` → `Companion: Start problem router`를 실행합니다.
   터미널의 `Companion router ready on 127.0.0.1:27121`과 현재 레포 경로를 확인합니다.
4. 종료된 문제의 원문 페이지에서 Companion의 `+`를 누릅니다.
   URL을 보고 AtCoder→`atcoder/`, Codeforces→`codeforces/`, CSES→`cses/`에 저장합니다.
5. 생성 파일이 루트 창에서 열리면 `Ctrl+Alt+B`로 CPH 테스트를 실행합니다.
   `code` CLI를 찾지 못하면 라우터 터미널에 나온 파일을 탐색기에서 직접 엽니다.

새 창을 열 때 자동 실행하는 설정은 넣지 않았습니다. 기본은 위의 명시적 Task 실행이며,
`Terminal: Terminate Task` 또는 작업 터미널의 `Ctrl+C`로 수신기를 멈출 수 있습니다.
자동 시작을 원한다면 사용자가 VS Code의 작업 실행 설정과 자동 작업 허용 여부를 직접 선택합니다.
저장소 신뢰·브라우저 권한·방화벽을 자동 승인하거나 바꾸지 않습니다.

### 왜 작은 수신기가 필요한가

기본 CPH는 사이트 URL이 아닌 **첫 워크스페이스 폴더**에 문제 파일을 만듭니다.
AtCoder 워크스페이스에서 CSES가 `atcoder/`에 생긴 이유가 이 동작입니다.
`cph.general.saveLocation`은 소스 폴더가 아니라 테스트 메타데이터 위치입니다.

이 레포의 `scripts/companion_router.py`는 Companion 공식 JSON 프로토콜을 받아 URL만으로
저장 폴더를 결정합니다. CPH 수신 서버는 `.vscode/settings.json`에서 꺼 두고,
라우터가 소스와 CPH 호환 `.cph` 파일을 만들면 CPH는 기존 방식으로 테스트합니다.
추가 VS Code 확장이나 브라우저 포트 설정은 필요하지 않습니다.
호환 형식은 [CPH 메타데이터 구현](https://github.com/agrawal-d/cph/blob/187590eae3379bad8caaf7bd930d2987557a7966/src/parser.ts),
[CPH 문제·테스트 타입](https://github.com/agrawal-d/cph/blob/187590eae3379bad8caaf7bd930d2987557a7966/src/types.ts),
[Companion 전송 구현](https://github.com/jmerle/competitive-companion/blob/df90fabb52e8f566ea3382405e22d246af5d6a69/src/hosts/CustomHost.ts)에 맞췄습니다.
확장 업데이트로 형식이 바뀌면 이 어댑터를 함께 확인해야 합니다.

수신기는 `127.0.0.1`에만 열리고 지원하는 HTTPS 문제 URL·JSON 스키마·2 MiB 제한을 검사합니다.
임의 경로·명령·custom checker 필드는 사용하지 않으며 풀이를 실행하거나 제출하지 않습니다.
VS Code 파일 열기는 `code --reuse-window`만 사용합니다. 여러 VS Code 창 중 어느 창이 선택될지
혼동하지 않도록 학습용 레포 창 하나를 유지합니다.

### 수신이 안 될 때

- 라우터 터미널의 `ready`와 이후 `created`/`preserved`/`rejected` 메시지를 먼저 확인합니다.
  Companion은 서버 오류 응답을 화면에 표시하지 않을 수 있습니다.
- 27121 포트가 사용 중이면 예전 CPH 창·다른 라우터를 닫습니다. 이미 실행 중인 작업을
  강제 종료하거나 다른 포트로 조용히 바꾸지 않습니다. 한 포트에 수신기 하나만 실행합니다.
- 작업 이름이 안 보이면 `.code-workspace`가 아니라 레포 루트를 열었는지 확인합니다.
  `.venv/bin/python`이 없다는 오류는 레포 루트에서 `uv sync --frozen`으로 준비합니다.
- Windows 브라우저→WSL 연결이면 CPH·작업이 실행되는 WSL과 VS Code Ports의 27121 전달 상태를 확인합니다.
- 외부 사이트·목록·프로필·제출 결과 URL은 거절합니다. 문제 원문 페이지에서 가져옵니다.
- 클라우드 설정 검증은 사용자 PC의 브라우저→수신기→CPH 연결 검증을 대신하지 않습니다.

## 잘못 분류된 기존 파일: 원본을 남기는 복구

예전에 CSES가 AtCoder 폴더에 만들어졌다면 VS Code에서 먼저 저장하고 모든 수신 작업을 멈춥니다.
파일 탐색기로 바로 옮기면 `.cph`의 절대경로 연결이 끊길 수 있습니다.
다음 명령의 파일명은 **실제 존재하는 파일명**으로 바꿉니다.

```bash
uv run --frozen python scripts/companion_router.py --recover atcoder/Range_Update_Queries.py
```

원래 `.cph`의 URL을 검증해 올바른 폴더로 코드와 테스트를 **복사**하고 새 절대경로로 연결합니다.
원본 코드·원본 `.cph`는 그대로 남깁니다. 같은 복구를 반복해도 대상 코드나 추가 반례를 덮어쓰지 않습니다.
대상에 다른 코드가 있거나 대상 테스트에 원본 반례가 누락되어 있거나 원본 메타데이터가 없으면
덮어쓰지 않고 중단합니다. 누락 반례는 두 원본을 비교해 별도로 옮겨야 합니다.
사용자 custom checker가 연결된 파일도 자동 복구하지 않습니다.

새 파일을 열어 사용자 코드·반례와 `Ctrl+Alt+B` 결과를 확인한 뒤 원본 정리 여부를 결정합니다.
복기 노트·링크까지 자동 이동하지 않으므로 원본 삭제나 경로 정리는 별도 확인 후 수행합니다.
현재 클라우드에는 사용자 PC의 잘못 생성된 파일이 없어 이 명령을 실제 사용자 파일에 실행하지 않았습니다.

## 매 문제: 가져오기·테스트·제출

1. 루트 창의 라우터가 준비된 상태에서 Companion으로 가져오고 생성된 Python 파일에 직접 풀이를 작성합니다.
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
가져올 수 있습니다. CPH와의 일관성을 위해 라우터도 CSES 제목 기반 파일명을
유지합니다. 예를 들어 1651은 `cses/Range_Update_Queries.py`이며 템플릿 상단에 원문 URL이 남습니다.
가져오기는 문제 페이지에서 수행하고, 기존 파일을 테스트할 때는 다시 가져오지 않고 직접 엽니다.
CSES 제출은 사이트에서 직접 하며 CPH의 Codeforces 제출 기능을 사용하지 않습니다.

### 템플릿과 풀이 실행기

라우터는 `templates/python.py`의 단일 `solve()` 템플릿으로 **새 파일만** 만듭니다.
입력 첫 줄이 테스트 수 `t`인 문제는 직접 호출 구조를 조정하거나 `templates/python-multi.py`를
참고합니다. 플랫폼만 보고 다중 테스트를 가정하지 않습니다. 기존 파일은 수정하지 않습니다.

VS Code Python 확장의 선택 인터프리터는 `.venv/bin/python`입니다.
**CPH는 별도로 `cph.language.python.Command`를 사용하며 기본값은 `python3`**입니다.
CPH에서 PyPy를 쓰려면 사용자 설정의 해당 항목을 실제 `pypy3` 실행 명령/경로로 지정합니다.
`${workspaceFolder}` 같은 변수를 CPH의 명령·템플릿 경로에서 지원한다고 가정하지 않습니다.
저지별 제출 언어와 로컬 실행기의 차이는 실제 제출 화면에서 확인합니다.

### 이전 플랫폼 워크스페이스 모드

`scripts/setup_workspace.py`와 기존 `.local/*.code-workspace`는 원본 보존을 위해 남겨 둡니다.
이전 모드는 첫 폴더에 저장하는 CPH 기본 동작이며 URL별 자동 분류를 제공하지 않습니다.
다시 쓸 경우 루트 라우터를 먼저 종료해야 합니다. 두 방식을 동시에 실행하지 않습니다.
새 기본 흐름에는 워크스페이스 생성기를 실행할 필요가 없습니다.

## 연결이 안 될 때와 테스트 보존

CPH에 샘플 입력·출력을 직접 추가하거나 기존 방식으로 실행할 수 있습니다.
아래 명령은 직접 준비한 `main.py`, `ex.in`을 사용하는 예시입니다.

```bash
uv run --frozen python main.py < ex.in
.venv-pypy/bin/python main.py < ex.in
```

`main.py`, `ex.in`, `.cph/`, `.local/`, 두 가상환경은 Git에서 제외됩니다.
기존 로컬 파일을 지우거나 초기화할 필요가 없습니다.

CPH와 라우터는 소스의 절대경로를 hash한 이름으로 테스트를 저장합니다. 소스를 옮기면 옛 테스트가
화면에서 보이지 않을 수 있습니다. 기본 CPH로 재가져오면 테스트가 교체될 수 있으므로,
**이동·재가져오기 전에 중요한 사용자 반례를 복기 문서에 입력·기대 출력으로 보존**합니다.
이미 이동했다면 기존 `.cph/*.prob`의 내용을 확인해 필요한 사례를 수동 복구합니다.
루트 라우터의 재가져오기는 기존 테스트를 그대로 보존합니다. 기존 URL을 확인할 수 없는
동명 파일은 덮어쓰지 않고 거절합니다. 동시 저장은 저장소 잠금으로 막으며, I/O 실패 때도
이미 만든 코드를 삭제하지 않습니다. 원인을 해결한 뒤 같은 문제를 다시 가져와 빠진 메타데이터만
생성할 수 있습니다. 메타데이터를 삭제하거나 성공 상태를 새로 만들어 채우지 않습니다.
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

`오늘 학습 시작` 또는 `계속`은 [STATE](../STATE.md)와 연결된 실제 코드·노트부터 재개합니다.
에이전트는 현재 요청에 맞는 목표·완료 기준을 잡고 필요한 설명 → 직접 설계·구현·실행 → 피드백으로
진행합니다. 막힌 부분에는 작은 힌트를 제공합니다. 설명·모범풀이를 원하면 요청할 수 있으며, 이미 작성한 구현을 처음부터 반복하지 않습니다.
`정리해줘` 요청은 관련 노트 저장까지 포함하고 같은 주제는 기존 노트를 보완합니다.

`오늘 학습 종료`에는 수업을 멈추고 확인된 결과·미확인·다음 한 행동·저장 상태를 정리합니다.
`STATE 반영해` 요청 또는 현재 대화에서 확인된 기존 위임 범위에서는 재개 위치를 함께 저장합니다.
그런 권한이 없다면 저장할 내용만 제안합니다. 상세 진행 기준은
[학습 스킬](../.agents/skills/study-algorithms/SKILL.md)을 따릅니다.

주제 학습은 [로드맵](../ROADMAP.md)의 연결된 기술 순서를 따르며, 범위를 직접 지정할 수도 있습니다.
이미 아는 주제는 먼저 대표 통합 문제로 설계·구현 능력을 확인해 필요한 부분만 연습합니다.
새 주제는 문제 풀이 전에 개념을 일관된 흐름으로 설명하고 목표와 완료 기준을 정한 뒤,
직접 설계·구현·실행·리뷰합니다. 한 세션 전체를 짧은 문답으로 잘게 나누지 않습니다.
여러 주제를 섞어 푸는 연습에서는 시도 전에 태그와 주제를 공개하지 않습니다.
예를 들어 `그래프 주제를 이어서 공부하자` 또는 `SCC를 대표 문제로 먼저 확인하자`라고 요청할 수 있습니다.
자료별 역할은 [참고 자료](REFERENCES.md)에 정리되어 있습니다.

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
단순 설명이나 `이해했어`는 새로운 저장 권한이 아닙니다. 종료 시 저장도 확인된 요청·위임
범위만 따릅니다. 커밋·push가 승인된 경우에는 [원격 동기화 규칙](../AGENTS.md#저장과-원격-동기화)에
따라 원격 SHA·CI까지 확인합니다. main push에는 Pages 자동 갱신도 포함되므로 해당 영향까지
승인되어야 합니다. 로컬 저장만 했거나 접근이 막혔다면 원격 반영 완료라고 하지 않습니다.
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
