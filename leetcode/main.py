from functools import cache


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        INF = 1234567890123

        # d는 오 밑 왼 위
        @cache
        def dp(i, j, turns, direction):
            if i == n - 1 and j == m - 1:
                return v

            return INF

        ans = min(dp(0, 0, 0, 0, 0), dp(0, 0, 0, 0, 1))

        if ans == INF:
            return -1

        return ans
