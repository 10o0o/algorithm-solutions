#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)

        # 1. 왼쪽부터 정렬된 prefix의 끝
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        # 이미 전체가 정렬됨
        if left == n - 1:
            return 0

        # 2. 오른쪽부터 정렬된 suffix의 시작
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # prefix를 전부 버리거나 suffix를 전부 버리는 경우
        answer = min(
            n - left - 1,  # suffix 제거
            right,  # prefix 제거
        )

        # 3. 정렬된 prefix와 suffix를 이어 붙이기
        i = 0
        j = right

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # i와 j 사이를 제거
                answer = min(answer, j - i - 1)
                i += 1
            else:
                j += 1

        return answer


# @lc code=end
