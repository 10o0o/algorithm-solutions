#
# @lc app=leetcode id=3921 lang=python3
#
# [3921] Score Validator
#

# @lc code=start
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            if event == "W":
                counter += 1
            elif event == "WD" or event == "NB":
                score += 1
            else:
                score += int(event)

            if counter == 10:
                break

        return [score, counter]


# @lc code=end
