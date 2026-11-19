#
# @lc app=leetcode id=3218 lang=python3
#
# [3218] Minimum Cost for Cutting Cake I
#

# @lc code=startimport heapq


import heapq


class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]
    ) -> int:
        cost = 0

        h = [-v for v in horizontalCut]
        c = [-v for v in verticalCut]

        heapq.heapify(h)
        heapq.heapify(c)

        hc = 0
        cc = 0

        while h or c:
            if not h:
                cost += -sum(c) * (hc + 1)
                break

            if not c:
                cost += -sum(h) * (cc + 1)
                break

            if h[0] < c[0]:
                cost += -heapq.heappop(h) * (cc + 1)
                hc += 1
            else:
                cost += -heapq.heappop(c) * (hc + 1)
                cc += 1

        return cost


# @lc code=end
