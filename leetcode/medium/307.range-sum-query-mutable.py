#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.n = n
        self.tree = [0] * (n * 2)

        for i in range(n):
            self.tree[i + n] = nums[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n
        self.tree[i] = val

        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        total = 0

        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1

            if right % 2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
