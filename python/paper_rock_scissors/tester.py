#/bin/python 
from opponent_hand import rock_o, paper_o, scissors_o
from user_hand import rock_u, paper_u, scissors_u


print(rock_u)

computer_turn = 'p'


def sec (computer_turn):
    if computer_turn == 'r':
        return rock_o
    elif computer_turn == 'p':
        return paper_o
    elif computer_turn == 's':
        return scissors_u

print(sec('p'))
print(sec('s'))
