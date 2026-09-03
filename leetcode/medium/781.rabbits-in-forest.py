#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counts = Counter(answers)

        ans = 0

        for answer, cnts in counts.items():
            cnts %= answer + 1
            if cnts != 0:
                ans += (answer + 1) - cnts

        return len(answers) + ans


# @lc code=end
