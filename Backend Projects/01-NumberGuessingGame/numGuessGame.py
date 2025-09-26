import random

def game_start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n" + 
          "You have 5 chances to guess the correct number.")

def choose_mode():
    print("\nPlease select the difficulty level: ")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    choice = 0
    diff = ["Easy", "Medium", "Hard"]
    choices = 10
    while (choice < 1 or choice > 3):
        choice = int(input("\nEnter your choice: "))
        if (choice != 1 and choice != 2 and choice != 3):
            print("\nSorry, that's not a valid option! Try again!")
            continue
    
    if (choice == 2):
        diff_guess = diff[1]
        choices = 5
    elif choice == 3:
        diff_guess = diff[2]
        choices = 3
    else:
        diff_guess = diff[0]
    
    print("\nGreat! You have selected the " + diff_guess + " difficulty level.")
    return choices


def game(guesses, num):
    print("Let's start the game!\n")
    i = 0
    while i != guesses:
        guess = int(input("Enter your guess: "))
        if (num == guess):
            print("Congratulations! You guessed the correct number in " + 
                  str(i+1) + " attempts.")
            break
        elif (guess < 1 or guess > 100):
            print("\nSorry! " + str(guess) + " is out of range Try again!\n")
            i += 1
            continue
        elif (num > guess):
            print("Incorrect! The number is greater than " + str(guess) + ".")
            i += 1
            continue
        elif (num < guess):
            print("Incorrect! The number is less than " + str(guess) + ".")
            i += 1
            continue
    if (i == guesses):
        print("Sorry! You ran out of chances! The answer is: " + str(num))




def main():
    game_start()
    guesses = choose_mode()
    num = random.randint(1,100)
    game(guesses, num)

main()