## Union Find

## 200. Number of Islands

```
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
```

### Solution 1. Union Find

* Find, Union

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        self.count = sum(grid[i][j] == '1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            self.count -= 1
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j
                if i < row - 1 and grid[i+1][j] == '1':
                    union(index, index + col)
                if j < col - 1 and grid[i][j+1] == '1':
                    union(index, index + 1)
        return self.count
```

### 305. Number of Islands II

```
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
```

### Solution 1. Union Find

* 

```python
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return []
        
        self.count = 0
        parent = {}
        res = []
        adjs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(a, b):
            xroot, yroot = find(a), find(b)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            self.count -= 1
            
        for i, j in positions:
            index = i * n + j
            if index in parent:
                res.append(self.count)
                continue
            self.count += 1
            parent[index] = index
            for adj in adjs:
                x = i + adj[0]
                y = j + adj[1]
                index2 = x * n + y
                if 0 <= x < m and 0 <= y <n and index2 in parent:
                    union(index, index2)
            res.append(self.count)
        
        return res
```

## 684. Redundant Connection\684. Redundant Connection

```
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
```

### Solution 1. DFS

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for neigh in graph[source]:
                    if dfs(neigh, target):
                        return True
        
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            
            graph[u].add(v)
            graph[v].add(u)
```

### Solution 2. Union Find

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(1001)]
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return [u, v]
            parent[xroot] = yroot
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []
```

## 128. Longest Consecutive Sequence

```
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Solution 1. Hashset

* The difficult is to minimum the time consuming, with hashset, find operation is $O(1)$. 

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                temp = 1
                while current + 1 in num_set:
                    current += 1
                    temp += 1
                
                ans = max(ans, temp)
                    
        return ans
```

### Solution 2. Union Find

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            rank[yroot] += 1
        
        nums = sorted(set(nums))
        parent = {}
        rank = {}
        for num in nums:
            parent[num] = num
            rank[num] = 1
            if num - 1 in parent:
                union(num, num - 1)
        
        return max(rank.values()) if rank else 0
```

## 399. Evaluate Division

```
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
```

### Solution 1. DFS

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        tables = collections.defaultdict(dict)
        
        def dfs(x, y, tables, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for neigh in tables[x]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                d = dfs(neigh, y, tables, visited)
                if d > 0:
                    return d * tables[x][neigh]
            return -1.0
        
        ans = []
        for (x, y), value in zip(equations, values):
            tables[x][y] = value
            tables[y][x] = 1.0 / value
        
        for x, y in queries:
            temp = -1.0
            if x in tables and y in tables:
                temp = dfs(x, y, tables, set())
            ans.append(temp)
        
        return ans 
```

### Solution 2. Union Find(PENDING)

