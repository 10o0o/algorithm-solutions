#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

from bisect import bisect_right


class Solution:
    def maximumCoins(self, coins: list[list[int]], k: int) -> int:
        coins.sort()
        starts = [l for l, r, c in coins]

        prefix = [0]
        for l, r, c in coins:
            prefix.append(prefix[-1] + (r - l + 1) * c)

        def get_sum(x):
            i = bisect_right(starts, x) - 1

            if i < 0:
                return 0

            l, r, c = coins[i]
            return prefix[i] + (min(x, r) - l + 1) * c

        ans = 0

        for l, r, c in coins:
            for start in (l, r - k + 1):
                total = get_sum(start + k - 1) - get_sum(start - 1)
                ans = max(ans, total)

        return ans


# @lc code=end
