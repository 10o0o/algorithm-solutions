#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        arr = [0] * n
        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i - 1] ^ pref[i]

        return arr


# @lc code=end
