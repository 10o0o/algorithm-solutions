#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        splited = text.split(" ")
        splited.sort(key=len)
        return " ".join(splited).capitalize()


# @lc code=end
