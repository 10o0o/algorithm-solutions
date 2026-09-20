---
title: "누적 집계 (Prefix Aggregates)"
updated: "2026-09-20"
tags:
  - "prefix-sum"
  - "prefix-aggregate"
  - "range-query"
---

# 누적 집계 (Prefix Aggregates)

## 핵심 요약

누적 집계는 앞에서부터 본 원소들의 결과를 저장해, 한 번 만든 상태로 구간 질의를 빠르게 계산하는 방법이다. 합처럼 구간을 앞부분의 두 상태로 되돌릴 수 있으면 전처리 $O(n)$ 뒤 각 구간을 $O(1)$에 처리할 수 있다.

## 개념 정리

배열 `a`에 대해 반열린 구간 `[0, i)`의 집계를 `prefix[i]`에 둔다. 합이라면 `prefix[0] = 0`이고

```text
prefix[i + 1] = prefix[i] + a[i]
```

이다. 그러면 `[left, right)`의 합은 `prefix[right] - prefix[left]`가 된다. 곱, XOR, 빈도 배열, 가중치 합처럼 한 원소를 기존 상태에 반영할 수 있는 값도 같은 방식으로 누적할 수 있다.

$$
P_{i+1} = P_i + a_i, \qquad
\sum_{j=l}^{r-1} a_j = P_r - P_l
$$

여기서 $P_i$는 `prefix[i]`다. 반대 방향으로 미리 집계한 `suffix[i]`를 $S_i$라 두면
빈 접미 구간의 합 $S_n=0$에서 시작한다.

$$
S_i = a_i + S_{i+1}
$$

같은 배열의 합을 양쪽에서 구했다면 `prefix[split] + suffix[split]`은 항상 전체 합이다.
1422처럼 왼쪽의 `0` 개수와 오른쪽의 `1` 개수를 각각 집계하면, 두 값을 합쳐
분할 위치마다 다른 점수를 계산할 수 있다.

문제에서 다음 표현이 보이면 후보로 삼는다.

- 같은 배열에서 연속 구간의 합·개수·점수를 여러 번 묻는다.
- 왼쪽부터 스캔하며 지금까지의 상태와 남은 오른쪽 상태를 비교한다.
- 특정 위치를 기준으로 왼쪽과 오른쪽의 집계를 합쳐 점수를 계산한다.

다만 모든 집계가 `prefix[right]`와 `prefix[left]`만으로 구간 값을 복원할 수 있는 것은 아니다. 합과 XOR는 역연산이 있지만, 일반적인 최솟값·최댓값에는 뺄셈에 해당하는 역연산이 없다. 그런 경우에는 다른 자료구조나 문제에 맞는 prefix/suffix 보조 배열이 필요하다.

## 적용 조건

다음 조건을 먼저 확인한다.

1. 대상 구간이 연속 구간이고, 구간의 끝점으로 답을 표현할 수 있는가?
2. 원소를 한 개 추가했을 때 집계를 $O(1)$에 갱신할 수 있는가?
3. 구간 질의라면 앞부분 두 집계에서 원하는 구간을 복원할 역연산이 있는가?
4. 배열이 질의 중 바뀌지 않는가? 값이 바뀌면 정적 prefix 배열은 낡으므로 Fenwick tree나 segment tree 같은 구조가 필요할 수 있다.

prefix 합은 원소가 음수여도 정확하다. `합이 K 이하인 가장 긴 구간`처럼 prefix 합의 단조성을 이용하는 별도 기법에서는 음수 허용 여부를 따로 확인해야 한다.

## 불변식과 정확성

인덱스 `i`의 원소를 처리하기 직전에 다음 불변식이 유지된다.

> `prefix[i]`는 정확히 `a[0]`부터 `a[i - 1]`까지의 집계이고, 현재 원소 `a[i]`는 아직 포함하지 않는다.

