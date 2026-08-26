#
# @lc app=leetcode id=2731 lang=python3
#
# [2731] Movement of Robots
#

# @lc code=start
class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        MOD = int(1e9 + 7)
        ans = 0
        pos = []

        for i, num in enumerate(nums):
            direction = s[i]

            if direction == "R":
                mul = 1
            else:
                mul = -1

            pos.append(num + mul * d)

        pos.sort()
        prefix_sum = 0

        for i, num in enumerate(pos):
            ans += num * i - prefix_sum
            prefix_sum += num

        return ans % MOD


# @lc code=end
