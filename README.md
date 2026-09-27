# Terminal Tic-Tac-Toe with Match History

A feature-rich, command-line Tic-Tac-Toe game written in pure Python. It supports two players, tracks cumulative session scores, and automatically logs each match result to a dynamic text file tied to the players' names.

---

## Features

- **Interactive Turn-Based Gameplay:** Clean CLI grid rendering with dynamic updates after each turn.
- **Move Validation:** Guards against invalid choices (non-numeric input, out-of-range numbers, and already-occupied cells).
- **Session Scoreboard:** Tracks wins for Player 1, wins for Player 2, draws, and total games played.
- **File Persistence:** Generates a custom log file (`<player1>_vs_<player2>.txt`) and writes every match outcome to disk.
- **Menu-Driven Dashboard:** Easily switch between playing, checking scores, reading match logs, viewing player profiles, and resetting state.

---

## Board Layout

Move choices map directly to cell numbers `1` through `9`:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
Getting Started
Prerequisites
Python 3.6 or higher. No external libraries or dependencies required.
Installation & Run

Clone or download this repository:

git clone https://github.com/pratyushsri0601-netizen/cli-tic-tac-toe.git


Run the script
python TIC_TAC_TOE.py

How to Play
Enter names for Player 1 (assigned X) and Player 2 (assigned O).
Use the main menu to navigate:
1: Start a new game.
2: View current scoreboard.
3: Read historical game records directly from the log file.
4: View active player names and assigned symbols.
5: Reset in-memory scores and clear the match file.
6: Exit the program.
During a match, input a number between 1 and 9 when prompted to place your mark.
The first player to align 3 symbols horizontally, vertically, or diagonally wins. If all 9 squares fill without a winner, the match ends in a draw.
