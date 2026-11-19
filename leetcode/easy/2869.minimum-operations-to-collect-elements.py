#
# @lc app=leetcode id=2869 lang=python3
#
# [2869] Minimum Operations to Collect Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        remain = sum([1 << i for i in range(1, k + 1)])
        cnts = 0

        while remain:
            bit = 1 << nums.pop()
            if remain & bit:
                remain -= bit
            cnts += 1

        return cnts


# @lc code=end
