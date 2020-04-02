class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(first = 0):
            if first == len(nums):
                result.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first+1)
                nums[first], nums[i] = nums[i], nums[first]
                
        result = []
        dfs(first = 0)
        return result