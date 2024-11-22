def print_board(board):
    """
    Function to display the game board
    """
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
    # X and O selection
    x_player_name = input(f"{player1_name} and {player2_name}, who will be X? (Enter name): ").strip()
    if x_player_name == player1_name:
        players = {"X": player1_name, "O": player2_name}
    elif x_player_name == player2_name:
        players = {"X": player2_name, "O": player1_name}
    else:
        print("Invalid selection! X is automatically assigned to Player 1.")
        players = {"X": player1_name, "O": player2_name}
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    moves = {"X": [], "O": []}  # Tracks each player's moves
    print_board(board)
    
    while True:
        for symbol, name in players.items():
            player_move(board, symbol, moves, name)
            print_board(board)
            if check_winner(board, symbol):
                print(f"Congratulations! {name} ({symbol}) wins!")
                return
            print("The game continues...")
 # Start the game
tic_tac_toe_fifo()