#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left = 0
        right = max(candies)

        def can_divide(value):
            cnts = 0

            for candy in candies:
                cnts += candy // value

            return cnts >= k

        while left < right:
            mid = (left + right + 1) // 2

            if can_divide(mid):
                left = mid
            else:
                right = mid - 1

        return left


# @lc code=end
