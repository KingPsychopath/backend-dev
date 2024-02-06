# Minesweeper

This is a simple implementation of the classic Minesweeper game in Python.

## How to Play

The game starts by creating a 10x10 board with 5 mines randomly placed. The board is printed to the console with each cell represented by a number. A '0' represents an uncovered cell, and a 'M' represents a mine.

The player is prompted to enter the row and column numbers of the cell they want to uncover. If the selected cell contains a mine, the game is over. If the cell does not contain a mine, it is marked as uncovered and the game continues.

## Code Structure

The program consists of three main functions:

- `create_board(m, n, num_mines)`: This function creates a game board of size `m` by `n` with `num_mines` mines randomly placed.

- `print_board(board)`: This function prints the current state of the game board. It prints the column numbers at the top and the row numbers at the start of each row.

- `play_game(m=10, n=10, num_mines=5)`: This is the main function that allows the user to play the game. It creates a game board and enters a loop where it continually prompts the user to uncover a cell until a mine is uncovered.

## Running the Program

To play the game, simply run the `mine_sweeper.py` script in Python:

```bash
python mine_sweeper.py
```

## Implementation

```python
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
```

In the `create_board` function, we generate a game board with mines. Here's how it works:

1. We start by initializing an `m` by `n` board with all cells set to 0.
2. We randomly select `num_mines` unique positions on the board using the `random.sample` function. The `random.sample` function returns a list of unique elements chosen from the given range.
3. For each mine position, we calculate the row and column indices using the `divmod` function. The `divmod` function takes two arguments and returns a tuple containing the quotient and remainder of the division.
4. We set the corresponding cell on the board to 'M' to indicate the presence of a mine.
5. Finally, we return the generated board.

```python
def print_board(board):
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(len(board[0]))))
    # Print each row with its row number
    for i, row in enumerate(board):
        print(str(i) + " " + ' '.join(str(cell) for cell in row))
```

The `print_board` function is responsible for printing the game board. Here's how it works:

1. We first print the column numbers at the top of the board. We use the `join` function to concatenate the column numbers with a space separator.
2. Next, we iterate over each row in the board using the `enumerate` function to get both the row index (`i`) and the row itself (`row`).
3. For each row, we print the row number followed by the cells joined with a space separator.

```python
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
```

The `play_game` function is the main function that allows the user to play the game. Here's how it works:

1. We start by creating a game board using the `create_board` function with the specified dimensions (`m` rows and `n` columns) and number of mines (`num_mines`).
2. We enter a while loop that continues indefinitely until the game is over.
3. Inside the loop, we print the current state of the board using the `print_board` function.
4. We prompt the user to enter the row and column numbers of the cell they want to uncover. The input is converted to integers using the `int` function.
5. If the selected cell contains a mine (`board[x][y] == 'M'`), we print "Game Over!" and return from the function, ending the game.
6. Otherwise, we mark the selected cell as uncovered by setting it to 'C' on the board.
7. The loop continues, allowing the user to make another move.

Overall, this code allows the user to play a simple minesweeper game by uncovering cells on the board and avoiding mines.
