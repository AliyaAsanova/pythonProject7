import random



def main():
    print("Welcome to Sea Battle Game!")
    
    # Initialize the board
    board = [["O"] * 5 for _ in range(5)]
    player_board = [["O"] * 5 for _ in range(5)]
    
    # Place player's ship
    print_board(player_board)
    print("Place your ship:")
    
  
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
        
        
     

if __name__ == "__main__":
    main()
