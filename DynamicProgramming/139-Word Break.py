class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #BFS
        #Every time search the neighbor
        #And mark as visited
        visit = [0] * len(s)
        queue = [0]
        while queue:
            start = queue[0]
            queue.pop(0)
            if visit[start] != 1:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
            visit[start] = 1
        return False
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #DP
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]