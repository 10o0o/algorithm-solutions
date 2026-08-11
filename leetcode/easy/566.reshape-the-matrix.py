#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n, m = len(mat), len(mat[0])

        if n * m != r * c:
            return mat

        reshaped_mat = [[0] * c for _ in range(r)]

        for a in range(n):
            for b in range(m):
                v = mat[a][b]
                cal = a * m + b
                i, j = cal // c, cal % c
                reshaped_mat[i][j] = v

        return reshaped_mat


# @lc code=end
