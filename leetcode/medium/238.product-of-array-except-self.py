#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        multiply_all = 1
        zero_index = -1
        zero_cnts = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero_cnts += 1
                zero_index = i
            else:
                multiply_all *= num

        ans = [0] * n

        if zero_cnts >= 2:
            return ans
        elif zero_cnts == 1:
            ans[zero_index] = multiply_all
            return ans

        ans = [multiply_all] * n

        for i in range(n):
            ans[i] //= nums[i]

        return ans


# @lc code=end
