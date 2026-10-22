# 001 - Yokan Party
# https://atcoder.jp/contests/typical90/tasks/typical90_a

import sys

input = sys.stdin.readline


def solve() -> None:
    n, l = map(int, input().split())
    k = int(input())
    cuts = list(map(int, input().split()))

    def can(x):
        rest_k = k + 1
        pos = 0

        for cut in cuts + [l]:
            if rest_k == 0:
                break

            if cut - pos >= x:
                rest_k -= 1
                pos = cut

        return rest_k == 0

    lo, hi = 0, l

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)


if __name__ == "__main__":
    solve()
