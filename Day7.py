import random

word_list = ['ardvark', 'baboon', 'camel','install', 'listen','stylistic','time','letter',
            'number','nigerian','nanotech','water']

chosen_word = random.choice(word_list)w
print(f'No of letters: {len(chosen_word)}')
print(f'{chosen_word[0]} and {chosen_word[-1]}')

display = []
end_of_game = False
lives = 6

for char in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess The Word: ").lower()
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
    
    if guess not in chosen_word:
        lives = lives - 1
        print(f'Lives left: {lives}')
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
