import random

def play_game(life):
    rand_num = random.randint(1,100) 
    while life > 0:
        guess = int(input("Make a guess: "))
        if guess == rand_num:
            print("You Win")
            break

        elif guess > rand_num:
            print(f'Life: {life}')
            print("Too High")

        elif guess < rand_num:
            print("Life: ", life)
            print("Too Low")

        life -= 1

print("Guess the number")
diff = input("Choose Difficulty (easy or hard): ").lower()

if diff == 'easy':
    life = 10
    play_game(life)
        
elif diff == 'hard':
    life = 5
    play_game(life)