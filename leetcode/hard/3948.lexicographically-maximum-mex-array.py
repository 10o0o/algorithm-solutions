#
# @lc app=leetcode id=3948 lang=python3
#
# [3948] Lexicographically Maximum MEX Array
#

# @lc code=start
class Solution:
    def maximumMEX(self, nums: list[int]) -> list[int]:
        n = len(nums)

        count = [0] * (n * 2)

        for num in nums:
            if num <= n:
                count[num] += 1

        mex = 0
        while count[mex] > 0:
            mex += 1

        result = []
        i = 0

        while i < n:
            target = mex
            result.append(target)

            if target == 0:
                x = nums[i]

                if x <= n:
                    count[x] -= 1

                    if count[x] == 0:
                        mex = min(mex, x)

                i += 1
                continue

            seen = set()
            need = target

            while need > 0:
                x = nums[i]

                if x < target and x not in seen:
                    seen.add(x)
                    need -= 1

                if x <= n:
                    count[x] -= 1

                    if count[x] == 0:
                        mex = min(mex, x)

                i += 1

        return result


# @lc code=end
