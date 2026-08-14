# AT ABC470 C
# https://atcoder.jp/contests/abc470/tasks/abc470_c

import sys

input = sys.stdin.readline


def solve() -> None:
    N, Q = map(int, input().split(" "))
    A = [0] * (N + 1)

    xor_value = 0
    active = set()

    for _ in range(Q):
        query = list(map(int, input().split(" ")))

        if query[0] == 1:
            xor_value ^= A[query[1]]
            A[query[1]] += 1
            active.add(query[1])
            xor_value ^= A[query[1]]

        if query[0] == 2:
            next_active = set()

            for x in active:
                xor_value ^= A[x]
                A[x] -= 1
                if A[x] != 0:
                    next_active.add(x)

                xor_value ^= A[x]

            active = next_active

        print(xor_value)


if __name__ == "__main__":
    solve()
