class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = int(sum_nums / 2)
        dp = [False] * (sum_nums + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = (dp[i] or dp[i - num])
        return dp[target] == True

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = int(sum_nums / 2)
        dp = [False] * (sum_nums + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(sum_nums, -1, -1):
                if dp[i]:
                    dp[num+i] = dp[i] 
        return dp[target] == True
