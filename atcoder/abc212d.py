# D - Querying Multiset
# https://atcoder.jp/contests/abc212/tasks/abc212_d?lang=en

import heapq
import sys

input = sys.stdin.readline


def process_queries(queries):
    heap = []
    add = 0
    answers = []

    for query in queries:
        if query[0] == 1:
            heapq.heappush(heap, query[1] - add)
        elif query[0] == 2:
            add += query[1]
        elif query[0] == 3:
            answers.append(heapq.heappop(heap) + add)

    return answers


def solve() -> None:
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    answers = process_queries(queries)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    solve()
