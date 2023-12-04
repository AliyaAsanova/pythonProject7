import os
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    header = "  " + " ".join(string.ascii_uppercase[:7])
    print(header)

    for i, row in enumerate(board, 1):
        print(f"{i} {' '.join(row)}")

def place_ships():
    ships = {'3': 1, '2': 2, '1': 4}
    board = [[' ']*7 for _ in range(7)]

    for ship_size, quantity in ships.items():
        for _ in range(quantity):
            while True:
                clear_screen()
                print_board(board)
                print(f"Placing {ship_size}-unit ship")

                try:
                    coords = input("Enter coordinates (e.g., A1): ").upper()
                    col, row = ord(coords[0]) - 65, int(coords[1]) - 1
                except (IndexError, ValueError, TypeError):
                    print("Invalid input. Please try again.")
                    continue

                if (
                    0 <= col < 7 and
                    0 <= row < 7 and
                    board[row][col] == ' ' and
                    all(board[i][j] == ' ' for i in range(row-1, row+2) for j in range(col-1, col+2) if 0 <= i < 7 and 0 <= j < 7)
                ):
                    for i in range(int(ship_size)):
                        if i == 0:
                            board[row][col] = 'O'
                        else:
                            board[row][col+i] = 'O'
                    break
                else:
                    print("Invalid placement. Please try again.")

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
    if board[row][col] == 'O':
        shot_board[row][col] = 'X'
        if all(cell != 'O' for cell in board[row]):
            print("Ship sunk!")
    else:
        shot_board[row][col] = 'M'
    return shot_board

def main():
    player_name = input("Enter your name: ")
    player_score = 0

    while True:
        clear_screen()
        print(f"Welcome, {player_name}!")

        board = place_ships()
        shot_board = [[' ']*7 for _ in range(7)]

        while any('O' in row for row in board):
            clear_screen()
            print_board(shot_board)

            col, row = take_shot(shot_board)
            shot_board = update_board(board, shot_board, col, row)

        clear_screen()
        print(f"Congratulations, {player_name}! You sank all the ships!")
        print(f"Number of shots: {player_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Game over. Here are the results:")
            # Display sorted list of players and their scores (if you are tracking scores)
            break

if __name__ == "__main__":
    main()
