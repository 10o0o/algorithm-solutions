#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def coloring(graph, size):
            color = [-1] * size
            count = [0, 0]

            q = deque([0])
            color[0] = 0

            while q:
                u = q.popleft()
                count[color[u]] += 1

                for v in graph[u]:
                    if color[v] != -1:
                        continue

                    color[v] = color[u] ^ 1
                    q.append(v)

            return color, count

        color1, count1 = coloring(graph1, n)
        _, count2 = coloring(graph2, m)

        best2 = max(count2)

        return [count1[color1[i]] + best2 for i in range(n)]


# @lc code=end
