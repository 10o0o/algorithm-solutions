# AT ABC381 D?LANG=EN
# https://atcoder.jp/contests/abc381/tasks/abc381_d?lang=en

import sys
from collections import Counter

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    a = list(map(int, input().split(" ")))

    mn = 0
    mx = n // 2

    def can(l):
        l *= 2
        cnts = Counter(a[:l])
        no_cond_nums = set()
        for k, v in cnts.items():
            if v != 2:
                no_cond_nums.add(k)

        def judge(s, e):
            if no_cond_nums:
                return False

            for i in range(s, e + 1, 2):
                if a[i] != a[i + 1]:
                    return False

            return True

        if judge(0, l - 1):
            return True

        for i in range(1, len(a) - l + 1):
            cnts[a[i - 1]] -= 1
            cnts[a[i + l - 1]] += 1

            if cnts[a[i - 1]] in (0, 2):
                no_cond_nums.discard(a[i - 1])
            else:
                no_cond_nums.add(a[i - 1])

            if cnts[a[i + l - 1]] in (0, 2):
                no_cond_nums.discard(a[i + l - 1])
            else:
                no_cond_nums.add(a[i + l - 1])

            if judge(i, i + l - 1):
                return True

        return False

    while mn < mx:
        mid = (mn + mx + 1) // 2

        if can(mid):
            mn = mid
        else:
            mx = mid - 1

    print(mn * 2)


if __name__ == "__main__":
    solve()
