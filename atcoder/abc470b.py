# AT ABC470 B
# https://atcoder.jp/contests/abc470/tasks/abc470_b

import sys
from collections import Counter

input = sys.stdin.readline


def solve() -> None:
    N = int(input())
    C = list(map(int, input().split(" ")))

    counts = Counter(C)
    print(N - max(counts.values()))


if __name__ == "__main__":
    solve()
