import random

def card_deck():
    deck = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
    random.shuffle(deck)
    return deck
def card_guess(correct_guess,previous_guess = None):
    while True:
        try:
            guess = input("Please enter your guess between 0-11, press R to restart:")
            if guess.lower() == "r":
                return guess.lower()
            guess = int(guess)
            if (guess>11) or (guess<0) or (guess == previous_guess) or (guess in correct_guess):
                raise Exception("invalid input")
            return guess
        except Exception as e:
            print("invalid input, try again")

def guess_pair(deck,correct_guess):
        first_guess = card_guess(correct_guess)
        if first_guess == 'r':
            return 'r'
        display_deck(deck,correct_guess,temp = first_guess)
        second_guess = card_guess(correct_guess, previous_guess= first_guess)
        if second_guess == 'r':
            return 'r'
        display_deck(deck, correct_guess, temp=first_guess, temp2=second_guess)
        if deck[first_guess]==deck[second_guess]:
            print("you found a pair")
            correct_guess.append(first_guess)
            correct_guess.append(second_guess)
            display_deck(deck, correct_guess)
            return True
        else:
            print("not a match")
            input("press any key to continue")
            return False

def display_deck(deck, correct_guess, temp = None, temp2 = None):
    for i in range(len(deck)):
        if i in correct_guess or i==temp or i==temp2:
            print(f"[{deck[i]}]",end=" ")
        else:
            print(f"[{i}]",end=" ")
        if (i+1) % 4==0:
            print()
def play_game():
    while True:
        result = None
        correct_guess = []
        deck = card_deck()
        while len(correct_guess) < 12:
            display_deck(deck, correct_guess)
            result = guess_pair(deck, correct_guess)
            if result == 'r':
                break
        if result == 'r':
            continue
        if len(correct_guess) == 12:
            print("you win")
            while True:
                play_again = input("would you like to play again?(Y/N):")
                play_again = play_again.lower()
                if play_again == "y":
                    break
                elif play_again == "n":
                    return
                else:
                    print("invalid input")
                    continue

play_game()


