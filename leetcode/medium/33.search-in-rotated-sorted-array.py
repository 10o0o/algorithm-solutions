#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n_to_i = {num: i for i, num in enumerate(nums)}

        if n_to_i.get(target) is None:
            return -1

        v = n_to_i[target]

        # if v < 0:
        # v += len(nums)

        return v


# @lc code=end
