from user_hand import rock_u, paper_u, scissors_u
from opponent_hand import rock_o, paper_o, scissors_o
from main import computer_turn, user_turn

# computer input
def computer_ch(computer_turn):
    if computer_turn == 'r':
        print(rock_o)
    elif computer_turn == 'p':
        print(paper_o)
    elif computer_turn == 's':
        print(scissors_o)
    return 

# user input 
def user_ch(user_turn):
    if user_turn == 'r':
        print(rock_u)
    elif user_turn == 'p':
        print(paper_u)
    elif user_turn == 'p':
        print(paper_u)
