#
# @lc app=leetcode id=3864 lang=python3
#
# [3864] Minimum Cost to Partition a Binary String
#

# @lc code=start
from functools import cache


class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        @cache
        def calculate(x):
            if len(x) == 1:
                return flatCost if x == "0" else encCost

            X = x.count("1")
            v = flatCost if X == 0 else encCost * X * len(x)

            if len(x) % 2 == 0:
                v = min(v, calculate(x[: len(x) // 2]) + calculate(x[len(x) // 2 :]))

            return v

        return calculate(s)


# @lc code=end
