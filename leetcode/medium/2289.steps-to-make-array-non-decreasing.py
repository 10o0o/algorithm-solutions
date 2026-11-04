#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        ans = 0

        for x in nums:
            steps = 0

            while stack and stack[-1][0] <= x:
                steps = max(steps, stack.pop()[1])

            if stack:
                steps += 1
            else:
                steps = 0

            stack.append((x, steps))
            ans = max(ans, steps)

        return ans


# @lc code=end
