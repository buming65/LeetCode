class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                right2left[i-1] = right2left[i] + 1
        
        ans = [0] * len(ratings)
        
        for i in range(len(ratings)):
            ans[i] = max(left2right[i], right2left[i])
            
        return sum(ans)
