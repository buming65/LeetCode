class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Divide and Conquer
        def helper(left, right):
            if left == right:
                return nums[left]
            mid = left + (right - left) // 2
            left_element = helper(left, mid)
            right_element = helper(mid+1, right)
            
            if left_element == right_element:
                return left_element
            
            left_count = sum(1 for i in range(left, right+1) if nums[i] == left_element)
            right_count = sum(1 for i in range(left, right+1)if nums[i] == right_element)
            return left_element if left_count > right_count else right_element
        
        return helper(0, len(nums)-1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #hash
        dic = {}
        for num in nums:
            if num not in dic:
                dic.setdefault(num, 0)
            dic[num] += 1
        dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
        print(dic)
        return dic[0][0]
