#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = -1

        while n:
            if last_bit == (n % 2):
                return False

            last_bit = n % 2
            n >>= 1

        return True


# @lc code=end
