#
# @lc app=leetcode id=2172 lang=python3
#
# [2172] Maximum AND Sum of Array
#

# @lc code=start
class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        max_state = 3**numSlots

        dp = [-1] * max_state
        dp[0] = 0

        powers = [3**i for i in range(numSlots)]

        for state in range(max_state):
            if dp[state] == -1:
                continue

            temp = state
            used = 0

            for _ in range(numSlots):
                used += temp % 3
                temp //= 3

            if used >= len(nums):
                continue

            for slot in range(numSlots):
                cnt = (state // powers[slot]) % 3

                if cnt == 2:
                    continue

                new_state = state + powers[slot]

                dp[new_state] = max(
                    dp[new_state],
                    dp[state] + (nums[used] & (slot + 1)),
                )

        ans = 0

        for state in range(max_state):
            temp = state
            used = 0

            for _ in range(numSlots):
                used += temp % 3
                temp //= 3

            if used == len(nums):
                ans = max(ans, dp[state])

        return ans


# @lc code=end
