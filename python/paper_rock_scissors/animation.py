from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o
from main import computer_turn, user_turn

# computer input
def computer_animation(computer_turn_tmp):
    if computer_turn_tmp == 'r':
        return rock_o
    elif computer_turn_tmp == 'p':
        return paper_o
    elif computer_turn == 's':
        return scissors_o

# user input 
def user_animation(user_turn_tmp):
    if user_turn_tmp == 'r':
        return rock_u
    elif user_turn_tmp == 'p':
        return paper_u
    elif user_turn_tmp == 'p':
        return paper_u

