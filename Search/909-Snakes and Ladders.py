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