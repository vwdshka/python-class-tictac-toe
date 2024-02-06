class TicTacToe:
    def __init__(self) -> None:
        self.player = 'X'
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=' ')
            print()

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row or Col out of range")
        elif self.board[row][col] != '-':
            print("Position already taken")
        else:
            self.board[row][col] = self.player
            self.player = 'X' if self.player == 'O' else 'O'

    def checkForWinner(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '-':
                return self.board[row][0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '-':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return self.board[0][2]
        
    def checkForTie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    return False
        return True

    def get_winner(self):
        # Exercise 1: find if there is a winner and return its symbol, if not return None
        self.checkForWinner()
        if self.checkForWinner() != None:
            return self.checkForWinner()
        else:
            return None
    
    def is_tie(self):
        # Exercise 2: find if it is a Tie
        if self.checkForTie() != None:
            return self.checkForTie()
        else:
            return False


game = TicTacToe()
while True:
    print(game.player, "plays")
    print("\n")
    game.print_board()
    row = int(input("Row: "))
    col = int(input("Col: "))
    game.play(row, col)
    winner = game.get_winner()
    if winner is not None:
        print(winner, "wins!")
        break
    if game.is_tie():
        print("It is a Tie")
        break

game.play(row, col)