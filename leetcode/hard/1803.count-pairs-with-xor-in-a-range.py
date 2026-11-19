#
# @lc app=leetcode id=1803 lang=python3
#
# [1803] Count Pairs With XOR in a Range
#

# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        root = {}
        BITS = 15

        def insert(x):
            node = root

            for i in range(BITS - 1, -1, -1):
                bit = (x >> i) & 1
                node = node.setdefault(bit, {})
                node["count"] = node.get("count", 0) + 1

        def count_less_than(x, limit):
            node = root
            result = 0

            for i in range(BITS - 1, -1, -1):
                if not node:
                    break

                xb = (x >> i) & 1
                lb = (limit >> i) & 1

                if lb == 1:
                    same = node.get(xb)

                    if same:
                        result += same["count"]

                    node = node.get(xb ^ 1)
                else:
                    node = node.get(xb)

            return result

        answer = 0

        for x in nums:
            answer += count_less_than(x, high + 1)
            answer -= count_less_than(x, low)

            insert(x)

        return answer


# @lc code=end
