#
# @lc app=leetcode id=1363 lang=python3
#
# [1363] Largest Multiple of Three
#

# @lc code=start
class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        digits.sort(reverse=True)
        dp = ["", None, None]

        for digit in digits:
            r = digit % 3
            new_dp = [""] * 3

            for i in range(3):
                offset = i - r
                if offset < 0:
                    offset += 3

                if dp[offset] is not None:
                    combined = (
                        str(digit) if dp[offset] == "0" else dp[offset] + str(digit)
                    )

                    if dp[i] is not None and (
                        len(dp[i]) > len(combined)
                        or (len(dp[i]) == len(combined) and dp[i] > combined)
                    ):
                        new_dp[i] = dp[i]
                    else:
                        new_dp[i] = combined
                else:
                    new_dp[i] = dp[i]

            dp = new_dp

        return dp[0]


# @lc code=end
