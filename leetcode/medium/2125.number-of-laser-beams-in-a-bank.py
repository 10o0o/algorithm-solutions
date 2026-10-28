#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        n = len(bank[0])
        empty = "0" * n
        prev = empty
        ans = 0

        for b in bank:
            if b == empty:
                continue

            ans += b.count("1") * prev.count("1")
            prev = b

        return ans


# @lc code=end
