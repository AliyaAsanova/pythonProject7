import os
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    header = "  " + " ".join(string.ascii_uppercase[:7])
    print(header)

    for i, row in enumerate(board, 1):
        print(f"{i} {' '.join(row)}")

def is_valid_placement(board, ship, start_row, start_col, direction):
    ship_length = int(ship)
    if direction == 'H':
        end_col = start_col + ship_length - 1
        if end_col >= 7:
            return False
        for col in range(start_col, end_col + 1):
            if board[start_row][col] != ' ':
                return False
    elif direction == 'V':
        end_row = start_row + ship_length - 1
        if end_row >= 7:
            return False
        for row in range(start_row, end_row + 1):
            if board[row][start_col] != ' ':
                return False
    else:
        return False
    return True

def place_ship(board, ship):
    while True:
        try:
            start_coords = input(f"Enter the starting coordinates for the {ship}-unit ship (e.g., A1): ").upper()
            start_col, start_row = ord(start_coords[0]) - 65, int(start_coords[1]) - 1
            direction = input("Enter the direction (H for horizontal, V for vertical): ").upper()
        except (IndexError, ValueError, TypeError):
            print("Invalid input. Please try again.")
            continue

        if (
            0 <= start_col < 7 and
            0 <= start_row < 7 and
            is_valid_placement(board, ship, start_row, start_col, direction)
        ):
            for i in range(int(ship)):
                if direction == 'H':
                    board[start_row][start_col + i] = ship
                elif direction == 'V':
                    board[start_row + i][start_col] = ship
            break
        else:
            print("Invalid placement. Please try again.")

def initialize_board():
    board = [[' ']*7 for _ in range(7)]
    ships = {'3': 1, '2': 2, '1': 4}

    for ship, quantity in ships.items():
        for _ in range(quantity):
            clear_screen()
            print_board(board)
            print(f"Place your ships. Remaining {ship}-unit ships: {quantity}")
            place_ship(board, ship)

    return board

def take_shot(shot_board):
    while True:
        try:
            coords = input("Enter coordinates to shoot (e.g., A1): ").upper()
            col, row = ord(coords[0]) - 65, int(coords[1]) - 1
        except (IndexError, ValueError, TypeError):
            print("Invalid input. Please try again.")
            continue

        if 0 <= col < 7 and 0 <= row < 7 and shot_board[row][col] == ' ':
            return col, row
        else:
            print("Invalid shot. Please try again.")

def update_board(board, shot_board, col, row):
    if board[row][col] != ' ':
        ship_type = board[row][col]
        shot_board[row][col] = 'X'
        if all(cell == 'X' for cell in board[row] if cell != ' '):
            print(f"You sunk a {ship_type}-unit ship!")
    else:
        shot_board[row][col] = 'M'
    return shot_board

def check_victory(board):
    return all(cell == ' ' for row in board for cell in row)

def main():
    player_name = input("Enter your name: ")
    player_score = 0

    while True:
        clear_screen()
        print(f"Welcome, {player_name}!")

        board = initialize_board()
        shot_board = [[' ']*7 for _ in range(7)]

        while not check_victory(board):
            clear_screen()
            print(f"{player_name}'s Board:")
            print_board(board)
            print("\nShot Board:")
            print_board(shot_board)

            col, row = take_shot(shot_board)
            shot_board = update_board(board, shot_board, col, row)
            player_score += 1

        clear_screen()
        print("Congratulations, you sank all the ships!")
        print(f"{player_name}'s Board:")
        print_board(board)
        print(f"Number of shots: {player_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Game over. Thank you for playing!")
            break

if __name__ == "__main__":
    main()
