#!/bin/python

import random
from words import words

def get_valid_word(words):
    random_word = random.chice(words)
    while '-' in word or '' in word:
        random_word = random.choice(words)
    return word
    



print(get_valid_word)
