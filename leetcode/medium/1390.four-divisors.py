#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start
class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def calculator(num):
            divisors = []

            for i in range(1, int(num**0.5) + 1):
                if num % i != 0:
                    continue

                divisors.append(i)

                if i != num // i:
                    divisors.append(num // i)

                if len(divisors) > 4:
                    return 0

            if len(divisors) == 4:
                return sum(divisors)

            return 0

        ans = 0

        for num in nums:
            ans += calculator(num)

        return ans


# @lc code=end
