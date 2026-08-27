#
# @lc app=leetcode id=2826 lang=python3
#
# [2826] Sorting Three Groups
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        dp = [0] * 4

        for num in nums:
            dp[num] = 1 + max(dp[1 : num + 1])

        return len(nums) - max(dp)


# @lc code=end
