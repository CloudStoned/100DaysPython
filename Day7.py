words = ['Testing']
life = 6
guess = ''

converted_word = ''.join(words)

for w in words:
    while life >= 0:
        guess = input("Guess the Word: ")
        if guess in words:
            print("Correct")
            for w in range(len(converted_word)):
                print("Done")
        else:
            print("Wrong")
            life = life - 1
