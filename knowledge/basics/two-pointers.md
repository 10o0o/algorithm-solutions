---
title: "투 포인터 (Two Pointers)"
updated: "2026-09-20"
tags:
  - "two-pointers"
  - "sliding-window"
  - "monotonicity"
---

# 투 포인터 (Two Pointers)

## 핵심 요약

투 포인터는 배열의 두 위치를 유지하면서 포인터를 한 방향으로만 이동시켜, 연속 구간·정렬된 두 구간·두 원소의 관계를 선형 시간에 조사하는 방법이다. 포인터를 움직여도 이미 버린 후보가 다시 최적 후보가 되지 않는 단조성이 있어야 한다.

## 개념 정리

포인터 left, right가 현재 구간의 양끝을 가리킨다고 하자. right를 확장해 조건을 깨뜨린 뒤 left를 줄이거나, 조건을 만족하는 동안 답을 갱신하는 전형이 슬라이딩 윈도우다. 정렬된 배열의 두 합을 찾을 때처럼 한 포인터를 왼쪽에서, 다른 포인터를 오른쪽에서 움직이는 전형도 투 포인터에 포함된다.

문제에서 다음 단서를 찾는다.

- 답이 연속 부분 배열·부분 문자열이고, 한 끝을 늘리거나 다른 끝을 줄이는 식으로 상태를 갱신할 수 있다.
- 배열이 정렬되어 있어 한 포인터의 값이 커질 때 다른 포인터의 후보가 한 방향으로만 움직인다.
- 이미 정렬된 prefix와 suffix를 이어 붙이며 중간에 버릴 구간을 고르는 문제다.

포인터를 두 개 쓴다는 사실만으로 충분하지 않다. 각 이동이 후보를 안전하게 버리는 근거가 필요하다. 특히 합이 특정 값 이하인 창을 유지하는 전형은 원소가 음수가 아니어야 left를 오른쪽으로 옮겼을 때 창의 합이 감소하거나 같다는 성질이 생긴다.

## 적용 조건

다음 조건을 점검한 뒤 선택한다.

1. 포인터마다 앞으로만 이동해도 되는가? 뒤로 돌아가야 하면 단순 투 포인터의 선형 보장이 깨진다.
2. 현재 상태에서 포인터 하나를 움직이는 비용이 O(1)인가?
3. 조건을 만족하지 않는 후보를 포인터 이동으로 영구히 버릴 수 있는가?
4. 슬라이딩 윈도우라면 길이·합·서로 다른 값 개수 같은 상태를 왼쪽 원소의 제거와 오른쪽 원소의 추가로 정확히 갱신할 수 있는가?
5. 음수나 중복이 조건의 단조성을 깨뜨리지 않는가? 음수 합, 임의의 비단조 조건은 prefix 합·해시·이분 탐색 등 다른 도구를 검토한다.

## 불변식과 정확성

현재 저장된 [1574 풀이 코드](../../leetcode/medium/1574.shortest-subarray-to-be-removed-to-make-array-sorted.py)는 일반적인 합 윈도우가 아니라 정렬된 prefix와 suffix를 이어 붙이는 투 포인터다. left가 가리키는 prefix [0, left]는 비내림차순이고, right에서 시작하는 suffix [right, n)는 비내림차순이라는 불변식을 먼저 만든다.

이후 i는 prefix 안에서, j는 suffix 안에서 움직인다.

- arr[i] <= arr[j]이면 두 구간을 이 위치에서 연결할 수 있으므로 j - i - 1개를 지우는 후보를 기록하고 i를 늘린다. 더 큰 i가 만드는 연결만 남겨도 prefix 내부의 순서는 유지된다.
- arr[i] > arr[j]이면 현재 j로는 이 i를 연결할 수 없다. suffix가 비내림차순이므로 j를 오른쪽으로 옮겨 값이 더 작아지지 않는 후보를 찾을 수 있다.

따라서 포인터가 지나간 조합은 다시 최적일 수 없고, 모든 i, j가 한 번씩만 지나간다. prefix 전체 제거와 suffix 전체 제거도 초기 후보로 넣으므로 연결하지 못한 경우까지 포함해 최솟값을 얻는다.

## 작은 예

다음은 모든 원소가 음이 아닌 배열에서 합이 limit 이하인 가장 긴 연속 구간을 찾는 독립 실행 예다. right를 늘린 뒤 합이 커지면 left를 줄여 다시 조건을 만족시킨다.

```python
def longest_window_at_most(values: list[int], limit: int) -> int:
    if limit < 0:
        return 0

    left = 0
    current = 0
    answer = 0

    for right, value in enumerate(values):
        current += value
        while left <= right and current > limit:
            current -= values[left]
            left += 1
        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    assert longest_window_at_most([2, 1, 3, 1, 1], 4) == 2
    assert longest_window_at_most([], 4) == 0
```

음수가 들어오면 왼쪽을 옮긴 뒤 합이 항상 줄어든다는 보장이 사라진다. 그때 위 코드를 그대로 재사용하지 말고, 문제의 정확한 단조성이나 prefix 합 기반 방법을 다시 확인한다.

$$
window = values[left:right + 1],
current = sum(window)
$$

## 복잡도

각 포인터가 배열 길이 n만큼 앞으로 최대 한 번씩 이동하므로 시간은 $O(n)$이다. 현재 창과 답만 보존하면 추가 공간은 $O(1)$이며, 빈도표·집합을 유지하면 그 자료구조의 크기만큼 $O(k)$가 추가된다. 1574의 저장된 코드는 별도 배열이나 자료구조를 만들지 않아 시간 $O(n)$, 추가 공간 $O(1)$이다.

## 경계와 함정

- 빈 배열, 원소 하나, 전체 배열이 이미 조건을 만족하는 경우를 별도로 확인한다.
- 창을 줄이는 while문에서 left를 실제로 이동시키지 않으면 무한 반복이 생긴다.
- right를 확장하기 전에 답을 갱신하는지, 조건을 복구한 뒤 갱신하는지 규칙을 일관되게 정한다.
- <=와 <는 중복 원소를 허용하는지에 따라 결과를 바꾼다. 1574의 정렬 조건은 비내림차순이므로 <=가 맞다.
- 두 포인터가 한 방향으로 간다는 설명만 하고, 왜 버린 조합이 복구될 필요가 없는지 증명하지 않으면 선형 시간 주장이 성립하지 않는다.
- 슬라이딩 윈도우와 정렬된 양끝 포인터는 같은 이름 아래 다른 불변식을 가진다. 문제의 조건에 맞는 쪽을 선택한다.

## 관련 노트와 코드

- [누적 집계 (Prefix Aggregates)](prefix-aggregates.md) — 구간 상태를 앞에서부터 누적하는 방법.
- [이분 탐색 (Binary Search)](../search/binary-search.md) — 포인터 이동의 단조성 대신 답 판정의 단조성을 이용하는 방법.
- [1574 풀이 코드](../../leetcode/medium/1574.shortest-subarray-to-be-removed-to-make-array-sorted.py) — 정렬된 prefix·suffix를 연결하는 실제 투 포인터.
- [1422 문제 노트](../../leetcode/easy/1422.maximum-score-after-splitting-a-string.md) — 두 count를 rolling하며 split을 한 번씩 검사하는 관련 선형 스캔.

## 출처

- [LeetCode 1574 공식 문제](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) — 저장된 prefix·suffix 연결 풀이가 적용되는 문제.
- [Python 공식 문서: enumerate](https://docs.python.org/3/library/functions.html#enumerate) — 포인터와 배열 인덱스를 함께 순회하는 예제의 기준.
