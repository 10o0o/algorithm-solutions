#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        bucket = []

        cur = nums[0] - 1
        counts = 0

        for num in nums:
            if cur != num:
                bucket.append((cur, counts))
                cur = num
                counts = 1
            else:
                counts += 1

        bucket.append((cur, counts))

        i = 0
        for a, c in bucket:
            for _ in range(min(2, c)):
                nums[i] = a
                i += 1

        k = i

        for j in range(i, n):
            nums[j] = "_"

        return k


# @lc code=end
