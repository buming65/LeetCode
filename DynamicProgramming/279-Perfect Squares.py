class Solution:
    def numSquares(self, n: int) -> int:
        square = [i ** 2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float("inf") for i in range(n+1)]
        
        dp[0] = 0
        
        for i in range(1, n+1):
            for s in square:
                if i < s:
                    break
                dp[i] = min(dp[i], dp[i-s]+1)
        return dp[-1]