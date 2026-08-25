#
# @lc app=leetcode id=3363 lang=python3
#
# [3363] Find the Maximum Number of Fruits Collected
#

# @lc code=start
class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        NEG = float("-inf")
        ans = 0

        for i in range(n):
            ans += fruits[i][i]

        right_top_dp = [NEG] * n
        right_top_dp[n - 1] = fruits[0][n - 1]

        for i in range(1, n - 1):
            next_dp = [NEG] * n

            for j in range(i + 1, n):
                best = right_top_dp[j]

                if j - 1 >= 0:
                    best = max(best, right_top_dp[j - 1])

                if j + 1 < n:
                    best = max(best, right_top_dp[j + 1])

                next_dp[j] = best + fruits[i][j]

            right_top_dp = next_dp

        ans += right_top_dp[n - 1]

        left_bottom_dp = [NEG] * n
        left_bottom_dp[n - 1] = fruits[n - 1][0]

        for j in range(1, n - 1):
            next_dp = [NEG] * n

            for i in range(j + 1, n):
                best = left_bottom_dp[i]

                if i - 1 >= 0:
                    best = max(best, left_bottom_dp[i - 1])

                if i + 1 < n:
                    best = max(best, left_bottom_dp[i + 1])

                next_dp[i] = best + fruits[i][j]

            left_bottom_dp = next_dp

        ans += left_bottom_dp[n - 1]

        return int(ans)


# @lc code=end
