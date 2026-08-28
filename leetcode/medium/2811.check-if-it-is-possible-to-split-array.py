#
# @lc app=leetcode id=2811 lang=python3
#
# [2811] Check if it is Possible to Split Array
#

# @lc code=start
class Solution:
    def canSplitArray(self, nums: list[int], m: int) -> bool:
        n = len(nums)

        if n == 1 or n == 2:
            return True

        for i in range(1, n):
            if (nums[i] + nums[i - 1]) >= m:
                return True

        return False


# @lc code=end
