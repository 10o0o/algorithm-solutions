#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        dicts = [defaultdict(int)]

        for i in range(n):
            c = formula[i]

            if c == "(":
                dicts.append(defaultdict(int))
            elif c.isupper():
                atom = c

                while i + 1 < n and formula[i + 1].islower():
                    atom += formula[i + 1]
                    i += 1

                digits = ""

                while i + 1 < n and formula[i + 1].isdigit():
                    digits += formula[i + 1]
                    i += 1

                if digits == "":
                    digits = 1
                else:
                    digits = int(digits)

                dicts[-1][atom] += digits
            elif c == ")":
                digits = ""

                while i + 1 < n and formula[i + 1].isdigit():
                    digits += formula[i + 1]
                    i += 1

                target = dicts.pop()

                if digits == "":
                    digits = 1
                else:
                    digits = int(digits)

                for atom, cnts in target.items():
                    dicts[-1][atom] += cnts * digits

        result = sorted(dicts[0].items())
        ans = ""

        for atom, cnts in result:
            ans += f"{atom}{cnts if cnts > 1 else ''}"

        return ans


# @lc code=end
