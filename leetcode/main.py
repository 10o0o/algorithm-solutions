class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        def merge(a, b):
            if a[0] == 0:
                return b
            if b[0] == 0:
                return a

            a_len, a_pre, a_suf, a_zero = a
            b_len, b_pre, b_suf, b_zero = b

            length = a_len + b_len

            if a_pre == b_len:
                prefix = b_len + a_suf
            else:
                prefix = b_suf

            if b_suf == b_len:
                suffix = b_len + a_suf
            else:
                suffix = b_suf

            zero_count = a_zero + b_zero + a_suf * b_pre
            return {length, prefix, suffix, zero_count}

        return [0]


Solution().countOfPeaks([1, 3, 2, 4], [[1]])
