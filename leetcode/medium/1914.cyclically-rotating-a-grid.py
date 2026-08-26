#
# @lc app=leetcode id=1914 lang=python3
#
# [1914] Cyclically Rotating a Grid
#

# @lc code=start
class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n, m = len(grid), len(grid[0])

        for layer in range(min(n, m) // 2):
            top = left = layer
            bottom = n - 1 - layer
            right = m - 1 - layer

            cells = []

            for j in range(left, right):
                cells.append((top, j))

            for i in range(top, bottom):
                cells.append((i, right))

            for j in range(right, left, -1):
                cells.append((bottom, j))

            for i in range(bottom, top, -1):
                cells.append((i, left))

            values = [grid[i][j] for i, j in cells]

            shift = k % len(values)

            for idx, (i, j) in enumerate(cells):
                grid[i][j] = values[(idx + shift) % len(values)]

        return grid


# @lc code=end
