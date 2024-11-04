
from random import randrange

def print_welcome():
    print("Rock, Paper, Scissors")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors") 
    print()
def play_game():
    user_choice = enter_user_choice()
    program_choice = enter_program_choice()   
    decide_winner(program_choice, user_choice)
def enter_user_choice():
    user_choice = int(input("Make your choice by entering 1, 2, or 3:"))  
    if user_choice == 1 or user_choice == 2 or user_choice == 3:
        return user_choice
    else:
        print("Please choose 1, 2, or 3.")
def enter_program_choice():
    return randrange(1, 4)
             
def decide_winner(program_choice, user_choice):
    if program_choice == user_choice:
        print("You tied!")
    elif (program_choice == 1 and user_choice == 2) or\
         (program_choice == 2 and user_choice == 3)or\
         (program_choice == 3 and user_choice == 1):
        print("You won :)")
    else:
        print("You lost :(")

def main():
    print_welcome() 
    play_again = "y"
    while play_again() == "y":
        play_game()
        print()
        play_again = input("Would you like to play again? y or n: ")
        if play_again != "y" or play_again != "n":
            print("Your choice is invalid.  Enter y or n:")
            play_again = input("Would you like to play again? y or n: ")
        elif play_again == "y":
            continue
        elif play_again == "n":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

print("Created by, Adair Salinas")