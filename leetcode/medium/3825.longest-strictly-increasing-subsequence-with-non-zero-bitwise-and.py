#
# @lc app=leetcode id=3825 lang=python3
#
# [3825] Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        ans = 0

        for bit in range(31):
            lis = []

            for num in nums:
                if num & (1 << bit) == 0:
                    continue

                idx = bisect_left(lis, num)

                if idx == len(lis):
                    lis.append(num)
                else:
                    lis[idx] = num

            ans = max(ans, len(lis))

        return ans


# @lc code=end
