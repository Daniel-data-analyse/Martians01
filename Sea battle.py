import os
import random
import string

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def make_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("~")
        board.append(row)
    return board

def show_board(board):
    letters = string.ascii_uppercase[:len(board)]
    print("  ", end="")
    for letter in letters:
        print(letter, end=" ")
    print()
    for i in range(len(board)):
        print(str(i + 1).rjust(2), end=" ")
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

def can_place_ship(board, x, y, size, dx, dy):
    for i in range(size):
        nx = x + dx * i
        ny = y + dy * i
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
            return False
        for adj_x in range(-1, 2):
            for adj_y in range(-1, 2):
                ax = nx + adj_x
                ay = ny + adj_y
                if 0 <= ax < len(board) and 0 <= ay < len(board) and board[ax][ay] != "~":
                    return False
    return True

def place_single_cell_ship(board):
    placed = False
    while not placed:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_ship(board, x, y, 1, 0, 0):
            board[x][y] = "O"
            placed = True

def place_double_cell_ship(board):
    directions = [(0, 1), (1, 0)]
    placed = False
    while not placed:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        dx, dy = random.choice(directions)
        if can_place_ship(board, x, y, 2, dx, dy):
            for i in range(2):
                board[x + dx * i][y + dy * i] = "O"
            placed = True

def place_triple_cell_ship(board):
    directions = [(0, 1), (1, 0)]
    placed = False
    while not placed:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        dx, dy = random.choice(directions)
        if can_place_ship(board, x, y, 3, dx, dy):
            for i in range(3):
                board[x + dx * i][y + dy * i] = "O"
            placed = True

def place_ships(board):
    for _ in range(4):
        place_single_cell_ship(board)
    for _ in range(2):
        place_double_cell_ship(board)
    place_triple_cell_ship(board)

def get_move(board, guesses):
    valid_move = False
    x, y = -1, -1
    while not valid_move:
        move = input("Enter your move (e.g., A5): ").strip().upper()
        if len(move) < 2 or move[0] not in string.ascii_uppercase[:len(board)] or not move[1:].isdigit():
            print("Invalid format! Use a letter and a number, e.g., A5.")
        else:
            x = int(move[1:]) - 1
            y = string.ascii_uppercase.index(move[0])
            if x < 0 or x >= len(board) or y < 0 or y >= len(board):
                print("Out of bounds! Stay within the board.")
            elif guesses[x][y] != "~":
                print("You already guessed that spot!")
            else:
                valid_move = True
    return x, y

def check_guess(board, guesses, x, y):
    hit = False
    if board[x][y] == "O":
        guesses[x][y] = "X"
        board[x][y] = "X"
        hit = True
    elif board[x][y] == "~":
        guesses[x][y] = "."
    return hit

def all_sunk(board):
    sunk = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "O":
                sunk = False
    return sunk

def print_instructions():
    print("Welcome to Battleship!")
    print("The goal is to sink all the enemy ships.")
    print("You will take turns guessing where the enemy ships are located.")
    print("Each ship occupies one or more squares, and you need to hit all of them.")
    print("Use coordinates like A1, B3 to shoot. Example: A1, C5.")
    print("Ships can be placed horizontally or vertically, and cannot touch each other.")
    print("Good luck!")

def play_game():
    size = 7
    scores = []
    playing = True

    while playing:
        clear()
        print_instructions()

        print("Enter your name:")
        name = input().strip()
        guesses_count = 0

        board = make_board(size)
        guesses = make_board(size)
        place_ships(board)

        game_active = True
        while game_active:
            clear()
            print("Player:")
            print(name)
            show_board(guesses)

            x, y = get_move(board, guesses)
            guesses_count += 1

            hit = check_guess(board, guesses, x, y)
            if hit:
                print("You hit a ship!")
            else:
                print("You missed!")

            sunk = all_sunk(board)
            if sunk:
                clear()
                print("*** Congratulations! ***")
                print(name)
                print("You sunk all the ships!")
                print("You took", guesses_count, "guesses.")
                scores.append((name, guesses_count))
                game_active = False

        print("Do you want to play again? (y/n):")
        again = input().strip().lower()
        if again == "y":
            playing = True
        elif again == "n":
            playing = False
        else:
            print("Invalid input, exiting the game.")
            playing = False

    clear()
    print("Leaderboard:")
    scores.sort(key=lambda x: x[1])
    for i in range(len(scores)):
        print(str(i + 1) + ". " + scores[i][0] + " - " + str(scores[i][1]) + " guesses")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()