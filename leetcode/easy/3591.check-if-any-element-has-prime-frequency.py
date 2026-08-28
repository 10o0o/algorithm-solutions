#
# @lc app=leetcode id=3591 lang=python3
#
# [3591] Check if Any Element Has Prime Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        primes = [True] * 101
        primes[0] = primes[1] = False

        for i in range(2, 101):
            if primes[i]:
                for j in range(i * 2, 101, i):
                    primes[j] = False

        counts = Counter(nums)
        values = counts.values()

        for v in values:
            if primes[v]:
                return True

        return False


# @lc code=end
