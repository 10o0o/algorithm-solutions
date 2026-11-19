#
# @lc app=leetcode id=2585 lang=python3
#
# [2585] Number of Ways to Earn Points
#

# @lc code=start


class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        MOD = 10**9 + 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            for score in range(target, -1, -1):
                for k in range(1, min(count, score // marks) + 1):
                    dp[score] += dp[score - k * marks]

                dp[score] %= MOD

        return dp[target]


# @lc code=end
