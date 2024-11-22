#!/bin/python

import random

attempt = 0
user_won = 0
#computer_won = 0

while attempt <= 3:
    attempt +=1
    computer_turn = random.choice (['r', 'p', 's'])
    user_turn = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n:")

    if (computer_turn == 'p') and (user_turn == 'r'):
        print('You lost!')
        print('Computer have paper!')
    elif (computer_turn == 's') and (user_turn == 'p'): 
        print('You lost!')
        print('Computer have scissors!')
    else:
        user_won +=1
        #temp_attempt = 3 - attempt
        print('You Won')
        #print(f'You have to win {temp_attempt} times')

if computer_turn == user_turn:
    attempt -=1
    print('its tie!')
    print('Try another play.')

if user_won == 3:
    print('You won the entire Game! Thank you, for playing :D')

    # r < p, p > s, s > r

