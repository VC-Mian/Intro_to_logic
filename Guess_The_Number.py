"""
Guess_The_Number.py: A mini-game where the player selects a number from 1-100. Each time a hint is given if the user is incorrect.

12/09/2021
"""

import random

def main():

    random_number = get_random_number()

    user_num = int(input("Guess the number: "))

    while user_num != random_number:

        if user_num > random_number:
            print("Too High")

        else:
            print("Too Low")

        user_num = int(input("Guess the number: "))

    else:
        print("Congrats you guessed the number!")
        print("Random number was: " + str(random_number))

def get_random_number():
    random_number = int(random.random() * 100)
    return random_number

main()
