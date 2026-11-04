#
# @lc app=leetcode id=2834 lang=python3
#
# [2834] Find the Minimum Possible Sum of a Beautiful Array
#

# @lc code=start
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7

        half = min(n, target // 2)
        rest = n - half

        s1 = half * (half + 1) // 2
        s2 = rest * (2 * target + rest - 1) // 2

        return (s1 + s2) % MOD


# @lc code=end
