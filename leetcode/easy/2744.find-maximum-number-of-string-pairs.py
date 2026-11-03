#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        ws = set(words)
        ans = 0

        for word in words:
            print(word[::-1])
            if word == word[::-1]:
                continue

            if word[::-1] in ws:
                ans += 1

        return ans // 2


# @lc code=end
