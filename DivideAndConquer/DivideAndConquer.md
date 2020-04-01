# Divide And Conquer

## 53. Maximum Subarray

```markdown
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
```

### Solution 1. Divide and Conquer

* Similar with the merge sort.
* if n == 1: return this single element.
* Middle element's index (left + right) / 2.
* left_sum = maxSubArray for the left subarray.
* right_sum = maxSubArray for the right subarray.
* cross_sum =  max sum of the subarray containing elements from both left and right subarrays and hence crossing the middle element.

![pic](DivideAndConquer.assets/dc.png)

* Red is the middle element, purple is the element which the max sum should contain.
* Green is the left list, blue is the right list.

```python
class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum
        
#        {
#            [-2, 1, -3]: left = 0, p = 1, right = 2
#            {first range: [1, -2], max: 1.
#             second range: [-3], max: -3.
#             sum = 1 - 3 = -2}
#        }
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
```

* Complexity

  * Time
    $$
    O(N logN)
    $$

  * Space
    $$
    O(NlogN)
    $$

### Solution 2. Greedy



### Solution 3. DP





## 215. Kth Largest Element in an Array

```
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

### Solution 1. Sort

### Solution 2. Heap

### Solution 3. QuickSort



## 240. Search a 2D Matrix II

```
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
```

### Solution 1. Brute Force

#### Complexity

* Time: 

$$
O(NM)
$$

* Space

$$
O(1)
$$

### Solution 2. Binary Search

### Solution 3. Divide and Conquer

* Two Cases
  * Base Cases: if the target is smaller than the smallest element(top-left corner) or greater than the greatest element(bottom-right corner), then it definitely not present.
  * Recursive Cases: The target is potentially present. So search 

