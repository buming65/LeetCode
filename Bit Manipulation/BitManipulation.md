# Bit Manipulation

## 136. Single Number

```
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
```

### Solution 1. Hash Table

* Iterate all elements in nums and set up key / value pair
* Return the element that appeared only once.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for i in nums:
            if i not in table:
                table.setdefault(i, 0)
            table[i] += 1
        
        for i in table:
            if table[i] == 1:
                return i
```

### Solution 2. Bit Manipulation

* Use XOR, a XOR 0 = a, a XOR a = 0, a XOR b XOR a = ( a XOR a ) XOR b = 0 XOR b = b
* Only when there only twice and ones number in the nums

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```

* Complexity
  * Time $O(n)$
  * Space $O(1)$

## 461. Hamming Distance

```
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

### Solution 1. Bit Manipulation

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        ans = 0
        while a:
            if a & 1:
                ans += 1
            a = a >> 1
        return ans 
```

