#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        dict = defaultdict(int)

        def go(treeNode):
            sum = treeNode.val

            if treeNode.left:
                sum += go(treeNode.left)

            if treeNode.right:
                sum += go(treeNode.right)

            dict[sum] += 1
            return sum

        go(root)

        max_freq = max(dict.values())

        return [sum for sum, count in dict.items() if count == max_freq]


# @lc code=end
