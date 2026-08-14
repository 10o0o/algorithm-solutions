#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        sum = (maxChoosableInteger + 1) * maxChoosableInteger // 2
        if desiredTotal > sum:
            return False

        if desiredTotal <= maxChoosableInteger:
            return True

        @cache
        def dfs(used_mask, remaining):
            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << (number - 1)

                if used_mask & bit:
                    continue

                if number >= remaining:
                    return True

                if not dfs(used_mask | bit, remaining - number):
                    return True

            return False

        return dfs(0, desiredTotal)


# @lc code=end
