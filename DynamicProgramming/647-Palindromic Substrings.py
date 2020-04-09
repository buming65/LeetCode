class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
        
        ans = 0
        
        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (s[i] == s[j] and dp[j+1][i-1])
        
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[j][i]:
                    ans += 1
        return ans



class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        for center in range(len(s)):
            self.helper(s, center, center)
            self.helper(s, center-1, center)
        return self.ans
            
            
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            self.ans += 1
    

class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            A = '^#' + '#'.join(s) + '#$'
            P = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    P[i] = min(right-i, P[2*center - i])
                while A[i+P[i]+1] == A[i-P[i]-1]:
                    P[i] += 1
                if i + P[i] > right:
                    center, right = i, i + P[i]
            return P
        
        P = manacher(s)
        ans = 0
        for raduis in P:
            ans += ((raduis+1) // 2)
        return ans 