# Others

## 283. Move Zeroes

```
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
```

### Solution 1. Two pointers

* Set cur as the non-zero position.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        return nums
```

## 202. Happy Number

```
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

### Solution 1. HashSet

* Store in the hashset to seen whether appear before or not.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                temp = n % 10
                n = n // 10
                total += temp ** 2
            n = total
        return n == 1
```

### Solution 2. Floyd Cycle Detection Algorithm

* Given two pointers with fast and slow speed, if there is a cycle, they must meet finally.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                temp = number % 10
                number = number // 10
                total += temp ** 2
            return total
        
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
```