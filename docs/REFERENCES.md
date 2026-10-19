# 참고 자료

자료는 학습 방향과 도구를 보조하는 용도로 사용한다. 실제 학습 기록에는 확인한 자료의 URL만 남기고, 자료를 읽었다는 사실만으로 숙달을 판정하지 않는다.

기존 자료·도구의 2026-10-06 확인 기록을 유지한다. 학습 자료의 구성·한계와 계정 출발점은 2026-10-19의 [개편 조사](../specs/001-redesign-learning-system/research-evidence.md)에 근거해 보완했다. 이번 구현 단계에서 외부 페이지를 새로 조회한 것은 아니다. 외부 자료의 개편과 실제 문제의 실행 제약은 해당 수업에서 다시 확인한다.

## 주제 지도와 연습 자료

주제 순서와 주간 운영의 기준은 [로드맵](../ROADMAP.md)이다. 아래 자료는 선택한 기술을 공부하고
직접 구현할 문제를 찾는 데 사용하며, 어떤 사이트의 전체 순서를 그대로 진도로 삼지 않는다.

### USACO Guide: 선택형 주제 지도

- [Using This Guide](https://usaco.guide/general/using-this-guide)에서 각 경로와 문제 페이지를 찾는다.
- [Graph Traversal](https://usaco.guide/silver/graph-traversal)은 DFS·BFS를 시작할 때 참고한다.
- [Gold](https://usaco.guide/gold)와 [Platinum](https://usaco.guide/plat)은 필요한 주제의 설명과 예제를 찾아보는 상위 주제 지도다.
- [Strongly Connected Components](https://usaco.guide/adv/SCC)와 [FFT](https://usaco.guide/adv/fft)는 해당 고급 주제를 다룰 때 선택해 참고한다.
- [Guide settings](https://usaco.guide/settings)는 Python 지원이 제한적임을 안내한다. 코드 예시와 지원 언어는 페이지마다 살펴본다.

USACO Guide는 고정된 완주 실라버스가 아니라 필요한 주제를 찾는 지도다. 한 모듈 안의 난도는 다른 모듈과의 절대 비교 척도가 아니다. 페이지에 C++ 예시만 있더라도 저장소의 주력 언어는 Python이다. 제한된 Python 지원과 실제 입력 크기·시간 제한을 따로 확인하며, C++로 일괄 전환하지 않는다.

### Competitive Programmer's Handbook와 CSES

- [Competitive Programmer's Handbook](https://cses.fi/book/book.pdf)은 아이디어와 기초 개념을 확인하는 참고서다. FFT 범위는 여기서 다루지 않으므로 필요하면 cp-algorithms를 본다.
- [CSES Problem Set](https://cses.fi/problemset/)은 탐색·DP·그래프·구간질의·트리·수학·문자열·기하 등의 대표 구현 과제를 골라 설계·구현·테스트하는 연습장이다.

책의 장이나 문제집 번호를 학습 진도로 그대로 옮기지 않는다. 자료를 읽은 것만으로 문제 해결이나 숙달을 판정하지 않는다.

### AtCoder 문제 묶음

- [Educational DP Contest 문제 목록](https://atcoder.jp/contests/dp/tasks)은 A–Z 26개의 DP 패턴 연습장이다. 상태·전이에 맞게 선별하며 문자 순서를 엄밀한 난도 순으로 가정하지 않는다.
- [Typical 90](https://atcoder.jp/contests/typical90)은 E869120이 기획·출제한 90개의 전형 문제 모음이며 제작자 설명의 별 1–7을 컬렉션 안의 선택 단서로 쓴다. 현재 기법의 선수와 실제 시도에 맞춰 고르며, 번호순 완주나 별에서 다른 플랫폼 rating으로의 환산을 요구하지 않는다.
- [AtCoder Library Practice Contest](https://atcoder.jp/contests/practice2/tasks)는 자료구조의 기술 구현과 경계 조건을 확인할 때 필요한 문제를 골라 쓴다.

### 세부 알고리즘 참고

- [cp-algorithms: Strongly Connected Components](https://cp-algorithms.com/graph/strongly-connected-components.html)는 SCC 분해와 축약 그래프의 세부 참고 자료다.
- [cp-algorithms: FFT and polynomial multiplication](https://cp-algorithms.com/algebra/fft.html)는 FFT·다항식 곱셈과 NTT 관련 구현 세부를 확인할 때 쓴다.

### 추가 연습 자료

- [Codeforces EDU](https://codeforces.com/edu/courses?locale=en) — 필요할 때 주제별 강의와 연습을 찾는다. 혼합 진단으로 사용할 문제는 풀이 전에 주제와 태그를 가린다.
- [USACO Guide: Practicing](https://usaco.guide/general/practicing) — 적정 난도의 독립 시도·시도 후 학습·직접 구현을 참고한다. 해설을 볼 시점에는 여러 작성자의 견해가 있으므로 하나의 의무 타이머로 일반화하지 않는다. 실제 막힘과 요청에 따라 도움을 조절한다.
- [cp-algorithms](https://cp-algorithms.com/) — 다른 알고리즘·자료구조 주제의 세부 참고 문서를 찾는다.

기본 구현 언어는 Python이다. C++로 된 설명은 필요한 개념만 읽고 Python으로 옮겨 실제 제약과 실행 결과를 확인한다. 성능 문제를 이유로 언어를 바꾸는 결정은 반복해서 확인된 병목에 한정한다.

## 계정 출발점과 목표의 근거

2026-10-19 KST에 조사한 `10o0o`의 **1065 (Provisional), rated 9회, 최신 ABC480, performance 1532**를 현재 출발점으로 삼는다. [공식 프로필](https://atcoder.jp/users/10o0o?lang=en)과 [공식 history JSON](https://atcoder.jp/users/10o0o/history/json)에 근거한 스냅샷이며, 상세 수치·최근 5회 performance 1197/1228/1272/1505/1532·평균 1346.8·중앙값 1272와 제출 ID는 [조사 근거](../specs/001-redesign-learning-system/research-evidence.md#최신-atcoder-기록)에서 관리한다. 현재 재개 요약은 [STATE](../STATE.md), 목표와 측정 정의는 [ROADMAP](../ROADMAP.md#목표와-측정)을 따른다.

- [ABC480 공식 안내](https://atcoder.jp/contests/abc480)·[문제 목록](https://atcoder.jp/contests/abc480/tasks): 2026-10-17 21:00–22:40 KST, 100분·A–G 7문제의 근거다. 다른 회차의 시간·문제 수를 대신하지 않는다.
- [AtCoder Problems 공개 API](https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=10o0o&from_second=1792238400)·[게시자 API 문서](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md): 대회 시간 구간에서 A–E AC 다섯 건을 확인한 **비공식 출처**다. 공식 제출 목록·standings의 직접 요청은 HTTP 429로 미확인이다. 누적 AC 시각은 각 문제의 순수 사고·구현 시간이 아니며, 도움·F/G 열람/시도·Codeforces 현재 기준선은 미확인이다.
- [AtCoder rating 안내](https://info.atcoder.jp/overview/contest/rating)·[Codeforces 공식 등급 공지](https://codeforces.com/blog/entry/20638): 각각의 색상 경계에 대한 출처다. 서로 환산하거나 단일 performance를 숙달로 해석하지 않는다.
- [AtCoder 대회 안내](https://info.atcoder.jp/overview/contest/algorithm)·[2026 ARC 안내](https://atcoder.jp/posts/2026ARC_en): 2026-10-19 조사에서는 ABC rated 0–1999와 ARC 형식별 조건을 확인했다. 노랑 목표 부근의 rating 점검은 해당 회차의 최신 조건을 다시 확인한다. ABC 올솔 연습은 rating 대상 여부와 별개다.

## Python과 실행 도구 비교

| 도구 | 역할 | 현재 판단 |
| --- | --- | --- |
| [PyRival](https://github.com/cheran-senthil/PyRival) | Python 자료구조·알고리즘 참고 구현 | 필요한 주제만 참고 |
| [Competitive Companion](https://github.com/jmerle/competitive-companion) | 문제와 예제를 VS Code로 가져오기 | 기본 도구. 실제 브라우저 버튼 연동은 [환경 검증 기록](VALIDATION.md)의 잔여 확인 참고 |
| [cph](https://github.com/agrawal-d/cph) | VS Code에서 예제 실행 | 기본 도구. 실제 브라우저 버튼 연동은 [환경 검증 기록](VALIDATION.md)의 잔여 확인 참고 |
| [online-judge-tools](https://github.com/online-judge-tools/oj) | 샘플 다운로드·테스트·제출 | 참고 도구. AtCoder의 Cloudflare CAPTCHA가 Selenium 로그인을 막을 수 있다는 [issue #934](https://github.com/online-judge-tools/oj/issues/934)가 있어 `oj login`을 현재 기본 흐름의 전제로 삼지 않음 |
| [acc](https://github.com/Tatamo/atcoder-cli) | AtCoder 대회·문제 생성과 제출 보조 | 보류. 현재 VS Code 흐름을 확인한 뒤 필요성을 다시 판단 |
| [pyforces](https://github.com/LZDQ/pyforces) | Codeforces 문제 파싱·테스트·제출 CLI | 보류. 로그인·bot detection 운영 부담을 먼저 확인 |
| [cf-tool](https://github.com/xalanq/cf-tool) | Codeforces CLI | 2024-12-14 archived라 기본 도구로 채택하지 않음 |

도구를 고르는 기준은 문제 생성, 예제 실행, 제출이 실제 Python·VS Code 흐름에서 안정적으로 이어지는지다. 보류 도구를 설치하거나 인증 정보를 저장소에 추가하지 않는다.

## AI 사용 참고

- [AtCoder LLM rules](https://info.atcoder.jp/entry/llm-rules-en) — AtCoder에서 LLM을 사용할 때 확인할 공식 안내.
- [Codeforces AI 관련 안내](https://codeforces.com/topic/134567/en4) — Codeforces의 최신 사용 범위와 논의를 확인할 링크.

대회 중 AI 사용 여부와 허용 범위는 해당 플랫폼의 최신 규칙을 먼저 확인한다. 이 저장소의 학습 루프에서는 문제를 먼저 직접 시도하고, 이후 규칙에 맞게 해설이나 AI를 사용한다.

## 관련 학습 기록

- [LLM Research Learning Lab](https://10o0o.github.io/llm-research-learning-lab/) — 학습 설계와 자기 설명을 참고할 공개 자료.

도구를 추가하거나 바꿀 때는 먼저 현재 VS Code 환경에서 문제 생성·예제 실행·제출 흐름을 확인하고, 비밀키나 인증 정보를 저장소에 기록하지 않는다.
