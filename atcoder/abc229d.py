# D - Longest X
# https://atcoder.jp/contests/abc229/tasks/abc229_d?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    s = input().strip()
    k = int(input())

    def can(x):
        cnts = 0

        for i in range(x):
            if s[i] == ".":
                cnts += 1

        if cnts <= k:
            return True

        for e in range(x, len(s)):
            if s[e - x] == ".":
                cnts -= 1

            if s[e] == ".":
                cnts += 1

            if cnts <= k:
                return True

        return False

    lo, hi = 0, len(s)

    while lo < hi:
        mid = (lo + hi + 1) // 2

        if can(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)


if __name__ == "__main__":
    solve()
