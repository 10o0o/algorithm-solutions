#
# @lc app=leetcode id=3490 lang=python3
#
# [3490] Count Beautiful Numbers
#

# @lc code=start
from functools import cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def get_beautiful(n):
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            length = len(digits)

            result = 0

            for target_sum in range(1, 9 * length + 1):

                @cache
                def dp(pos, digit_sum, product_mod, tight, started):
                    if digit_sum > target_sum:
                        return 0

                    remain = length - pos
                    if digit_sum + 9 * remain < target_sum:
                        return 0

                    if pos == length:
                        return int(
                            started and digit_sum == target_sum and product_mod == 0
                        )

                    limit = digits[pos] if tight else 9
                    count = 0

                    for d in range(limit + 1):
                        next_tight = tight and d == digits[pos]

                        if not started and d == 0:
                            count += dp(
                                pos + 1, digit_sum, product_mod, next_tight, False
                            )
                            continue

                        count += dp(
                            pos + 1,
                            digit_sum + d,
                            (product_mod * d) % target_sum,
                            next_tight,
                            True,
                        )

                    return count

                result += dp(0, 0, 1 % target_sum, True, False)

            return result

        return get_beautiful(r) - get_beautiful(l - 1)


# @lc code=end
