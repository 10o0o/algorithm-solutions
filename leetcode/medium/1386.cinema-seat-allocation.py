#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved = defaultdict(set)

        for row, num in reservedSeats:
            reserved[row].add(num)

        ans = n * 2

        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}

        for seats in reserved.values():
            left_available = not (seats & left)
            middle_available = not (seats & middle)
            right_available = not (seats & right)

            if left_available and right_available:
                possible = 2
            elif left_available or right_available or middle_available:
                possible = 1
            else:
                possible = 0

            ans -= 2 - possible

        return ans


# @lc code=end
