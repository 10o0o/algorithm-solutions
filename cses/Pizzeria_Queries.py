# Pizzeria Queries
# https://cses.fi/problemset/task/2206/

import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        tree = [0] * (n * 2)

        for i in range(n):
            tree[i + n] = arr[i]

        for i in range(n - 1, 0, -1):
            tree[i] = min(tree[i * 2], tree[i * 2 + 1])

        self.tree = tree

    def update(self, node, v):
        node += self.n
        self.tree[node] = v

        while node:
            parent = node // 2
            self.tree[parent] = min(self.tree[parent * 2], self.tree[parent * 2 + 1])
            node = parent

    def query(self, left, right):
        left += self.n
        right += self.n
        result = float("inf")

        while left <= right:
            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1

            if right % 2 == 0:
                result = min(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result


def solve() -> None:
    n, q = map(int, input().split())
    p = list(map(int, input().split()))

    a = [e + i for i, e in enumerate(p)]
    b = [e + (n - 1 - i) for i, e in enumerate(p)]

    st = SegmentTree(a)
    rst = SegmentTree(b)

    ans = []

    for _ in range(q):
        commands = list(map(int, input().split()))

        if commands[0] == 1:
            i, v = commands[1], commands[2]
            i -= 1
            st.update(i, v + i)
            rst.update(i, v + (n - 1 - i))
        elif commands[0] == 2:
            i = commands[1]
            i -= 1
            v = min(st.query(i, n - 1) - i, rst.query(0, i) - (n - 1 - i))
            ans.append(v)

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
