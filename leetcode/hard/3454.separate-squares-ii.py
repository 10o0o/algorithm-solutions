#
# @lc app=leetcode id=3454 lang=python3
#
# [3454] Separate Squares II
#

# @lc code=start
class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1

        # 이 노드 구간 전체를 덮는 사각형 개수
        self.cover = [0] * (self.n * 4)

        # 이 노드 구간에서 실제로 덮인 x 길이
        self.length = [0] * (self.n * 4)

    def update(self, node, l, r, ql, qr, delta):
        # 전혀 겹치지 않음
        if qr < l or r < ql:
            return

        # 현재 노드 구간 전체가 update 범위에 포함됨
        if ql <= l and r <= qr:
            self.cover[node] += delta

        else:
            mid = (l + r) // 2

            self.update(
                node * 2,
                l,
                mid,
                ql,
                qr,
                delta,
            )

            self.update(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr,
                delta,
            )

        # 현재 노드 전체가 하나 이상의 사각형에 덮여 있음
        if self.cover[node] > 0:
            self.length[node] = self.xs[r + 1] - self.xs[l]

        # leaf인데 아무것도 덮지 않음
        elif l == r:
            self.length[node] = 0

        # 직접 덮고 있는 사각형은 없으므로
        # 자식들의 covered length를 합침
        else:
            self.length[node] = self.length[node * 2] + self.length[node * 2 + 1]

    def covered_length(self):
        return self.length[1]


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        events = []
        xs = []

        # 1. square -> y 이벤트 2개
        for x, y, size in squares:
            events.append((y, +1, x, x + size))
            events.append((y + size, -1, x, x + size))

            xs.append(x)
            xs.append(x + size)

        # 2. y 이벤트 정렬 + x 좌표압축
        events.sort()
        xs = sorted(set(xs))

        x_index = {x: i for i, x in enumerate(xs)}

        # 3. y sweep하면서 horizontal strip 저장
        tree = SegmentTree(xs)
        strips = []

        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]

            # prev_y ~ y에서는 활성 상태가 바뀌지 않음
            if y > prev_y:
                width = tree.covered_length()
                strips.append((prev_y, y, width))

            # y에서 발생하는 이벤트를 모두 처리
            while i < len(events) and events[i][0] == y:
                _, delta, x1, x2 = events[i]

                left = x_index[x1]
                right = x_index[x2] - 1

                tree.update(
                    1,
                    0,
                    len(xs) - 2,
                    left,
                    right,
                    delta,
                )

                i += 1

            prev_y = y

        # 4. 전체 union area
        total_area = 0

        for y1, y2, width in strips:
            total_area += (y2 - y1) * width

        # 5. 아래에서부터 절반 면적이 되는 최초 y 찾기
        area = 0

        for y1, y2, width in strips:
            # 이미 정확히 절반이라면
            # 이 y1이 가능한 최소 y
            if area * 2 == total_area:
                return float(y1)

            strip_area = (y2 - y1) * width

            if (area + strip_area) * 2 >= total_area:
                need = total_area / 2 - area

                return y1 + need / width

            area += strip_area

        return float(strips[-1][1])


# @lc code=end
