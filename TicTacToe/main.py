board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def display_board():
    for row in board:
        print(" | ".join(str(cell) if cell != 0 else " " for cell in row))
        print("-" * 9)

def replace_pos(pos1,pos2,symbol):
    board[pos1][pos2] = symbol

def input_pos(symbol):
    while True:
        try:
            pos1 = int(input(f'Enter row (0, 1, 2) for {symbol}: '))
            pos2 = int(input(f'Enter column (0, 1, 2) for {symbol}: '))

            # Check if the position is within bounds and unoccupied
            if 0 <= pos1 <= 2 and 0 <= pos2 <= 2 and board[pos1][pos2] == 0:
                replace_pos(pos1, pos2, symbol)
                break
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Please enter valid integers.")


def check_winner(symbol):

    for row in range(3):
        if all(board[row][col] == symbol for col in range(3)):
            return True

    for row in range(3):
        if all(board[col][row] == symbol for col in range(3)):  
            return True
    
    # Diagonals
    if all(board[row][row] == symbol for i in range(3)):
        return True
    
    if all(board[row][2 - i] == symbol for i in range(3)):
        return True
    
    return False

def is_draw():
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True
    

def start_game():
    current_symbol = 'X'    

    while True:
        display_board()
        print(f"Player {current_symbol}'s Turn")

        input_pos(current_symbol)

        if check_winner(current_symbol):
            display_board()
            print(f'Player {current_symbol} wins')
            break

        if is_draw():
            display_board()
            print("It's a draw!")
            break
    
        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'



if __name__ == '__main__':
    start_game()

