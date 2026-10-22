# Array Division
# https://cses.fi/problemset/task/1085/

import sys

input = sys.stdin.readline


def solve() -> None:
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    def can(x):
        acc = 0
        cut = 0

        for v in values + [0]:
            if v > x:
                return False

            if acc + v > x:
                acc = v
                cut += 1
            else:
                acc += v

            if cut > k - 1:
                break

        return cut <= k - 1

    lo, hi = 0, sum(values)

    while lo < hi:
        mid = (lo + hi) // 2

        if can(mid):
            hi = mid
        else:
            lo = mid + 1

    print(hi)


if __name__ == "__main__":
    solve()
