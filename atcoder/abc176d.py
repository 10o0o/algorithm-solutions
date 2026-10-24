# AT ABC176 D?LANG=EN
# https://atcoder.jp/contests/abc176/tasks/abc176_d?lang=en

import heapq
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dijkstra(n, graph, start):
    dists = [float("inf")] * n
    dists[start] = 0
    heap = [(0, start)]

    while heap:
        weight, node = heapq.heappop(heap)

        if weight > dists[node]:
            continue

        for dest in graph[node]:
            next_weight = weight + 1
            if dists[dest] > next_weight:
                dists[dest] = next_weight
                heapq.heappush(heap, (next_weight, dest))

    return dists


def solve() -> None:
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    maze = [list(input().strip()) for _ in range(h)]
    ids = [[-1] * w for _ in range(h)]
    cur_id = 0

    for i in range(h):
        for j in range(w):
            if maze[i][j] == "#":
                continue

            if ids[i][j] != -1:
                continue

            q = deque()
            q.append((i, j))
            ids[i][j] = cur_id

            while q:
                qi, qj = q.popleft()

                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    mi = qi + di
                    mj = qj + dj

                    if (
                        mi < 0
                        or mj < 0
                        or mi >= h
                        or mj >= w
                        or maze[mi][mj] == "#"
                        or ids[mi][mj] != -1
                    ):
                        continue

                    ids[mi][mj] = cur_id
                    q.append((mi, mj))

            cur_id += 1

    graph = defaultdict(set)

    for i in range(h):
        for j in range(w):
            if ids[i][j] == -1:
                continue

            for di in range(-2, 3):
                for dj in range(-2, 3):
                    mi = i + di
                    mj = j + dj

                    if mi < 0 or mj < 0 or mi >= h or mj >= w or ids[mi][mj] == -1:
                        continue

                    if ids[mi][mj] == ids[i][j]:
                        continue

                    id_a, id_b = ids[i][j], ids[mi][mj]

                    graph[id_a].add(id_b)
                    graph[id_b].add(id_a)

    start = ids[c_h - 1][c_w - 1]
    dest = ids[d_h - 1][d_w - 1]

    dists = dijkstra(cur_id, graph, start)

    print(dists[dest] if dists[dest] != float("inf") else -1)


if __name__ == "__main__":
    solve()
