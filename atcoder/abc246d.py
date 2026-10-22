# D - 2-variable Function
# https://atcoder.jp/contests/abc246/tasks/abc246_d?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    ans = 10**18

    def cal(a):
        a_squared = a * a
        lo, hi = 0, 10**6

        while lo < hi:
            b = (lo + hi) // 2
            x = (a + b) * (a_squared + b * b)
            if x >= n:
                hi = b
            else:
                lo = b + 1

        b = hi
        return (a + b) * (a_squared + b * b)

    for a in range(10**6):
        ans = min(ans, cal(a))

    print(ans)


if __name__ == "__main__":
    solve()
