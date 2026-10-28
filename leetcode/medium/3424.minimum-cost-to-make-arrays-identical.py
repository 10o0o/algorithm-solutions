#
# @lc app=leetcode id=3424 lang=python3
#
# [3424] Minimum Cost to Make Arrays Identical
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minCost(self, arr: list[int], brr: list[int], k: int) -> int:
        n = len(arr)
        sa = sorted(arr)
        sb = sorted(brr)
        matching = defaultdict(int)
        total = 0

        for i in range(n):
            matching[(sa[i], sb[i])] += 1

        for i in range(n):
            if matching[(arr[i], brr[i])] == 0:
                total += k
                break

        for i in range(n):
            total += abs(sa[i] - sb[i])

        total_origin = 0

        for i in range(n):
            total_origin += abs(arr[i] - brr[i])

        return min(total, total_origin)


# @lc code=end
