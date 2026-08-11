# AT ABC453 A
# https://atcoder.jp/contests/abc453/tasks/abc453_a

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    s = input()
    i = 0

    while i < n:
        if s[i] != "o":
            break

        i += 1

    print(s[i:])


if __name__ == "__main__":
    solve()
