#!/bin/python

import random
from words import words

print(71 * '-')
print("| In this games, you have to guess the right word, befor going to die!|")
print('|'+25*'-'+"You have 6 guesses"+26*'-'+'|')
print(71 * '-')

random_word = random.choice(words)

print(random_word)
attampts = 0

def get_valid_word(word_v)
    if guess in random_word
    

while attampts <= 6:
    attampts = +1

    guess = input('Your guess: ')
    if guess in random_word:
        print

    print('The game is over')
    print(f'The search word was: {random_word}')
        
       
#guess = input("Your guss: ")

#while True:
#    if random_word == guess:
#        print("Congratulations, you guessed the word")
#        break
#    else:
#        print("The wrong word! Try it again ({}/6 ")
#
#print(random_word)

