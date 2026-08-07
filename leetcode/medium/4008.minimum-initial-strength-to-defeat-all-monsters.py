#
# @lc app=leetcode id=4008 lang=python3
#
# [4008] Minimum Initial Strength to Defeat All Monsters
#

# @lc code=start
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        bonuses = [0] * (n + 1)

        for boost in boosts:
            [l, r, v] = boost
            bonuses[l] += v
            bonuses[r + 1] -= v

        for i in range(n):
            bonuses[i + 1] += bonuses[i]

        initial_strength = 0
        idx = n - 1

        while idx >= 0:
            required_strength = max(0, monsters[idx] - bonuses[idx])
            idx -= 1
            if required_strength > 0:
                initial_strength += required_strength
                break

        if idx >= 0:
            initial_strength += sum(monsters[: idx + 1])

        return initial_strength


# @lc code=end
