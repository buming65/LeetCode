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

