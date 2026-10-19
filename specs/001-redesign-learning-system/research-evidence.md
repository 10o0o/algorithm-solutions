# 학습 구성 조사와 출발점 근거

확인일: 2026-10-19 KST. 이 문서는 명세 검토를 위한 조사 근거이며, 새 학습 과정의 적용 또는 사용자의 학습 완료 기록이 아니다.

## 확인한 사용자 조건

- 주 5–7시간.
- AtCoder 파랑(1600) → 노랑(2000), 별도로 ABC 실전 올솔, 장기 Codeforces 빨강(2400+).
- 사용자가 직접 설계·구현·실행하면서 충분히 시도한다.

## 최신 AtCoder 기록

[공식 프로필](https://atcoder.jp/users/10o0o?lang=en)과 [공식 기록 JSON](https://atcoder.jp/users/10o0o/history/json)을 직접 조회했다. 프로필 검색 캐시와 기존 STATE의 ABC478·972 수치보다 최신 기록을 사용한다.

| 항목 | 확인한 값 |
| --- | --- |
| 최신 rated 참가 | ABC480, 2026-10-17 |
| Rating | 972 → 1065, provisional |
| Performance / 순위 | 1532 / 1306위 |
| Rated 참가 수 | 9회 |
| 최근 5회 performance | 1197, 1228, 1272, 1505, 1532 |
| 위 5회 평균 / 중앙값 | 1346.8 / 1272 |

[ABC480 공식 안내](https://atcoder.jp/contests/abc480)에 따르면 21:00–22:40 KST의 100분 대회이며 A–G 7문제로 구성되었다.

공식 제출 목록과 standings JSON의 직접 요청은 HTTP 429로 확인하지 못했다. 아래는 [AtCoder Problems 공개 API](https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=10o0o&from_second=1792238400)를 대회 시간 구간으로 필터링한 **비공식 자료**다. [API 제공자의 문서](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md)와 출처를 구분한다.

| 문제 | 판정 | 대회 시작 후 AC 제출 시각 | 제출 ID |
| --- | --- | --- | --- |
| A | AC | 5:30 | 80107263 |
| B | AC | 18:32 | 80117377 |
| C | AC | 34:58 | 80127069 |
| D | AC | 55:05 | 80137079 |
| E | AC | 87:01 | 80149668 |

- 위 시간은 누적 제출 시각이다. 문제별 순수 사고 시간·구현 시간은 알 수 없다.
- 도움 여부와 F/G를 읽거나 시도했는지는 미확인이다.
- 한 대회의 performance나 AC 기록만으로 주제별 숙달과 독립 해결을 판정하지 않는다.
- 직접 조회한 원본 응답과 URL·조회 시각·SHA-256 영수증은 Git에서 제외된 `.local/curriculum-research-2026-10-19/`에 보관했다.

## 실제 파일에서 확인한 재개 지점

- `cses/Planets_and_Kingdoms.py`에 반복형 Kosaraju 코드가 있다. 파일 존재만으로 도움 여부·온라인 판정을 추정하지 않는다.
- 로컬 scratch `main.py`에 `find_scc`, `build_condensation` 구현이 있고 `max_coins`는 `NotImplementedError`다. 이 파일은 Git에서 제외되어 공개 기록이나 다른 기기에서 사용할 수 있는 보장된 재개 자료로 삼지 않는다.
- 기존 STATE의 SCC 시작 전 안내와 현재 코드가 다르다. 후속 계획에서 이미 구현된 범위와 남은 DAG DP를 분리해 반영해야 한다.

## 학습 자료에서 채택할 점

아래의 적용 방향은 조사에 근거한 설계 제안이다. 전문가 개인의 권장안을 모든 학습자에게 보장되는 최적 방법으로 해석하지 않는다.

### [rng_58: 노랑을 목표로 한 연습](https://info.atcoder.jp/entry/2025/12/03/170000)

확인한 내용: 전형 문제의 이해, 정당성 확인, 직접 구현과 시간이 지난 뒤 재풀이를 강조한다. 새 개념을 처음 만날 때 해설을 빠르게 활용하는 것도 허용하는 개인 권장안이다.

이 요청에 대한 적용 제안: 새 기법에는 필요한 설명을 제공하고, 사용자가 원하는 독립 시도 시간을 확보한다. 해설을 즉시 보도록 강제하지 않는다.

### [rng_58: 상위권을 위한 연습](https://info.atcoder.jp/entry/2025/12/05/170000)

확인한 내용: 기본 지식을 활용하는 사고력과 실제 대회 경험을 강조하고, 어려워서 손대기 힘든 문제는 보류할 수 있다고 안내한다.

이 요청에 대한 적용 제안: 고급 알고리즘 목록의 완주만으로 Codeforces 빨강이 된다고 가정하지 않는다. 증명, 혼합 문제의 접근 선택, 대회 및 업솔빙을 이어간다.

### [USACO Guide 사용법](https://usaco.guide/general/using-this-guide)

확인한 내용: 고정된 실라버스가 아니며 모듈 내부의 난도는 모듈 간 절대 비교 척도가 아니다. Python 지원이 제한적이다.

이 요청에 대한 적용 제안: 주제와 선수 관계를 찾는 지도로 사용하고, 저장소의 Python 구현과 문제 제약을 별도로 확인한다.

### [USACO Guide 연습 방법](https://usaco.guide/general/practicing)

확인한 내용: 적절한 난도, 시도 후 학습, 구현의 정확성과 속도를 다룬다. 해설을 볼 시점에는 여러 작성자의 서로 다른 견해가 있다.

이 요청에 대한 적용 제안: 난도 조정과 힌트 공개는 사용자의 시도 및 막힌 지점에 맞춘다. 단일한 의무 타이머를 근거 있는 최적해처럼 쓰지 않는다.

### [Educational DP Contest](https://atcoder.jp/contests/dp/tasks)

확인한 내용: A–Z 26개의 DP 과제가 있다.

이 요청에 대한 적용 제안: DP 상태와 전이 패턴에 맞게 선별한다. 문제 문자만으로 엄밀한 난도 순서를 가정하지 않는다.

### [Typical 90](https://atcoder.jp/contests/typical90)

확인한 내용: 제작자 안내에 90개 문제와 별 1–7 난도 체계가 제시되어 있다.

이 요청에 대한 적용 제안: 주제와 현재 단계에 맞는 전형 연습으로 사용한다. 번호순 완주나 다른 플랫폼 등급 환산을 필수로 삼지 않는다.

### [CSES Problem Set](https://cses.fi/problemset/)

확인한 내용: 탐색, DP, 그래프, 구간질의, 트리, 수학, 문자열, 기하 등의 문제를 제공한다.

이 요청에 대한 적용 제안: 특정 알고리즘을 직접 구현하고 검증할 대표 과제를 선별한다.

### [cp-algorithms](https://cp-algorithms.com/)

확인한 내용: 자료구조, 그래프, 문자열, 수학 등 세부 알고리즘 참고 자료를 제공한다.

이 요청에 대한 적용 제안: 선수 관계를 갖춘 뒤 심화 기법을 확인하는 참고 자료로 사용한다.

### [AtCoder 대회 종류](https://info.atcoder.jp/overview/contest/algorithm)

확인한 내용: ABC의 rated 범위는 0–1999이며 ARC 계열은 각기 다른 rated 범위를 가진다.

이 요청에 대한 적용 제안: ABC 올솔 목표와 노랑 도달 후 rating 점검을 분리한다.

### [2026 ARC 개편](https://atcoder.jp/posts/2026ARC_en)

확인한 내용: ARC, ARC--, ARC++ 형식과 rated 범위, 대회 시간이 제시되어 있다.

이 요청에 대한 적용 제안: 참가 시 해당 회차의 최신 조건을 확인하고 5–7시간 예산에 맞춰 대회를 배치한다.

## 목표 해석의 근거

[AtCoder rating 안내](https://info.atcoder.jp/overview/contest/rating)의 파랑은 1600–1999, 노랑은 2000–2399다. [Codeforces 공식 색·칭호 안내](https://codeforces.com/blog/entry/20638)에서 빨강 Grandmaster는 2400부터다. 두 플랫폼의 수치를 서로 환산하지 않는다.

ABC 올솔은 해당 회차의 모든 문제를 정해진 대회 시간 안에 AC한 사실로 확인한다. 대회 후 업솔빙 전체 AC와 이미 본 세트의 재풀이 올솔은 별도로 기록한다. 노랑 도달과 특정 ABC의 올솔은 서로를 보장하지 않는다.
