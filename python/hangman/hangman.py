#!/bin/python

import random
import sys

from words import words
from player import print_hangman

print(71 * '-')
print("| In this games, you have to guess the right word, befor going to die!|")
print(71 * '-')


random_word = random.choice(words)
print(random_word)

guess = input("Your guss: ")

while True:
    if random_word == guess:
        print("Congratulations, you guessed the word")
        break
    else:
        print("The wrong word, ")
print(random_word)

