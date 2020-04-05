class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        
        ans = ""
        for i in range(len(dp)):
            dp[i][i] = True
            ans = s[i]
        max_len = 1
        
        #reverse end and start since start+1:end-1 could be unknown for this stage
        for end in range(len(s)):
            for start in range(end+1):
                if s[start] == s[end] and ( end - start < 2 or dp[start+1][end-1] ):
                    dp[start][end] = True
                    temp = end - start + 1
                    if max_len < temp:
                        max_len = temp
                        ans = s[start:end+1]
        return ans