from gamemoves import gamemoves

# this class starts the game and connects all of the other classes together
class output:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.game = None

    # this method is for the beginning and ending of the game
    def start(self):
        while True:
            choice = input("Enter 'P' to play or 'Q' to quit: ")
            if choice.lower() == "p":
                self.play()
            elif choice.lower() == "q":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please 'P' or 'Q'.")
    # this method begins the game of connect 4
    def play(self):
        self.game = gamemoves(self.rows, self.columns)
        self.game.play()

# this starts the process
if __name__ == "__main__":
    s = output()
    s.start()
