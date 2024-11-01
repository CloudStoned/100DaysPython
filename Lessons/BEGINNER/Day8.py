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
        print(encrypted_text, end='')

def decrypt(encryp_text, shift):
    for char in encryp_text:
        char_pos = int(alphabet.index(char))
        char_shift = int(char_pos) - shift
        decrypted_text = alphabet[char_shift]
        print(decrypted_text, end='')

decrypt(text,shift)