처음에는 빈 구간의 항등원 `prefix[0]`만 있으므로 성립한다. `a[i]`를 처리하면 누적 연산의 정의에 따라 `prefix[i + 1]`가 `[0, i + 1)`의 집계가 된다. 합의 경우 전체 `[0, right)`는 `[0, left)`와 `[left, right)`의 합으로 분해되므로 `prefix[right] - prefix[left]`가 `[left, right)`를 정확히 돌려준다. 이 반열린 구간 규칙을 끝까지 유지하면 `left == right`인 빈 구간도 자연스럽게 0이 된다.

## 작은 예

다음 예는 실행할 수 있는 완전한 Python 3.10 코드다. `prefix`의 길이를 원본보다 하나 크게 잡아 인덱스 경계를 단순하게 한다.

```python
def build_prefix(values: list[int]) -> list[int]:
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    return prefix[right] - prefix[left]


if __name__ == "__main__":
    values = [4, -1, 3, 2]
    prefix = build_prefix(values)
    assert prefix == [0, 4, 3, 6, 8]
    assert range_sum(prefix, 1, 3) == 2  # values[1:3] == [-1, 3]
    assert range_sum(prefix, 0, 0) == 0
```

문자열 문제에서는 집계를 두 개 유지할 수도 있다. [1422. Maximum Score After Splitting a String](../../leetcode/easy/1422.maximum-score-after-splitting-a-string.md)의 저장된 구현은 `s.count("1")`로 오른쪽 `1` 개수를 한 번 세고, 왼쪽 `0` 개수와 오른쪽 `1` 개수를 매 위치에서 갱신한다. 이 방식은 prefix 배열 전체를 만드는 대신 현재 split에 필요한 두 집계만 보존하는 rolling aggregate다.

## 복잡도

길이 `n` 배열의 prefix 배열을 만드는 데 시간 $O(n)$, 공간 $O(n)$이 든다. 이후 구간 합 질의는 하나당 $O(1)$이다. rolling 집계 상태 자체와 인덱스 기반 순회 변형은 추가 공간 $O(1)$로 줄일 수 있다. 다만 [1422 풀이 코드](../../leetcode/easy/1422.maximum-score-after-splitting-a-string.py)는 s[:-1] 문자열 슬라이스를 만들므로 현재 저장된 구현의 추가 공간이 $O(n)$이다. 누적 배열 자체를 반환하는 예제는 질의용 상태를 보존하므로 $O(n)$ 공간을 사용한다.

## 경계와 함정

- `[left, right)`인지 `[left, right]`인지 먼저 정하고, 둘을 섞어 마지막 원소를 빠뜨리거나 두 번 세지 않는다.
- `prefix[0]`은 빈 prefix의 항등원이다. 처음부터 `values[0]`을 넣는 방식은 질의 식의 인덱스를 함께 바꿔야 한다.
- 1422의 코드는 전체 prefix-sum 배열을 만들지 않는다. `left_zeros`와 `right_ones` 두 rolling count를 유지하는 풀이이므로 이를 일반적인 prefix array 구현이라고 설명하면 안 된다.
- 배열이 온라인으로 수정되면 한 번 계산한 prefix 값은 자동으로 갱신되지 않는다.
- 합은 음수에서도 동작하지만, 누적값이 증가한다고 가정하는 투 포인터·이분 탐색 조건과는 별개의 문제다.
- Python의 정수는 overflow가 없지만, 다른 언어에서는 합의 최대 크기에 맞는 자료형을 선택한다.

## 관련 노트와 코드

- [투 포인터 (Two Pointers)](two-pointers.md) — 누적 상태를 창의 양끝과 함께 갱신하는 경우의 선택 기준.
- [1422 문제 노트](../../leetcode/easy/1422.maximum-score-after-splitting-a-string.md) · [풀이 코드](../../leetcode/easy/1422.maximum-score-after-splitting-a-string.py)

## 출처

- [LeetCode 1422 공식 문제](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) — 두 rolling count로 split 점수를 계산하는 실제 적용.
- [Python 공식 문서: 자료형(sequence)의 인덱싱](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) — 반열린 슬라이스와 인덱스 관례를 확인할 때 참고.
