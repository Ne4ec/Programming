#!/bin/python3

import random
# r < p, p > s, s > r
from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o

attempt = 0
user_won = 0

print(40 * '-')
print("| In this game you have to win 3 times |")
print("Just remember: \n"
      "'r' for rock \n"
      "'p' for paper \n"
      "'s' for scissors")
print(40 * '-')

# computer input
def computer_animation(computer_turn_tmp):
    if computer_turn_tmp == 'r':
        return rock_o
    elif computer_turn_tmp == 'p':
        return paper_o
    elif computer_turn_tmp == 's':
        return scissors_o

# user input 
def user_animation(user_turn_tmp):
    if user_turn_tmp == 'r':
        return rock_u
    elif user_turn_tmp == 'p':
        return paper_u
    elif user_turn_tmp == 's':
        return scissors_u

while attempt <= 2:
    computer_turn = random.choice (['r', 'p', 's'])
    user_turn = input('Your choice: ')
    attempt +=1
    if (computer_turn == 'p') and (user_turn == 'r'):
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        attempt -=1
        print('You lost!')
        print('Computer have paper!')
    elif (scissors_o == 's') and (paper_u == 'p'): 
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        appempt -=1
        print('You lost!')
        print('Computer have scissors!')
    elif computer_turn == user_turn:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        attempt -=1
        print('its tie!')
        print('Try another play.')
    else:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        user_won +=1
        print('You Won')

if user_won == 3:
    print('You won the entire Game! Thank you, for playing :D')
