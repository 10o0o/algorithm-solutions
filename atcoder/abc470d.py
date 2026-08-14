# AT ABC470 D
# https://atcoder.jp/contests/abc470/tasks/abc470_d

import sys

input = sys.stdin.readline


def solve() -> None:
    n, q = map(int, input().split())
    p = list(map(int, input().split()))

    inverse = [0] * n

    for i, value in enumerate(p):
        inverse[value - 1] = i + 1

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1

            p[x], p[y] = p[y], p[x]
            inverse[p[x] - 1] = x + 1
            inverse[p[y] - 1] = y + 1
        else:
            p, inverse = inverse, p

    print(*p)


if __name__ == "__main__":
    solve()
