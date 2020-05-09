class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)
        if length < k + 1:
            return length
        
        left, right = 0, 0
        hashmap = collections.defaultdict()
        
        ans = 0
        while right < length:
            if len(hashmap) < k + 1:
                hashmap[s[right]] = right
                right += 1
                
            if len(hashmap) == k + 1:
                delete = min(hashmap.values())
                del hashmap[s[delete]]
                left = delete + 1
            
            ans = max(ans, right - left)
        
        return ans 