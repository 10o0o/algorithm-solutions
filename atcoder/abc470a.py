# AT ABC470 A
# https://atcoder.jp/contests/abc470/tasks/abc470_a

import sys

input = sys.stdin.readline


def solve() -> None:
    N = int(input())

    for i in range(1, N + 1):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    solve()
