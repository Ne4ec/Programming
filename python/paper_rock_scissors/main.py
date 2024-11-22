#!/bin/python3

import random
# r < p, p > s, s > r
from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o
#import characters

#print(characters())
attempt = 0
user_won = 0
#computer_won = 0

print(40 * '-')
print("| In this game you have to win 3 times |")
print("Just remember: \n"
      "'r' for rock \n"
      "'p' for paper \n"
      "'s' for scissors")
print(40 * '-')

#print(rock_u, paper_o, scissors_u)

while attempt <= 3:
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



