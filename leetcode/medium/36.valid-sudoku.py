#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def check_valid(nums):
            s = set()

            for v in nums:
                if v == ".":
                    continue

                if v in s:
                    return False

                s.add(v)

            return True

        for row in board:
            if not check_valid(row):
                return False

        for i in range(len(board)):
            nums = []

            for j in range(9):
                nums.append(board[j][i])

            if not check_valid(nums):
                return False

        for k in range(3):
            for l in range(3):
                nums = []

                for i in range(3):
                    for j in range(3):
                        nums.append(board[i + 3 * k][j + 3 * l])

                if not check_valid(nums):
                    return False

        return True


# @lc code=end
