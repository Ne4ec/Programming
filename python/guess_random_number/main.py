#!/bin/python

import random

guessed = 0
lower = 1
upper = 100
random_number = random.randint(lower, upper)

print(53 * '-')
print("| In this game, you have to guess the right number! |")
print(53 * '-')
while True:
    try:
        guessed += 1
        guess = int(input("Enter your guess: "))
        
        if guess == random_number:
            print(f"Congratulations! You guessed the number {random_number} :D")
            print(f"You took {guessed} attempts.")
            break  # Exit the loop once the number is guessed correctly
        elif guess > random_number:
            print("The random number is smaller!")
        else:
            print("The random number is greater!")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 100.")
        print("Make sure the input does not contain:")
        print("- commas")
        print("- spaces")
        print("- letters")
