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
     # Kazanma durumunu kontrol edelim
def check_winner(board, player):
    # Satırları, sütunları ve çaprazları kontrol et
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
    # Beraberlik kontrolü
def check_draw(board):
    return all(cell != " " for row in board for cell in row)
