# Road Reparation
# https://cses.fi/problemset/task/1675/

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
        if find(a) == find(b):
            continue

        ans += c
        union(a, b)

    is_valid = True
    id = find(1)

    for i in range(2, n + 1):
        if find(i) != id:
            is_valid = False
            break

    if is_valid:
        print(ans)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    solve()
