class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        ans = 0
        while a:
            if a & 1:
                ans += 1
            a = a >> 1
        return ans 