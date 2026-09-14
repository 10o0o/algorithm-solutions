#
# @lc app=leetcode id=3576 lang=python3
#
# [3576] Transform Array to All Equal Elements
#

# @lc code=start
class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        cnts = [0, 0]

        for num in nums:
            if num == 1:
                cnts[0] += 1
            else:
                cnts[1] += 1

        targets = []

        if cnts[0] % 2 == 0:
            targets.append(-1)
        if cnts[1] % 2 == 0:
            targets.append(1)

        def calculate(target):
            copied = nums.copy()
            n = len(nums)
            cnts = 0

            for i in range(n - 1):
                if copied[i] != target:
                    copied[i] = target
                    copied[i + 1] *= -1
                    cnts += 1

            if copied[n - 1] == target:
                return cnts

            return 10**6

        for target in targets:
            cal_k = calculate(target)
            if cal_k <= k:
                return True

        return False


# @lc code=end
