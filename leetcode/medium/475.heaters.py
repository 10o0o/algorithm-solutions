#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()

        ans = 0

        for house in houses:
            i = bisect_left(heaters, house)

            left = float("inf")
            right = float("inf")

            if i > 0:
                left = house - heaters[i - 1]

            if i < len(heaters):
                right = heaters[i] - house

            radius = min(left, right)
            ans = max(ans, radius)

        return ans


# @lc code=end
