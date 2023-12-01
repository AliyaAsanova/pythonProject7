import random



def main():
    print("Welcome to Sea Battle Game!")
    
    # Initialize the board
    board = [["O"] * 5 for _ in range(5)]
    player_board = [["O"] * 5 for _ in range(5)]
    
    # Place player's ship
    print_board(player_board)
    print("Place your ship:")
    player_ship_row, player_ship_col = player_input()
    player_board[player_ship_row][player_ship_col] = "S"
    
    # Place computer's ship
    comp_ship_row, comp_ship_col = random_row_col(), random_row_col()
    
    print("\nPlayer's Board:")
    print_board(player_board)
    
    # Game loop
    while True:
        print("\nYour Turn!")
        print_board(board)
        guess_row, guess_col = player_input()
        
        if guess_row == comp_ship_row and guess_col == comp_ship_col:
            print("Congratulations! You sank the computer's ship. You win!")
            break
        elif board[guess_row][guess_col] == "X":
            print("You already guessed that one. Try again.")
        else:
            print("You missed!")
            board[guess_row][guess_col] = "X"
        
        print("\nComputer's Turn!")
        comp_guess_row, comp_guess_col = random_row_col(), random_row_col()
        
        if comp_guess_row == player_ship_row and comp_guess_col == player_ship_col:
            print("Oh no! The computer sank your ship. You lose!")
            break
        elif board[comp_guess_row][comp_guess_col] == "X":
            print("The computer already guessed that one. It tries again.")
        else:
            print("The computer missed!")
            board[comp_guess_row][comp_guess_col] = "X"

if __name__ == "__main__":
    main()
