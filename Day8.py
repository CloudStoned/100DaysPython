alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")

text = input("Type your message: ").lower()
shift = int(input("Type shift number: "))


def encrypt (text, shift):
    for char in text:
        char_pos = int(alphabet.index(char))
        char_shift = int(char_pos) + shift
        encrypted_text = alphabet[char_shift]
        print(encrypted_text)

"""
Course Version
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift_amount
        new_let = alphabet[new_pos]
        cipher_text += new_let
    print(cipher_text)
"""

encrypt(text,shift)


