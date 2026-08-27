#
# @lc app=leetcode id=3200 lang=python3
#
# [3200] Maximum Height of a Triangle
#

# @lc code=start
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        small, large = (blue, red) if red > blue else (red, blue)
        layers = [(0, 0) for _ in range(101)]

        for i in range(1, 101):
            layers[i] = (layers[i - 1][1], layers[i - 1][0] + i)

        left, right = 1, 100

        while left < right:
            mid = (left + right + 1) // 2

            lsmall, llarge = layers[mid]

            if lsmall <= small and llarge <= large:
                left = mid
            else:
                right = mid - 1

        return left


# @lc code=end
