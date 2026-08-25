#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root) -> int:
        q = [root]
        max_value = -123_456_789
        max_level = -1
        cur_level = 1

        while q:
            sum = 0
            new_q = []

            for tree_node in q:
                sum += tree_node.val

                if tree_node.left:
                    new_q.append(tree_node.left)

                if tree_node.right:
                    new_q.append(tree_node.right)

            q = new_q

            if sum > max_value:
                max_value = sum
                max_level = cur_level

            cur_level += 1

        return max_level


# @lc code=end
