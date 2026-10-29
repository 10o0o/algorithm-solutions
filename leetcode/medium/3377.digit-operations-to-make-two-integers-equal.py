#
# @lc app=leetcode id=3377 lang=python3
#
# [3377] Digit Operations to Make Two Integers Equal
#

# @lc code=start

from heapq import heappop, heappush
from math import isqrt


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        digits = len(str(n))
        limit = 10**digits
        lower = 10 ** (digits - 1)

        primes = [True] * limit
        primes[0] = primes[1] = False

        for i in range(2, isqrt(limit - 1) + 1):
            if not primes[i]:
                continue

            for j in range(i * i, limit, i):
                primes[j] = False

        if primes[n] or primes[m]:
            return -1

        dist = [float("inf")] * limit
        dist[n] = n

        heap = [(n, n)]

        while heap:
            cost, cur = heappop(heap)

            if cost != dist[cur]:
                continue

            if cur == m:
                return cost

            place = 1

            for _ in range(digits):
                digit = (cur // place) % 10

                for delta in (-1, 1):
                    if not 0 <= digit + delta <= 9:
                        continue

                    next = cur + delta * place

                    if next < lower or next >= limit or primes[next]:
                        continue

                    new_cost = cost + next

                    if new_cost < dist[next]:
                        dist[next] = new_cost
                        heappush(heap, (new_cost, next))

                place *= 10

        return -1


# @lc code=end
