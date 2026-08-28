#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)

        sum = 0

        for i in range(n):
            sum += mat[i][i]
            sum += mat[n - 1 - i][i]

        if n % 2 == 1:
            sum -= mat[n // 2][n // 2]

        return sum


# @lc code=end
