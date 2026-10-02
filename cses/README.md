# CSES · CPH 작업 폴더

[CSES Problem Set](https://cses.fi/problemset/)의 Python 풀이를 이 폴더에서 관리합니다.
설정과 사용법만 준비되어 있으며, 아래 대응표는 풀이 파일 존재나 AC 여부를 의미하지 않습니다.
기존 제출 코드를 가져와 보관할 때는 실제 사용자 코드를 그대로 사용합니다.

## 시작

레포 루트 하나를 열고 URL별 자동 분류 수신 작업을 실행합니다.

```bash
uv sync --frozen
code .
```

VS Code의 `Tasks: Run Task` → `Companion: Start problem router`를 실행한 뒤
[CSES 문제 본문](https://cses.fi/problemset/task/1651/)에서 Competitive Companion의 `+`를 누릅니다.
수신기가 `cses/`에 소스·샘플을 만들고 CPH에서 `Ctrl+Alt+B`로 테스트합니다.
사이트에서 직접 제출하고 실제 결과를 확인합니다.

[설치·수신 연결·잘못 분류된 파일 복구](../docs/USAGE.md)를 따릅니다.
기존 플랫폼 `.code-workspace` 창과 라우터를 동시에 사용하지 않습니다.
클라우드 설정 생성은 사용자 PC의 브라우저·CPH 연결 확인을 의미하지 않습니다.

## URL과 파일명

라우터도 CPH 기본 제목 기반 파일명을 유지합니다. 파일 이름·경로를 수동으로 바꾸면
기존 `.cph` 반례 연결이 끊길 수 있으므로 먼저 원본 테스트를 보존합니다. 원문 URL의 문제 번호를 식별자로 사용하고,
템플릿의 `# $name$`, `# $url$`은 최초 가져오기 때 실제 값으로 치환됩니다.
같은 URL의 파일이 이미 있으면 제목이 바뀌어도 기존 파일을 다시 사용합니다.

| CSES 원문 | CPH Python 파일명 |
| --- | --- |
| [1648 · Dynamic Range Sum Queries](https://cses.fi/problemset/task/1648/) | `Dynamic_Range_Sum_Queries.py` |
| [1649 · Dynamic Range Minimum Queries](https://cses.fi/problemset/task/1649/) | `Dynamic_Range_Minimum_Queries.py` |
| [1143 · Hotel Queries](https://cses.fi/problemset/task/1143/) | `Hotel_Queries.py` |
| [1749 · List Removals](https://cses.fi/problemset/task/1749/) | `List_Removals.py` |
| [1651 · Range Update Queries](https://cses.fi/problemset/task/1651/) | `Range_Update_Queries.py` |

루트 수신기는 CSES 문제 URL을 확인한 후 `cses/`를 선택합니다.
`saveLocation`은 소스 위치가 아닌 테스트 메타데이터 위치이므로 빈 값을 유지합니다.
소스 옆 `cses/.cph/`에 현재 컴퓨터의 경로에 맞는 테스트 연결이 저장됩니다.

## 테스트 재사용과 기록

- 같은 컴퓨터·경로에서 이어 풀 때는 기존 `.py`를 열고 `Ctrl+Alt+B`를 실행합니다.
  루트 라우터로 다시 가져와도 기존 코드·테스트를 보존합니다. 기본 CPH의 직접 가져오기는
  테스트를 교체할 수 있으므로 이전 수신 창을 혼용하지 않습니다.
- `.cph/*.prob`는 소스 절대경로와 연결된 로컬 상태이므로 Git에서 제외합니다.
  이전 `.local/` 워크스페이스 역시 절대경로가 있어 제외합니다. 풀이 `.py`와 요청한 복기 `.md`는 추적합니다.
- 보존할 사용자 반례는 **이동·재가져오기 전** 같은 이름의 복기 문서에 입력, 기대 출력, 확인 이유로 남깁니다.
  복기는 [문제 노트 템플릿](../templates/problem-note.md)을 따르며 실제 소스가 있을 때 작성합니다.
  예를 들어 `Range_Update_Queries.md`의 `solution`은 `Range_Update_Queries.py`입니다.
- 다른 컴퓨터에서는 원문 샘플을 새로 가져온 뒤 보존한 반례를 CPH에 다시 추가합니다.
  `.cph`를 삭제하거나 과거 성공 상태를 복제하지 말고 다시 실행해 확인합니다.
- 새 복기 노트는 기존 노트 검사기와 웹의 CSES 필터·상대 링크에서 읽습니다.
  이 README와 임시 설정은 학습 결과·문제 복기로 색인하지 않습니다.

## 지원 근거

2026-10-02 공식 소스 확인 기준:

- [Competitive Companion CSES 파서](https://github.com/jmerle/competitive-companion/blob/df90fabb52e8f566ea3382405e22d246af5d6a69/src/parsers/problem/CSESProblemParser.ts)
- [Companion 기본 수신 포트](https://github.com/jmerle/competitive-companion/blob/df90fabb52e8f566ea3382405e22d246af5d6a69/src/hosts/hosts.ts)
- [CPH 파일명·첫 폴더·템플릿·재가져오기 처리](https://github.com/agrawal-d/cph/blob/187590eae3379bad8caaf7bd930d2987557a7966/src/companion.ts)
- [CPH 메타데이터 저장](https://github.com/agrawal-d/cph/blob/187590eae3379bad8caaf7bd930d2987557a7966/src/parser.ts)
- [CPH 사용법](https://github.com/agrawal-d/cph/blob/187590eae3379bad8caaf7bd930d2987557a7966/docs/user-guide.md)
