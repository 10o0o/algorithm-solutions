#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        k = 1

        while k * (k + 1) // 2 <= n:
            rest = n - k * (k - 1) // 2

            if rest % k == 0:
                ans += 1

            k += 1

        return ans


# @lc code=end
