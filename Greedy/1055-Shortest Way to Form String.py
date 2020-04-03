class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        result = 0
        i = 0
        while i < len(target):
            j = source.find(target[i])
            if j == -1:
                return -1
            result += 1
            while j != -1 and i < len(target) - 1:
                i += 1
                k = source[j+1:].find(target[i])
                if k == -1:
                    j = -1
                else:
                    j = j + k + 1
            if j != -1:
                i += 1
        return result
