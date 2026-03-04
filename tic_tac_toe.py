import random
board = [1,2,3,4,5,6,7,8,9]
def print_board(board):
    for i in range(len(board)):
        if (i+1) % 3 != 0:
            print(board[i], end=" | ")
        if (i+1) % 3 == 0:
            print(board[i])
            if i != len(board)-1:
                print("----------")
    return board

def player_symbol_choose():
    symbols = ["X", "O"]
    name = input("welcome to the game, please enter your name:")
    while True:
        try:
            symbol_choose = input(f"Hello {name}, welcome to TIC-TAC-TOE,please enter your symbol: X or O, press R for random: ")
            symbol_choose = symbol_choose.upper()
            if symbol_choose not in symbols and symbol_choose.lower() != "r":
                raise Exception("please enter a valid symbol")
        except Exception as e:
            print("please enter a valid symbol")
            continue
        if symbol_choose.lower() == "r":
            random.shuffle(symbols)
            symbol_choose = symbols[0]
        return symbol_choose

def player_symbol_place(symbol_choose,board):
    while True:
        try:
            symbol_place = int(input("please enter a position to place your symbol:"))
        except ValueError as e:
            print("please enter a valid number")
            continue
        if symbol_place not in range(1,10):
            print("please enter a valid number")
            continue
        if type(board[symbol_place-1])!= int:
            print("the place is taken, please enter a valid number")
            continue
        board[symbol_place-1] = symbol_choose
        break
    if check_winner(board):
        return

def check_winner(board):
    winning_rows = [[board[0], board[1], board[2]],[board[3], board[4], board[5]],[board[6], board[7], board[8]]]
    winning_columns = [[board[0], board[3], board[6]],[board[1], board[4], board[7]],[board[2], board[5], board[8]]]
    winning_diagonals = [[board[0], board[4], board[8]],[board[2], board[4], board[6]]]
    winning_positions = winning_rows + winning_columns + winning_diagonals
    for line_type in winning_positions:
        if line_type[0] == line_type[1] == line_type[2] and type(line_type[0]) is str:
            return True

    return False

def play_game(board,symbol_choose):
    while True:
        current_player = symbol_choose
        while True:
            print_board(board)
            player_symbol_place(current_player, board)
            if check_winner(board):
                print_board(board)
                print(f"[{current_player}] is the winner!")
                break
            tie = True
            for number in board:
                if type(number)== int:
                    tie = False
                    break
            if tie:
                print("Tie")
                break
            if current_player == "X":
                    current_player = "O"
            else:
                current_player = "X"
        while True:
            play_again = input("would you like to play again?,(Y/N): ")
            if play_again.lower() == "y":
                board[:] = [1,2,3,4,5,6,7,8,9]
                break
            elif play_again.lower() == "n":
                return
            else:
                print("please enter y or n")
                continue
##bonus




if __name__ == "__main__":
    symbol = player_symbol_choose()
    play_game(board, symbol)