#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        str_nums = [str(num) for num in nums]

        ans = 0

        for str_num in str_nums:
            if len(str_num) % 2 == 0:
                ans += 1

        return ans


# @lc code=end
