#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        best = {}
        ans = -1

        for num in nums:
            s = sum(map(int, str(num)))

            if s in best:
                ans = max(ans, best[s] + num)

            best[s] = max(best.get(s, 0), num)

        return ans


# @lc code=end
