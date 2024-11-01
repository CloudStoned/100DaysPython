line1 = [' ', ' ', ' ']
line2 = [' ', ' ', ' ']
line3 = [' ', ' ', ' ']

map = [line1,line2,line3]

print("Hiding your treasure! X marks the spot.")
position = input()

letter = position[0].lower()
cols = ['a','b','c']

cols_index = cols.index(letter)
row_index = int(position[1]) - 1

map[row_index][cols_index] = "X"

print(f'{line1} \n {line2} \n {line3}')

