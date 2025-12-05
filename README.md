# ludo-on-chess-board
Rules of the game:
1. All players take turns rolling the dice. The player who rolls a 6 starts the game. They place the first piece on the board.

2. You can move all your pieces onto the board, one at a time, and only when the number 6 rolls. If the corner from which a player begins their move is occupied by their own piece, they cannot move a second piece onto the board. They can only move forward.

3. If an opponent's piece is in that corner, the player removes that piece from the board and brings their own piece in. The opponent will have to wait for a "6" to roll again to bring that piece back onto the board.

4. If during the game the dice roll a number that exceeds the number of empty squares before the opponent's piece, the player remains in place or moves another piece. Jumping over your own or opponent's pieces is prohibited.


how to play the game (ludogame.py):
at each turn the program displays the board, all possible moves, a letter represnting whose turn it is ('B' for blue, 'R' for red). the player whose turn is shown chooses a number from zero to number of moves -1, indecating the index of the move you want.
the program stops when someone wins and displays the winner.
