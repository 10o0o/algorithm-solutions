#
# @lc app=leetcode id=2857 lang=python3
#
# [2857] Count Pairs of Points With Distance k
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        counts = defaultdict(int)
        ans = 0

        for x, y in coordinates:
            for a in range(k + 1):
                b = k - a

                prev_x = x ^ a
                prev_y = y ^ b

                ans += counts[(prev_x, prev_y)]

            counts[(x, y)] += 1

        return ans


# @lc code=end
