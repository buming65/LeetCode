class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        result = 0
        for i in range(1, len(A)):
            for j in range(i):
                dif = A[j] - A[i]
                if dif in dp[j]:
                    dp[i][dif] = dp[j][dif] + 1
                else:
                    dp[i][dif] = 2
                result = max(dp[i][dif], result)
        return result