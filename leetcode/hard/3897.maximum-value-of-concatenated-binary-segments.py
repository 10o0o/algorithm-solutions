#
# @lc app=leetcode id=3897 lang=python3
#
# [3897] Maximum Value of Concatenated Binary Segments
#

# @lc code=start
class Solution:
    def max_value(self, nums1, nums0):
        MOD = 10**9 + 7

        segments = sorted(
            zip(nums1, nums0),
            key=lambda x: (
                x[1] != 0,  # 1만 있는 구간이 먼저
                -x[0],  # 1 개수 내림차순
                x[1],  # 같으면 0 개수 오름차순
            ),
        )

        answer = 0

        for ones, zeros in segments:
            for _ in range(ones):
                answer = (answer * 2 + 1) % MOD

            for _ in range(zeros):
                answer = (answer * 2) % MOD

        return answer


# @lc code=end
