#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start
class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        ans = [0] * len(queries)

        for i, (val, index) in enumerate(queries):
            before_num = nums[index]
            before_even = nums[index] % 2 == 0
            nums[index] += val
            after_even = nums[index] % 2 == 0

            if before_even and after_even:
                even_sum += val
            elif before_even and not after_even:
                even_sum -= before_num
            elif not before_even and after_even:
                even_sum += nums[index]

            ans[i] = even_sum

        return ans


# @lc code=end
