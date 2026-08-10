#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#

# @lc code=start
import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm(a, b)
        MOD = 1_000_000_007
        left = 1
        right = n * min(a, b)

        def count_nth(value):
            return value // a + value // b - value // lcm

        while left < right:
            mid = (left + right) // 2
            cal_n = count_nth(mid)

            if cal_n >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD


# @lc code=end
