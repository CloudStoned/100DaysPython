import random

word_list = ['ardvark', 'baboon', 'camel','install', 'listen','stylistic']
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
convert_chosen_word = ''

for char in range(len(chosen_word)):
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess The Letter: ").lower()
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess

    convert_chosen_word = ''.join(display)
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

# for char in display:
#     if char == '_':
#         while convert_chosen_word != chosen_word:
#             guess = input("Guess The Letter: ").lower()

#             for letter in range(len(chosen_word)):
#                 if guess == chosen_word[letter]:
#                     display[letter] = guess

#             convert_chosen_word = ''.join(display)
#             print(display)
#     else:
#         break