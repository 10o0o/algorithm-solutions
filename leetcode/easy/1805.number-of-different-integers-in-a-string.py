#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_set = set()

        tmp_int_sequence = ""

        for c in word:
            if c.isdigit():
                tmp_int_sequence += c
            else:
                if tmp_int_sequence:
                    num_set.add(int(tmp_int_sequence))
                    tmp_int_sequence = ""

        if tmp_int_sequence != "":
            num_set.add(int(tmp_int_sequence))

        return len(num_set)


# @lc code=end
