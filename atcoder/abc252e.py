# AT ABC252 E?LANG=EN
# https://atcoder.jp/contests/abc252/tasks/abc252_e?lang=en

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(n, graph, start):
    dists = [float("inf")] * (n + 1)
    prev_edge = [-1] * (n + 1)

    dists[start] = 0
    heap = [(0, start)]

    while heap:
        weight, node = heapq.heappop(heap)

        if dists[node] < weight:
            continue

        for dest, d_weight, edge in graph[node]:
            next_weight = weight + d_weight

            if dists[dest] > next_weight:
                dists[dest] = next_weight
                prev_edge[dest] = edge

                heapq.heappush(heap, (next_weight, dest))

    return dists, prev_edge


def solve() -> None:
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c, i + 1))
        graph[b].append((a, c, i + 1))

    _, prev_edge = dijkstra(n, graph, 1)

    ans = [edge for edge in prev_edge if edge != -1]
    print(*ans, sep=" ")


if __name__ == "__main__":
    solve()
