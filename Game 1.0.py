# Oyun tahtasını oluşturalım
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Oyuncunun hamlesini alalım
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, hamleni yap (1-9): "))
            if move < 1 or move > 9:
                print("1-9 arasında bir sayı gir!")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Bu kare dolu, başka bir kare seç!")
        except ValueError:
            print("Geçerli bir sayı gir!")

