import random

gestures = ['Rock', 'Paper', 'Scissors']

user_choice = int(input("0 - Rock | 1 - Paper | 2 - Scissors: "))
computer_choice = random.randint(0,2)

print(f"You Choose: {gestures[user_choice]} ")
print(f"AI Choose: {gestures[computer_choice]}")

if computer_choice > user_choice:
    print("AI Wins")

elif user_choice == 2 and computer_choice == 1:
    print("You Win!")

elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")

elif user_choice == 1 and computer_choice == 0:
    print("You Lose!")

elif user_choice == computer_choice:
    print("Draw")