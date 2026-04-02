class Solution:
    def maximumAmount(self, coins):
        m = len(coins)
        n = len(coins[0])
        
        # dp[i][j][k] => max coins at (i,j) using k neutralizations
        dp = [[[-10**15]*3 for _ in range(n)] for _ in range(m)]
        
        # Start position
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                # either take loss or neutralize if possible
                dp[0][0][k] = coins[0][0]
                if k > 0:
                    dp[0][0][k] = max(dp[0][0][k], 0)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    best_prev = -10**15
                    
                    if i > 0:
                        best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j-1][k])
                    
                    if best_prev == -10**15:
                        continue
                    
                    # Case 1: take value
                    dp[i][j][k] = max(dp[i][j][k], best_prev + coins[i][j])
                    
                    # Case 2: neutralize robber (if negative)
                    if coins[i][j] < 0 and k > 0:
                        best_prev_kminus = -10**15
                        
                        if i > 0:
                            best_prev_kminus = max(best_prev_kminus, dp[i-1][j][k-1])
                        if j > 0:
                            best_prev_kminus = max(best_prev_kminus, dp[i][j-1][k-1])
                        
                        if best_prev_kminus != -10**15:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_kminus)
        
        return max(dp[m-1][n-1])