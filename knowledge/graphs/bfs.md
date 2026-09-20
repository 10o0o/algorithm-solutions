---
title: "너비 우선 탐색 (BFS)"
updated: "2026-09-20"
tags:
  - "bfs"
  - "graph"
  - "tree"
  - "shortest-path"
---

# 너비 우선 탐색 (BFS)

## 핵심 요약

너비 우선 탐색은 시작점에서 최소 간선 수가 작은 정점부터 큐로 처리하는 탐색이다. 모든 간선 비용이 같은 비음수 값이면 최소 비용 경로도 구할 수 있으며, 트리에서는 한 레벨의 집계·가장 깊은 레벨을 간단히 계산할 수 있다.

## 개념 정리

큐에 시작 정점을 넣고, 앞에서 꺼낸 정점의 이웃을 뒤에 넣는다. 시작점에서의 간선 수가 같은 정점들이 같은 레벨에 모인다. 일반 그래프에서는 이미 큐에 넣은 정점을 visited로 표시해 사이클과 중복 간선을 막는다. 여러 시작점에서 동시에 출발하는 다중 소스 BFS라면 모든 시작점을 거리 0으로 큐에 넣는다.

다음 단서가 있으면 BFS를 먼저 검토한다.

- 모든 간선 비용이 같은 비음수 값이고 최소 비용을 묻는다. 이때는 최소 간선 수 최단 경로와 같은 레벨 순서를 쓴다.
- 트리의 깊이별 합·최댓값·노드 수처럼 레벨 단위 집계가 필요하다.
- 한 단계에서 갈 수 있는 상태를 다음 단계로 확장하며 최소 횟수를 찾는다.

간선 비용이 0과 1로 섞여 있으면 0-1 BFS를 사용하고, 임의의 비음수 비용이면 Dijkstra를 사용한다. 일반 BFS의 큐 레벨을 비용 최단 거리로 쓰는 것은 모든 간선 비용이 같을 때의 조건이다.

저장된 [1302 구현](../../leetcode/medium/1302.deepest-leaves-sum.py)은 트리의 각 레벨을 순서대로 처리해 마지막 레벨의 합을 반환한다. 트리 입력에서는 자식 참조가 유일하고 사이클이 없으므로 visited가 없어도 된다. 이 코드 자체를 일반 그래프의 최단 경로 구현이라고 부르면 안 된다. 그래프 인접 목록, 거리 배열, visited 관리가 없고 목표도 가장 깊은 트리 레벨의 합으로 한정되어 있다.

## 적용 조건

1. “가까움”을 간선 수 또는 동일한 비용의 단계 수로 정의할 수 있는가?
2. 한 레벨을 모두 처리한 뒤 다음 레벨로 넘어가야 하는가? 그렇다면 큐 길이를 레벨 시작 때 저장한다.
3. 그래프에 사이클이나 여러 경로가 있는가? 있다면 큐에 넣을 때 visited를 표시한다.
4. 간선 비용이 0과 1로 섞여 있으면 0-1 BFS, 임의의 비음수 비용이면 Dijkstra를 선택한다. 일반 BFS의 레벨 순서는 모든 간선 비용이 같을 때만 비용 최단 거리와 일치한다.
5. 최단 거리 하나만 필요하다면 목표를 처음 꺼냈을 때 종료할 수 있는가? 레벨 전체 집계라면 현재 레벨을 끝까지 처리해야 한다.

## 불변식과 정확성

일반 그래프 BFS에서는 큐에 들어간 정점의 거리가 이미 계산된 최단 거리이고, 큐의 앞에서 뒤로 갈수록 거리가 감소하지 않는다. 간선 (u, v)의 비용이 모두 같다고 1로 두면

$$
dist[v] = dist[u] + 1
$$

어떤 정점을 처음 방문할 때 그 정점으로 가는 경로는 이전 레벨에서 한 간선을 추가한 경로이므로 거리 후보가 최단이다. 더 짧은 경로가 있었다면 그 경로의 앞 정점이 먼저 처리되어 같은 정점을 더 일찍 큐에 넣었어야 한다.

1302의 트리 코드는 이 성질을 레벨 집계에 사용한다. 바깥 while 한 번이 큐에 있던 한 레벨을 고정하고, for문에서 그 레벨의 노드를 모두 꺼내 자식들을 다음 레벨로 넣는다. 따라서 for문이 끝날 때 level_sum은 정확히 현재 깊이의 합이고, 큐가 비기 직전에 계산된 마지막 level_sum이 가장 깊은 리프 레벨의 합이다.

## 작은 예

다음은 저장된 문제 코드와 같은 “트리 레벨 합”을 작은 독립 프로그램으로 만든 예다. 큐 길이를 for문 범위에 먼저 복사해 현재 레벨과 다음 레벨을 구분한다.

```python
from collections import deque


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def deepest_level_sum(root: Node | None) -> int:
    if root is None:
        return 0

    queue = deque([root])
    answer = 0
    while queue:
        answer = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            answer += node.value
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return answer


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(6)))
    assert deepest_level_sum(root) == 15
    assert deepest_level_sum(None) == 0
```

## 복잡도

인접 목록으로 표현한 그래프에서 각 정점과 간선을 최대 한 번 처리하므로 시간은 $O(V + E)$이다. 큐와 visited, 거리 배열을 사용하면 공간은 $O(V)$이다. 트리에서는 노드 수를 n, 한 레벨의 최대 너비를 w라 할 때 시간 $O(n)$, 큐 공간 $O(w)$이다. 현재 1302 구현은 TreeNode를 입력으로 받고 별도 visited를 만들지 않으므로 추가 큐 공간은 최대 레벨 너비만큼이다.

## 경계와 함정

- 빈 root는 저장된 1302 코드가 0을 반환한다. 마지막 합을 초기값 0으로 두지 않고 root가 없는 경우를 먼저 처리한다.
- len(queue)를 for문 안에서 계속 다시 읽지 말고 레벨 시작값을 범위로 사용한다. 자식을 추가하는 동안 큐 길이가 바뀌기 때문이다.
- 일반 그래프에서 visited를 큐에서 꺼낼 때 표시하면 같은 정점이 여러 번 들어갈 수 있다. 보통 큐에 넣는 순간 표시한다.
- 가중치가 다른 그래프에서 BFS의 깊이를 비용 최단 거리로 해석하면 안 된다.
- 깊이별 합을 구할 때 level_sum을 레벨마다 초기화하고, 가장 마지막으로 처리한 레벨의 값을 반환한다.
- 트리라고 주어지지 않은 입력에는 부모·자식의 중복 참조나 사이클이 있을 수 있으므로 저장된 1302 코드를 그대로 일반화하지 않는다.

## 관련 노트와 코드

- [깊이 우선 탐색 (DFS)](dfs.md) — 재귀·스택으로 한 가지 가지를 깊게 처리하는 탐색.
- [1302 문제 노트](../../leetcode/medium/1302.deepest-leaves-sum.md) · [풀이 코드](../../leetcode/medium/1302.deepest-leaves-sum.py)
- [101 풀이 코드](../../leetcode/easy/101.symmetric-tree.py) — 트리 구조를 재귀 DFS로 비교하는 예.

## 출처

- [LeetCode 1302 공식 문제](https://leetcode.com/problems/deepest-leaves-sum/) — 트리 레벨 BFS의 실제 적용.
- [Python 공식 문서: collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) — 양끝 큐 연산의 시간 특성을 확인할 때 참고.
