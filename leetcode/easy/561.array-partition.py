#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        ans = 0

        for i in range(1, n, 2):
            ans += nums[i]

        return ans


# @lc code=end
