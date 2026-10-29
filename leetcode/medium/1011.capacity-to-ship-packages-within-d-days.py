#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        def can(w):
            d = 0
            cur_w = 0

            for weight in weights:
                if cur_w + weight > w:
                    d += 1
                    cur_w = weight
                else:
                    cur_w += weight

                if d > days:
                    break

            if cur_w != 0:
                d += 1

            return d <= days

        while lo < hi:
            mid = (lo + hi) // 2

            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


# @lc code=end
