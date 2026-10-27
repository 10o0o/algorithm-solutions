# Download Speed
# https://cses.fi/problemset/task/1694

import sys
from collections import deque

input = sys.stdin.readline


def find_path(graph, remain, source, sink, limit):
    parent = [-1] * len(graph)
    parent[source] = source
    q = deque([source])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if parent[v] != -1:
                continue
            if remain[u][v] < limit:
                continue

            parent[v] = u
            if v == sink:
                return parent
            q.append(v)

    return None


def send_flow(remain, parent, source, sink):
    d = float("inf")
    v = sink

    while v != source:
        u = parent[v]
        d = min(d, remain[u][v])
        v = u

    v = sink

    while v != source:
        u = parent[v]
        remain[u][v] -= d
        remain[v][u] += d
        v = u

    return d


def max_flow(graph, remain, source, sink):
    if source == sink:
        return 0

    max_capacity = max(max(row) for row in remain)
    limit = 1
    while limit * 2 <= max_capacity:
        limit *= 2

    ans = 0

    while limit > 0:
        while True:
            parent = find_path(graph, remain, source, sink, limit)
            if parent is None:
                break

            ans += send_flow(remain, parent, source, sink)

        limit //= 2

    return ans


def solve() -> None:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    remain = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        remain[a][b] += c

    print(max_flow(graph, remain, 1, n))


if __name__ == "__main__":
    solve()
