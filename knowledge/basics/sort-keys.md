---
title: "Python 정렬 키와 lambda"
updated: "2026-10-01"
tags:
  - "python"
  - "sorting"
  - "implementation"
---

# Python 정렬 키와 lambda

## 핵심 요약

`sorted(items, key=...)`는 각 원소에서 비교 키를 구해 정렬한 새 리스트를 반환한다. 여러 조건은 우선순위대로 튜플에 넣고, 숫자 기준의 내림차순은 해당 값의 부호를 바꿔 표현할 수 있다.

## 개념 정리

`(이름, 점수)`를 점수 내림차순, 같은 점수에서는 이름 오름차순으로 정렬할 때의 키는 `(-점수, 이름)`이다. 튜플은 첫 값을 먼저 비교하고, 같으면 다음 값을 비교한다.

```python
sorted(items, key=lambda x: (-x[1], x[0]))
```

`lambda x: 표현식`은 표현식 하나의 값을 반환하는 함수다. 이번 정렬 키에서는 일반 함수처럼 아래에 대입문과 `return`을 쓰지 않고, 반환할 튜플을 콜론 뒤에 둔다. `sorted`에 이 함수를 전달할 때는 `key=`를 쓴다.

문자열 길이 오름차순, 같은 길이에서는 사전순 정렬은 `(len(x), x)`이고, 길이 내림차순, 같은 길이에서는 사전순 정렬은 `(-len(x), x)`이다. `len(x) or x`는 두 기준을 묶는 표현이 아니다. `or`는 왼쪽 값이 참으로 평가되면 그 값을, 아니면 오른쪽 값을 반환한다.

안정 정렬은 **전체 키가 같은** 원소들의 기존 순서를 유지한다. 길이만 키로 쓰면 같은 길이의 단어는 원래 순서를 유지하고, `(len(x), x)`를 쓰면 길이가 같아도 단어 값이 두 번째 기준으로 비교된다.

## 작은 예

아래 입력은 확인한 정렬 키의 동작을 검사하기 위한 작은 예다. 사용자의 실제 실행 출력 기록은 아니다.

```python
items = [("B", 80), ("A", 80), ("C", 90)]
ranked = sorted(items, key=lambda x: (-x[1], x[0]))
assert ranked == [("C", 90), ("A", 80), ("B", 80)]
assert items == [("B", 80), ("A", 80), ("C", 90)]

words = ["bb", "aa", "c", ""]
assert sorted(words, key=lambda x: (len(x), x)) == ["", "c", "aa", "bb"]
assert sorted(words, key=lambda x: (-len(x), x)) == ["aa", "bb", "c", ""]

same_length = ["bb", "aa"]
assert sorted(same_length, key=len) == ["bb", "aa"]
assert sorted(same_length, key=lambda x: (len(x), x)) == ["aa", "bb"]
```

## 2026-10-01 KST 학습 기록

오늘은 Python 기초 전체를 다시 배우기보다 구현 훈련에서 필요한 문법을 점검했다. 빈 파일에서 구현할 때의 코드 명료성과 `lambda`·정렬 키 사용에 어려움이 있다고 확인했다. 세션의 목표와 세그먼트 트리 재개 위치는 [반복형 세그먼트 트리 기록](../data-structures/segment-tree.md)에 함께 남겼다.

| 항목 | 확인한 시도와 피드백 |
| --- | --- |
| 점수·이름 키 | `(-점수, 이름)`을 정확히 설명했다. |
| lambda 문법 | 처음에는 `lambda(x):` 아래에 대입문과 `return`을 써 일반 함수 문법과 혼동했다. `lambda x: (-x[1], x[0])`로 교정받았다. |
| 함수 전달 | `sorted` 호출에서 `key=` 누락을 교정받았다. |
| 반환값 | `sorted`가 새 리스트를 반환한다고 정확히 답했다. |
| 길이·사전순 키 | `len(x) or x`를 사용해 `or`와 튜플 키를 혼동했다. `(len(x), x)`와 동일 키의 안정 정렬에 대한 설명을 받았다. |
| 조건 변경 | 이후 `sorted(words, key=lambda x: (-len(x), x))`를 정확히 작성했다. |

마지막 항목은 도움을 받은 뒤 조건 하나를 바꾼 단일 응용에 성공한 기록이다. 독립적인 장기 숙달이나 이후 재구현은 아직 확인하지 않았다.

## 출처와 연결

- 학습 경험: 2026-10-01 KST 알고리즘 학습 대화에서 확인한 사용자 코드와 설명.
- [Python 공식 문서: 정렬](https://docs.python.org/3/howto/sorting.html) — 키 함수, 튜플 비교, 새 리스트 반환과 안정 정렬.
- [Python 공식 문서: lambda 표현식](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) — 표현식 하나를 반환하는 함수 문법.
- [Python 공식 문서: Boolean 연산](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) — `or`가 반환하는 값.
