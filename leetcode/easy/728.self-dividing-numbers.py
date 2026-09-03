#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []

        def judge(num):
            if num == 0:
                return False

            copy = num

            while copy != 0:
                sliced = copy % 10
                copy //= 10

                if sliced == 0 or num % sliced:
                    return False

            return True

        for num in range(left, right + 1):
            if judge(num):
                ans.append(num)

        return ans


# @lc code=end
