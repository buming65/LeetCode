class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for i in nums:
            if i not in table:
                table.setdefault(i, 0)
            table[i] += 1
        
        for i in table:
            if table[i] == 1:
                return i

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a