#
# @lc app=leetcode id=3654 lang=python3
#
# [3654] Minimum Sum After Divisible Sum Deletions
#

# @lc code=start
class Solution:
    def minArraySum(self, nums: list[int], k: int) -> int:
        best = {0: 0}
        prefix = 0
        dp = 0

        for num in nums:
            prefix = (prefix + num) % k

            # 선택 1: 현재 원소를 남긴다
            keep = dp + num

            # 선택 2: 현재 위치까지의 구간을 삭제한다
            delete = best.get(prefix, float("inf"))

            dp = min(keep, delete)

            # 현재 나머지에 대한 최적 DP 갱신
            best[prefix] = min(best.get(prefix, float("inf")), dp)

        return dp


# @lc code=end
