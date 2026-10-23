# E - Crystal Switches
# https://atcoder.jp/contests/abc277/tasks/abc277_e?lang=en

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(n, graph, switches, start):
    dists = [[float("inf")] * 2 for _ in range(n + 1)]
    dists[start][0] = 0
    dq = deque()
    dq.append((0, start, 0))

    while dq:
        weight, node, is_switch_on = dq.popleft()

        if dists[node][is_switch_on] < weight:
            continue

        if node in switches and dists[node][is_switch_on ^ 1] > weight:
            dists[node][is_switch_on ^ 1] = weight
            dq.appendleft((weight, node, is_switch_on ^ 1))

        for v, a in graph[node]:
            if is_switch_on == a:
                continue

            next_weight = weight + 1

            if dists[v][is_switch_on] > next_weight:
                dists[v][is_switch_on] = next_weight
                dq.append((next_weight, v, is_switch_on))

    return dists


def minimum_moves(n, edges, switches):
    graph = defaultdict(list)

    for u, v, a in edges:
        graph[u].append((v, a))
        graph[v].append((u, a))

    dists = bfs(n, graph, switches, 1)

    return -1 if min(dists[n]) == float("inf") else min(dists[n])


def solve() -> None:
    n, m, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    switches = set(map(int, input().split())) if k else set()
    print(minimum_moves(n, edges, switches))


if __name__ == "__main__":
    solve()
