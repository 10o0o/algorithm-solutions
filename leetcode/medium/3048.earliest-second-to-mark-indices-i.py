#
# @lc app=leetcode id=3048 lang=python3
#
# [3048] Earliest Second to Mark Indices I
#

# @lc code=start
class Solution:
    def earliestSecondToMarkIndices(
        self, nums: list[int], changeIndices: list[int]
    ) -> int:
        n = len(nums)
        m = len(changeIndices)

        left = 1
        right = m
        answer = -1

        def can(t):
            last = [-1] * n

            for s in range(t):
                idx = changeIndices[s] - 1
                last[idx] = s

            if -1 in last:
                return False

            free = 0

            for s in range(t):
                idx = changeIndices[s] - 1

                if s == last[idx]:
                    if free < nums[idx]:
                        return False

                    free -= nums[idx]

                else:
                    free += 1

            return True

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer


# @lc code=end
