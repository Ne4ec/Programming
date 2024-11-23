# Code from wynand1004 (https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe)

import main 

print(main.whoami)

# Rock
rock_u = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper_u = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors_u = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            """)


if user_turn == 'r':
    print(rock_u)
elif user_turn == 'p':
    print(paper_u)
elif user_turn == 's':
    print(scissors_u)