class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        ans = max(max(dp))
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    ans = max(dp[i][j], ans)
        return ans * ans 



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [0 for i in range(len(matrix[0]) + 1)]
        
        ans = 0
        prev = 0
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j],dp[j-1],prev) + 1
                    ans = max(dp[j], ans)
                else:
                    dp[j] = 0
                prev = temp
        return ans * ans 