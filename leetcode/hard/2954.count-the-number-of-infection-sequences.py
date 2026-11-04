#
# @lc app=leetcode id=2954 lang=python3
#
# [2954] Count the Number of Infection Sequences
#

# @lc code=start
class Solution:
    def numberOfSequence(self, n: int, sick: list[int]) -> int:
        MOD = 10**9 + 7
        healthy = n - len(sick)

        fact = [1] * (healthy + 1)
        for i in range(1, healthy + 1):
            fact[i] = fact[i - 1] * i % MOD

        denom = fact[sick[0]] * fact[n - 1 - sick[-1]] % MOD
        exponent = 0

        for a, b in zip(sick, sick[1:]):
            gap = b - a - 1

            denom = denom * fact[gap] % MOD
            exponent += max(0, gap - 1)

        return fact[healthy] * pow(denom, MOD - 2, MOD) * pow(2, exponent, MOD) % MOD


# @lc code=end
