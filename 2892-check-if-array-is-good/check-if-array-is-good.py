class Solution:
    def isGood(self, nums):
        n = max(nums)

        # Length must be n + 1
        if len(nums) != n + 1:
            return False

        nums.sort()

        # Expected array: [1, 2, ..., n, n]
        expected = list(range(1, n + 1)) + [n]

        return nums == expected