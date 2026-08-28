#
# @lc app=leetcode id=828 lang=python3
#
# [828] Count Unique Characters of All Substrings of a Given String
#

# @lc code=start


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)

        indices = {}

        for i, c in enumerate(s):
            if c not in indices:
                indices[c] = [-1]

            indices[c].append(i)

        poses = indices.values()
        ans = 0

        for pos in poses:
            pos.append(n)

            for i in range(1, len(pos) - 1):
                ans += (pos[i] - pos[i - 1]) * (pos[i + 1] - pos[i])

        return ans


# @lc code=end
