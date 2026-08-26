#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#

# @lc code=start


from collections import defaultdict


class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        n, m = len(matrix), len(matrix[0])
        values = defaultdict(list)

        for i in range(n):
            for j in range(m):
                values[matrix[i][j]].append((i, j))

        row_rank = [0] * n
        col_rank = [0] * m

        answer = [[0] * m for _ in range(n)]

        for value in sorted(values):
            cells = values[value]

            parent = {}

            def find(x):
                if x not in parent:
                    parent[x] = x

                if parent[x] != x:
                    parent[x] = find(parent[x])

                return parent[x]

            def union(a, b):
                a = find(a)
                b = find(b)

                if a != b:
                    parent[b] = a

            for i, j in cells:
                union(i, n + j)

            groups = defaultdict(list)

            for i, j in cells:
                root = find(i)
                groups[root].append((i, j))

            updates = []

            for group in groups.values():
                rank = 1

                for i, j in group:
                    rank = max(
                        rank,
                        row_rank[i] + 1,
                        col_rank[j] + 1,
                    )

                for i, j in group:
                    answer[i][j] = rank
                    updates.append((i, j, rank))

            for i, j, rank in updates:
                row_rank[i] = max(row_rank[i], rank)
                col_rank[j] = max(col_rank[j], rank)

        return answer


# @lc code=end
