#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        times = sorted({*startTime, *endTime, queryTime})
        idx = {t: i for i, t in enumerate(times)}
        diff = [0] * (len(times) + 1)

        for start, end in zip(startTime, endTime):
            diff[idx[start]] += 1
            diff[idx[end] + 1] -= 1

        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]

        return diff[idx[queryTime]]


# @lc code=end
