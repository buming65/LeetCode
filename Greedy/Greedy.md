

# Greedy

## 253. Meeting Rooms II

```
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

### Solution 1. Priority Queues(Greedy)

* Sort by their start time
* To find if the room is available or not, using min-heap and add the first meeting's ending time to the heap. So only compare the top of the heap to see if free or not.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free = []
        
        intervals.sort(key = lambda x : x[0])
        heapq.heappush(free, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if free[0] <= intervals[i][0]:
                #Meaning there a free room
                heapq.heappop(free)
            heapq.heappush(free, intervals[i][1])
        
        return len(free)
```

* Complexity:

  * Time
    $$
    O(NlogN)
    $$
    Sorting: Takes O(NlogN) time

    For min-heap: worst O(NlogN)

  * Space
    $$
    O(N)
    $$

### Solution 2. Chronological Ordering

* Separate out the start times and the end times, Sort them separately.
* Consider two points: start_point, end_point. If sp > ep, some room is free. Else, the number of the room will be added.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        start_point = 0
        end_point = 0
        
        while start_point < len(intervals):
            if starts[start_point] >= ends[end_point]:
                count -= 1
                end_point += 1
            start_point += 1
            count += 1
        return count 
```

## 944. Delete Columns to Make Sorted

```
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

 

Example 1:

Input: ["cba","daf","ghi"]
Output: 1
Explanation: 
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:

Input: ["a","b"]
Output: 0
Explanation: D = {}
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 1000
```

### Solution 1. Greedy

* Check each column to see if they are sorted.

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for i in range(len(A[0])):
            for j in range(len(A) - 1):
                if A[j][i] > A[j+1][i]:
                    res += 1
                    break
        return res
```

* Complexity:

  * Time
    $$
    O(N)
    $$

  * Space
    $$
    O(1)
    $$

## 1007. Minimum Domino Rotations For Equal Row

```
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
```

### Solution1. Greedy

* If we want to make all the elements to be the same after rotated, then the base must be either the first of the A list or the first of the B list.

```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            count_a = 0
            count_b = 0
            for i in range(length):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    count_a += 1
                if B[i] != x:
                    count_b += 1
            return min(count_a, count_b)
        
        length = len(A)
        result = check(A[0])
        if result != -1 or A[0] == B[0]:
            return result
        else:
            return check(B[0])
```

## 1055. Shortest Way to Form String

```
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
```

### Solution1. Greedy

* So the target is constructed by the combination of the subsequence of the source.

  For the first example: source has the subsequence of "abc", "bc". target is "abcbc", so it could be constructed by "abc" + "bc".

* At first, for each element in target, find correspond position in source. If can't find, return -1.

* Then, if find a position, that means there is a subsequence, result += 1.

* And, we find source[j+1:] which is the next of the position, find target[i]. until no found in the source.

```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        result = 0
        i = 0
        while i < len(target):
            j = source.find(target[i])
            if j == -1:
                return -1
            result += 1
            while j != -1 and i < len(target) - 1:
                i += 1
                k = source[j+1:].find(target[i])
                if k == -1:
                    j = -1
                else:
                    j = j + k + 1
            if j != -1:
                i += 1
        return result

```

## 1221. Split a String in Balanced Strings

```
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
```

### Solution1. Greedy

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        temp = 0
        for i in s:
            if i == 'R':
                temp += 1
            else:
                temp -= 1
            if temp == 0:
                count += 1
        return count 
```

## 621. Task Scheduler

```
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
```

### Solution 1. Formula

* Assume $n=4, tasks=[A,A,A,A,B,B,B,C,C,C]$

* ```
  A B C idle idle
  A B C idle idle
  A B C idle idle 
  A
  ```

* Consider this as a matrix, the length is $n+1$, the width is $maxvalue -1$ 

* For the last row, for values in the task, if value equal max_value, it will add one.

* If, n is too small, then it's just the length of tasks

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = collections.defaultdict(int)
        for task in tasks:
            dic[task] += 1
        
        max_val = max(dic.values())
        
        total = (max_val-1) * (n + 1)
        for key, value in dic.items():
            if value == max_val:
                total += 1
        return max(total, len(tasks))
```

### Solution 2. Priority Queues

* I think it's same as the solution 1.

## 406. Queue Reconstruction by Height

```
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

### Solution 1. Greedy

* Sort by height, and the index, ensure that higher people will relocate first. By index is to ensure there must have equal height before the element.
* Then insert into answer, that ensure the person put on the index based on p[1] will have that many taller people before him

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0],x[1]))
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans
```

## 316. Remove Duplicate Letters

```
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
```

### Solution 1. Greedy + Stack

* The character is greater than the current characters
* The character can be removed because it occurs later on

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last = {value:index for index, value in enumerate(s)}
        
        for index, value in enumerate(s):
            if value not in stack:
                while stack and value < stack[-1] and index < last[stack[-1]]:
                    stack.pop()
                stack.append(value)
        return "".join(stack)
```

## 45. Jump Game II

```
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
```

### Solution 1. Greedy

- Initiate the maximum position that one could reach starting from the current index `i` or before: `max_pos = nums[0]`.
- Initiate the maximum position reachable *during* the current jump: `max_steps = nums[0]`.
- Initiate number of steps: at least one, if array has more than 1 cell.
- Iterate over number of elements in the input array:
  - If `max_step < i`, one needs one more jump: `jumps += 1`. To minimize the number of jumps, choose the longest possible one: `max_steps = max_pos`.
  - Update `max_pos = max(max_pos, i + nums[i])`.
- Return the number of jumps.

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_pos, max_steps = nums[0], nums[0]
        
        jumps = 1
        for i in range(1, len(nums)):
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)
            
        return jumps
```

## 134. Gas Station

