#
# @lc app=leetcode id=1735 lang=python3
#
# [1735] Count Ways to Make Array With Product
#

# @lc code=start
from collections import defaultdict
from math import comb


class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        answer = []

        def prime_factorize(n):
            factors = defaultdict(int)

            i = 2

            while i * i <= n:
                while n % i == 0:
                    factors[i] += 1
                    n //= i

                i += 1

            if n > 1:
                factors[n] += 1

            return factors

        for n, k in queries:
            factors = prime_factorize(k)
            ways = 1

            for exponent in factors.values():
                ways *= comb(n + exponent - 1, exponent)
                ways %= MOD

            answer.append(ways)

        return answer


# @lc code=end
