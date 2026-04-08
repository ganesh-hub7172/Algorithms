class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        
        result = 0
        for num in nums:
            result ^= num
        
        return result