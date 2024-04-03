import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)


print(chosen_word)
guess =input("Guess The Letter: ").lower()
display = []

for char in range(len(chosen_word)):
    display.append("_")

for letter in range(len(chosen_word)):
    if guess == chosen_word[letter]:
        display[letter] = guess