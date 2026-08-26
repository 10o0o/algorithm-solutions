#
# @lc app=leetcode id=3272 lang=python3
#
# [3272] Find the Count of Good Integers
#

# @lc code=start
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10**half

        valid = set()

        for x in range(start, end):
            s = str(x)

            if n % 2:
                palindrome = s + s[-2::-1]
            else:
                palindrome = s + s[::-1]

            if int(palindrome) % k != 0:
                continue

            count = [0] * 10

            for digit in palindrome:
                count[int(digit)] += 1

            valid.add(tuple(count))

        fact = [factorial(i) for i in range(n + 1)]

        answer = 0

        for count in valid:
            denominator = 1

            for c in count:
                denominator *= fact[c]

            total = fact[n] // denominator

            # leading zero 제거
            invalid = 0

            if count[0] > 0:
                denominator = fact[count[0] - 1]

                for digit in range(1, 10):
                    denominator *= fact[count[digit]]

                invalid = fact[n - 1] // denominator

            answer += total - invalid

        return answer


# @lc code=end
