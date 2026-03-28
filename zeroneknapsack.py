#tabulation
class Solution:
    def knapSack(self, W, wt, val, n):
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                
                if wt[i-1] <= w:
                    # include or exclude
                    dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]],
                                   dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n][W]
W = 4
wt = [1, 2, 3]
val = [4, 5, 1]
n = 3
#space optimized
class Solution:
    def knapSack(self, W, wt, val, n):
        dp = [0] * (W + 1)
        
        for i in range(n):
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
        
        return dp[W]