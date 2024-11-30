import random
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size):
    """Creates an empty board of given size."""
    return [["~"] * size for _ in range(size)]

def print_board(board, show_ships=False):
    """Prints the board with optional ship visibility."""
    print("  " + " ".join("ABCDEFG"[:len(board)]))  # Column headers
    for i, row in enumerate(board):
        print(f"{i + 1} " + " ".join(cell if show_ships or cell not in {"O", "X", "S"} else "~" for cell in row))

def is_valid_placement(board, x, y, length, orientation):
    """Checks if a ship can be placed at the given position."""
    if orientation == "H":
        if y + length > len(board): return False
        for i in range(length):
            if not is_cell_empty(board, x, y + i): return False
    elif orientation == "V":
        if x + length > len(board): return False
        for i in range(length):
            if not is_cell_empty(board, x + i, y): return False
    return True

def is_cell_empty(board, x, y):
    """Checks if a cell and its surroundings are empty."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] != "~": return False
    return True

def place_ship(board, x, y, length, orientation):
    """Places a ship on the board."""
    if orientation == "H":
        for i in range(length):
            board[x][y + i] = "S"
    elif orientation == "V":
        for i in range(length):
            board[x + i][y] = "S"

def generate_ships(board, ships):
    """Randomly generates ships on the board."""
    for length in ships:
        placed = False
        while not placed:
            x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
            orientation = random.choice(["H", "V"])
            if is_valid_placement(board, x, y, length, orientation):
                place_ship(board, x, y, length, orientation)
                placed = True

def parse_coordinates(coord):
    """Parses letter-number coordinates into board indices."""
    try:
        letter, number = coord[0].upper(), int(coord[1:])
        x, y = number - 1, "ABCDEFG".index(letter)
        return x, y
    except (ValueError, IndexError):
        return None, None

def shoot(board, visible_board, x, y):
    """Handles the shooting logic."""
    if board[x][y] == "S":  # Hit
        visible_board[x][y] = "X"
        board[x][y] = "H"  # Mark ship as hit
        print("Hit!")
        if is_ship_sunk(board, x, y):
            print("Ship sunk!")
            mark_sunk_ship(visible_board, board)
        return True
    elif board[x][y] == "~":  # Miss
        visible_board[x][y] = "O"
        print("Miss!")
        return False
    else:  # Already shot
        print("You already shot here!")
        return None

def is_ship_sunk(board, x, y):
    """Checks if a ship is completely sunk."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == "S":
                    return False
    return True

def mark_sunk_ship(visible_board, board):
    """Marks a sunk ship on the visible board."""
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == "H":
                visible_board[x][y] = "X"

def is_game_over(board):
    """Checks if all ships are sunk."""
    for row in board:
        if "S" in row:
            return False
    return True

def play_game():
    """Main game loop."""
    size = 7
    ships = [3, 2, 2, 1, 1, 1, 1]  # Ship sizes
    board = create_board(size)
    visible_board = create_board(size)
    generate_ships(board, ships)
    
    shots = 0
    clear_screen()
    print("Welcome to Battleship!")
    player_name = input("Enter your name: ")
    
    while not is_game_over(board):
        clear_screen()
        print(f"{player_name}'s Battlefield:")
        print_board(visible_board)
        
        coord = input("Enter your shot (e.g., B3): ")
        x, y = parse_coordinates(coord)
        if x is None or y is None or not (0 <= x < size and 0 <= y < size):
            print("Invalid coordinates. Try again.")
            continue

        result = shoot(board, visible_board, x, y)
        if result is not None:
            shots += 1

    clear_screen()
    print(f"Congratulations, {player_name}! You won in {shots} shots.")
    return player_name, shots

def main():
    """Runs the game and manages leaderboard."""
    leaderboard = []
    while True:
        player_name, shots = play_game()
        leaderboard.append((player_name, shots))
        leaderboard.sort(key=lambda x: x[1])  # Sort by shots (ascending)
        
        replay = input("Play again? (yes/no): ").lower()
        if replay != "yes":
            clear_screen()
            print("Leaderboard:")
            for i, (name, score) in enumerate(leaderboard, 1):
                print(f"{i}. {name} - {score} shots")
            break

if __name__ == "__main__":
    main()
