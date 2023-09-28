import random

user_choice=int(input("enter your choice:Type 0 for ROCK, Type 1 for PAPER, Type 2 for SCISSORS."))

if user_choice >=3 or user_choice <0:
    print("the number is invalid,You Lost The Game...")
else:
    computer_choice=random.randint(0,2)
    print("computer_choice:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU LOST THE GAME.")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN.")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win.")
