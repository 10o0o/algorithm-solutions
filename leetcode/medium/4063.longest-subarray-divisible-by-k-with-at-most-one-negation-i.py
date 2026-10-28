#
# @lc app=leetcode id=4063 lang=python3
#
# [4063] Longest Subarray Divisible by K with At Most One Negation I
#

# @lc code=start


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def can(l):
            if l == 0:
                return True

            neg_opts = {}
            sum = 0

            for i in range(l):
                sum += nums[i]
                sum %= k

                neg = k - (nums[i] * 2) % k
                neg_opts[neg] = neg_opts.get(neg, 0) + 1

            r = sum % k
            if r == 0 or (k - r) in neg_opts:
                return True

            for i in range(l, len(nums)):
                sum -= nums[i - l]
                sum += nums[i]

                neg_before = k - (nums[i - l] * 2) % k
                neg_opts[neg_before] -= 1
                if neg_opts[neg_before] == 0:
                    del neg_opts[neg_before]

                neg = k - (nums[i] * 2) % k
                neg_opts[neg] = neg_opts.get(neg, 0) + 1

                r = sum % k
                if r == 0 or (k - r) in neg_opts:
                    return True

            return False

        for i in range(len(nums), 0, -1):
            if can(i):
                return i

        return 0


# @lc code=end
