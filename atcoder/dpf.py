# AT DP F?LANG=EN
# https://atcoder.jp/contests/dp/tasks/dp_f?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    s = input().strip()
    t = input().strip()

    n, m = len(s), len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        previous = dp[i - 1]
        current = dp[i]
        char = s[i - 1]

        for j in range(1, m + 1):
            if char == t[j - 1]:
                current[j] = previous[j - 1] + 1
            else:
                up = previous[j]
                left = current[j - 1]
                current[j] = max(up, left)

    answer = []
    i, j = n, m

    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            answer.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("".join(reversed(answer)))


if __name__ == "__main__":
    solve()
