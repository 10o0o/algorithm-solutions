#
# @lc app=leetcode id=2091 lang=python3
#
# [2091] Removing Minimum and Maximum From Array
#

# @lc code=start
class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = sorted((nums.index(min(nums)), nums.index(max(nums))))
        return min(right + 1, n - left, n - right + left + 1)


# @lc code=end
