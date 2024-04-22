"""
Jahlil Owens & Jacin Anderson
3/18/2023
Project 1
This Is Our Original Work
"""
columns = 7
rows = 6
# this class is for setting up the board and creating the movements.
class table():
    #start off with our constructor that will have the basic variable needed for the board and its process
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = self.newboard()
        self.turns = 0
        self.player = '🔴'# since connect 4 has colors we want to use a color icon for the players
        self.move = []

    # this method creates the rows and columns of the board
    def newboard(self):
        board = []
        for i in range(self.rows):
            i_list = []
            for j in range(self.columns):
                i_list.append('.')
            board.append(i_list)# append the list so we can obtain the values inside of the list for the rows.
        return board
    
    # this method is how players are allowed to decide their position for the game.
    def createmove(self, col): # we include a col variable to contribute with the self.column variable
        if col < 0 or col >= self.columns:
            print("invalid move.")
            return False
        
        # this will help us identify the rows length and then connect this will the columns
        # we will connect the board to the columns and rows and then connect it to the player
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == '.':
                self.board[row][col] = self.player
                self.move.append((row, col))
                return True
        print("invalid move.")
        return False
    
    # this method just helps identify the difference between players and their turns
    def switchturn(self):
        if self.player == '🔴':
            self.player = '🔵'
        else:
            self.player = '🔴'
        
    
    def print_board(self):
        print("\n")
        # Number the columns seperately to keep it cleaner
        for r in range(columns):
            print(f"  ({r}) ", end="")
        print("\n")

        # This will print the rows and columns but also help seperate each row.
        for r in range(rows):
            print('|', end="")
            for c in range(columns):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")

        print(f"{'-' * 42}\n")
    
    # this method helps identify who if there is a winner between the players.
    def checkwinner(self):
        for row, col in self.move:
            if self.checkrow(row) or self.checkcolumn(col) or self.checkdiag(row, col):
                return self.player
        return None

    # this method helps check to see if a player has gotten four in a row horizontally 
    def checkrow(self, row):
        count = 0 # gonna use this to increment later
        for columns in range(self.columns):
            if self.board[row][columns] == self.player:
                count += 1
                if count == 4: # if the player coin equals 4
                    return True
            else:
                count = 0
        return False
    # this method is the same as the checkrow method just now focus on vertical
    def checkcolumn(self, col):
        count = 0
        for row in range(self.rows):
            if self.board[row][col] == self.player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    
    # this method is for checking if a player obtains 4 in a row but diagonal instead
    def checkdiag(self, row, col):
        count = 0
        r, c = row, col
        # we now are gonna use the rows and columns to compliant with the player
        # each section focueses on the different angles for the player
        while r >= 0 and c < self.columns and self.board[r][c] == self.player:
            count += 1
            r -= 1
            c += 1
        r, c = row+1, col-1
        while r < self.rows and c >= 0 and self.board[r][c] == self.player:
            count += 1
            r += 1
            c -= 1
        if count >= 4:
            return True
        
        count = 0
        r, c = row, col
        while r >= 0 and c >= 0 and self.board[r][c] == self.player:
            count += 1
            r -= 1
            c -= 1
        r, c = row+1, col+1
        while r < self.rows and c < self.columns and self.board[r][c] == self.player:
            count += 1
            r += 1
            c += 1
        if count >= 4:
            return True
        return False
