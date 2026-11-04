#
# @lc app=leetcode id=2592 lang=python3
#
# [2592] Maximize Greatness of an Array
#

# @lc code=start
class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        i = 0

        for j in range(n):
            while i < n and nums[i] <= nums[j]:
                i += 1

            if i >= n:
                break

            ans += 1
            i += 1

        return ans


# @lc code=end
