# D - Count Interval
# https://atcoder.jp/contests/abc233/tasks/abc233_d?lang=en

import sys
from collections import defaultdict

input = sys.stdin.readline


def solve() -> None:
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    counts = defaultdict(int)
    counts[0] += 1

    ans = 0
    acc = 0

    for value in values:
        acc += value
        find_v = acc - k
        ans += counts[find_v]
        counts[acc] += 1

    print(ans)


if __name__ == "__main__":
    solve()
