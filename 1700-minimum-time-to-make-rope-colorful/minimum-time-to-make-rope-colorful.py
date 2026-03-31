class Solution:
    def minCost(self, colors, neededTime):
        total = 0
        prev_time = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # remove the smaller one
                total += min(prev_time, neededTime[i])
                
                # keep the larger one
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_time = neededTime[i]
        
        return total