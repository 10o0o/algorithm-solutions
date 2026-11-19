#
# @lc app=leetcode id=3668 lang=python3
#
# [3668] Restore Finishing Order
#

# @lc code=start
class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        order_dict = {v: i for i, v in enumerate(order)}
        return sorted(friends, key=lambda x: order_dict[x])


# @lc code=end
