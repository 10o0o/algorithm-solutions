# Prefix Sum Queries
# https://cses.fi/problemset/task/2166/

import sys

input = sys.stdin.readline


def solve() -> None:
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    prefixes = [0] * (n + 1)
    for i in range(n):
        prefixes[i + 1] = prefixes[i] + x[i]

    tree = [0] * ((n + 1) * 2)

    for i in range(n + 1):
        tree[i + n + 1] = prefixes[i]

    for i in range(n, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])

    ans = []

    for _ in range(q):
        a, b, c = map(int, input().split())

        if a == 1:



if __name__ == "__main__":
    solve()
