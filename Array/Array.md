# Array

## 448. Find All Numbers Disappeared in an Array

```
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

### Solution 1. Hash Table

* Use hash table

```python
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
```

* Complexity:
  * Time: $O(N)$
  * Space: $O(N)$

### Solution 2. $O(1)$ Space Solution

* This method is set the element as the index, for example, 3 put into the third position.
* Since the elements only appear once or twice, so we set the index negative, and if the index is negative, skip the element.

```python
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
```

## 581. Shortest Unsorted Continuous Subarray

```
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
```

### Solution 1. Sort

* Sort the list, find the left most and right most

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #Sort
        sort_nums = sorted(nums)
        start = len(nums) - 1
        end = 0
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:
                start = min(start, i)
                end = max(end, i)
        
        return end - start + 1 if end - start > 0 else 0
```

### Solution 2. Stack 

## 15. 3Sum

```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### Solution 1.

```python
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
```

