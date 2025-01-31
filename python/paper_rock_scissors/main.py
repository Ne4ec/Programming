#!/bin/python3

import random
from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o

# r < p, p > s, s > r

print(40 * '-')
print("| In this game you have to win 3 times |")
print("Just remember: \n"
      "'r' for rock \n"
      "'p' for paper \n"
      "'s' for scissors")
print(40 * '-')

attempt = 0
user_won = 0

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

while user_won < 3:  
    computer_turn = random.choice(['r', 'p', 's'])
    

    user_turn = input('Your choice: ')
    if user_turn not in ['r', 'p', 's']: 
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
    elif (computer_turn == 's') and (user_turn == 'p'): 
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('You lost! Computer has scissors!')
    elif computer_turn == user_turn:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        print('It\'s a tie! Try another play.')
    else:
        print(user_animation(user_turn))
        print(computer_animation(computer_turn))
        user_won += 1 
        print('You Won!')
        if user_won == 3:
            print('You won the entire Game! Thank you for playing :D')


