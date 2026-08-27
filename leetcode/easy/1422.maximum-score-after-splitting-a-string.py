#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = s.count("1")
        ans = 0

        for c in s[:-1]:
            if c == "0":
                left_zeros += 1
            else:
                right_ones -= 1

            ans = max(ans, left_zeros + right_ones)

        return ans


# @lc code=end
