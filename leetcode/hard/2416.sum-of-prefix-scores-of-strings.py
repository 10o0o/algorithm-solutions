#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#


# @lc code=startclass Solution:
class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        class Trie:
            def __init__(self):
                self.count = 0
                self.next = {}

        root = Trie()

        # Trie 구성
        for word in words:
            node = root

            for c in word:
                if c not in node.next:
                    node.next[c] = Trie()

                node = node.next[c]
                node.count += 1

        ans = []

        for word in words:
            node = root
            score = 0

            for c in word:
                node = node.next[c]
                score += node.count

            ans.append(score)

        return ans


# @lc code=end
