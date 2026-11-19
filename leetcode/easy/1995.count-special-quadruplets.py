#
# @lc app=leetcode id=1995 lang=python3
#
# [1995] Count Special Quadruplets
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        nums.sort()
        s = set(nums)
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] + nums[k]) in s:
                        ans += 1

        return ans


# @lc code=end
