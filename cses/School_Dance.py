# School Dance
# https://cses.fi/problemset/task/1696

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m, k = map(int, input().split())

    b_to_g = [[] for _ in range(n + 1)]
    g_to_b = [[] for _ in range(m + 1)]

    for _ in range(k):
        b, g = map(int, input().split())
        b_to_g[b].append(g)
        g_to_b[g].append(b)

    matched_boy = [0] * (m + 1)
    visited = [False] * (m + 1)
    success_count = 0

    def dfs(b):
        for g in b_to_g[b]:
            if visited[g]:
                continue

            visited[g] = True

            if matched_boy[g] == 0 or dfs(matched_boy[g]):
                matched_boy[g] = b
                return True

        return False

    for b in range(1, n + 1):
        visited = [False] * (m + 1)

        if dfs(b):
            success_count += 1

    print(success_count)
    for g in range(1, m + 1):
        if matched_boy[g] != 0:
            print(f"{matched_boy[g]} {g}")


if __name__ == "__main__":
    solve()
