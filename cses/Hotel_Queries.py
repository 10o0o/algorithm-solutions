# Hotel Queries
# https://cses.fi/problemset/task/1143/

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    r = list(map(int, input().split()))

    tl = 1
    while tl < n:
        tl <<= 1

    tree = [0] * (tl * 2)

    for i in range(n):
        tree[tl + i] = h[i]

    for i in range(tl - 1, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])

    def query(p):
        node = 1
        if tree[node] < p:
            return 0

        while node < tl:
            if tree[node * 2] >= p:
                node = node * 2
            else:
                node = node * 2 + 1

        return node - tl + 1

    def update(node, v):
        node += tl - 1
        tree[node] += v

        while node:
            p = node // 2
            tree[p] = max(tree[p * 2], tree[p * 2 + 1])

            node = p

    ans = []
    for p in r:
        node = query(p)
        ans.append(node)

        if node:
            update(node, -p)

    print(*ans, sep=" ")


if __name__ == "__main__":
    solve()
