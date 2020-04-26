class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for i in range(num+1)]
        b = 1
        i = 0
        while b <= num:
            while i < b and i + b <= num:
                ans[i + b] = ans[i] + 1
                i += 1
            i = 0
            b *= 2
        return ans 