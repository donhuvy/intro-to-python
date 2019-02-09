"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    number = random.randint(1, 21)

    print("I'm thinking of a number between 1 and 20")

    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    print("Nope! It was " + str(number))


run_game()
