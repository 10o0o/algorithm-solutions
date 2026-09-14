#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] < target:
                i += 1
            else:
                break

        return i


# @lc code=end
