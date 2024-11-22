# Tic-Tac-Toe
Here’s a detailed explanation of the game:

---

### Infinite Tic-Tac-Toe Game with FIFO System

This program is a Python implementation of a customizable Tic-Tac-Toe game designed to create an infinite play experience using a FIFO (First In, First Out) system. Players can continuously play without limitations, as the program automatically manages the number of pieces each player can have on the board. Below is a breakdown of the game features and how it works:

---

Key Features:

1. Player Name Input:
   - At the beginning of the game, both players are prompted to enter their names, personalizing the game experience.

2. Symbol Selection**:
   - The program allows players to choose their preferred symbol (**X** or **O**) at the start of the game. 
   - If a player enters an invalid name during selection, the program automatically assigns **X** to Player 1 and **O** to Player 2.

3. Dynamic FIFO Gameplay:
   - Each player can only have a maximum of three pieces on the board at any given time.
   - When a player places a fourth piece, the oldest piece they placed is automatically removed (FIFO system).
   - This ensures the board never fills up, allowing the game to continue indefinitely.

4. Win Conditions:
   - The program automatically checks for win conditions after each move.
   - A player wins if they place three of their symbols in a row (horizontally, vertically, or diagonally).

5. Interactive Prompts:
   - During each turn, players are asked to make their moves by choosing a number between 1 and 9, corresponding to the position on the board.
   - The board is displayed after each turn, showing the current game state.

6. **Error Handling**:
   - The program prevents players from choosing already occupied spaces.
   - It handles invalid inputs gracefully, asking players to try again if they make a mistake.

---

### How the Game Works:

1. Game Setup:
   - The program starts by welcoming the players and asking them to enter their names.
   - Players then select who will use the **X** symbol. The other player is automatically assigned the **O** symbol.

2. Taking Turns:
   - Players take turns making moves by selecting a position on the 3x3 grid (numbered 1-9).
   - If the selected position is already occupied, the program asks the player to choose another spot.

3. FIFO Mechanism:
   - If a player already has three pieces on the board and attempts to place another, the oldest piece they placed is removed.
   - This mechanism ensures the game can continue indefinitely without filling up the board.

4. Winning the Game:
   - After each move, the program checks for win conditions:
     - Three symbols in a row (horizontally, vertically, or diagonally).
   - If a player wins, the program announces the winner and ends the game.

5. Continuing the Game:
   - If no winner is found after each turn, the game continues, and players can keep placing pieces according to the FIFO rule.

---

Example Gameplay:

1. Player Setup:
   - Player 1: Alice
   - Player 2: Bob
   - Alice chooses to play as X, and Bob plays as **O**.

2. Initial Moves:
   - Alice places X in position 1.
   - Bob places O in position 5.
   - Alice places X in position 2.

3. FIFO in Action:
   - Alice places her fourth X in position 3.
   - The oldest **X** (in position 1) is automatically removed.

4. Winning the Game:
   - Bob places O in position 6, completing a row of three O symbols.
   - The program announces Bob as the winner.

---

Customization Opportunities:
- Add an AI opponent for single-player mode.
- Expand the grid size for more complex games.
- Introduce adjustable rules, such as allowing more pieces on the board or changing the win condition.

This implementation makes Tic-Tac-Toe engaging and fun by ensuring continuous play while maintaining fair and logical rules. Enjoy the infinite possibilities of this classic game with a modern twist! 😊
