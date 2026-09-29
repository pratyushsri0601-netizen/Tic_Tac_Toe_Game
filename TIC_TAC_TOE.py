print("================================================")
print("              TIC TAC TOE GAME")
print("================================================")

print()
print("Welcome to the Tic Tac Toe game!")
print("Two players can play this game.")
print("Player 1 will use X.")
print("Player 2 will use O.")
print()

player1 = input("Enter name of Player 1: ")
player2 = input("Enter name of Player 2: ")

while player1 == "":
    print("Name cannot be empty.")
    player1 = input("Enter name of Player 1: ")

while player2 == "":
    print("Name cannot be empty.")
    player2 = input("Enter name of Player 2: ")

filename = player1 + "_vs_" + player2 + ".txt"

file = open(filename, "a")
file.close()

def save_game_to_file(game_num, result):
    file = open(filename, "a")
    line = "Game " + str(game_num) + ": " + result + "\n"
    file.write(line)
    file.close()

def clear_game_file():
    file = open(filename, "w")
    file.close()

score1 = 0
score2 = 0

draws = 0
total_games = 0

history = []

def show_menu():

    print()
    print("--------------- MENU ---------------")
    print("1. Start Game")
    print("2. Show Score")
    print("3. Show Game History (from file)")
    print("4. Show Player Details")
    print("5. Reset Score & Clear File")
    print("6. Exit")
    print("------------------------------------")

def create_board():

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    return board

def show_board(board):

    print()
    print("        " + board[0] + " | " + board[1] + " | " + board[2])
    print("       ---+---+---")
    print("        " + board[3] + " | " + board[4] + " | " + board[5])
    print("       ---+---+---")
    print("        " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def show_position_guide():

    print()
    print("Position numbers are:")
    print()

    print("        1 | 2 | 3")
    print("       ---+---+---")
    print("        4 | 5 | 6")
    print("       ---+---+---")
    print("        7 | 8 | 9")
    print()

def position_available(board, position):

    if board[position] == "X":
        return False

    if board[position] == "O":
        return False

    return True

def get_move(board, player_name):

    while True:

        choice = input(player_name + ", enter position (1-9): " )

        if choice.isdigit() == False:

            print("Please enter a number.")

        else:

            position = int(choice)

            if position < 1 or position > 9:

                print("Please enter a number between 1 and 9.")

            else:

                position = position - 1

                if position_available(board, position):

                    return position

                else:

                    print("This position is already taken.")

def check_rows(board, symbol):

    if board[0] == symbol:
        if board[1] == symbol:
            if board[2] == symbol:
                return True

    if board[3] == symbol:
        if board[4] == symbol:
            if board[5] == symbol:
                return True

    if board[6] == symbol:
        if board[7] == symbol:
            if board[8] == symbol:
                return True

    return False

def check_columns(board, symbol):

    if board[0] == symbol:
        if board[3] == symbol:
            if board[6] == symbol:
                return True

    if board[1] == symbol:
        if board[4] == symbol:
            if board[7] == symbol:
                return True

    if board[2] == symbol:
        if board[5] == symbol:
            if board[8] == symbol:
                return True

    return False

def check_diagonals(board, symbol):

    if board[0] == symbol:
        if board[4] == symbol:
            if board[8] == symbol:
                return True

    if board[2] == symbol:
        if board[4] == symbol:
            if board[6] == symbol:
                return True

    return False

def check_winner(board, symbol):

    if check_rows(board, symbol):
        return True

    if check_columns(board, symbol):
        return True

    if check_diagonals(board, symbol):
        return True

    return False

def check_draw(board):

    for position in board:

        if position != "X":
            if position != "O":
                return False

    return True

def show_score():

    print()
    print("========================================")
    print("                 SCORE")
    print("========================================")

    print(player1, "(X) :", score1)
    print(player2, "(O) :", score2)
    print("Draws       :", draws)
    print("Total Games :", total_games)

    print("========================================")

def show_player_details():

    print()
    print("========================================")
    print("             PLAYER DETAILS")
    print("========================================")

    print("Player 1")
    print("Name   :", player1)
    print("Symbol :", "X")
    print()

    print("Player 2")
    print("Name   :", player2)
    print("Symbol :", "O")
    print()
    print("Match File:", filename)

    print("========================================")

def reset_score():

    global score1
    global score2
    global draws
    global total_games

    confirm = input(
        "Are you sure you want to reset the score and clear file? (y/n): "
    )

    if confirm.lower() == "y":

        score1 = 0
        score2 = 0
        draws = 0
        total_games = 0

        history.clear()
        clear_game_file()

        print("Score and file records have been reset.")

    else:

        print("Score was not reset.")

def add_history(result):

    game_number = total_games

    history.append([game_number, result])
    save_game_to_file(game_number, result)

def show_history():

    print()
    print("========================================")
    print("       GAME HISTORY (FROM FILE)")
    print("========================================")

    file = open(filename, "r")
    records = file.readlines()
    file.close()

    if len(records) == 0:
        print("No games recorded in file yet.")
    else:
        for line in records:
            print(line, end="")

    print("========================================")

def start_game():

    global score1
    global score2
    global draws
    global total_games

    board = create_board()

    current_player = player1
    current_symbol = "X"

    print()
    print("========================================")
    print("              GAME STARTED")
    print("========================================")

    show_position_guide()

    for turn in range(9):

        show_board(board)

        print(
            current_player,
            "is playing with",
            current_symbol
        )

        position = get_move(
            board,
            current_player
        )

        board[position] = current_symbol

        if check_winner(
            board,
            current_symbol
        ):

            show_board(board)

            print()
            print(
                "Congratulations",
                current_player,
                "!"
            )

            print(
                "You won the game."
            )

            if current_symbol == "X":

                score1 = score1 + 1

            else:

                score2 = score2 + 1

            total_games = total_games + 1

            add_history(
                current_player + " won"
            )

            return

        if check_draw(board):

            show_board(board)

            print()
            print("The game is a draw.")

            draws = draws + 1
            total_games = total_games + 1

            add_history("Draw")

            return

        if current_symbol == "X":

            current_symbol = "O"
            current_player = player2

        else:

            current_symbol = "X"
            current_player = player1

def instructions():

    print()
    print("========================================")
    print("            HOW TO PLAY")
    print("========================================")

    print("1. Player 1 uses X.")
    print("2. Player 2 uses O.")
    print("3. Players select positions from 1 to 9.")
    print("4. First player to get three symbols")
    print("   in a row wins.")
    print("5. A row can be horizontal, vertical")
    print("   or diagonal.")
    print("6. If all positions are filled and")
    print("   nobody wins, the game is a draw.")

    print()
    print("Example board:")

    show_position_guide()

    print("========================================")

print()
print("========================================")
print("           WELCOME PLAYERS")
print("========================================")

print(
    "Player 1:",
    player1,
    "(X)"
)

print(
    "Player 2:",
    player2,
    "(O)"
)

print("Game Data File:", filename)
print("========================================")

while True:

    show_menu()

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":

        start_game()

    elif choice == "2":

        show_score()

    elif choice == "3":

        show_history()

    elif choice == "4":

        show_player_details()

    elif choice == "5":

        reset_score()

    elif choice == "6":

        print()
        print("========================================")
        print("          THANK YOU FOR PLAYING")
        print("========================================")

        print(
            "Final Score:",
            player1,
            "=",
            score1,
            "|",
            player2,
            "=",
            score2
        )

        break

    else:

        print()
        print("Invalid choice.")
        print("Please select a number from 1 to 6.")
