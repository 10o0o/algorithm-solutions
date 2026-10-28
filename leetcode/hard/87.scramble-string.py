#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def dfs(a, b):
            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for k in range(1, n):
                # 교환하지 않는 경우
                if dfs(a[:k], b[:k]) and dfs(a[k:], b[k:]):
                    return True

                # 교환하는 경우
                if dfs(a[:k], b[n - k :]) and dfs(a[k:], b[: n - k]):
                    return True

            return False

        return dfs(s1, s2)


# @lc code=end
