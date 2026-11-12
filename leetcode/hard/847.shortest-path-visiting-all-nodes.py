#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        for i, r in enumerate(graph):
            if len(r) == 1:
                node = i
                break

        visited = set()
        visited.add(node)

        def dfs(node, v):
            if len(graph[node]) == 1:
                return dfs(graph[node][0], v + 1)

            for next in graph[node]:
                if next in visited:
                    continue
                v += dfs(next, 1)

            return v

        return dfs(node, 0)


# @lc code=end
