#
# @lc app=leetcode id=2584 lang=python3
#
# [2584] Split the Array to Make Coprime Products
#

# @lc code=start
class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        def factorize(x):
            factors = set()

            d = 2

            while d * d <= x:
                if x % d == 0:
                    factors.add(d)

                    while x % d == 0:
                        x //= d

                d += 1

            if x > 1:
                factors.add(x)

            return factors

        n = len(nums)
        factors = [factorize(num) for num in nums]
        last = {}

        for i in range(n):
            for p in factors[i]:
                last[p] = i

        right = 0

        for i in range(n - 1):
            for p in factors[i]:
                right = max(right, last[p])

            if i == right:
                return i

        return -1


# @lc code=end
