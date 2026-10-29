#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        prefix = 1
        sum = 0
        while n:
            sum += prefix * (n % 10)
            prefix *= -1
            n //= 10

        if prefix == 1:
            sum *= -1

        return sum


# @lc code=end
