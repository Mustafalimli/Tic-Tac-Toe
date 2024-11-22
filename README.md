Infinite Tic-Tac-Toe with a FIFO System

This is a fun twist on the classic Tic-Tac-Toe game where the gameplay never stops. Instead of ending when the board is full or someone runs out of moves, the game uses a FIFO (First In, First Out) system to keep things flowing. Here's how it works:

---

Features

- Custom Names: At the start, players are asked for their names. No more boring "Player 1" and "Player 2" — personalize it!
- Symbol Choice: Players can pick whether they want to be X or O. Don’t worry, if you can’t decide or input something invalid, the game will assign X to the first player.
- FIFO Rule: Each player can only have three pieces on the board at a time. If you want to place a fourth piece, the game automatically removes your oldest one — like a queue! This keeps the board manageable and ensures you can play endlessly.
- Win Detection: The game checks for a win after every turn. If you get three of your pieces in a row, you win — simple and classic.
- Interactive Gameplay: The game board updates after every move, so you can see what’s happening in real-time. It also gives helpful messages if you make an invalid move.

---

How It Plays Out

1. Setup: The game starts by asking for each player’s name. Then, you choose who gets to be X. The other player automatically becomes O.
2. Taking Turns: Players alternate turns by picking a number between 1 and 9 to place their symbol on the grid. It’s numbered like this:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

    If a spot is already taken, the game will let you know and ask you to choose again.
4. FIFO in Action: If you already have three pieces on the board and place another, the oldest piece is removed automatically. This makes room for your new move while keeping the game interesting.
5. Winning: The game constantly checks if anyone has three in a row. If you do, congrats — you win, and the game ends!
6. Ongoing Fun: If no one wins, the game keeps going forever. You’ll always have three pieces to work with, so it’s a battle of strategy and endurance.
