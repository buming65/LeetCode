class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, remain):
            if len(remain) == 0:
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != remain[0]:
                return False
            temp = board[x][y]
            board[x][y] = '~'
            for a, b in [(0,1), (0,-1), (1,0), (-1,0)]:
                ret = dfs(x+a,y+b,remain[1:])
                if ret:
                    return True
            board[x][y] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True

        return False