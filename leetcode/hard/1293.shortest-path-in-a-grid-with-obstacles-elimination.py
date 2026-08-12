#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

        q = deque([[0, 0, 0, 0]])
        visited[0][0][0] = 1
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        min_walked = -1

        while q:
            [eliminated, walked, i, j] = q.popleft()

            if i == n - 1 and j == m - 1:
                if min_walked == -1:
                    min_walked = walked
                else:
                    min_walked = min(min_walked, walked)

                continue

            for d in range(4):
                mi = i + dx[d]
                mj = j + dy[d]

                if mi < 0 or mj < 0 or mi >= n or mj >= m:
                    continue

                new_eliminated = eliminated + (grid[mi][mj] == 1)

                if new_eliminated > k:
                    continue

                if visited[new_eliminated][mi][mj] == 1:
                    continue

                visited[new_eliminated][mi][mj] = 1

                q.append([new_eliminated, walked + 1, mi, mj])

        return min_walked


# @lc code=end
