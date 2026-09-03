#
# @lc app=leetcode id=3953 lang=python3
#
# [3953] Maximum Score with Co-Prime Element
#

# @lc code=start
from math import isqrt


class Solution:
    def maxScore(self, nums: list[int], maxVal: int) -> int:
        M = max(max(nums), maxVal)

        # 값별 등장 횟수
        freq = [0] * (M + 1)

        for num in nums:
            freq[num] += 1

        # div_count[d]:
        # nums 중 d의 배수인 원소 개수
        div_count = [0] * (M + 1)

        for d in range(1, M + 1):
            for multiple in range(d, M + 1, d):
                div_count[d] += freq[multiple]

        # smallest prime factor
        spf = list(range(M + 1))

        for p in range(2, isqrt(M) + 1):
            if spf[p] == p:
                for multiple in range(p * p, M + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # x와 서로소가 아닌 nums 원소 개수
        def get_bad(x):
            if x == 1:
                return 0

            # 서로 다른 소인수만 추출
            primes = []

            while x > 1:
                p = spf[x]
                primes.append(p)

                while x % p == 0:
                    x //= p

            bad = 0
            k = len(primes)

            # 포함배제
            for mask in range(1, 1 << k):
                divisor = 1
                count = 0

                for i in range(k):
                    if mask & (1 << i):
                        divisor *= primes[i]
                        count += 1

                if count % 2 == 1:
                    bad += div_count[divisor]
                else:
                    bad -= div_count[divisor]

            return bad

        # 후보:
        # 1 ~ maxVal은 새로 만들 수 있고
        # 기존 nums 값은 maxVal보다 커도 그대로 선택 가능
        candidates = set(nums)

        for x in range(1, maxVal + 1):
            candidates.add(x)

        ans = -(10**18)

        for x in candidates:
            bad = get_bad(x)

            if freq[x] > 0:
                # 이미 x가 있으므로 그 x를 selected로 사용
                if x == 1:
                    cost = 0
                else:
                    cost = bad - 1

            else:
                # x 자체를 만들기 위한 수정이 하나는 필요
                cost = max(1, bad)

            ans = max(ans, x - cost)

        return ans


# @lc code=end
