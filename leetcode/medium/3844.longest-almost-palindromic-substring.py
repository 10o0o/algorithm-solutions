#
# @lc app=leetcode id=3844 lang=python3
#
# [3844] Longest Almost-Palindromic Substring
#

# @lc code=start


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 2

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            best = r - l - 1

            # 2. 왼쪽 문자 하나를 제거한 경우
            if l >= 0:
                x, y = l - 1, r

                while x >= 0 and y < n and s[x] == s[y]:
                    x -= 1
                    y += 1

                best = max(best, y - x - 1)

            # 3. 오른쪽 문자 하나를 제거한 경우
            if r < n:
                x, y = l, r + 1

                while x >= 0 and y < n and s[x] == s[y]:
                    x -= 1
                    y += 1

                best = max(best, y - x - 1)

            return best

        for i in range(n):
            ans = max(ans, expand(i - 1, i + 1))
            ans = max(ans, expand(i, i + 1))

        return ans


# @lc code=end
