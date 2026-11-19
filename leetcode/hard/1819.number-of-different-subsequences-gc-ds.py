#
# @lc app=leetcode id=1819 lang=python3
#
# [1819] Number of Different Subsequences GCDs
#

# @lc code=start
from math import gcd


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        mx = max(nums)

        exists = [False] * (mx + 1)
        for num in nums:
            exists[num] = True

        answer = 0

        for x in range(1, mx + 1):
            g = 0

            for multiple in range(x, mx + 1, x):
                if exists[multiple]:
                    g = gcd(g, multiple)

                    if g == x:
                        answer += 1
                        break

        return answer


# @lc code=end
