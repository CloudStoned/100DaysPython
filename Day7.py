import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
guess =input("Guess The Letter: ")

for c in chosen_word:
    if c.lower() == guess.lower():
        print("Correct")