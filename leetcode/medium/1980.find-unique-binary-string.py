#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        cnums = sorted([int(num, 2) for num in nums])

        if cnums[0] != 0:
            return "0" * n

        for i in range(len(cnums) - 1):
            if (cnums[i + 1] - cnums[i]) != 1:
                return bin(cnums[i] + 1)[2:].zfill(n)

        return bin(cnums[-1] + 1)[2:].zfill(n)


# @lc code=end
