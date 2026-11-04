#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return list(set(edges[0]) & set(edges[1]))[0]


# @lc code=end
