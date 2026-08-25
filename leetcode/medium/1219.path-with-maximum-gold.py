#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        def dfs(x, y):
            gold = grid[x][y]

            grid[x][y] = 0

            best = 0

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if grid[nx][ny] == 0:
                    continue

                best = max(best, dfs(nx, ny))

            grid[x][y] = gold

            return gold + best

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue

                ans = max(ans, dfs(i, j))

        return ans


# @lc code=end
