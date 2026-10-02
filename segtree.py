INF = float("inf")


class Segtree:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        self.tree = [INF] * (2 * n)

        for i in range(n):
            self.tree[i + n] = arr[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, idx, v):
        tree_idx = idx + self.n
        self.tree[tree_idx] = v

        while tree_idx > 1:
            tree_idx //= 2
            self.tree[tree_idx] = min(
                self.tree[tree_idx * 2], self.tree[tree_idx * 2 + 1]
            )

    def query(self, left, right):
        left += self.n
        right += self.n
        res = INF

        while left <= right:
            if left % 2 == 1:
                res = min(res, self.tree[left])
                left += 1

            if right % 2 == 0:
                res = min(res, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return res


arr = [5, 2, 7, 1, 4]
seg = Segtree(arr)

print(seg.query(0, 4))
seg.update(3, 6)
print(seg.query(0, 4))
print(seg.query(3, 3))
