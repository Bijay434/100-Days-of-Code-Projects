rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
"""
For computer choice are as follows:
Rock - 0
Paper - 1
Scissor - 2
"""
computer = random.randint(0,3)

player = input("Choose: 'Rock', 'Paper', 'Scissors' ").lower()
if player == 'rock':
    if computer == 0:
        print(rock)
        print("It's a draw!")
    elif computer == 1:
        print(paper)
        print("Paper wins against rock. Computer wins!")
    elif computer == 2:
        print(scissors)
        print("Rock wins against scissors. Player wins!")
elif player == 'paper':
    if computer == 1:
        print(paper)
        print("It's a draw!")
    elif computer == 2:
        print(scissors)
        print("Scissors wins against paper. Computer wins!")
    elif computer == 0:
        print(rock)
        print("Paper wins against rock. Player wins!")
elif player == 'scissors':
    if computer == 2:
        print(scissors)
        print("It's a draw!")
    elif computer == 0:
        print(rock)
        print("Rock wins against scissors. Computer wins!")
    elif computer == 1:
        print(paper)
        print("Scissors wins against paper. Player wins!")