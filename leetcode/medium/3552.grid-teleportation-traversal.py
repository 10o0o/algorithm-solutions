#
# @lc app=leetcode id=3552 lang=python3
#
# [3552] Grid Teleportation Traversal
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        n, m = len(matrix), len(matrix[0])

        tp = defaultdict(list)

        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c not in (".", "#"):
                    tp[c].append((i, j))

        costs = [[-1] * m for _ in range(n)]
        costs[0][0] = 0

        used = set()
        dq = deque([(0, 0, 0)])

        while dq:
            cost, i, j = dq.popleft()

            if costs[i][j] != cost:
                continue

            if (i, j) == (n - 1, m - 1):
                return cost

            c = matrix[i][j]

            # 순간이동: 비용 0
            if c in tp and c not in used:
                used.add(c)

                for ni, nj in tp[c]:
                    if costs[ni][nj] == -1 or costs[ni][nj] > cost:
                        costs[ni][nj] = cost
                        dq.appendleft((cost, ni, nj))

            # 일반 이동: 비용 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj

                if not (0 <= ni < n and 0 <= nj < m):
                    continue

                if matrix[ni][nj] == "#":
                    continue

                if costs[ni][nj] == -1 or costs[ni][nj] > cost + 1:
                    costs[ni][nj] = cost + 1
                    dq.append((cost + 1, ni, nj))

        return -1


# @lc code=end
