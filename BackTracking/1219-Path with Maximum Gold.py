class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col, cur):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] > 0 :
                temp = grid[row][col]
                grid[row][col] = 0
                # to aviod repeat calculate
                dfs(row,col-1,cur + temp)
                dfs(row,col+1,cur + temp)
                dfs(row-1,col,cur + temp)
                dfs(row+1,col,cur + temp)
                self.max_temp = max(self.max_temp, cur + temp)
                grid[row][col] = temp
                
        self.max_temp = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i,j,0)
        return self.max_temp