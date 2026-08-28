#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start


from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        nums = [num for row in grid for num in row]
        counts = Counter(nums)

        repeated = -1
        missing = -1

        for num in range(1, len(nums) + 1):
            if counts[num] == 2:
                repeated = num
            elif counts[num] == 0:
                missing = num

        return [repeated, missing]


# @lc code=end
