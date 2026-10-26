# AT ABC208 D?LANG=EN
# https://atcoder.jp/contests/abc208/tasks/abc208_d?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())

    dists = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dists[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dists[a][b] = c

    ans = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dists[i][j] = min(
                    dists[i][j],
                    dists[i][k] + dists[k][j],
                )

                if dists[i][j] not in (0, float("inf")):
                    ans += dists[i][j]

    print(ans)


if __name__ == "__main__":
    solve()
