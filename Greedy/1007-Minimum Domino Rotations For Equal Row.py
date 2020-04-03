class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            count_a = 0
            count_b = 0
            for i in range(length):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    count_a += 1
                if B[i] != x:
                    count_b += 1
            return min(count_a, count_b)
        
        length = len(A)
        result = check(A[0])
        if result != -1 or A[0] == B[0]:
            return result
        else:
            return check(B[0])