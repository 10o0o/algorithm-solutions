# D - Super Takahashi Bros.
# https://atcoder.jp/contests/abc340/tasks/abc340_d?lang=en

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(n, graph, start):
    dists = [float("inf")] * (n + 1)
    dists[start] = 0
    heap = [(0, start)]
    heapq.heappush(heap, (0, start))

    while heap:
        acc, node = heapq.heappop(heap)

        if dists[node] < acc:
            continue

        dists[node] = acc

        for weight, dest in graph[node]:
            next_dist = acc + weight
            if dists[dest] > next_dist:
                dists[dest] = next_dist
                heapq.heappush(heap, (next_dist, dest))

    return dists


def minimum_time(n, stages):
    graph = defaultdict(list)

    for i, (a, b, x) in enumerate(stages, start=1):
        graph[i].append((a, i + 1))
        graph[i].append((b, x))

    dists = dijkstra(n=n, graph=graph, start=1)

    return dists[n]


def solve() -> None:
    n = int(input())
    stages = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(minimum_time(n, stages))


if __name__ == "__main__":
    solve()
