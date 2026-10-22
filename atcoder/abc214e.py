# AT ABC214 E?LANG=EN
# https://atcoder.jp/contests/abc214/tasks/abc214_e?lang=en

import heapq
import sys

input = sys.stdin.readline


def can_pack(intervals):
    # 시작점 L이 작은 공부터 확인한다.
    intervals.sort()
    n = len(intervals)
    box = 0
    i = 0
    heap = []  # 현재 배치할 수 있고, 아직 배치하지 않은 공들의 끝점 R

    while i < n or heap:
        # 기다리는 공이 없으면 다음 공의 시작점까지 건너뛴다.
        if not heap:
            box = max(box, intervals[i][0])

        # 현재 상자에 들어갈 수 있게 된 공을 모두 후보에 추가한다.
        while i < n and intervals[i][0] <= box:
            heapq.heappush(heap, intervals[i][1])
            i += 1

        # 끝점이 가장 작은 공을 먼저 현재 상자에 배치한다.
        end = heapq.heappop(heap)
        if end < box:
            return False

        box += 1

    return True


def solve():
    n = int(input().strip())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    print("Yes" if can_pack(intervals) else "No")


def main() -> None:
    t = int(input().strip())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
