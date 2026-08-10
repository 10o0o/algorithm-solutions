#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)

        max_prefix = [0] * (n + 1)
        min_suffix = [1e9] * (n + 1)

        for i in range(n):
            max_prefix[i + 1] = max(max_prefix[i], nums[i])

        for i in range(n - 1, -1, -1):
            min_suffix[i] = min(min_suffix[i + 1], nums[i])

        for i in range(1, n):
            if max_prefix[i] <= min_suffix[i]:
                return i

        return 0


# @lc code=end
