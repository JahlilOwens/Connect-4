from table import table

# this class protains around the players movement and plays for the game
class gamemoves:
    def __init__(self, rows, columns):
        self.board = table(rows, columns)
        # this accepts the players name before the game.
        self.player1 = input("Enter name of player 1: ")
        self.player2 = input("Enter name of player 2: ")
    
    # this is where the game is being played in a loop throughout the game until someone wins.
    def play(self):
        while True:
            self.board.print_board()
            currentplayer = self.player1 if self.board.player == '🔴' else self.player2
            col = int(input(f"{currentplayer}, enter a number (0-6): "))
            if self.board.createmove(col):
                self.board.turns += 1
                if self.board.checkwinner():
                    self.board.print_board()
                    print(f"{currentplayer} wins!")
                    return
                if self.board.turns == self.board.rows * self.board.columns:
                    self.board.print_board()
                    print("Tie Game!")
                    return
                self.board.switchturn()