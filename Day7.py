import random

#word_list = ['ardvark', 'baboon', 'camel']
word_list = ['ardvark']
chosen_word = random.choice(word_list)


print(chosen_word)
guess =input("Guess The Letter: ").lower()
display = []

for char in range(len(chosen_word)):
    display.append("_")

match = 0
for letter in range(len(chosen_word)):
    if guess == letter:
        print(chosen_word.index(letter))
        replace_letter = chosen_word.index(letter)
        display[replace_letter] = letter
