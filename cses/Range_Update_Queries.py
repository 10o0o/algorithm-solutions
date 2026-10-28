# Range Update Queries
# https://cses.fi/problemset/task/1651/

import sys

input = sys.stdin.readline


def solve() -> None:
    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    tl = 1
    while tl < n:
        tl <<= 1

    tree = [0] * (tl * 2)

    for i in range(n):
        tree[i + tl] = x[i]

    ans = []

    def query(p):
        node = 1
        left, right = 0, tl - 1
        total = 0

        while left < right:
            total += tree[node]
            mid = (left + right) // 2

            if p <= mid:
                node = node * 2
                right = mid
            else:
                node = node * 2 + 1
                left = mid + 1

        return total + tree[node]

    def update(s, e, v):
        s += tl
        e += tl

        while s <= e:
            if s % 2 == 1:
                tree[s] += v
                s += 1

            if e % 2 == 0:
                tree[e] += v
                e -= 1

            s //= 2
            e //= 2

    for _ in range(q):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            update(cmd[1] - 1, cmd[2] - 1, cmd[3])
        else:
            ans.append(query(cmd[1] - 1))

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
