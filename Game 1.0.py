# Create the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Get the player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, make your move (1-9): "))
            if move < 1 or move > 9:
                print("Enter a number between 1 and 9!")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This cell is occupied, choose another one!")
        except ValueError:
            print("Enter a valid number!")
# Check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
# Check for a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)
# Ana oyun fonksiyonu
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    for turn in range(9):  # Maksimum 9 hamle
        player = players[turn % 2]
        player_move(board, player)
        print_board(board)
        if check_winner(board, player):
            print(f"Congratulations! Player {player} won!")
            return
        if check_draw(board):
            print("The game is a draw!")
            return
    
    print("The game ended in a draw!")

# Start the game
tic_tac_toe()
