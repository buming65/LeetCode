class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.columns = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        temp = 1 if player == 1 else -1
        self.rows[row] += temp
        self.columns[col] += temp
        if row == col:
            self.diagonal += temp
        if row + col == self.n - 1:
            self.anti_diagonal += temp
        
        if abs(self.rows[row]) == self.n or \
        abs(self.columns[col]) == self.n or \
        abs(self.anti_diagonal) == self.n or \
        abs(self.diagonal) == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

