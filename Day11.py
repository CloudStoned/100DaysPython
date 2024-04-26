import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
ai_cards = []


def draw_card(card_list, number_of_cards):
    while len(card_list) < number_of_cards:
        card_list.append(random.choice(cards))

def sum_card(card):
    return sum(card)

def IsBlackjack():
    if sum_card(user_cards) == 21:
        print("User has blackjack")
        return True
    elif sum_card(ai_cards) == 21:
        print("Ai has blackjack")
        return True
    else:
        return False
    
draw_card(user_cards, 2)
draw_card(ai_cards, 2)

print("User cards:", user_cards)
print("AI cards:", ai_cards)

if IsBlackjack() == False:
    choice = input("Do you want to draw another card (Yes or No): ").lower()
    if choice == 'yes':
        draw_card(user_cards, 1)
        print(user_cards)







        




