#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#

# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        res_arr = []
        n = len(s)

        for i in range(n):
            if not res_arr:
                res_arr.append(s[i])
                continue

            if s[i].isdigit():
                if not res_arr[-1].isdigit():
                    res_arr.pop()
                else:
                    res_arr.append(s[i])
            else:
                res_arr.append(s[i])

        return "".join(res_arr)


# @lc code=end
