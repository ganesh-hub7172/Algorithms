class Solution:
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # Store indices for each value
        for i in range(len(nums)):
            pos[nums[i]].append(i)
        
        ans = float('inf')
        
        # Check each value group
        for indices in pos.values():
            if len(indices) >= 3:
                # Try consecutive triples
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i+2] - indices[i])
                    ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1