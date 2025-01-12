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

continue_game = True

while continue_game:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    computer_choice = random.randint(0,2)

    if choice == 0:
        print(rock)
        print("\nComputer Chose:")
        if computer_choice == 0:
            print(rock)
            print("Both same")
        elif computer_choice == 1:
            print(paper)
            print("You lose")
        else:
            print(scissors)
            print("You won")
    elif choice == 1:
        print(paper)
        print("\nComputer Chose:")
        if computer_choice == 0:
            print(rock)
            print("You won")
        elif computer_choice == 1:
            print(paper)
            print("Both same")
        else:
            print(scissors)
            print("You lose")
    else:
        print(scissors)
        print("\nComputer Chose:")
        if computer_choice == 0:
            print(rock)
            print("You lose")
        elif computer_choice == 1:
            print(paper)
            print("You win")
        else:
            print(scissors)
            print("Both same")

    want_to_continue = ''
    while want_to_continue != 'Y' and want_to_continue != 'N':
        want_to_continue = input('\nDo you want to continue the Game? (Y/N) ').upper()
        if want_to_continue == 'N':
            continue_game = False 
        elif want_to_continue != 'Y':
            print('Error! Try Again!')
    


