class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * (len(nums)+2)
        dp[0] = 0
        dp[1] = 0
        
        #there are two zero position
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-2]+nums[i-2], dp[i-1])
        return max(dp[-1], dp[-2])
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        #pre: two behind, cur: one behind
        for i in range(len(nums)):
            temp = cur
            cur = max(pre+nums[i], cur)
            pre = temp
        return cur