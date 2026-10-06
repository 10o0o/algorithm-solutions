# Planets and Kingdoms
# https://cses.fi/problemset/task/1683/

import sys
from collections import defaultdict

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())

    graph = defaultdict(list)
    graph_reverse = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph_reverse[v].append(u)

    visited = [False] * (n + 1)
    order = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        stack = [(0, start)]

        while stack:
            state, u = stack.pop()

            if state == 1:
                order.append(u)
                continue

            if visited[u]:
                continue

            visited[u] = True

            stack.append((1, u))
            for v in graph[u]:
                stack.append((0, v))

    visited = [False] * (n + 1)
    ids = [0] * (n + 1)
    cur_id = 1

    for start in order[::-1]:
        if visited[start]:
            continue

        stack = [start]

        while stack:
            u = stack.pop()

            if visited[u]:
                continue

            visited[u] = True
            ids[u] = cur_id

            for v in graph_reverse[u]:
                stack.append(v)

        cur_id += 1

    print(cur_id - 1)
    print(*ids[1:])


if __name__ == "__main__":
    solve()
