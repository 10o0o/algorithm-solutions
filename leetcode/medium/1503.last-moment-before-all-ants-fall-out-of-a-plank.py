#
# @lc app=leetcode id=1503 lang=python3
#
# [1503] Last Moment Before All Ants Fall Out of a Plank
#

# @lc code=start
class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        merged = left + [n - v for v in right]
        return max(merged)


# @lc code=end
