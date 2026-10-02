# CSES · CPH 작업 폴더

[CSES Problem Set](https://cses.fi/problemset/)의 Python 풀이를 이 폴더에서 관리합니다.
설정과 사용법만 준비되어 있으며, 아래 대응표는 풀이 파일 존재나 AC 여부를 의미하지 않습니다.
기존 제출 코드를 가져와 보관할 때는 실제 사용자 코드를 그대로 사용합니다.

## 시작

실제로 VS Code를 실행할 컴퓨터의 저장소 루트에서 실행합니다.

```bash
uv sync --frozen
uv run --frozen python scripts/setup_workspace.py --platform cses
code .local/cses.code-workspace
```

1. VS Code 추천 확장인 CPH·Python과 브라우저의
   [Competitive Companion](https://github.com/jmerle/competitive-companion#install)을 준비합니다.
   WSL 사용자는 CPH가 해당 WSL 확장 호스트에서 실행되는지 확인합니다.
2. 첫 워크스페이스 폴더가 `CSES (CPH target)`인지 확인하고 CPH 수신 창은 하나만 둡니다.
3. CSES **문제 페이지**에서 Companion의 `+`를 누릅니다. 목록·통계·제출 결과 페이지가 아닙니다.
4. 생성된 파일 상단 제목·URL과 CPH의 샘플을 원문과 대조한 뒤 직접 풀이를 작성합니다.
5. `Ctrl+Alt+B`로 샘플·추가 반례를 실행하고 CSES 사이트에서 직접 제출합니다.
   로컬 통과, 사용자가 보고한 AC, 직접 확인한 온라인 판정을 서로 구분합니다.

전체 설치·PyPy·연결 문제 해결은 [공통 사용법](../docs/USAGE.md)을 따릅니다.
클라우드에서 설정 생성에 성공해도 사용자 PC의 Companion→CPH 연결이 확인된 것은 아닙니다.
수신 포트는 27121이며, 연결 문제가 있을 때 확장 호스트·중복 창·WSL 포트 전달을 확인합니다.
방화벽이나 브라우저 권한을 임의로 변경하지 않습니다.

## URL과 파일명

CPH 기본 제목 기반 파일명을 유지합니다. 임의로 번호 이름으로 바꾸면 재가져오기 때 별도 파일이
생기거나 기존 반례 연결이 끊길 수 있습니다. 원문 URL의 문제 번호를 식별자로 사용하고,
템플릿의 `# $name$`, `# $url$`은 최초 가져오기 때 실제 값으로 치환됩니다.

| CSES 원문 | CPH Python 파일명 |
| --- | --- |
| [1648 · Dynamic Range Sum Queries](https://cses.fi/problemset/task/1648/) | `Dynamic_Range_Sum_Queries.py` |
| [1649 · Dynamic Range Minimum Queries](https://cses.fi/problemset/task/1649/) | `Dynamic_Range_Minimum_Queries.py` |
| [1143 · Hotel Queries](https://cses.fi/problemset/task/1143/) | `Hotel_Queries.py` |
| [1749 · List Removals](https://cses.fi/problemset/task/1749/) | `List_Removals.py` |
| [1651 · Range Update Queries](https://cses.fi/problemset/task/1651/) | `Range_Update_Queries.py` |

CPH에 CSES 번호형 이름을 지정하는 설정은 없습니다. 설정 생성기는 `cses/`를 첫 폴더로 지정하며
`saveLocation`은 소스 위치가 아닌 **테스트 메타데이터 위치**입니다. 빈 값으로 두어
`cses/.cph/`를 사용합니다. 문제 코드는 Companion으로 가져올 때 생성되며 설정 생성기는 만들지 않습니다.

## 테스트 재사용과 기록

- 같은 컴퓨터·경로에서 이어 풀 때는 기존 `.py`를 열고 `Ctrl+Alt+B`를 실행합니다.
  매번 Companion의 `+`를 누르지 않습니다. 재가져오기는 기존 코드가 있어도 테스트를 샘플로 교체할 수 있습니다.
- `.cph/*.prob`는 소스 절대경로와 연결된 로컬 상태이므로 Git에서 제외합니다.
  `.local/` 워크스페이스 역시 절대경로가 있어 제외합니다. 풀이 `.py`와 요청한 복기 `.md`는 추적합니다.
- 보존할 사용자 반례는 **이동·재가져오기 전** 같은 이름의 복기 문서에 입력, 기대 출력, 확인 이유로 남깁니다.
  복기는 [문제 노트 템플릿](../templates/problem-note.md)을 따르며 실제 소스가 있을 때 작성합니다.
  예를 들어 `Range_Update_Queries.md`의 `solution`은 `Range_Update_Queries.py`입니다.
- 다른 컴퓨터에서는 원문 샘플을 새로 가져온 뒤 보존한 반례를 CPH에 다시 추가합니다.
  `.cph`를 삭제하거나 과거 성공 상태를 복제하지 말고 다시 실행해 확인합니다.
- 새 복기 노트는 기존 노트 검사기와 웹의 CSES 필터·상대 링크에서 읽습니다.
  이 README와 임시 설정은 학습 결과·문제 복기로 색인하지 않습니다.

## 지원 근거

2026-10-02 공식 소스 확인 기준:

- [Competitive Companion CSES 파서](https://github.com/jmerle/competitive-companion/blob/master/src/parsers/problem/CSESProblemParser.ts)
- [Companion 기본 수신 포트](https://github.com/jmerle/competitive-companion/blob/master/src/hosts/hosts.ts)
- [CPH 파일명·첫 폴더·템플릿·재가져오기 처리](https://github.com/agrawal-d/cph/blob/main/src/companion.ts)
- [CPH 메타데이터 저장](https://github.com/agrawal-d/cph/blob/main/src/parser.ts)
- [CPH 사용법](https://github.com/agrawal-d/cph/blob/main/docs/user-guide.md)
