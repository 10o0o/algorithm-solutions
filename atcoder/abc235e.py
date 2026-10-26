# AT ABC235 E?LANG=EN
# https://atcoder.jp/contests/abc235/tasks/abc235_e?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m, q = map(int, input().split())
    infos = [(*map(int, input().split()), 0) for _ in range(m)]
    infos.extend([(*map(int, input().split()), 1, i) for i in range(q)])

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

    infos.sort(key=lambda info: info[2])
    ans = ["No"] * q

    for info in infos:
        if info[3] == 0:
            union(info[0], info[1])
        elif info[3] == 1:
            if find(info[0]) != find(info[1]):
                ans[info[4]] = "Yes"

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
