

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

