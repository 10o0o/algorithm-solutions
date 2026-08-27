#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(
        self,
        n: int,
        present: list[int],
        future: list[int],
        hierarchy: list[list[int]],
        budget: int,
    ) -> int:
        children = [[] for _ in range(n)]

        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        INF = 10**10

        def merge(a, b):
            res = [-INF] * (budget + 1)

            for ca in range(budget + 1):
                if a[ca] == -INF:
                    continue

                for cb in range(budget - ca + 1):
                    if b[cb] == -INF:
                        continue

                    res[ca + cb] = max(res[ca + cb], a[ca] + b[cb])

            return res

        def dfs(u):
            child_dp = []

            for v in children[u]:
                child_dp.append(dfs(v))

            result = []

            for parent_bought in range(2):
                not_buy = [-INF] * (budget + 1)
                not_buy[0] = 0

                for dp0, dp1 in child_dp:
                    not_buy = merge(not_buy, dp0)

                price = present[u] // 2 if parent_bought else present[u]
                buy = [-INF] * (budget + 1)

                if price <= budget:
                    buy[price] = future[u] - price

                    for dp0, dp1 in child_dp:
                        buy = merge(buy, dp1)

                cur = [-INF] * (budget + 1)

                for b in range(budget + 1):
                    cur[b] = max(not_buy[b], buy[b])

                result.append(cur)

            return result[0], result[1]

        root_no_discount, _ = dfs(0)

        return max(root_no_discount)


# @lc code=end
