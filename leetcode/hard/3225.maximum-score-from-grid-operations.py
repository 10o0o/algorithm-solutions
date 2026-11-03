#
# @lc app=leetcode id=3225 lang=python3
#
# [3225] Maximum Score From Grid Operations
#

# @lc code=start
class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        prefix = [[0] * (n + 1) for _ in range(n)]

        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        print(f"prefix: {prefix}")

        return 0


# @lc code=end
