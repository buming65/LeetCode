class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        ans = 0
        while right < len(A):
            if A[right] == 0:
                K -= 1
            
            right += 1
            
            while K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            
            ans = max(ans, right - left)
        return ans 