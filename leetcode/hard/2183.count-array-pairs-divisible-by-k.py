#
# @lc app=leetcode id=2183 lang=python3
#
# [2183] Count Array Pairs Divisible by K
#

# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        def gcd(a, b):
            if a < b:
                a, b = b, a

            while b != 0:
                a, b = b, a % b

            return a

        count = {}
        answer = 0

        for x in nums:
            g = gcd(x, k)

            for prev_g, cnt in count.items():
                if (g * prev_g) % k == 0:
                    answer += cnt

            count[g] = count.get(g, 0) + 1

        return answer


# @lc code=end
