# E - Train
# https://atcoder.jp/contests/abc192/tasks/abc192_e?lang=en

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(n, graph, start):
    dists = [float("inf")] * (n + 1)
    dists[start] = 0
    heap = [(0, start)]

    while heap:
        acc, node = heapq.heappop(heap)

        if dists[node] < acc:
            continue

        for weight, dest, k in graph[node]:
            time_delay = (k - (acc % k)) % k
            next_dist = acc + weight + time_delay

            if dists[dest] > next_dist:
                dists[dest] = next_dist
                heapq.heappush(heap, (next_dist, dest))

    return dists


def earliest_arrival(n, routes, start, goal):
    # routes의 각 원소는 (A_i, B_i, T_i, K_i)입니다.
    graph = defaultdict(list)

    for a, b, t, k in routes:
        graph[a].append((t, b, k))
        graph[b].append((t, a, k))

    dists = dijkstra(n, graph, start)

    return -1 if dists[goal] == float("inf") else dists[goal]


def solve() -> None:
    n, m, start, goal = map(int, input().split())
    routes = [tuple(map(int, input().split())) for _ in range(m)]
    print(earliest_arrival(n, routes, start, goal))


if __name__ == "__main__":
    solve()
