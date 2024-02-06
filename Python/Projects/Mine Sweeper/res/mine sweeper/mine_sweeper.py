import random

def create_board(m, n, num_mines):
    # Initialize board with 0
    board = [[0]*n for _ in range(m)]
    
    # Place mines
    mines = random.sample(range(m*n), num_mines)
    for mine in mines:
        x, y = divmod(mine, n)
        board[x][y] = 'M'
        
    return board

def print_board(board):
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(len(board[0]))))
    # Print each row with its row number
    for i, row in enumerate(board):
        print(str(i) + " " + ' '.join(str(cell) for cell in row))

def play_game(m=10, n=10, num_mines=5):
    board = create_board(m, n, num_mines)
    while True:
        print_board(board)
        x = int(input("Enter row number (0-indexed): "))
        y = int(input("Enter column number (0-indexed): "))
        if board[x][y] == 'M':
            print("Game Over!")
            return
        else:
            board[x][y] = 'C'

play_game()