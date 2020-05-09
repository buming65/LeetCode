class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length = len(s)
        if length < 3:
            return length
        
        left, right = 0, 0
        hashmap = collections.defaultdict()
        
        ans = 0
        while right < length:
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1
                
            if len(hashmap) == 3:
                delete = min(hashmap.values())
                del hashmap[s[delete]]
                left = delete + 1
            
            ans = max(ans, right - left)
        
        return ans 