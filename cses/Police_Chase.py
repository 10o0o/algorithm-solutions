# Police Chase
# https://cses.fi/problemset/task/1695

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())

    graph = defaultdict(list)
    remain = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

        remain[u][v] += 1
        remain[v][u] += 1

    while True:
        parent = [-1] * (n + 1)
        q = deque([1])

        while q:
            u = q.popleft()

            for v in graph[u]:
                if parent[v] != -1:
                    continue
                if remain[u][v] <= 0:
                    continue

                parent[v] = u
                q.append(v)

        if parent[n] == -1:
            group = {1}

            for node in range(2, n + 1):
                if parent[node] != -1:
                    group.add(node)

            roads_to_block = []

            for u in group:
                for v in graph[u]:
                    if v not in group:
                        roads_to_block.append((u, v))

            print(len(roads_to_block))
            for u, v in roads_to_block:
                print(f"{u} {v}")

            return

        v = n
        while v != 1:
            u = parent[v]
            remain[v][u] += 1
            remain[u][v] -= 1
            v = u


if __name__ == "__main__":
    solve()
