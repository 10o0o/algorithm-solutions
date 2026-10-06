# 개념 노트

명시적으로 요청한 전형·기초 주제는 참고 정리로 먼저 작성할 수 있다. 정리 요청에 진단 문제나 독립 설명 시험을 선행 조건으로 붙이지 않는다. 이후 같은 노트에 실제 학습에서 확인한 시도, 구현, 실행, 자기 설명을 덧붙인다. 참고 정리를 작성하거나 읽었다는 사실, 풀이 파일의 존재만으로 독립 해결·숙달을 기록하지 않으며 학습 경험과 판정은 확인한 범위만 적는다. 주제별 설명과 진단을 선택하는 학습 운영은 [로드맵](../ROADMAP.md)을 따른다.

## 초기 읽기 목록

이미 아는 기초를 다시 수강할 필요 없이, 문제를 풀다가 조건·경계·구현을 확인하고 싶을 때 찾아 읽는다.

1. [누적 집계 (Prefix Aggregates)](basics/prefix-aggregates.md)
2. [투 포인터 (Two Pointers)](basics/two-pointers.md)
3. [이분 탐색 (Binary Search)](search/binary-search.md)
4. [너비 우선 탐색 (BFS)](graphs/bfs.md)
5. [깊이 우선 탐색 (DFS)](graphs/dfs.md)

연결해서 읽을 현재 문제 노트는 [1422. Maximum Score After Splitting a String](../leetcode/easy/1422.maximum-score-after-splitting-a-string.md), [2226. Maximum Candies Allocated to K Children](../leetcode/medium/2226.maximum-candies-allocated-to-k-children.md), [1302. Deepest Leaves Sum](../leetcode/medium/1302.deepest-leaves-sum.md)이다.

## 최소 형식

모든 개념 노트의 YAML 메타데이터에는 다음 세 필드만 기본으로 둔다.

```yaml
---
title: "개념 제목"
updated: "YYYY-MM-DD"
tags:
  - "tag"
---
```

본문의 첫 H1은 메타데이터 `title`과 같은 문자열이어야 하며, `## 핵심 요약`과 `## 개념 정리` heading도 반드시 있어야 한다. 참고 정리에는 정의, 알아보는 기준, 적용 조건, 불변식과 정확성, 실행 가능한 작은 Python 예, 복잡도, 경계와 함정, 관련 노트·코드, 출처를 가능한 한 함께 적는다. 문제나 대회와 연결할 때는 실제로 존재하는 상대 링크와 원문 URL을 사용한다.

`knowledge/template.md`는 복사해 쓰는 참고 템플릿이며 자동 기록으로 취급하지 않는다. 템플릿의 placeholder를 실제 내용과 날짜로 바꾼 뒤 저장한다.

## 학습 내용을 덧붙이는 순서

1. 이미 아는 주제는 기존 증거를 읽고 필요하면 대표 과제를 시도한다. 새 주제는 목표와 필요한 개념 설명을 확인한다.
2. 문제를 독립적으로 설계하고 직접 구현해 테스트를 실행한다. 필요한 경우에만 해설이나 AI와 함께 조건과 증명을 확인한다.
3. 핵심 불변식과 복잡도를 자기 말로 설명하고, 필요하면 조건을 바꿨을 때 무엇이 달라지는지 점검한다. 매번 퀴즈를 강제하지 않는다.
4. 개념 정리를 요청하면 실제로 확인한 시도·구현·실행·설명과 남은 질문을 기존 노트에 덧붙인다.

판정, 도움 여부, 재풀이 상태는 실제로 확인한 경우에만 본문에 기록한다. 아직 확인하지 않은 값은 `unknown`으로 남겨도 된다.
사용자 작성과 AI 제공·수정, 사용자 실행 보고와 에이전트 실행, 공식 판정 확인과 사용자 보고,
같은 세션 재구현과 다른 날 재현을 구분한다. 근거 코드·테스트·문제 노트는 실제 상대 링크로 연결한다.
