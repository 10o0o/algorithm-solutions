#
# @lc app=leetcode id=4006 lang=python3
#
# [4006] Count Valid Prefixes
#

# @lc code=start
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(1):
            for j in range(i, n):
                cnts = [0, 0]

                for k in range(i, j + 1):
                    if s[k] == "1":
                        cnts[0] += 1
                    else:
                        cnts[1] += 1

                diffs = cnts[0] - cnts[1]
                diffs = abs(diffs)

                if diffs <= 1:
                    ans += 1

        return ans


# @lc code=end
