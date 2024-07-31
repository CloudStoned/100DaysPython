import pandas as pd
data = pd.read_csv("Pandas/Day26/nato_phonetic_alphabet.csv")
phonetic = {row.letter: row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
result = [phonetic[letter] for letter in word] 
print(result)