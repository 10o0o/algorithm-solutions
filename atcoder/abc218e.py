# AT ABC218 E?LANG=EN
# https://atcoder.jp/contests/abc218/tasks/abc218_e?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    infos = [tuple(map(int, input().split())) for _ in range(m)]
    infos.sort(key=lambda info: info[2])

    parent = [i for i in range(n + 1)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return

        (mn, mx) = (min(root_x, root_y), max(root_x, root_y))
        parent[mx] = mn

    ans = 0

    for a, b, c in infos:
        if find(a) != find(b):
            union(a, b)
            continue

        ans += max(0, c)

    print(ans)


if __name__ == "__main__":
    solve()
