#
# @lc app=leetcode id=2930 lang=python3
#
# [2930] Number of Strings Which Can Be Rearranged to Contain Substring
#

# @lc code=start


class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7

        return (
            pow(26, n, MOD)
            - 3 * pow(25, n, MOD)
            - n * pow(25, n - 1, MOD)
            + 3 * pow(24, n, MOD)
            + 2 * n * pow(24, n - 1, MOD)
            - pow(23, n, MOD)
            - n * pow(23, n - 1, MOD)
        ) % MOD


# @lc code=end
