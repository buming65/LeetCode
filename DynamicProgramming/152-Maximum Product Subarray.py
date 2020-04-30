class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        max_dp[0], min_dp[0] = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            
        return max(max_dp)



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        prev_min = prev_max = ans = nums[0]
        
        for i in range(1, len(nums)):
            temp = prev_min
            prev_min = min(prev_max * nums[i], temp * nums[i], nums[i])
            prev_max = max(prev_max * nums[i], temp * nums[i], nums[i])
            ans = max(ans, prev_max)
        
        return ans