#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        freq = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            answer += freq.get(prefix - k, 0)

            freq[prefix] = freq.get(prefix, 0) + 1

        return answer


# @lc code=end
