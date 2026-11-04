#
# @lc app=leetcode id=3573 lang=python3
#
# [3573] Best Time to Buy and Sell Stock V
#

# @lc code=start
class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        dp = [[-1] * k for _ in range(len(prices))]


# @lc code=end
