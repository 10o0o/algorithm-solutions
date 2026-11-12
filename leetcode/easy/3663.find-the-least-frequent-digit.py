#
# @lc app=leetcode id=3663 lang=python3
#
# [3663] Find The Least Frequent Digit
#

# @lc code=start
from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c = Counter()
        while n:
            c[n % 10] += 1
            n //= 10

        s = sorted([(k, v) for k, v in c.items()])
        print(s)


# @lc code=end
