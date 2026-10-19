# 현재 학습 위치

기준일: 2026-10-19 KST

- 목표: AtCoder 파랑 1600 → 노랑 2000, 별도 ABC 실전 올솔, 장기 Codeforces 빨강 2400+. 정의와 범위는 [로드맵](ROADMAP.md#목표와-측정)을 따른다.
- 운영: 설명·독립 작업·대회·복기·기록을 합쳐 주 5–7시간이다. [첫 4주 시범](ROADMAP.md#첫-4주-시범과-이후-조정)은 다음 실제 학습일부터 시작하며 아직 수행 결과가 없다.

## 출발점과 확인 범위

2026-10-19에 확인한 [공식 프로필](https://atcoder.jp/users/10o0o?lang=en)·[history JSON](https://atcoder.jp/users/10o0o/history/json)의 rating은 **1065 (Provisional), rated 9회**다. 최신 참가는 2026-10-17 ABC480, performance 1532다. 단일 performance를 개별 주제 숙달로 해석하지 않는다.

대회 시간 내 A–E AC 다섯 건은 비공식 AtCoder Problems 자료다. 공식 제출 목록·standings는 HTTP 429로 직접 확인하지 못했고 도움·F/G 열람/시도·Codeforces 현재 기준선은 미확인이다. 상세 수치·출처·누적 제출 시각의 한계는 [조사 근거](specs/001-redesign-learning-system/research-evidence.md#최신-atcoder-기록)와 [참고 자료](docs/REFERENCES.md#계정-출발점과-목표의-근거)에 있다.

## 현재 구현과 보류 질문

- [공유 SCC 코드](cses/Planets_and_Kingdoms.py)에 반복형 Kosaraju 구현이 있다. 현재 로컬 scratch에는 SCC와 축약 그래프 구현이 있으며 동전 최대값을 구하는 `max_coins`는 `NotImplementedError`다. 코드 존재를 AC·독립 해결로 바꾸지 않는다. 이번 개편에서는 코드를 실행·수정하거나 남은 구현을 대신하지 않았다.
- scratch는 Git에서 제외되어 다른 기기에 없을 수 있다. 없으면 공유 SCC 코드와 [Coin Collector 원문](https://cses.fi/problemset/task/1686/)에서 남은 설계·구현을 이어간다. 입출력 준비는 요청받은 범위만 수행하며 SCC 입문을 재개 관문으로 반복하지 않는다.
- 세그먼트 트리의 `tn`을 2의 거듭제곱으로 맞추는 이유에 대한 손 추적은 답변 전에 중단했다. 이해 완료로 표시하지 않으며 [자료구조 재방문 범위](knowledge/data-structures/segment-tree.md#자료구조-묶음에서-이어갈-범위)와 [확인 기준](ROADMAP.md#현재-세그먼트-트리-단계의-확인-기준)에서 전체 구현·변형과 함께 다룬다.

2026-10-06의 계정 스냅샷·구간 합/최솟값/순위 탐색 관찰은 [당시 STATE 원문](https://github.com/10o0o/algorithm-solutions/blob/7c5bf71e96e2fefd3451178470662554d209232e/STATE.md)과 [세그먼트 트리 노트](knowledge/data-structures/segment-tree.md)에 보존한다. 당시 결과·도움·미확인을 현재 숙달로 승격하지 않는다.

## 다음 독립 행동

**과제 하나**: 현재 SCC·축약 그래프에서 성분별 동전 값을 모으고 DAG 위의 최대 수집량을 모델링해 `max_coins`를 직접 설계·구현·실행한다.

**이유**: SCC와 축약은 이미 작성되어 있고, 남은 공백은 값 집계와 DAG DP의 연결이다. 필요한 원리 설명이 있으면 그 부분만 보완한다.

**완료 기준**: 상태·계산 순서·복잡도를 설명하고 직접 구현한 결과를 샘플과 필요한 경계에서 확인한다. 고립 성분·여러 SCC·중복 간선 등 실제 사용한 입력과 결과, 도움 범위를 구분한다. 온라인 판정·다른 날 재현은 실제 근거가 생길 때 별도로 확인한다.

이 문서는 이번에 승인한 학습 체계 개편 범위에서 갱신했다. 새로운 DAG DP 완료·AC·학습 경험을 기록한 것은 아니다.
