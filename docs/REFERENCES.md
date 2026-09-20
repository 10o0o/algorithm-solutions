# 참고 자료

자료는 학습 방향과 도구를 보조하는 용도로 사용한다. 실제 학습 기록에는 확인한 자료의 URL만 남기고, 자료를 읽었다는 사실만으로 숙달을 판정하지 않는다.

## 학습 안내와 연습

- [USACO Guide: Using This Guide](https://usaco.guide/general/using-this-guide) — 전체 경로를 고르는 안내. Python 지원 범위는 주제별로 확인한다.
- [USACO Guide: Practicing](https://usaco.guide/general/practicing) — 문제를 고르고 복습하는 방법.
- [cp-algorithms](https://cp-algorithms.com/) — 알고리즘과 자료구조 참고서.
- [Competitive Programmer's Handbook](https://cses.fi/book/index.php) — 알고리즘 책.
- [CSES Problem Set](https://cses.fi/problemset/) — 구현과 검증에 사용할 문제 모음.
- [Codeforces EDU](https://codeforces.com/edu/courses?locale=en) — 주제별 강의와 연습.
- [AtCoder DP contest](https://atcoder.jp/contests/dp/tasks) — DP 기초 연습.
- [AtCoder Typical 90](https://atcoder.jp/contests/typical90/tasks?lang=ja) — 다양한 전형 연습.

USACO Guide는 학습 경로와 연습 문제를 고르는 데 사용한다. Python 지원은 주제별로 제한될 수 있고 자료에는 C++ 예시가 많으므로, Python 구현은 별도로 제약과 실행 결과를 확인한다.

자료를 그대로 진도로 이식하지 않는다. USACO의 경로 구조만 참고하고, Handbook·cp-algorithms의 C++ 예시는 Python으로 별도 검증한다. CSES는 필요한 문제를 선별하고, Codeforces EDU는 태그를 가린 혼합 연습과 연결한다. Typical 90은 별도 등급으로 환산하지 않는다. PyRival은 구현을 이해하고 동작을 확인한 뒤 필요한 템플릿만 추가한다.

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
