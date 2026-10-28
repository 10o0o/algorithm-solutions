#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start


from math import factorial


class Solution:
    def permute(self, n: int, k: int) -> list[int]:
        odd_left = (n + 1) // 2
        even_left = n // 2
        res = []
        used = [False] * (n + 1)

        for pos in range(n):
            selected = False

            for num in range(1, n + 1):
                if used[num]:
                    continue

                if pos > 0 and num % 2 == res[-1] % 2:
                    continue

                if pos == 0 and n % 2 == 1:
                    if num % 2 == 0:
                        continue

                odd = odd_left - num % 2
                even = even_left - (1 - num % 2)

                ways = factorial(odd) * factorial(even)

                if k > ways:
                    k -= ways
                else:
                    res.append(num)
                    used[num] = True
                    odd_left = odd
                    even_left = even
                    selected = True
                    break

            if not selected:
                return []

        return res


# @lc code=end
