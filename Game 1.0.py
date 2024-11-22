# Function to display the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to handle player moves and apply the FIFO system
def player_move(board, player, moves, player_name):
    while True:
        try:
            move = int(input(f"{player_name} ({player}), make your move (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9!")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] == " ":
                # FIFO system: Limit to 3 moves
                if len(moves[player]) == 3:
                    # Remove the oldest move
                    old_row, old_col = moves[player].pop(0)
                    board[old_row][old_col] = " "
                # Add the new move
                board[row][col] = player
                moves[player].append((row, col))
                break
            else:
                print("This square is already occupied. Choose another one!")
        except ValueError:
            print("Please enter a valid number!")
# Function to check for a winner
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

# Main game function
def tic_tac_toe_fifo():
    print("Welcome to Tic-Tac-Toe!")
    
    # Get player names
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    