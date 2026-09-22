# AT ABC384 E?LANG=EN
# https://atcoder.jp/contests/abc384/tasks/abc384_e?lang=en

import heapq
import sys

input = sys.stdin.readline


def solve() -> None:
    h, w, x = map(int, input().split(" "))
    p, q = map(int, input().split(" "))
    s = [[-1] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        row = list(map(int, input().split(" ")))
        for j in range(w):
            s[i][j] = row[j]

    pq = []

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    def is_valid_pos(x, y):
        return x >= 0 and y >= 0 and x < h and y < w

    p -= 1
    q -= 1
    visited[p][q] = True

    def add_candidate(x, y):
        for k in range(4):
            mx = x + dx[k]
            my = y + dy[k]

            if is_valid_pos(mx, my) and not visited[mx][my]:
                heapq.heappush(pq, (s[mx][my], mx, my))
                visited[mx][my] = True

    add_candidate(p, q)
    power = s[p][q]

    while pq:
        cell_power, cx, cy = heapq.heappop(pq)

        if cell_power < (power // x + (1 if power % x != 0 else 0)):
            power += cell_power
            add_candidate(cx, cy)

    print(power)


if __name__ == "__main__":
    solve()
