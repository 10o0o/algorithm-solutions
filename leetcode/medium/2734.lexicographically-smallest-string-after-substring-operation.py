#
# @lc app=leetcode id=2734 lang=python3
#
# [2734] Lexicographically Smallest String After Substring Operation
#

# @lc code=start
class Solution:
    def smallestString(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        i = 0

        while i < n and chars[i] == "a":
            i += 1

        if i == n:
            chars[-1] = "z"
            return "".join(chars)

        while i < n and chars[i] != "a":
            chars[i] = chr(ord(chars[i]) - 1)
            i += 1

        return "".join(chars)


# @lc code=end
