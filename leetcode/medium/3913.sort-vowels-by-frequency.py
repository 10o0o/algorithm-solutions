#
# @lc app=leetcode id=3913 lang=python3
#
# [3913] Sort Vowels by Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"

        counts = Counter(c for c in s if c in vowels)
        ordered = sorted(counts, key=lambda c: -counts[c])

        chars = iter("".join(c * counts[c] for c in ordered))
        return "".join(next(chars) if c in vowels else c for c in s)


# @lc code=end
