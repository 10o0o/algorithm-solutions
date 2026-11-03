import sys


def solve():
    input = sys.stdin.buffer.readline
    n, q = map(int, input().split())
    s = input().strip()

    size = 1
    while size < n:
        size <<= 1

    tree = [0] * (size * 2)

    for i in range(n - 1):
        tree[size + i] = int(s[i] == s[i + 1])

    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    def toggle(i):
        if not 0 <= i < n - 1:
            return

        i += size
        tree[i] ^= 1

        i //= 2
        while i:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
            i //= 2

    def query(left, right):
        left += size
        right += size
        total = 0

        while left <= right:
            if left & 1:
                total += tree[left]
                left += 1

            if not right & 1:
                total += tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    ans = []

    for _ in range(q):
        kind, left, right = map(int, input().split())
        left -= 1
        right -= 1

        if kind == 1:
            toggle(left - 1)
            toggle(right)
        else:
            count = query(left, right - 1)
            ans.append("Yes" if count == 0 else "No")

    print("\n".join(ans))


if __name__ == "__main__":
    solve()
