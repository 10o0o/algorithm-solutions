#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start


import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        t = grid[0][0]
        n, m = len(grid), len(grid[0])
        heap = [(t, 0, 0)]
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        while heap:
            weight, i, j = heapq.heappop(heap)
            t = max(t, weight)
            if i == n - 1 and j == m - 1:
                return t

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                mi, mj = i + di, j + dj

                if (
                    mi >= 0
                    and mj >= 0
                    and mi < n
                    and mj < m
                    and visited[mi][mj] == False
                ):
                    visited[mi][mj] = True
                    heapq.heappush(heap, (grid[mi][mj], mi, mj))

        return 0


# @lc code=end
