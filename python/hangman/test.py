#!/bin/python

import random
from words import words
import animation_visual from animation
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set (string.ascii_uppercase)
    user_letters = set()

    user_letter = input('Guess a letter:'.upper())
    if user_letter in alphabet - used_lettes:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    
