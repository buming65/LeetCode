class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 or not nums:
            return []
        nums.sort()
        result = set()
        for i in range(len(nums)):
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            d = {}
            for j in range(i+1, len(nums)):
                if nums[j] not in d:
                    d[-nums[i]-nums[j]] = 0
                else:
                    result.add((nums[i],-nums[j]-nums[i],nums[j]))
        return result