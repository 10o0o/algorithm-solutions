#
# @lc app=leetcode id=3380 lang=python3
#
# [3380] Maximum Area Rectangle With Point Constraints I
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, points: list[list[int]]) -> int:
        n = len(points)
        if n < 4:
            return -1

        points.sort()

        ys = sorted({y for x, y in points})
        y_to_idx = {y: i for i, y in enumerate(ys)}

        size = 1
        while size < len(ys):
            size <<= 1

        tree = [0] * (size * 2)

        def update(pos):
            i = size + pos
            tree[i] += 1

            while i > 1:
                i >>= 1
                tree[i] = tree[i * 2] + tree[i * 2 + 1]

        def query(left, right):
            left += size
            right += size
            result = 0

            while left <= right:
                if left & 1:
                    result += tree[left]
                    left += 1

                if not (right & 1):
                    result += tree[right]
                    right -= 1

                left //= 2
                right //= 2

            return result

        last = {}
        max_area = -1

        i = 0

        while i < n:
            x = points[i][0]
            j = i

            while j < n and points[j][0] == x:
                y = points[j][1]
                update(y_to_idx[y])
                j += 1

            for k in range(i, j - 1):
                y1 = points[k][1]
                y2 = points[k + 1][1]

                pair = (y1, y2)

                count = query(y_to_idx[y1], y_to_idx[y2])

                if pair in last:
                    prev_x, prev_count = last[pair]

                    if count - prev_count == 2:
                        area = (x - prev_x) * (y2 - y1)
                        max_area = max(max_area, area)

                last[pair] = (x, count)

            i = j

        return max_area


# @lc code=end
