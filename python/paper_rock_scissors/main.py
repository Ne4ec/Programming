#!/bin/python3

import random
from opponent_hand import *
from user_hand import *
# r < p, p > s, s > r

print(40 * '-')
print("| In this game you have to win 3 times |")
print("Just remember: \n"
      "'r' for rock \n"
      "'p' for paper \n"
      "'s' for scissors")
print(40 * '-')

attempt = 0
round = 0
won_times = 0
user_won = False

def computer_animation(computer_turn_tmp):
    if computer_turn_tmp == 'r':
        return rock_o
    elif computer_turn_tmp == 'p':
        return paper_o
    elif computer_turn_tmp == 's':
        return scissors_o

def user_animation(user_turn_tmp):
    if user_turn_tmp == 'r':
        return rock_u
    elif user_turn_tmp == 'p':
        return paper_u
    elif user_turn_tmp == 's':
        return scissors_u

def new_line():
    print("\n")
    print(40*'_')

while not user_won:  
    computer_turn = random.choice(['r', 'p', 's'])
    print(f"Round: {round}")
    user_turn = input('Your choice: ')
    if user_turn not in ['r', 'p', 's']:
        new_line()
        print("Invalid input! Please enter 'r', 'p' or 's'!")
        print("Just remember: \n"
              "'r' for rock \n"
              "'p' for paper \n"
              "'s' for scissors")
        continue

    if (computer_turn == 'p') and (user_turn == 'r'):
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('You lost! Computer has paper!')
        round =+ 1
        new_line()
    elif (computer_turn == 's') and (user_turn == 'p'): 
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('You lost! Computer has scissors!')
        round =+ 1
        new_line()
    elif (computer_turn == 'r') and (user_turn == 'p'):
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('You lost! Computer has rock!')
        round =+ 1
        new_line()
    elif (computer_turn == 'r') and (user_turn == 's'):
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('You lost! Computer has rock!')
        round =+ 1
        new_line()
    elif computer_turn == user_turn:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('It\'s a tie! Try another play.')
        round =+ 1
        new_line()
    else:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        won_times += 1
        round =+ 1
        print("You Won!") #computer_won missing
        new_line()
        if won_times == 3:
            user_won = True
            print('You won the entire Game! Thank you for playing :D')
            new_line()
