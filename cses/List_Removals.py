# List Removals
# https://cses.fi/problemset/task/1749/

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input().strip())
    x = list(map(int, input().split()))
    p = list(map(int, input().split()))

    tl = 1
    while tl < n:
        tl <<= 1

    tree = [0] * (tl * 2)

    for i in range(n):
        tree[i + tl] = 1

    for i in range(tl - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    def query(v):
        node = 1

        while node < tl:
            if tree[node * 2] >= v:
                node = node * 2
            else:
                v -= tree[node * 2]
                node = node * 2 + 1

        return node - tl

    def update(node, v):
        node += tl
        tree[node] += v

        while node:
            node //= 2
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

    ans = []

    for v in p:
        i = query(v)
        ans.append(x[i])
        update(i, -1)

    print(*ans, sep=" ")


if __name__ == "__main__":
    solve()
