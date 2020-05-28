# 找出数组中重复的数字。 
# 
#  
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。 
# 
#  示例 1： 
# 
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
#  
# 
#  
# 
#  限制： 
# 
#  2 <= n <= 100000 
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    #Solution 1. Sort the array, then traverse the array, O(nlogn)
    '''
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp == nums[i]:
                return temp
            temp = nums[i]
    '''

    #Solution 2. HashMap, O(n) space O(n)
    '''
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            else:
                return nums[i]
                
    '''

    #Solution 3. Index, O(n) Space O(1)
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return None

# leetcode submit region end(Prohibit modification and deletion)
