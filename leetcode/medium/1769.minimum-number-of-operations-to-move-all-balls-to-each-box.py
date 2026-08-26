#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        moves = sum(i for i, c in enumerate(boxes) if c == "1")

        left = int(boxes[0])
        right = boxes.count("1") - left

        ans = [0] * n
        ans[0] = moves

        for i in range(1, n):
            moves += left - right
            ans[i] = moves

            if boxes[i] == "1":
                left += 1
                right -= 1

        return ans


# @lc code=end
