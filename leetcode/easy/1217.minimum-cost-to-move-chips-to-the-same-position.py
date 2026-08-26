#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Minimum Cost to Move Chips to The Same Position
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        cnt_pos = [0, 0]

        for po in position:
            cnt_pos[po % 2] += 1

        return min(cnt_pos)


# @lc code=end
