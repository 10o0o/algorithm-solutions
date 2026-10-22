# D - Online games
# https://atcoder.jp/contests/abc221/tasks/abc221_d?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    periods = [tuple(map(int, input().split())) for _ in range(n)]
    dates = set()
    for s, e in periods:
        dates.add(s)
        dates.add(s + e)

    dates = sorted(dates)
    dates_flag = [0] * len(dates)
    dates_idx_map = {date: index for index, date in enumerate(dates)}

    for s, e in periods:
        dates_flag[dates_idx_map[s]] += 1
        dates_flag[dates_idx_map[s + e]] -= 1

    for i in range(1, len(dates)):
        dates_flag[i] += dates_flag[i - 1]

    ans = [0] * (n + 1)

    for i in range(len(dates_flag) - 1):
        cur_counts = dates_flag[i]
        ans[cur_counts] += dates[i + 1] - dates[i]

    print(*ans[1:], sep=" ")


if __name__ == "__main__":
    solve()
