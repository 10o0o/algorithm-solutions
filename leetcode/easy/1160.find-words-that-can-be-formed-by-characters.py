#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= chars_count[c] for c in word_count):
                ans += len(word)

        return ans


# @lc code=end
