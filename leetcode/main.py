from math import isqrt


class Solution:
    def validSubarrays(self, nums, k, queries):
        n = len(nums)
        block = isqrt(n) + 1

        qs = []

        for idx, (l, r) in enumerate(queries):
            qs.append((l, r, idx))

        qs.sort(
            key=lambda q: (
                q[0] // block,
                q[1] if (q[0] // block) % 2 == 0 else -q[1],
            )
        )

        freq = {}
        distinct = 0
        odd_count = 0

        def add(x):
            nonlocal distinct, odd_count

            old = freq.get(x, 0)

            if old == 0:
                distinct += 1

            if old % 2 == 0:
                odd_count += 1
            else:
                odd_count -= 1

            freq[x] = old + 1

        def remove(x):
            nonlocal distinct, odd_count

            old = freq[x]

            if old % 2 == 0:
                odd_count += 1
            else:
                odd_count -= 1

            freq[x] = old - 1

            if freq[x] == 0:
                distinct -= 1

        ans = [False] * len(queries)

        cur_l = 0
        cur_r = -1

        for l, r, idx in qs:
            while cur_l > l:
                cur_l -= 1
                add(nums[cur_l])

            while cur_r < r:
                cur_r += 1
                add(nums[cur_r])

            while cur_l < l:
                remove(nums[cur_l])
                cur_l += 1

            while cur_r > r:
                remove(nums[cur_r])
                cur_r -= 1

            ans[idx] = distinct == k and odd_count == 0

        return ans
