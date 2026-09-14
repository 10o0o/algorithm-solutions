#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]

            if b + c > a:
                return a + b + c

        return 0


# @lc code=end
