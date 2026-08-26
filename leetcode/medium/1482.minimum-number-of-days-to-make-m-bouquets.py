#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        day_map = defaultdict(list)

        for i, day in enumerate(bloomDay):
            day_map[day].append(i)

        uf = UnionFind(n)
        active = [False] * n
        bouquets = 0

        for day in sorted(day_map):
            for i in day_map[day]:
                active[i] = True
                bouquets += 1 // k

                if i > 0 and active[i - 1]:
                    a = uf.find(i)
                    b = uf.find(i - 1)

                    if a != b:
                        bouquets -= uf.size[a] // k
                        bouquets -= uf.size[b] // k

                        uf.union(a, b)

                        root = uf.find(a)
                        bouquets += uf.size[root] // k

                if i + 1 < n and active[i + 1]:
                    a = uf.find(i)
                    b = uf.find(i + 1)

                    if a != b:
                        bouquets -= uf.size[a] // k
                        bouquets -= uf.size[b] // k

                        uf.union(a, b)

                        root = uf.find(a)
                        bouquets += uf.size[root] // k

            if bouquets >= m:
                return day

        return -1


# @lc code=end
