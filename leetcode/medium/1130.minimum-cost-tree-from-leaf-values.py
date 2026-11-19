#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        stack = [float("inf")]
        ans = 0

        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                ans += mid * min(stack[-1], x)

            stack.append(x)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans


# @lc code=end
