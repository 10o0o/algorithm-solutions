#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        graph = [[] for _ in range(n + 1)]
        reverse = [[] for _ in range(n + 1)]

        for u, v in invocations:
            graph[u].append(v)
            reverse[v].append(u)

        visited = [False] * (n + 1)
        order = []

        def dfs1(u):
            visited[u] = True

            for v in graph[u]:
                if not visited[v]:
                    dfs1(v)

            order.append(u)

        for u in range(n + 1):
            if not visited[u]:
                dfs1(u)

        visited = [False] * (n + 1)
        sccs = []

        def dfs2(u, component):
            visited[u] = True
            component.append(u)

            for v in reverse[u]:
                if not visited[v]:
                    dfs2(v, component)

        for u in order[::-1]:
            if not visited[u]:
                component = []
                dfs2(u, component)
                sccs.append(component)

        ids = [-1] * (n + 1)

        for i, c in enumerate(component):
            for v in c:
                ids[v] = i

        return []


# @lc code=end
