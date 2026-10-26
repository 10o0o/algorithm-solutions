# AT ABC061 D?LANG=EN
# https://atcoder.jp/contests/abc061/tasks/abc061_d?lang=en

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    scores = [-float("inf")] * (n + 1)
    scores[1] = 0

    q = deque([(1, 0)])

    for _ in range(n - 1):
        for node in range(1, n + 1):
            if scores[node] == -float("inf"):
                continue

            for dest, weight in graph[node]:
                dest_score = scores[node] + weight

                scores[dest] = max(scores[dest], dest_score)

    affected = [False] * (n + 1)
    q = deque([(1, scores[1])])

    for node in range(1, n + 1):
        if scores[node] == -float("inf"):
            continue

        for dest, weight in graph[node]:
            if scores[node] + weight > scores[dest]:
                if not affected[dest]:
                    affected[dest] = True
                    q.append(dest)

    while q:
        node = q.popleft()

        for dest, _ in graph[node]:
            if not affected[dest]:
                affected[dest] = True
                q.append(dest)

    print("inf" if affected[n] else scores[n])


if __name__ == "__main__":
    solve()
