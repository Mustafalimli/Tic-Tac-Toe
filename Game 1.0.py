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
# Ana oyun fonksiyonu
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Oyununa Hoş Geldiniz!")
    print_board(board)
    
    for turn in range(9):  # Maksimum 9 hamle
        player = players[turn % 2]
        player_move(board, player)
        print_board(board)
        if check_winner(board, player):
            print(f"Tebrikler! Player {player} kazandı!")
            return
        if check_draw(board):
            print("Oyun berabere!")
            return
    
    print("Oyun berabere bitti!")

