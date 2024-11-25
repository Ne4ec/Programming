#!/bin/python3

import random
# r < p, p > s, s > r
from user_hand import rock_u, paper_u, scissors_u
# yxy nur die user_hand importieren
from opponent_hand import rock_o, paper_o, scissors_o
import characters

attempt = 0
user_won = 0

print(40 * '-')
print("| In this game you have to win 3 times |")
print("Just remember: \n"
      "'r' for rock \n"
      "'p' for paper \n"
      "'s' for scissors")
print(40 * '-')


while attempt <= 2:
    computer_turn = random.choice (['r', 'p', 's'])
    user_turn = input('Your choice: ')
    attempt +=1
    if (computer_turn == 'p') and (user_turn == 'r'):
        print(paper_o, rock_u)
        print('You lost!')
        print('Computer have paper!')
    elif (scissors_o == 's') and (paper_u == 'p'): 
        print('You lost!')
        print('Computer have scissors!')
    elif computer_turn == usr_turn:
        attempt -=1
        print('its tie!')
        print('Try another play.')
    else:
        user_won +=1
        print('You Won')
        print()

if user_won == 3:
    print('You won the entire Game! Thank you, for playing :D')


