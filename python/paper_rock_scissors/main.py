#!/bin/python

import random

attempt = 0

computer_turn = random.choice (['r', 'p', 's'])
user_turn = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n:")
    
 while True: #attempt <= 3:
    if (computer_turn == 'p') and (user_turn == 'r'):
        print('You lost!')
        print('Computer have paper!')
    elif (computer_turn == 's') and (user_turn == 'p'):             print('You lost!')
        print('Computer have scissors!')
    else:
        print('You Won')
        print(f'You have to win {attempt} times')

if computer_turn == user_turn:
    print('its tie!')
    print('Try another play.')

print(0)

    # r < p, p > s, s > r

