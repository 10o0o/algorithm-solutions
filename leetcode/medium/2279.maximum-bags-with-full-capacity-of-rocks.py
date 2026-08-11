#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#

# @lc code=start
class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        left_capacity = capacity.copy()

        for i, rock in enumerate(rocks):
            left_capacity[i] -= rock

        sorted_capacity = sorted(left_capacity)

        for counts, sc in enumerate(sorted_capacity):
            additionalRocks -= sc

            if additionalRocks < 0:
                return counts

        return len(sorted_capacity)


# @lc code=end
