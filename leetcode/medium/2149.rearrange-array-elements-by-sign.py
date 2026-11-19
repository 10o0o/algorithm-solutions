#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        negatives = []
        positives = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)

        ans = []

        for i in range(len(nums) // 2):
            ans.append(positives[i])
            ans.append(negatives[i])

        return ans


# @lc code=end
