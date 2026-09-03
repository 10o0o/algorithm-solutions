#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            memo = [False] * n

            for j in range(n):
                if matrix[i][j] < 1 or matrix[i][j] > n or memo[matrix[i][j] - 1]:
                    return False

                memo[matrix[i][j] - 1] = True

        for j in range(n):
            memo = [False] * n

            for i in range(n):
                if matrix[i][j] < 1 or matrix[i][j] > n or memo[matrix[i][j] - 1]:
                    return False

                memo[matrix[i][j] - 1] = True

        return True


# @lc code=end
