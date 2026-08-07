#
# @lc app=leetcode id=4007 lang=python3
#
# [4007] Widest Possible Fence
#

# @lc code=start


from collections import Counter, defaultdict


class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        counts = Counter(planks)
        width_by_height = defaultdict(int)

        for height, count in counts.items():
            width_by_height[height] += count

        heights = list(counts)

        for i, left in enumerate(heights):
            for right in heights[i:]:
                if left == right:
                    pair_count = counts[left] // 2
                else:
                    pair_count = min(counts[left], counts[right])

                target_height = left + right
                width_by_height[target_height] += pair_count

        return max(width_by_height.values())


# @lc code=end
