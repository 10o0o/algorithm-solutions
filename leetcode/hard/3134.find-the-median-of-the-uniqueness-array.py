#
# @lc app=leetcode id=3134 lang=python3
#
# [3134] Find the Median of the Uniqueness Array
#

# @lc code=start
class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        n = len(nums)

        total = n * (n + 1) // 2
        target = (total + 1) // 2

        def at_most(k):
            freq = {}
            left = 0
            distinct = 0
            count = 0

            for right, x in enumerate(nums):
                if freq.get(x, 0) == 0:
                    distinct += 1

                freq[x] = freq.get(x, 0) + 1

                while distinct > k:
                    y = nums[left]
                    freq[y] -= 1

                    if freq[y] == 0:
                        distinct -= 1

                    left += 1

                count += right - left + 1

            return count

        lo = 1
        hi = len(set(nums))

        while lo < hi:
            mid = (lo + hi) // 2

            if at_most(mid) >= target:
                hi = mid
            else:
                lo = mid + 1

        return lo


# @lc code=end
