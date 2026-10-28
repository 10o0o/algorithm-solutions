#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)

        l, r = 0, 0
        counts = Counter(s[0])
        ans = 1

        while l < n and r < n:
            while r + 1 < n and counts[s[r + 1]] <= 1:
                counts[s[r + 1]] += 1
                r += 1

            ans = max(ans, r - l + 1)

            counts[s[l]] -= 1
            l += 1
            if r < l:
                r = l
                if l < n:
                    counts = Counter(s[l])

        return ans


# @lc code=end
