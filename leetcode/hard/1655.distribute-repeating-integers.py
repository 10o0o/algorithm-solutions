#
# @lc app=leetcode id=1655 lang=python3
#
# [1655] Distribute Repeating Integers
#

# @lc code=start


from collections import Counter


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        counts = sorted(Counter(nums).values(), reverse=True)
        quantity.sort(reverse=True)

        def dfs(i):
            if i == len(quantity):
                return True

            need = quantity[i]

            for j in range(len(counts)):
                if counts[j] < need:
                    continue

                counts[j] -= need

                if dfs(i + 1):
                    return True

                counts[j] += need

            return False

        return dfs(0)


# @lc code=end
