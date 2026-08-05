# Algorithm Solutions

LeetCode, AtCoder, Codeforces 문제를 Python으로 풀고 기록하는 저장소입니다.

## 처음 한 번만 할 일

1. 브라우저에 [Competitive Companion](https://github.com/jmerle/competitive-companion#install)을 설치합니다.
2. VS Code에서 이 저장소를 연 뒤 `Developer: Reload Window`를 한 번 실행합니다.
3. LeetCode 사이드바에서 `Sign in to LeetCode`를 누르고 `Third Party` 로그인을 선택합니다.

## AtCoder / Codeforces

1. 브라우저에서 문제 페이지를 엽니다.
2. Competitive Companion의 초록색 `+` 버튼을 누릅니다.
3. VS Code 루트에 Python 파일이 열리고 예제 입력/출력이 CPH에 채워집니다.
4. 코드를 작성하고 `Ctrl+Alt+B`로 예제 테스트를 실행합니다.
5. 사이트에서 직접 제출합니다.
6. 정답 처리 후 파일을 `atcoder/` 또는 `codeforces/`로 옮깁니다.

CPH 단축키:

- `Ctrl+Alt+B`: 모든 테스트케이스 실행
- `Ctrl+Alt+D`: CPH 채점 화면 열기

CPH가 만드는 테스트 메타데이터는 `.cph/`에 저장되며 Git에는 포함되지 않습니다.

## LeetCode

1. LeetCode 사이드바에서 문제를 고릅니다.
2. `Show Problem`을 선택하면 `leetcode/문제번호.문제이름.py`가 생성됩니다.
3. 문제 설명은 별도의 Webview 탭으로 열립니다.
4. 풀이 코드 아래의 `# @lc code=end` 근처에서 `Submit | Test | Description` 버튼을 사용합니다.
5. `Test`로 사용자 테스트를 실행하고, 통과하면 `Submit`으로 제출합니다.

문제 설명 탭을 닫았을 때는 풀이 파일 아래쪽의 `Description`을 누르면 다시 열립니다. 현재 설정은 `In Webview`이므로 문제 설명 전문을 Python 파일에 주석으로 저장하지 않습니다. 대신 파일 위쪽의 `@lc app=leetcode ...` 메타데이터를 이용해 필요할 때 LeetCode에서 다시 불러옵니다. `@lc`로 시작하는 줄과 `@lc code=start`, `@lc code=end`는 테스트와 제출에 필요하므로 삭제하지 않습니다.

### LeetCode Contest 문제

진행 중인 Contest 문제는 VS Code 확장의 문제 목록에 바로 나타나지 않을 수 있으므로 LeetCode 웹사이트에서 푸는 것이 가장 안정적입니다. Contest가 끝나고 문제가 일반 문제 목록에 등록되면 다음 순서로 가져옵니다.

1. LeetCode 사이드바에서 새로고침합니다.
2. 검색 버튼으로 문제 번호 또는 정확한 제목을 검색합니다.
3. 문제를 우클릭하고 `Show Problem`을 선택합니다.

검색되지 않으면 명령 팔레트에서 `LeetCode: Delete Cache`를 실행한 뒤 `Developer: Reload Window`로 다시 불러오고 검색합니다.

### LeetCode 버튼이 보이지 않을 때

1. 풀이 파일의 맨 아래 `# @lc code=end`까지 이동합니다.
2. 파일 안에 `@lc app=leetcode` 메타데이터가 남아 있는지 확인합니다.
3. `Developer: Reload Window`를 실행합니다.

이 저장소에서는 CodeLens와 `Submit`, `Test`, `Description` 버튼이 모두 활성화되어 있습니다.

`leetcode.com` 로그인 방식이 바뀌어 일반 아이디/비밀번호 로그인은 잘 동작하지 않을 수 있습니다. 먼저 GitHub 같은 제3자 계정을 LeetCode 계정에 연결한 뒤 `Third Party` 로그인을 사용하는 것이 권장됩니다.

## 폴더

```text
algorithm-solutions/
├── atcoder/
├── codeforces/
├── leetcode/
└── templates/
    └── python.py
```

문제 풀이 파일에는 비밀번호, 세션 쿠키, API 키를 저장하지 않습니다.
