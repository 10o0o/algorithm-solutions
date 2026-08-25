#
# @lc app=leetcode id=2790 lang=python3
#
# [2790] Maximum Number of Groups With Increasing Length
#

# @lc code=start
class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        usageLimits.sort()

        available = 0
        groups = 0

        for limit in usageLimits:
            available += limit

            if available >= groups + 1:
                available -= groups + 1
                groups += 1

        return groups


# @lc code=end
