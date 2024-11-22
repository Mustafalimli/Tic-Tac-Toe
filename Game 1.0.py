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
