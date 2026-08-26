#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)

        return sum(c.islower() and c.upper() in chars for c in chars)


# @lc code=end
