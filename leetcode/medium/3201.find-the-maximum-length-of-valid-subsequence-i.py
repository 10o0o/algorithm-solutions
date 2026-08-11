#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#

# @lc code=start
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        even, odd = 0, 0
        last = nums[0] % 2
        alternate = 1

        for num in nums:
            parity = num % 2

            if parity == 0:
                even += 1
            else:
                odd += 1

        for num in nums[1:]:
            parity = num % 2

            if parity != last:
                alternate += 1
                last = parity

        return max(even, odd, alternate)


# @lc code=end
