print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")

if direction == 'right':
    choice = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across")
    if choice == 'wait':
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if color == 'yellow':
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
