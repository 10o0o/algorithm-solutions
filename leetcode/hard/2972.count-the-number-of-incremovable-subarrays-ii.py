#
# @lc app=leetcode id=2972 lang=python3
#
# [2972] Count the Number of Incremovable Subarrays II
#

# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        n = len(nums)

        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1

        if left == n - 1:
            return n * (n + 1) // 2

        ans = left + 2

        right = n - 1

        while right == n - 1 or nums[right] < nums[right + 1]:
            while left >= 0 and nums[left] >= nums[right]:
                left -= 1

            ans += left + 2
            right -= 1

        return ans


# @lc code=end
