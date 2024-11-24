from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o
from main import computer_turn, user_turn

# computer input
def computer_ch(computer_turn):
    if computer_turn == 'r':
        return rock_o
    elif computer_turn == 'p':
        return paper_o
    elif computer_turn == 's':
        return scissors_o

# user input 
def user_ch(user_turn):
    if user_turn == 'r':
        return rock_u
    elif user_turn == 'p':
        return paper_u
    elif user_turn == 'p':
        return paper_u






