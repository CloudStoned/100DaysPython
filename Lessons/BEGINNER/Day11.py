import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
ai_cards = []

def initial_card(card_list, number_of_cards):
    while len(card_list) < number_of_cards:
        card_list.append(random.choice(cards))

def draw_card(card_list, no_of_draw):
    for _ in range(no_of_draw):
        card_list.append(random.choice(cards))

def sum_cards(card_list):
    total_score = sum(card_list)
    # Check for aces and adjust if needed
    while total_score > 21 and 11 in card_list:
        # Replace one ace (11) with 1 to avoid busting
        card_list[card_list.index(11)] = 1
        total_score = sum(card_list)
    return total_score

def is_blackjack(card_list):
    return sum_cards(card_list) == 21

def display_game_state(user_cards, ai_cards):
    print("User cards:", user_cards)
    print("AI cards:", ai_cards)

# Initial deal
initial_card(user_cards, 2)
initial_card(ai_cards, 2)
display_game_state(user_cards, ai_cards)

# Check for blackjack
if is_blackjack(user_cards):
    print("User has blackjack!")
elif is_blackjack(ai_cards):
    print("AI has blackjack!")
else:
    # User's turn
    while True:
        choice = input("Do you want to draw another card (Yes or No): ").lower()
        if choice == 'yes':
            draw_card(user_cards, 1)
            user_score = sum_cards(user_cards)

            if user_score > 21:
                print("YOU LOSE")
                print(f"Cards: {user_cards}")
                print(f"Score: {user_score}")
                break

            elif user_score == 21:
                print("You Won !")
                break

        elif choice == 'no':
            # AI's turn
            while sum_cards(ai_cards) < 17:
                draw_card(ai_cards, 1)
                ai_score = sum_cards(ai_cards)

            # Determine winner
            user_score = sum_cards(user_cards)
            ai_score = sum_cards(ai_cards)
            if ai_score > 21:
                print("USER WINS")
                print(f"AI Cards: {ai_cards}")
                print(f"AI Score: {ai_score}")
                break
            else:
                if user_score > ai_score:
                    print("USER WINS")
                    print(f"User Cards: {user_cards}")
                    print(f"User Score: {user_score}")

                elif ai_score > user_score:
                    print("AI WINS")
                    print(f"AI Cards: {ai_cards}")
                    print(f"AI Score: {ai_score}")

                else:
                    print("Draw")
                break
