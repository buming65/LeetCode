# Dynamic Programming

## 5. Longest Palindromic Substring

```
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
```

### Solution 1. DP

* Saying the case "ababa", if we know "bab" is a palindrome, and the left and the right is same, so obviously, "ababa" is palindrome.
* So define P(i, j) = true if the substring from i to j is palindrome, else P( i, j) = false.
* The base condition is P(i, i) = true, P(i, i+1) = (S(i) == S(i+1))

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        
        ans = ""
        for i in range(len(dp)):
            dp[i][i] = True
            ans = s[i]
        max_len = 1
        
        #reverse end and start since start+1:end-1 could be unknown for this stage
        for end in range(len(s)):
            for start in range(end+1):
                if s[start] == s[end] and ( end - start < 2 or dp[start+1][end-1] ):
                    dp[start][end] = True
                    temp = end - start + 1
                    if max_len < temp:
                        max_len = temp
                        ans = s[start:end+1]
        return ans
```

## 70. Climbing Stairs

```
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Solution 1. DP

* The formula is $dp[i] = dp[i-1]+dp[i-2]$.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
```

## 121. Best Time to Buy and Sell Stock

```
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### Solution 1. One Pass

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_price:
                max_price = i - min_price
        return max_price
```

## 122. Best Time to Buy and Sell Stock II

```
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### Solution 1. One Pass

* For $i-1, i$, If $nums[i] > nums[i-1]$, then $sum += nums[i]-nums[i-1]$ .

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i]-prices[i-1])
        return max_profit
```



## 139. Word Break

```
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

### Solution 1. DP

* Two index pointers $i, j$ . $DP[i] = DP[j] + substring(j, i) $

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #DP
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]
```

### Solution 2. BFS

* From the start, find all the possibilities that the word in dictionary. Use queue maintain bfs.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #BFS
        #Every time search the neighbor
        #And mark as visited
        visit = [0] * len(s)
        queue = [0]
        while queue:
            start = queue[0]
            queue.pop(0)
            if visit[start] != 1:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
            visit[start] = 1
        return False
        
```

## 198. House Robber

```
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

### Solution 1. DP

* $f(k) = max\{f(k-2)+A_k,f(k-1)\}$

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * (len(nums)+2)
        dp[0] = 0
        dp[1] = 0
        
        #there are two zero position
        for i in range(2, len(nums)+2):
            dp[i] = max(dp[i-2]+nums[i-2], dp[i-1])
        return max(dp[-1], dp[-2])
        
```

### Solution 2 Improve DP

* Only need to remember two pointers, cur and pre

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        #pre: two behind, cur: one behind
        for i in range(len(nums)):
            temp = cur
            cur = max(pre+nums[i], cur)
            pre = temp
        return cur
```

## 1027. Longest Arithmetic Sequence

```
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```

### Solution 1. DP

* Double traverse, find the difference between two element, set the difference as key, value is the number of the elements.
* $DP[k]$ is a dictionary that the difference is key, value is the number of element that has the same difference to k.
* $\ if \ A[j] - A[i] = dif, \ if\ dif\ in\ A[j], A[i][dif] = A[j][dif]+1 $

```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        result = 0
        for i in range(1, len(A)):
            for j in range(i):
                dif = A[j] - A[i]
                if dif in dp[j]:
                    dp[i][dif] = dp[j][dif] + 1
                else:
                    dp[i][dif] = 2
                result = max(dp[i][dif], result)
        return result
```

