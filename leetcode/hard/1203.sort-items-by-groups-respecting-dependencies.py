#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def sortItems(
        self, n: int, m: int, group: list[int], beforeItems: list[list[int]]
    ) -> list[int]:

        for i, _ in enumerate(group):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_indegree = [0] * n
        group_indegree = [0] * m

        graph_items = defaultdict(list)
        graph_group = [set() for _ in range(m)]

        for i, items in enumerate(beforeItems):
            for item in items:
                # item에서 i 방향으로 가는 그래프
                graph_items[item].append(i)
                item_indegree[i] += 1

                if group[item] != group[i]:
                    prev_group = group[item]
                    next_group = group[i]

                    if next_group not in graph_group[prev_group]:
                        graph_group[prev_group].add(next_group)
                        group_indegree[next_group] += 1

        def topo_sort(graph, indegree, size):
            q = deque()

            for i in range(size):
                if indegree[i] == 0:
                    q.append(i)

            result = []

            while q:
                cur = q.popleft()
                result.append(cur)

                for nxt in graph[cur]:
                    indegree[nxt] -= 1

                    if indegree[nxt] == 0:
                        q.append(nxt)

            if len(result) != size:
                return []

            return result

        item_order = topo_sort(graph_items, item_indegree, n)
        group_order = topo_sort(graph_group, group_indegree, m)

        items_by_group = defaultdict(list)

        for item in item_order:
            items_by_group[group[item]].append(item)

        ans = []

        for g in group_order:
            ans.extend(items_by_group[g])

        return ans


# @lc code=end
