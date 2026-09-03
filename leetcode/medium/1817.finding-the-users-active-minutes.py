#
# @lc app=leetcode id=1817 lang=python3
#
# [1817] Finding the Users Active Minutes
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        ans = [0] * k

        log_map = defaultdict(set)

        for id, time in logs:
            log_map[id].add(time)

        for s in log_map.values():
            ans[len(s) - 1] += 1

        return ans


# @lc code=end
