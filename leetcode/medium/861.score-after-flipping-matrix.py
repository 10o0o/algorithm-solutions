#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def flip(v):
            return 1 if v == 0 else 0

        def flip_row(i):
            for j in range(m):
                grid[i][j] = flip(grid[i][j])

        def flip_col(j):
            for i in range(n):
                grid[i][j] = flip(grid[i][j])

        for i in range(n):
            if grid[i][0] == 0:
                flip_row(i)

        for j in range(m):
            cnts = [0, 0]

            for i in range(n):
                cnts[grid[i][j]] += 1

            if cnts[0] > cnts[1]:
                flip_col(j)

        def matrix_sum():
            total = 0

            for i in range(n):
                for j in range(m):
                    total += (1 << (m - 1 - j)) * grid[i][j]

            return total

        return matrix_sum()


# @lc code=end
