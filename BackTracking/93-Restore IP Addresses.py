class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(ip):
            return int(ip) <= 255 if ip[0] != '0' else len(ip) == 1
        
        def insert(cur):
            temp = s[cur+1:]
            if valid(temp):
                segments.append(temp)
                result.append('.'.join(segments))
                segments.pop()
        def dfs(prev = -1, dots = 3):
            for cur in range(prev + 1, min(len(s) - 1, prev + 4)):
                segment = s[prev + 1: cur + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots == 1:
                        insert(cur)
                    else:
                        dfs(cur, dots - 1)
                    segments.pop()
                    

        result, segments = [], []
        dfs() 
        return result