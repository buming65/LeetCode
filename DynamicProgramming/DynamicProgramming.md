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

## 647. Palindromic Substrings

```
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
```

### Solution 1. DP

* Use dp to store the status for each substring
* $dp[i,i] = True$
* $dp[j,i] = (s[i]==s[j])\ if\ i-j >=2$
* $dp[j,i] = (s[i]==s[j]\ and \ dp[j+1][i-1])$

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
        
        ans = 0
        
        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (s[i] == s[j] and dp[j+1][i-1])
        
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[j][i]:
                    ans += 1
        return ans
```

### Solution 2. Manacher Algorithm

* See the analysis in README for this algorithm

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            A = '^#' + '#'.join(s) + '#$'
            P = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    P[i] = min(right-i, P[2*center - i])
                while A[i+P[i]+1] == A[i-P[i]-1]:
                    P[i] += 1
                if i + P[i] > right:
                    center, right = i, i + P[i]
            return P
        
        P = manacher(s)
        ans = 0
        for raduis in P:
            ans += ((raduis+1) // 2)
        return ans 
```

### Solution 3. Expand Around Center

* Choose a center, from this point, move to left and right.
* There're $2N-1$ centers, because the substring could be odd and even 

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        for center in range(len(s)):
            self.helper(s, center, center)
            self.helper(s, center-1, center)
        return self.ans
            
            
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            self.ans += 1
```

* Complexity:
  * Time $O(N^2)$
  * Space $O(1)$

## 494. Target Sum

```
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
```

### Solution 1. DP

* Set the key as the number of total sum, the value is the times that could reach this value at this point.
* So every time, use the last dictionary to compute the next dictionary
* For the last dictionary, the $key==S$ is the result.

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums or sum(nums) < S:
            return 0
        dic = {0:1}
        for i in range(len(nums)):
            temp = collections.defaultdict(int)
            for d in dic:
                temp[d+nums[i]] += dic[d]
                temp[d-nums[i]] += dic[d]
            dic = temp
        return dic[S]
```

## 416. Partition Equal Subset Sum

```
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

### Solution 1. DP

* Key is the sum, value is Boolean, indicate that this sum could be reached or not.
* Since the two subarray are equal in sum, so target could be determined.
* Plus this number only could reach in $nums[i], target$, Beyond target are not considered.
* And if $dp[j-nums[i]]$ is true, that means $dp[j]$ is reachable since there's already a sum.
* So the formula could be $dp[i] = dp[i]\ ||\ dp[i-sum]$ 

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = int(sum_nums / 2)
        dp = [False] * (sum_nums + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = (dp[i] or dp[i - num])
        return dp[target] == True

```

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = int(sum_nums / 2)
        dp = [False] * (sum_nums + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(sum_nums, -1, -1):
                if dp[i]:
                    dp[num+i] = dp[i] 
        return dp[target] == True

```

## 322. Coin Change

```
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
```

### Solution 1. DP

* Like the last problem, the key is the sum, the value is the min number of coins that reach this sum.
* $dp[i] = min(dp[i], dp[i-num]+1)$

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for num in coins:
            for i in range(num, amount+1):
                dp[i] = min(dp[i], dp[i-num]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
    
```

## 309. Best Time to Buy and Sell Stock with Cooldown

```
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

### Solution 1. DP

* 

```

```

## 300. Longest Increasing Subsequence

```
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
```

### Solution 1. DP

* Key is the number in the input list, value is the number of elements before that are smaller than this number.
* $DP[x]=max(DP[i])+1,0\le i \le x$

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            temp = 0
            for j in range(i+1):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        return max(dp)
```

* Complexity:
  * Time $O(n^2)$
  * Space $O(n)$

### Solution 2. DP + Binary Search(PENDING)

* Use Binary Search to make the time complexity become $O(nlogn)$
* [Refer][https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation]

```

```

