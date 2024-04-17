import art
import random

EASY_TURNS = 10
HARD_TURNS = 5
continue_game = True

def choose_number():
    return random.randrange(1,100)



def difficulty(level):
    if level.lower() == 'easy':
        return EASY_TURNS
    elif level.lower() == 'hard':
        return HARD_TURNS



def compare(actual_number, guessed_number,turns):
    if actual_number > guessed_number:
        print("Too low.")
        return turns-1
    elif guessed_number > actual_number:
        print("Too High")
        return turns-1
    else:
        print("Thats the correct Number! You guessed it.")
    


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!!")
    print("I am thinking between number 1 to 100")
    answer = choose_number()
    turns = difficulty(input("Choose the difficult. Type 'easy' or 'hard': "))
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining")
        guess  =  int(input("Guess a number: "))
        turns = compare(actual_number= answer, guessed_number= guess, turns=turns)
        if turns == 0:
            print("You have run out of guesses!!")
            return
        elif guess != answer:
            print("Guess again!")


game()








