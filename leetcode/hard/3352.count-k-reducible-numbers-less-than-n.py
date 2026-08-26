#
# @lc app=leetcode id=3352 lang=python3
#
# [3352] Count K-Reducible Numbers Less Than N
#

# @lc code=start
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        m = len(s)

        steps = [0] * (m + 1)

        for i in range(2, m + 1):
            steps[i] = 1 + steps[i.bit_count()]

        valid = []

        for ones in range(1, m + 1):
            if steps[ones] <= k - 1:
                valid.append(ones)

        # C(n, r)
        comb = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            comb[i][0] = comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def count(ones):
            used = 0
            result = 0

            for i, bit in enumerate(s):
                if bit == "1":
                    remaining = m - i - 1
                    need = ones - used

                    if 0 <= need <= remaining:
                        result += comb[remaining][need]
                        result %= MOD

                    used += 1

                    if used > ones:
                        break

            return result

        ans = 0

        for ones in valid:
            ans += count(ones)
            ans %= MOD

        return ans


# @lc code=end
