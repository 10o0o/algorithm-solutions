# E - Mancala 2
# https://atcoder.jp/contests/abc340/tasks/abc340_e?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    tl = 1
    while tl < n:
        tl <<= 1

    tree = [0] * (tl * 2)
    for i in range(n):
        tree[i + tl] = a[i]

    def query(x):
        node = 1
        left, right = 0, tl - 1
        total = 0

        while left < right:
            total += tree[node]
            mid = (left + right) // 2

            if x <= mid:
                node = node * 2
                right = mid
            else:
                node = node * 2 + 1
                left = mid + 1

        return total + tree[node]

    def update_range(ql, qr, v, node=1, left=0, right=tl - 1):
        if qr < left or right < ql:
            return

        if ql <= left and right <= qr:
            tree[node] += v
            return

        mid = (left + right) // 2
        update_range(ql, qr, v, node * 2, left, mid)
        update_range(ql, qr, v, node * 2 + 1, mid + 1, right)

    for i in b:
        x = query(i)
        v = x // n

        update_range(i, i, -x)

        if v:
            update_range(0, n - 1, v)

        r = x % n

        if r:
            left = (i + 1) % n
            right = (i + r) % n

            queries = []

            if left <= right:
                queries.append((left, right))
            else:
                queries.append((left, n - 1))
                queries.append((0, right))

            for l, r in queries:
                update_range(l, r, 1)

    ans = [query(i) for i in range(n)]
    print(*ans, sep=" ")


if __name__ == "__main__":
    solve()
