#
# @lc app=leetcode id=3181 lang=python3
#
# [3181] Maximum Total Reward Using Operations II
#

# @lc code=start
class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        values = sorted(set(rewardValues))

        dp = 1

        for v in values:
            dp |= (dp & ((1 << v) - 1)) << v

        return dp.bit_length() - 1


# @lc code=end
