#
# @lc app=leetcode id=2766 lang=python3
#
# [2766] Relocate Marbles
#

# @lc code=start


class Solution:
    def relocateMarbles(
        self, nums: list[int], moveFrom: list[int], moveTo: list[int]
    ) -> list[int]:
        occupied = set(nums)

        for src, dst in zip(moveFrom, moveTo):
            occupied.remove(src)
            occupied.add(dst)

        return sorted(occupied)


# @lc code=end
