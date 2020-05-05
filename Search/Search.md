# Search 

## 695. Max Area of Island

```
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
```

### Solution 1. DFS

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in seen or not grid[r][c]:
                return 0
            seen.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
        return max(dfs(r,c)
                  for r in range(len(grid))
                  for c in range(len(grid[0])))
```

## 694. Number of Distinct Islands

```
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
```

### Solution 1. Coordinates

```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        queue = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    shape = []
                    
                    while queue:
                        r, c = queue.pop(0)
                        for nr, nc in (r+1, c), (r-1,c), (r,c+1), (r,c-1):
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr,nc))
                                shape.append((nr-i, nc-j))
                    
                    islands.add(tuple(shape))
        
        return len(islands)
```

## 909. Snakes and Ladders

![img](Search.assets/snakes.png)

```
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
```

* This problem is say there's a ladder of snaketo jump into the destination.
* If `S` has a snake or ladder, you move to the destination of that snake or ladder. Otherwise, you move to `S`. It's means it always jump when there's a snake or ladder.

### Solution 1. BFS

* Use queue to memory each step's possibility, use hashtable to remember the destination.

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def get(s):
            #need to minus 1, the distance 
            x, y = (s-1) // N, (s-1) % N
            
            row = N - 1 - x
            col = y if row % 2 != N % 2 else N - 1 - y
            return row, col
        
        dist = collections.defaultdict(int)
        dist[1] = 0
        
        queue = collections.deque([1])
        
        while queue:
            temp = queue.popleft()
            if temp == N * N:
                return dist[temp]
            
            for i in range(temp + 1, min(N*N, temp+6)+1):
                row, col = get(i)
                if board[row][col] != -1:
                    i = board[row][col]
                if i not in dist:
                    dist[i] = dist[temp] + 1
                    queue.append(i)
        return -1
```

