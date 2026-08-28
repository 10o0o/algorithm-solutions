#
# @lc app=leetcode id=3850 lang=python3
#
# [3850] Count Sequences to K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countSequences(self, nums: list[int], k: int) -> int:
        def convert(n) -> tuple[tuple[int, int, int], int]:
            ret = [0, 0, 0]

            primes = [2, 3, 5]

            for i, p in enumerate(primes):
                while n % p == 0:
                    ret[i] += 1
                    n //= p

            return (ret[0], ret[1], ret[2]), n

        target, rest = convert(k)

        if rest != 1:
            return 0

        dp = {(0, 0, 0): 1}

        for num in nums:
            (x, y, z), _ = convert(num)
            next_dp = defaultdict(int)

            for (a, b, c), count in dp.items():
                next_dp[(a, b, c)] += count
                next_dp[(a + x, b + y, c + z)] += count
                next_dp[(a - x, b - y, c - z)] += count

            dp = next_dp

        return dp.get(target, 0)


# @lc code=end
