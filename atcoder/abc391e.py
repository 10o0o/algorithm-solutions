# AT ABC391 E?LANG=EN
# https://atcoder.jp/contests/abc391/tasks/abc391_e?lang=en

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input().strip())
    a = input().strip()
    tree = []

    for i in range(len(a)):
        tree.append((int(a[i]), 1))

    while len(tree) > 1:
        new_tree = []

        for i in range(0, len(tree), 3):
            cnts = [0, 0]

            for k in range(3):
                cnts[tree[i + k][0]] += 1

            v = 0 if cnts[0] > cnts[1] else 1

            flips = []

            for k in range(3):
                if tree[i + k][0] == v:
                    flips.append(tree[i + k][1])

            flips.sort()
            flips.pop()

            new_tree.append((v, sum(flips)))

        tree = new_tree

    print(tree[0][1])


if __name__ == "__main__":
    solve()
