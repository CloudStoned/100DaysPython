import random
import string


print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))

password = []

for let in range(1, letters + 1):
    letter = random.choice(string.ascii_letters)
    password.append(letter)

for sym in range(0, symbols):
    symbol = random.choice(string.punctuation)
    password.append(symbol)

for num in range(0,numbers):
    number = random.randint(0, numbers)
    password.append(number)

random.shuffle(password)

print("Your password is: ", end='')
for c in password:
    print(c,end='')
