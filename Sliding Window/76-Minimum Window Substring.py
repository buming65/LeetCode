class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = collections.Counter(t)
        left, right = 0, 0
        ans = [left, right]
        missing = len(t)
        
        while right < len(s):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1
            right += 1
            
            while missing == 0:
                if ans[1] == 0 or ans[1] - ans[0] > right - left:
                    ans[0], ans[1] = left, right
                
                need[s[left]] += 1
                # if less than need
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[ans[0]:ans[1]]
        