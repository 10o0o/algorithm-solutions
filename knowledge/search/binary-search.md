---
title: "이분 탐색 (Binary Search)"
updated: "2026-09-20"
tags:
  - "binary-search"
  - "monotone-predicate"
  - "parametric-search"
---

# 이분 탐색 (Binary Search)

## 핵심 요약

이분 탐색은 순서가 있는 후보 공간에서 판정 결과가 한 번만 바뀐다는 단조성을 이용해, 가능한 범위를 절반씩 줄이는 방법이다. 정렬된 값을 찾을 때뿐 아니라 “답을 x로 만들 수 있는가?”라는 판정이 단조이면 답 자체에도 적용할 수 있다.

## 개념 정리

먼저 탐색 공간과 판정 함수 can(x)를 정한다. 최대화 문제에서 작은 값은 가능하고 큰 값은 불가능하다면 가능한 답은 [0, answer] 같은 접두 구간을 이룬다. 최소화 문제에서는 반대로 불가능 구간 뒤에 가능한 구간이 올 수 있다.

정확한 값의 위치를 찾는 일반 이분 탐색과, 가능한 답의 최댓값·최솟값을 찾는 답에 대한 이분 탐색을 구분한다. 답에 대한 탐색은 배열을 정렬할 필요가 없지만 다음 두 성질이 반드시 필요하다.

- 후보가 숫자처럼 순서가 있는 유한한 영역에 있다.
- can(x)의 참·거짓이 영역에서 한 방향으로만 변한다.

