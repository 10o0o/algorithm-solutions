# AT ABC378 E?LANG=EN
# https://atcoder.jp/contests/abc378/tasks/abc378_e?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    for i in range(n):
        a[i] %= m

    a.reverse()


if __name__ == "__main__":
    solve()
