---
title: "깊이 우선 탐색 (DFS)"
updated: "2026-09-20"
tags:
  - "dfs"
  - "tree"
  - "graph"
  - "recursion"
---

# 깊이 우선 탐색 (DFS)

## 핵심 요약

깊이 우선 탐색은 한 정점에서 갈 수 있는 한 경로를 먼저 끝까지 내려간 뒤 돌아와 다른 선택지를 처리하는 방법이다. 트리의 하위 구조를 반환하는 재귀, 그래프의 연결 요소·사이클 확인, 선택을 쌓고 되돌리는 백트래킹에 잘 맞는다.

## 개념 정리

DFS는 재귀 호출 스택이나 명시적 stack을 사용한다. 현재 정점에서 아직 방문하지 않은 이웃을 하나 선택해 더 깊이 들어가고, 더 내려갈 수 없으면 호출이 끝나며 이전 정점으로 돌아온다. 그래프에서는 사이클과 중복 경로를 막기 위해 visited를 관리한다.

다음 단서를 찾는다.

- 트리 노드의 왼쪽·오른쪽 결과를 모아 현재 노드의 값을 계산한다.
- 연결 요소, 도달 가능성, 사이클, 위상 순서처럼 전체를 방문해야 한다.
- 선택을 하나 추가한 뒤 재귀하고, 반환할 때 선택을 되돌리는 백트래킹이 필요하다.
- 방문 순서보다 한 경로의 내부 구조나 후위 결과가 중요하다.

간선 가중치가 같은 그래프에서 최단 거리 자체가 목표라면 DFS의 먼저 찾은 경로를 최단이라고 해석할 수 없다. 그 경우는 [BFS 노트](bfs.md)처럼 레벨을 보거나 다른 최단 경로 알고리즘을 선택한다.

## 적용 조건

1. 입력이 트리인가, 일반 그래프인가? 트리도 공유 참조 가능성이 있으면 visited가 필요하다.
2. 재귀 함수가 반환해야 하는 값과 현재 노드에서 갱신할 전역·외부 상태를 분리했는가?
3. 그래프라면 방문 표시를 재귀 호출 전 어느 시점에 할 것인가? 보통 진입 시 표시한다.
4. 깊이가 Python 재귀 제한을 넘을 수 있는가? 긴 선형 트리나 큰 그래프는 명시적 stack을 검토한다.
5. 백트래킹이라면 재귀 호출 후 선택을 원상 복구하는가?

## 불변식과 정확성

현재 저장된 [101 풀이 코드](../../leetcode/easy/101.symmetric-tree.py)의 is_mirror(left, right)는 두 입력 서브트리가 서로 거울 대칭인지 판정한다.

- 두 노드가 모두 None이면 대응할 구조가 없으므로 대칭이다.
- 한쪽만 None이면 구조가 다르므로 대칭이 아니다.
- 두 값이 다르면 대칭일 수 없다.
- 값이 같으면 왼쪽 노드의 왼쪽 자식과 오른쪽 노드의 오른쪽 자식, 그리고 왼쪽 노드의 오른쪽 자식과 오른쪽 노드의 왼쪽 자식이 각각 대칭인지 재귀적으로 확인한다.

귀납적으로, 함수가 반환하는 True는 두 서브트리의 모든 대응 노드가 같은 값과 거울 위치를 가진다는 뜻이고, False는 위 세 가지 배제 조건 중 하나가 실제로 성립한다는 뜻이다. root의 두 자식을 최초의 대응쌍으로 호출하면 전체 트리의 대칭 여부를 얻는다. 저장된 LeetCode 메서드는 문제 입력의 root가 노드라는 조건에 맞춰 root.left와 root.right에서 시작한다.

$$
is_mirror(left, right) =
same_value(left, right)
and is_mirror(left.left, right.right)
and is_mirror(left.right, right.left)
$$

## 작은 예

다음은 root가 비어 있는 경우도 처리하도록 만든 독립 실행 예다. 문제의 비어 있지 않은 root 조건에 맞춘 저장 코드와 달리, 일반 함수로 사용할 때의 안전한 시작점을 함께 보여 준다.

```python
class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_mirror(left: Node | None, right: Node | None) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.value != right.value:
        return False
    return is_mirror(left.left, right.right) and is_mirror(
        left.right, right.left
    )


def is_symmetric(root: Node | None) -> bool:
    return root is None or is_mirror(root.left, root.right)


if __name__ == "__main__":
    symmetric = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
    asymmetric = Node(1, Node(2), Node(2, right=Node(3)))
    assert is_symmetric(symmetric)
    assert not is_symmetric(asymmetric)
    assert is_symmetric(None)
```

## 복잡도

트리의 각 노드를 한 번 방문하므로 시간은 $O(n)$이다. 재귀 호출 스택은 트리 높이 h만큼 사용해 추가 공간 $O(h)$이다. 균형 트리는 $O(log n)$이지만 한쪽으로 치우친 트리는 $O(n)$ 깊이가 된다. 일반 그래프에서 visited와 stack을 쓰면 시간 $O(V + E)$, 공간 $O(V)$이다.

## 경계와 함정

- 저장된 101 코드는 root가 None이면 root.left에서 오류가 난다. 원문 제약이 바뀌어 빈 트리를 허용하면 시작 전에 None을 처리한다.
- Python 재귀 제한 때문에 깊은 트리는 RecursionError가 날 수 있다. 노드 수가 큰 선형 구조라면 명시적 stack이나 재귀 제한 변경의 필요성을 먼저 판단한다.
- 일반 그래프에서 visited 없이 재귀하면 사이클에서 끝나지 않거나 같은 정점을 반복 처리한다.
- 방문 표시를 늦게 하면 두 경로가 같은 정점을 동시에 stack에 넣을 수 있다. 그래프에서는 보통 이웃을 stack에 넣을 때 표시한다.
- 백트래킹 상태는 호출 후 되돌려야 다음 형제 분기가 이전 선택의 영향을 받지 않는다.
- DFS의 방문 순서로 최단 거리를 주장하지 않는다. 같은 가중치 최단 경로는 BFS나 거리 알고리즘의 불변식을 사용해야 한다.

## 관련 노트와 코드

- [너비 우선 탐색 (BFS)](bfs.md) — 레벨 순서와 무가중치 최단 거리.
- [101 풀이 코드](../../leetcode/easy/101.symmetric-tree.py) — 두 서브트리를 교차 비교하는 실제 재귀 DFS.
- [1302 문제 노트](../../leetcode/medium/1302.deepest-leaves-sum.md) · [풀이 코드](../../leetcode/medium/1302.deepest-leaves-sum.py) — 같은 트리를 레벨 BFS로 집계하는 비교 대상.

## 출처

- [LeetCode 101 공식 문제](https://leetcode.com/problems/symmetric-tree/) — 트리 재귀 DFS의 실제 적용.
- [Python 공식 문서: 재귀 호출 제한](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit) — 깊은 재귀의 실행 한계를 확인할 때 참고.
