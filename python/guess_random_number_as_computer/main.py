#!/bin/python

import random

guess = 0
low = 1
high = x
def computer_guessing (x)
    feedback = ''
    while feedback != 'c':
        computer_guess = random.randint(1, x)    
        feedback = input(f"Is the guessed number too low {l}, too high {h} or is it correct {c}? ".lower()) 
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guss + 1
    print(f"The computer guessed your number! The numer is {computer_guess}")
