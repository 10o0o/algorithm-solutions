#
# @lc app=leetcode id=4013 lang=python3
#
# [4013] Count Subarrays With Even Odd Ratio II
#

# @lc code=start


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, index, value=1):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index):
        result = 0

        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        scores = [0]
        current_score = 0

        for num in nums:
            if num % 2 == 0:
                current_score += b
            else:
                current_score -= a

            scores.append(current_score)

        sorted_scores = sorted(set(scores))
        rank = {value: index + 1 for index, value in enumerate(sorted_scores)}
        fenwick = FenwickTree(len(sorted_scores))

        answer = 0
        seen_count = 0

        for score in scores:
            current_rank = rank[score]

            less_count = fenwick.prefix_sum(current_rank - 1)
            greater_equal_count = seen_count - less_count
            answer += greater_equal_count

            fenwick.add(current_rank)
            seen_count += 1

        return answer


# @lc code=end
