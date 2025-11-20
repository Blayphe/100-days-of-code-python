import random

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

option_list = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
rand_choice = random.randint(0,2)
if player_choice > 2:
    print("Invalid number you lose!")
else:
    print(option_list[player_choice])
    print(f"Computer chose: {option_list[rand_choice]}")

    if player_choice == rand_choice:
        print("Draw")
    elif player_choice == 0 and rand_choice == 2:
        print("You Win!")
    elif rand_choice == 0 and player_choice == 2:
        print("You lose!")
    elif player_choice > rand_choice:
        print("You Win!")
    elif rand_choice > player_choice:
        print("You lose!")