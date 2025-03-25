#!/bin/python3

import random
from words import words
from animation import *

def new_line():
    return 38*'_'

print('_' * 38)
print("| In this game, you have to guess the\n| correct letters to form a word or\n| guess the word before you run out of\n| lives!")
print("| You have 6 guesses/lives! ")
print('_' * 38)

random_word = random.choice(words)
random_word_visul = [] 
user_won_game = False
round = 1
used_letters = []
user_lives = 6
list_random_word = list(random_word)

def sub_user_lives(lives):
    lives -= 1 
    print(lives)

def user_won():
    return f"Great, you won the game! :D\nIn the {round}th round, with {user_lives} lives left!\n{random_word_visual}\n"

def visualization(lives):
    if lives == 6:
        return lives_6
    elif lives == 5:
        return lives_5
    elif lives == 4:
        return lives_4
    elif lives == 3:
        return lives_3
    elif lives == 2:
        return lives_2
    elif lives == 1:
        return lives_1
    else:
        return lives_0

for letter in random_word:
    random_word_visul += '_' 

if __name__ == "__main__":
    while not user_won_game:
        if '_' not in random_word_visul:
            user_won_game = True
            print(user_won())
            print(list_random_word)
        else:
            print(new_line())
            print(f"Round: {round}\nLives left: {user_lives}\nSearched word: {random_word_visul}")
            print(visualization(user_lives))
            print(f"Used letters: {used_letters}")
            user_guess = input("What is your guess: ").lower()
            used_letters.append (user_guess)
            round +=1
            new_line()
            if (1 != len(user_guess)) and (random_word != user_guess):
                print("Please, input only one valid letter\n"
                "Note: see ASCII characters!")
                continue
            if user_guess == random_word:
                print(user_won())
                user_won_game = True
            elif user_guess not in random_word:
                if user_lives == 0:
                    print(new_line())
                    print(f"Unfortunately, you don't have any more lives!\nAt round {round}, it's over. Try another game...")
                    user_won_game = True
                    print(list_random_word)
                else:
                    user_lives -= 1
                    print("The letter is not matching up with any\nletters in the searched word!, try\nanother letter!")
            else:
                
                for letter_position in range(len(random_word)):
                    letter = random_word[letter_position]
                    if user_guess == letter:
                        random_word_visul[letter_position] = letter