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

* current element
* current element + local sum

```python
class Solution:    
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(cur_sum, max_sum)
        
        return max_sum
```

### Solution 3. DP

* DP[i] = max(DP[i-1], 0) + arr[i]

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
```



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

  * Base Cases 
    * if the target is smaller than the smallest element(top-left corner) 
    * Greater than the greatest element(bottom-right corner), then it definitely not present.
  * Recursive Cases 
    * The target is potentially present. 
    * Locate matrix (row-1, mid) < target < (row,mid). Search along the matrix's middle, if find during this process, return true
    * Else, search (left, row, mid-1, down)(target < matrix(row, mid), target in the bottom-left part.) or (mid+1, up, right, row-1)(target > matrix(row,mid), target in the top-right part) (just two sectors of the matrix)

  ```python
  class Solution:
      def searchMatrix(self, matrix, target):
          """
          :type matrix: List[List[int]]
          :type target: int
          :rtype: bool
          """
          if not matrix:
              return False
          def search(left, up, right, down):
              if left > right or up > down:
                  return False
              if target < matrix[up][left] or target > matrix[down][right]:
                  return False
              
              mid = left + (right - left)//2
              
              # Locate
              row = up
              while row <= down and matrix[row][mid] <= target:
                  if matrix[row][mid] == target:
                      return True
                  row += 1
              return search(left, row, mid - 1, down) or search(mid + 1, up, right, row - 1)
          
          return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
  ```

* Complexity(Pending)

  * Time
    $$
    O(nlogn)
    $$

  * Space
    $$
    O(logn)
    $$

### Solution 4. Search Space Reduction

* From the bottom-left. 
  * If current is larger than target, row up.
  * If current is smaller than target, column right.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        
        r = row - 1
        c = 0
        
        while r >= 0 and c < col:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False
```

## 973. K Closest Points to Origin

```
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
```

### Solution 1. Sort

* In python, default algorithm for sorted method is tim-sort which could be considered as the combination of merge sort and insertion sort.

* Complexity

  * Time
    $$
    O(NlogN)
    $$

  * Space
    $$
    O(N)
    $$

### Solution 2. Divide and Conquer

* Quick Sort

* Pick a random pivot, if K > mid, then all the element in the left will put out, and K-mid+1 elements will be sorted, saying the right list need partially sort. If K < mid, then partially sort the left side.

  ```python
  def kClosest(self, points, K):
      dist = lambda i: points[i][0]**2 + points[i][1]**2
  
      def findKthSmallest(nums, start, end, kth):
  	    # kth is zero based
          left, right = start, end
          mid = (left + right)//2
          pivot = dist(mid)
  
          while left <= right:
              while left <= right and dist(left) < pivot:
                  left += 1
              while left <= right and dist(right) > pivot:
                  right -= 1
              if left <= right:
                  nums[left], nums[right] = nums[right], nums[left]
                  left, right = left + 1, right - 1
  
          if kth <= right:
              return findKthSmallest(nums, start, right, kth)
          elif kth >= left:
              return findKthSmallest(nums, left, end, kth)
          else:
              return nums[:kth+1]
  
      return findKthSmallest(points, 0, len(points) - 1, K-1)
  ```
