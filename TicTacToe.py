import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def draw_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def choose_player_symbol():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input("Do you want to be X or O? ").upper()
    return ['X', 'O'] if symbol == 'X' else ['O', 'X']

def is_space_free(board, row, col):
    return board[row][col] == ' '

def player_move(board, player_symbol):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
            elif not is_space_free(board, row, col):
                print("That space is already taken.")
            else:
                board[row][col] = player_symbol
                break
        except:
            print("Invalid input. Please enter a number.")

def computer_move(board, comp_symbol):
    possible_moves = [(r, c) for r in range(3) for c in range(3) if is_space_free(board, r, c)]
    move = random.choice(possible_moves)
    board[move[0]][move[1]] = comp_symbol
    print("Computer has made its move.")

def check_win(board, symbol):
    # Rows, columns and diagonals
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[r][c] != ' ' for r in range(3) for c in range(3))

def main():
    print("Welcome to Tic Tac Toe!")
    board = create_board()
    player_symbol, comp_symbol = choose_player_symbol()
    current_turn = 'player' if random.choice([True, False]) else 'computer'

    while True:
        draw_board(board)

        if current_turn == 'player':
            print("Your turn.")
            player_move(board, player_symbol)
            if check_win(board, player_symbol):
                draw_board(board)
                print("You win! 🎉")
                break
            current_turn = 'computer'
        else:
            print("Computer's turn.")
            computer_move(board, comp_symbol)
            if check_win(board, comp_symbol):
                draw_board(board)
                print("Computer wins! 🤖")
                break
            current_turn = 'player'

        if is_board_full(board):
            draw_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
