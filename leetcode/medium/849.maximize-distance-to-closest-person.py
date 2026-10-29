#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        last = -1
        ans = -1

        for i, p in enumerate(seats):
            if p == 0:
                continue

            if last == -1:
                ans = i
            else:
                ans = max(ans, (i - last) // 2)

            last = i

        ans = max(ans, len(seats) - 1 - last)

        return ans


# @lc code=end
