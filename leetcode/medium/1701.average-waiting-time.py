#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#

# @lc code=start


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_wait = 0

        for arrival, cook_time in customers:
            current_time = max(current_time, arrival)
            current_time += cook_time
            total_wait += current_time - arrival

        return total_wait / len(customers)


# @lc code=end
