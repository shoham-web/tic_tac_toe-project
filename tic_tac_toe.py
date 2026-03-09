import random
board = [1,2,3,4,5,6,7,8,9]
def print_board(board):
    for i in range(len(board)):
        place = board[i]
        if isinstance(place, int):
            place = " "
        if (i+1) % 3 != 0:
            print(place, end=" | ")
        if (i+1) % 3 == 0:
            print(place)
            if i != len(board)-1:
                print("----------")


def get_player_name(message):
    while True:
        name = input(message)
        if name:
            return name

def player_symbol_choose(name):
    symbols = ["X", "O"]
    while True:
        try:
            symbol_choose = input(f"Hello {name}, please choose your symbol: X or O, press R for random: ")
            symbol_choose = symbol_choose.upper()
            if symbol_choose not in symbols and symbol_choose.lower() != "r":
                raise Exception("please enter a valid symbol")
        except Exception as e:
            print("please enter a valid symbol")
            continue
        if symbol_choose.lower() == "r":
            random.shuffle(symbols)
            symbol_choose = symbols[0]
            print(f"{name}, your symbol is {symbol_choose}")
        return symbol_choose

def player_symbol_place(symbol_choose,board,name):
    while True:
        try:
            print(f"{name} ({symbol_choose}), your turn!")
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

def check_winner(board):
    winning_rows = [[board[0], board[1], board[2]],[board[3], board[4], board[5]],[board[6], board[7], board[8]]]
    winning_columns = [[board[0], board[3], board[6]],[board[1], board[4], board[7]],[board[2], board[5], board[8]]]
    winning_diagonals = [[board[0], board[4], board[8]],[board[2], board[4], board[6]]]
    winning_positions = winning_rows + winning_columns + winning_diagonals
    for line_type in winning_positions:
        if line_type[0] == line_type[1] == line_type[2] and type(line_type[0]) is str:
            return True

    return False

def play_vs_computer(board,computer_symbol):
    empty_place =[]
    for idx,value in enumerate(board):
        if isinstance(value,int):
            empty_place.append(idx)
    if empty_place:
        computer_choice = random.choice(empty_place)
        print(f"the computer chose to place on index {board[computer_choice]}, your turn:")
        board[computer_choice] = computer_symbol




def play_game(board):
    while True:
        print("Hello, welcome to TIC-TAC-TOE! ")
        while True:
            mode_select = input("Choose mode,\n1). player vs player 2). player vs computer: ")
            if mode_select in ("1", "2"):
                break
            print("please enter either 1 or 2")

        if mode_select == "1":
            player_name1 = get_player_name("Enter player 1 name: ")
            player_name2 = get_player_name("Enter player 2 name: ")
        else:
            player_name1 = get_player_name("Enter your name: ")
            player_name2 = "computer"
        symbol_choose = player_symbol_choose(player_name1)
        current_player = symbol_choose
        computer_symbol = "O" if current_player == "X" else "X"
        while True:
            print_board(board)
            if mode_select == "2" and current_player == computer_symbol:
                play_vs_computer(board, current_player)
            else:
                if current_player == symbol_choose:
                    current_name = player_name1
                else:
                    current_name = player_name2
                player_symbol_place(current_player,board,current_name)

            if check_winner(board):
                print_board(board)
                if current_player == symbol_choose:
                    print(f"{player_name1} is the winner!")
                else:
                    print(f"{player_name2} is the winner!")
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







if __name__ == "__main__":
    play_game(board)