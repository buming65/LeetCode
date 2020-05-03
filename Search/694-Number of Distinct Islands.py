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