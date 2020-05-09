# Sliding Window

## 3. Longest Substring Without Repeating Characters

```
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Solution 1. Sliding Window

* The point is, once find the word in temp, reset temp between the position of the first word to the last.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp = []
        result = 0

        for word in s:
            if word in temp:
                temp = temp[temp.index(word) + 1:]
            temp.append(word)
            result = max(len(temp),result)
        return result
```

## 76. Minimum Window Substring

```
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
```

### Solution 1. SW

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = collections.Counter(t)
        left, right = 0, 0
        ans = [left, right]
        missing = len(t)
        
        while right < len(s):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1
            right += 1
            
            while missing == 0:
                if ans[1] == 0 or ans[1] - ans[0] > right - left:
                    ans[0], ans[1] = left, right
                
                need[s[left]] += 1
                # if less than need
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[ans[0]:ans[1]]
```

## 239. Sliding Window Maximum(PENDING)

```
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
```

### Solution 1. SW

## 159. Longest Substring with At Most Two Distinct Characters

```
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
```

### Solution 1. SW

* use hashmap to store the last index of each element.
* move left when len(hashmap) == 3

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length = len(s)
        if length < 3:
            return length
        
        left, right = 0, 0
        hashmap = collections.defaultdict()
        
        ans = 0
        while right < length:
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1
                
            if len(hashmap) == 3:
                delete = min(hashmap.values())
                del hashmap[s[delete]]
                left = delete + 1
            
            ans = max(ans, right - left)
        
        return ans 
```

## 340. Longest Substring with At Most K Distinct Characters

```
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
```

### Solution 1. SW

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)
        if length < k + 1:
            return length
        
        left, right = 0, 0
        hashmap = collections.defaultdict()
        
        ans = 0
        while right < length:
            if len(hashmap) < k + 1:
                hashmap[s[right]] = right
                right += 1
                
            if len(hashmap) == k + 1:
                delete = min(hashmap.values())
                del hashmap[s[delete]]
                left = delete + 1
            
            ans = max(ans, right - left)
        
        return ans 
```

## 992. Subarrays with K Different Integers

```
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
```

### Solution 1. SW

* The problem ask for `exactly k`, the typical problem for sw is `at most k`, so we can use `at most k - at most (k-1)`
* And also for the statement `ans += right - left`, because we add the new element `right`, and to construct subarray that not occur before, you need to union each element between left and right.`[1,2,3]`, when add `3`, the subarray is `[3], [3,2], [3,2,1]`.

```python
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)
    
    def atMostK(self, s, k):
        length = len(s)
        
        left, right = 0, 0
        hashmap = collections.defaultdict(int)
        
        ans = 0
        count = 0
        
        while right < length:
            hashmap[s[right]] += 1
            if hashmap[s[right]] == 1:
                count += 1
            right += 1
            while left < right and count > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    count -= 1
                left += 1
            ans += right - left
        return ans
```

