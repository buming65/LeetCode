class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            temp = 0
            for j in range(i+1):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        return max(dp)


