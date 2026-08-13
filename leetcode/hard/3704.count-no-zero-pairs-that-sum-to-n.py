#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = [int(ch) for ch in str(n)[::-1]]
        digits.append(0)

        dp = defaultdict(int)
        dp[(0, True, True)] = 1

        def choices(alive, pos):
            if not alive:
                return [(0, False)]

            result = [(digit, True) for digit in range(1, 10)]

            if pos > 0:
                result.append((0, False))

            return result

        for pos, target in enumerate(digits):
            next_dp = defaultdict(int)

            for (carry, alive_a, alive_b), ways in dp.items():
                choices_a = choices(alive_a, pos)
                choices_b = choices(alive_b, pos)

                for digit_a, next_alive_a in choices_a:
                    for digit_b, next_alive_b in choices_b:
                        total = digit_a + digit_b + carry

                        if total % 10 != target:
                            continue

                        next_carry = total // 10
                        next_state = (
                            next_carry,
                            next_alive_a,
                            next_alive_b,
                        )

                        next_dp[next_state] += ways

            dp = next_dp

        return dp[(0, False, False)]


# @lc code=end
