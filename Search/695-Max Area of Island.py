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