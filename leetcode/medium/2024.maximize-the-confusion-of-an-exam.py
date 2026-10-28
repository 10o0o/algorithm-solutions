#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        t = f = 0
        answer = 0

        for right, c in enumerate(answerKey):
            if c == "T":
                t += 1
            else:
                f += 1

            while min(t, f) > k:
                if answerKey[left] == "T":
                    t -= 1
                else:
                    f -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer


# @lc code=end
