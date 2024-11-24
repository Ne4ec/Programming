#!/bin/python3

import random
# r < p, p > s, s > r
from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o
#import characters

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

def opponent_animation(computer_turn):
    if computer_turn == 'r':
        return rock_o
    elif computer_turn == 'p':
        return paper_o
    elif computer_turn == 's':
        return scissors_o

# user input
def user_animation(user_turn):
    if user_turn == 'r':
        return rock_u
    elif user_turn == 'p':
        return paper_u
    elif user_turn == 'p':
        return paper_u


while attempt <= 3:
    attempt +=1
    computer_turn = random.choice (['r', 'p', 's'])
    user_turn = input('Your choice: ')
    if (computer_turn == 'p') and (user_turn == 'r'):
        print('You lost!')
        print('Computer have paper!')
    elif (scissors_o == 's') and (paper_u == 'p'): 
        print('You lost!')
        print('Computer have scissors!')
    elif (computer_turn == user_turn):
        #attemp -=1
        print('Its tie')
        print('Try another play')
    else:
        user_won +=1
        print('You Won')


if user_won == 3:
    print('You won the entire Game! Thank you, for playing :D')



