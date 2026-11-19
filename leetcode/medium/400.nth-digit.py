#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        # 1. n번째 자릿수가 속한 그룹 찾기
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # 2. 해당 그룹에서 몇 번째 숫자인지 계산
        num = start + (n - 1) // digits

        # 3. 해당 숫자에서 몇 번째 자릿수인지 계산
        index = (n - 1) % digits

        return int(str(num)[index])


# @lc code=end
