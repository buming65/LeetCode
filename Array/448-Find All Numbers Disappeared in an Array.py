class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic.setdefault(num, 1)
        result = []
        
        for num in range(1, len(nums)+1):
            if num not in dic:
                result.append(num)
            
        return result

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = nums[index] * (-1)
        result = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                result.append(i)
        return result