```
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

### Solution 1. Greedy

**Algorithm**

Now the algorithm is straightforward :

1. Initiate `total_tank` and `curr_tank` as zero, and choose station `0` as a starting station.
2. Iterate over all stations :
   - Update `total_tank` and `curr_tank` at each step, by adding `gas[i]` and subtracting `cost[i]`.
   - If `curr_tank < 0` at `i + 1` station, make `i + 1` station a new starting point and reset `curr_tank = 0` to start with an empty tank.
3. Return `-1` if `total_tank < 0` and `starting station` otherwise.

* Notice the problem indicate that `if there exists a solution, it's guaranteed to be unique.` So generally, if we find the station that with the negative `curr_tank`, we need to search the loop to ensure it could reach the prev station. But with unique solution, there's no necessary to loop again.

> How one could ensure that it's possible to loop around to $$N_s$$ ?

Let's use here the [proof by contradiction](https://en.wikipedia.org/wiki/Proof_by_contradiction) and assume that there is a station 0 < k < N_s0<*k*<*N**s* such that one couldn't reach this station starting from N_s*N**s*.

The condition `total_tank >= 0` could be written as

$$\sum_{i = 0}^{i = N}{\alpha_i} \ge 0 \qquad (1)$$ where $$\alpha_i = \textrm{gas[i]} - \textrm{cost[i]}$$

Let's split the sum on the right side by the starting station $$N_s$$ and unreachable station `k` :

$$\sum_{i = 0}^{i = k}{\alpha_i} + \sum_{i = k + 1}^{i = N_s - 1}{\alpha_i} + \sum_{i = N_s}^{i = N}{\alpha_i} \ge 0 \qquad (2)$$

The second term is negative by the algorithm definition - otherwise the starting station would be before $$N_s$$. It could be equal to zero only in the case of $$k = N_s - 1$$.

$$\sum_{i = k + 1}^{i = N_s - 1}{\alpha_i} \le 0 \qquad (3)$$

Equations `(2)` and `(3)` together results in

$$\sum_{i = 0}^{i = k}{\alpha_i} + \sum_{i = N_s}^{i = N}{\alpha_i} \ge 0 \qquad (4)$$

At the same time the station k*k* is supposed to be unreachable from $$N_s$$that means

$$\sum_{i = N_s}^{i = N}{\alpha_i} + \sum_{i = 0}^{i = k}{\alpha_i} < 0 \qquad (5)$$

Eqs. `(4)` and `(5)` together result in a contradiction. Therefore, the initial assumption — that there is a station $$0 < k < N_s$$such that one couldn't reach this station starting from $$N_s$$ — must be false.

Hence, one could do a round trip starting from$$ N_s$$, that makes $$N_s$$ to be an answer. The answer is unique according to the problem definition.

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        start_pos = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start_pos = i + 1
                curr = 0
        return start_pos if total >= 0 else -1
```

## 763. Partition Labels

```
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
```

### Solution 1. Greedy

* Check the interval, to search the max interval.
* We need an array `last[char] -> index of S where char occurs last`. Then, let `anchor` and `j` be the start and end of the current partition. If we are at a label that occurs last at some index after `j`, we'll extend the partition `j = last[c]`. If we are at the end of the partition (`i == j`) then we'll append a partition size to our answer, and set the start of our new partition to `i+1`.

```python 
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {value: index for index, value in enumerate(S)}
        max_index, pivot = 0, 0
        ans = []
        
        for index, value in enumerate(S):
            max_index = max(max_index, last[value])
            if index == max_index:
                ans.append(max_index - pivot + 1)
                pivot = max_index + 1
        
        return ans 
```

## 135. Candy

```
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
```

### Solution 1. Two Arrays (One Array) 

* In this approach, we make use of two 1-d arrays $$left2right$$ and $$right2left$$. The $$left2right$$ array is used to store the number of candies required by the current student taking care of the distribution relative to the left neighbours only. i.e. Assuming the distribution rule is: The student with a higher ratings than its left neighbour should always get more candies than its left neighbour. Similarly, the $$right2left$$ array is used to store the number of candies candies required by the current student taking care of the distribution relative to the right neighbours only. i.e. Assuming the distribution rule to be: The student with a higher ratings than its right neighbour should always get more candies than its right neighbour. To do so, firstly we assign 1 candy to each student in both $$left2right$$ and $$right2left$$ array. Then, we traverse the array from left-to-right and whenever the current element's ratings is larger than the left neighbour we update the current element's candies in the $$left2right$$ array as $$left2right[i] = left2right[i-1] + 1$$, since the current element's candies are always less than or equal candies than its left neighbour before updation. After the forward traversal, we traverse the array from left-to-right and update $$right2left[i]$$ as $$right2left[i] = right2left[i + 1] + 1$$, whenever the current ( $$i^{th}$$ ) element has a higher ratings than the right ( $$(i+1)^{th}$$ element.

  Now, for the $$i^{th}$$ student in the array, we need to give $$\text{max}(left2right[i], right2left[i])$$ to it, in order to satisfy both the left and the right neighbour relationship. Thus, at the end, we obtain the minimum number of candies required as:

  $$\text{minimum_candies}=\sum_{i=0}^{n-1} \text{max}(left2right[i], right2left[i]), \text{where } n = \text{length of the ratings array.}$$

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                right2left[i-1] = right2left[i] + 1
        
        ans = [0] * len(ratings)
        
        for i in range(len(ratings)):
            ans[i] = max(left2right[i], right2left[i])
            
        return sum(ans)

```

### Solution 2. Single Pass(Pending)

* 

## 1111. Maximum Nesting Depth of Two Valid Parentheses Strings(PENDING)

```
A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

 

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length).

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.
```

### Solution 1. Greedy

* 