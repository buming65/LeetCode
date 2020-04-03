class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        temp = 0
        for i in s:
            if i == 'R':
                temp += 1
            else:
                temp -= 1
            if temp == 0:
                count += 1
        return count 