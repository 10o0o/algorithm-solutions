# E - Flip Edge
# https://atcoder.jp/contests/abc395/tasks/abc395_e?lang=en

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(n, graph, graph_reverse, start, flip_cost):
    dists = [[float("inf"), float("inf")] for _ in range(n + 1)]
    graphs = [graph, graph_reverse]
    dists[start][0] = 0
    dists[start][1] = flip_cost
    heap = [(0, start, 0), (flip_cost, start, 1)]

    while heap:
        weight, node, is_flip = heapq.heappop(heap)

        if dists[node][is_flip] < weight:
            continue

        for dest in graphs[is_flip][node]:
            next_weight = weight + 1

            if dists[dest][is_flip] > next_weight:
                dists[dest][is_flip] = next_weight
                heapq.heappush(heap, (next_weight, dest, is_flip))

        # flip
        is_flip ^= 1
        weight += flip_cost

        for dest in graphs[is_flip][node]:
            next_weight = weight + 1

            if dists[dest][is_flip] > next_weight:
                dists[dest][is_flip] = next_weight
                heapq.heappush(heap, (next_weight, dest, is_flip))

    return dists


def minimum_cost(n, edges, flip_cost):
    graph = defaultdict(list)
    graph_reverse = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph_reverse[v].append(u)

    dists = dijkstra(n, graph, graph_reverse, 1, flip_cost)

    return min(dists[n])


def solve() -> None:
    n, m, flip_cost = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(minimum_cost(n, edges, flip_cost))


if __name__ == "__main__":
    solve()
