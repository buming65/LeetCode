class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)
    
    def atMostK(self, s, k):
        length = len(s)
        
        left, right = 0, 0
        hashmap = collections.defaultdict(int)
        
        ans = 0
        count = 0
        
        while right < length:
            hashmap[s[right]] += 1
            if hashmap[s[right]] == 1:
                count += 1
            right += 1
            while left < right and count > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    count -= 1
                left += 1
            ans += right - left
        return ans