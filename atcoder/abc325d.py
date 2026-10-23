# D - Printing Machine
# https://atcoder.jp/contests/abc325/tasks/abc325_d?lang=en

import heapq
import sys

input = sys.stdin.readline


def max_printed(products):
    products = [(product[0], product[0] + product[1]) for product in products]
    products.sort()

    t = 0
    ans = 0

    heap = []
    i = 0

    while i < len(products) or heap:
        if not heap:
            t = max(t, products[i][0])

        while i < len(products) and products[i][0] <= t:
            heapq.heappush(heap, products[i][1])
            i += 1

        while heap and heap[0] < t:
            heapq.heappop(heap)

        if heap:
            heapq.heappop(heap)
            ans += 1
            t += 1

    return ans


def solve() -> None:
    n = int(input())
    products = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_printed(products))


if __name__ == "__main__":
    solve()
