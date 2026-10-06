# 참고 자료

자료는 학습 방향과 도구를 보조하는 용도로 사용한다. 실제 학습 기록에는 확인한 자료의 URL만 남기고, 자료를 읽었다는 사실만으로 숙달을 판정하지 않는다.

아래 커리큘럼 자료의 구성과 역할은 2026-10-06에 확인했다. 외부 자료의 개편과 실제 문제의 실행 제약은 해당 수업에서 다시 확인한다.

## 주제 지도와 연습 자료

주제 순서와 주간 운영의 기준은 [로드맵](../ROADMAP.md)이다. 아래 자료는 선택한 기술을 공부하고
직접 구현할 문제를 찾는 데 사용하며, 어떤 사이트의 전체 순서를 그대로 진도로 삼지 않는다.

### USACO Guide: 선택형 주제 지도

- [Using This Guide](https://usaco.guide/general/using-this-guide)에서 각 경로와 문제 페이지를 찾는다.
- [Graph Traversal](https://usaco.guide/silver/graph-traversal)은 DFS·BFS를 시작할 때 참고한다.
- [Gold](https://usaco.guide/gold)와 [Platinum](https://usaco.guide/plat)은 필요한 주제의 설명과 예제를 찾아보는 상위 주제 지도다.
- [Strongly Connected Components](https://usaco.guide/adv/SCC)와 [FFT](https://usaco.guide/adv/fft)는 해당 고급 주제를 다룰 때 선택해 참고한다.
- [Guide settings](https://usaco.guide/settings)는 Python 지원이 제한적임을 안내한다. 코드 예시와 지원 언어는 페이지마다 살펴본다.

USACO Guide는 전체 코스를 순서대로 끝내는 교재가 아니라 필요한 주제를 찾는 지도다. 페이지에 C++ 예시만 있더라도 저장소의 주력 언어는 Python이다. 실제 입력 크기와 시간 제한으로 Python 구현을 판단하며, C++로 일괄 전환하지 않는다.

### Competitive Programmer's Handbook와 CSES

- [Competitive Programmer's Handbook](https://cses.fi/book/book.pdf)은 아이디어와 기초 개념을 확인하는 참고서다. FFT 범위는 여기서 다루지 않으므로 필요하면 cp-algorithms를 본다.
- [CSES Problem Set](https://cses.fi/problemset/)은 현재 학습 주제와 맞는 문제를 골라 설계·구현·테스트하는 연습장이다.

책의 장이나 문제집 번호를 학습 진도로 그대로 옮기지 않는다. 자료를 읽은 것만으로 문제 해결이나 숙달을 판정하지 않는다.

### AtCoder 문제 묶음

- [Educational DP Contest](https://atcoder.jp/contests/dp)은 A–Z 26문제로 구성된 DP 연습 모음이다. 문제 문자가 난이도 순서를 뜻한다고 가정하지 않고, 상태와 점화식 패턴에 맞춰 고른다.
- [Typical 90](https://atcoder.jp/contests/typical90)은 여러 전형을 연습하는 모음이다. 이미 익숙한 주제에서 ★4–5 문제부터 살펴보고, 대표 문제 진단 결과에 따라 범위를 조정한다. 별 개수를 다른 사이트 등급으로 환산하지 않는다.
- [AtCoder Library Practice Contest](https://atcoder.jp/contests/practice2/tasks)는 자료구조의 기술 구현과 경계 조건을 확인할 때 필요한 문제를 골라 쓴다.

### 세부 알고리즘 참고

- [cp-algorithms: Strongly Connected Components](https://cp-algorithms.com/graph/strongly-connected-components.html)는 SCC 분해와 축약 그래프의 세부 참고 자료다.
- [cp-algorithms: FFT and polynomial multiplication](https://cp-algorithms.com/algebra/fft.html)는 FFT·다항식 곱셈과 NTT 관련 구현 세부를 확인할 때 쓴다.

### 추가 연습 자료

- [Codeforces EDU](https://codeforces.com/edu/courses?locale=en) — 필요할 때 주제별 강의와 연습을 찾는다. 혼합 진단으로 사용할 문제는 풀이 전에 주제와 태그를 가린다.
- [USACO Guide: Practicing](https://usaco.guide/general/practicing) — 선택한 문제를 연습하고 복습하는 방법을 참고한다.
- [cp-algorithms](https://cp-algorithms.com/) — 다른 알고리즘·자료구조 주제의 세부 참고 문서를 찾는다.

기본 구현 언어는 Python이다. C++로 된 설명은 필요한 개념만 읽고 Python으로 옮겨 실제 제약과 실행 결과를 확인한다. 성능 문제를 이유로 언어를 바꾸는 결정은 반복해서 확인된 병목에 한정한다.

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
