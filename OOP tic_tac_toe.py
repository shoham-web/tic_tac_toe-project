import random
from operator import truediv


class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("---------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("---------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")

    def make_move(self, position, symbol):
            if self.cells[position] == " ":
                self.cells[position] = symbol
                return True
            return False

    def is_move_valid(self, position):
        return self.cells[position] == " "

    def check_win(self):
        winning_position =[(0,1,2), (3,4,5), (6,7,8),
                           (0,3,6), (1,4,7), (2,5,8),
                           (0,4,8), (2,4,6)]
        for a,b,c in winning_position:
            if self.cells[a] == self.cells[b] == self.cells[c] and self.cells[a] != " ":
                return True
        return False

    def check_tie(self):
        for cell in self.cells:
            if cell == " ":
                return False
        return True

class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self,board):
        while True:
            symbol_place = (input(f"{self.name} please enter a position to move: "))
            if not symbol_place.isdigit():
                print("please enter a valid number")
                continue
            position = int(symbol_place)-1

            if not (0<= position <=8):
                print("please enter a number between 1 and 9")
                continue
            if not board.is_move_valid(position):
                print("The position you entered is Taken,please try again")
                continue
            return position

    def choose_symbol(self):
        symbols = ["X","O"]
        while True:
            symbol_choose = input("Choose a symbol (X/O) press R for random: ")
            symbol_choose = symbol_choose.upper()
            if not symbol_choose in ["X","O","R"]:
                print("please enter a valid symbol")
                continue
            if symbol_choose == "R":
                random.shuffle(symbols)
                symbol_choose = symbols[0]
            self.symbol = symbol_choose
            return symbol_choose

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def switch_symbol(self):
        self.symbol = "X" if self.symbol == "O" else "O"
        return self.symbol


class Game:
    def __init__(self):
        self.board = Board()
        print("Hello, welcome to TIC-TAC-TOE! ")
        player1_name = input("Enter player 1 name: ")
        player2_name = input("Enter player 2 name: ")
        self.player1 = Player(player1_name,None)
        self.player2 = Player(player2_name,None)
        self.current_player = self.player1

        self.player1.choose_symbol()
        print(f"{self.player1.name} will be {self.player1.symbol}")

        self.player2.symbol = self.player1.symbol
        self.player2.switch_symbol()
        print(f"{self.player2.name} will be {self.player2.symbol}")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        return self.current_player

    def game_loop(self):
        while True:
            while True:
                self.board.display()
                print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")
                position = self.current_player.get_move(self.board)
                self.board.make_move(position, self.current_player.symbol)
                if self.board.check_win():
                    self.board.display()
                    print(f"{self.current_player.name} won the game")
                    break
                if self.board.check_tie():
                    self.board.display()
                    print("Tie")
                    break
                self.switch_player()

            while True:
                play_again = input("would you like to play again?,(Y/N): ")
                play_again = play_again.upper()
                if play_again == "Y":
                    self.board = Board()
                    self.current_player = self.player1
                    break

                elif play_again == "N":
                    return
                else:
                    print("please enter Y or N")
                    continue

game = Game()
game.game_loop()