[2226 풀이 코드](../../leetcode/medium/2226.maximum-candies-allocated-to-k-children.py)는 각 아이에게 x개를 줄 수 있는지를 sum(candy // x) >= k로 판정한다. x가 커질수록 각 candy // x는 커지지 않으므로 이 합도 커지지 않는다. 따라서 가능한 x의 구간 끝을 이분 탐색할 수 있다.

$$
\operatorname{can}(x) \iff \sum_i \left\lfloor \frac{c_i}{x} \right\rfloor \ge k, \quad x \ge 1
$$

정렬된 배열에서 첫 번째로 x 이상인 위치를 찾는 lower_bound도 같은 경계 탐색이다. Python에서는 bisect_left가 이 역할을 한다.

```python
from bisect import bisect_left


if __name__ == "__main__":
    values = [1, 3, 3, 7]
    index = bisect_left(values, 3)
    assert index == 1
    assert values[index] >= 3
```

## 적용 조건

다음 항목을 먼저 적어 본다.

1. 전체 답의 최솟값과 최댓값은 무엇인가?
2. 중간값을 판정하는 함수가 원래 문제를 정확히 결정하는가?
3. 중간값을 키웠을 때 가능성이 유지되는가, 아니면 작게 했을 때 유지되는가?
4. 반복 중 left와 right가 각각 어떤 의미를 가지는가? 예를 들어 left는 항상 feasible인 값이고 right는 아직 조사하지 않은 상한일 수 있다.
5. 정수 나눗셈, 빈 입력, 답이 0인 경우를 포함해 판정 함수가 모든 호출값에서 정의되는가?

답에 대한 이분 탐색에서 판정이 단조가 아니면, 우연히 샘플을 통과해도 이분 탐색을 사용할 수 없다. 그 경우에는 상태를 더 추가하거나 다른 알고리즘을 선택한다.

## 불변식과 정확성

현재 저장된 2226 구현은 가능한 양의 분배량의 최댓값을 찾는다.

- 초기 left = 0은 항상 가능하다고 해석한다. 아이들에게 양을 0으로 주는 경우는 목표량이 0인 답이므로, 판정 함수에 0을 넘기지 않고 경계값으로만 사용한다.
- right = max(candies)는 한 더미보다 많이 줄 수 없으므로 답의 상한이다.
- 반복 중 left보다 작거나 같은 값은 가능하고, right보다 큰 값은 답이 될 수 없다는 범위를 유지한다.
- mid가 가능하면 답이 mid 이상일 수 있으므로 left를 mid로 올린다. mid가 불가능하면 mid 이상은 모두 불가능하므로 right를 mid - 1로 내린다.

이 구현의 mid는 (left + right + 1) // 2인 upper-mid다. $left < right$이고 right가 적어도 1일 때 mid는 적어도 1이므로, candy // mid에서 0으로 나누는 일이 발생하지 않는다. 이것이 이 코드가 left = 0을 경계로 두면서도 can_divide 내부에서 0을 특별 처리하지 않는 이유다. 반복이 끝나면 left == right이고, 불변식에 따라 그 값이 가능한 최댓값이다.

## 작은 예

다음은 저장된 풀이와 같은 방향의 독립 실행 예다. 후보 x가 1 이상인 경우에만 나눗셈 판정을 호출하고, 모두 0인 입력은 즉시 0을 반환한다.

```python
def maximum_equal_share(candies: list[int], children: int) -> int:
    if not candies:
        return 0

    left = 0
    right = max(candies)

    def can_divide(value: int) -> bool:
        return sum(candy // value for candy in candies) >= children

    while left < right:
        mid = (left + right + 1) // 2
        if can_divide(mid):
            left = mid
        else:
            right = mid - 1

    return left


if __name__ == "__main__":
    assert maximum_equal_share([5, 8], 3) == 4
    assert maximum_equal_share([1, 2], 5) == 0
    assert maximum_equal_share([0, 0], 2) == 0
```

[5, 8]에서 x = 4이면 1 + 2 = 3명을 만들 수 있지만, x = 5이면 1 + 1 = 2명뿐이다. 따라서 최댓값은 4다.

## 복잡도

후보 판정이 원소 n개를 한 번 보는 $O(n)$이고, 후보 범위의 크기를 매번 절반으로 줄이므로 전체 시간은 $O(n\log(M+1))$이다. 여기서 M은 candies의 최댓값이다. 현재 2226 구현은 별도 배열을 만들지 않아 추가 공간 $O(1)$이다. 다른 문제에서는 판정 비용에 탐색 반복 횟수를 곱한다.

## 경계와 함정

- upper-mid를 쓰지 않고 (left + right) // 2를 쓰면 left와 right가 한 칸 차이일 때 mid가 left가 되어 진행하지 않을 수 있다.
- 2226의 can_divide는 value = 0을 받으면 0으로 나누기 오류가 난다. 현재 코드는 right > 0인 반복에서 upper-mid가 절대 0이 되지 않는 구조다. 다른 이분 탐색 틀에 옮길 때 이 보장을 잃지 않는다.
- candies가 비어 있으면 저장된 코드는 max(candies)에서 실패한다. 이는 원문 입력 제약 밖의 일반화 사례이며, 독립 예제는 방어적으로 처리했다.
- 전체 사탕 수가 children보다 적으면 양의 x는 불가능하고 답 0이다.
- 정답 공간이 실수이거나 판정이 오차를 포함하면 정수 이분 탐색 종료 조건을 그대로 쓰지 않는다.
- C++에서는 left + right overflow를 피하는 mid 식을 사용해야 하지만, Python 정수는 overflow가 없다. 그래도 경계 불변식은 동일하게 작성한다.

## 관련 노트와 코드

- [누적 집계 (Prefix Aggregates)](../basics/prefix-aggregates.md) — 판정에 누적 합·개수를 사용하는 방법.
- [투 포인터 (Two Pointers)](../basics/two-pointers.md) — 답 판정의 이분 대신 양끝 포인터의 단조 이동을 사용하는 방법.
- [2226 문제 노트](../../leetcode/medium/2226.maximum-candies-allocated-to-k-children.md) · [풀이 코드](../../leetcode/medium/2226.maximum-candies-allocated-to-k-children.py)

## 출처

- [LeetCode 2226 공식 문제](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) — floor-sum feasibility와 답에 대한 이분 탐색의 실제 적용.
- [Python 공식 문서: 정수 나눗셈](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) — Python의 정수 연산 의미를 확인할 때 참고.
