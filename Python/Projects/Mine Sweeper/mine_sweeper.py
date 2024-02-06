# Python Standard Library Imports
import random
import time
import copy
import asyncio
from datetime import datetime as dt

# Third Party Imports
import httpx

class API:
    def __init__(self):
        pass

    # Still feels fuzzy with this; not like JS where you can just do a fetch and get the data
    # Need to do more research on this
    async def get_my_ip(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get('https://api.ipify.org/')
                data = response.text
                # print(f'Your IP is: {data}')
                return data # Return the ip key from the JSON body
        except httpx.RequestError as e:
            print(f'Request Exception (IP): {e}')
            return None
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def get_local_time(self):
        try:
            ip = await self.get_my_ip()
            async with httpx.AsyncClient() as client:
                response = await client.get(f'http://worldtimeapi.org/api/ip/{ip}')
                data = response.json() # Create JSON body
                return dt.fromisoformat(data['datetime']) # Return the datetime key from the JSON body
        except httpx.RequestError as e:
            print(f'Requests Exception (Date): {e}')
            return None
        except Exception as e:
            print(f'Error: {e}')
            return None

# My Version that I did entirely myself.
class Cell:
    def __init__(self, is_bomb=False, is_flagged=False, is_revealed=False, value=0):
        self.__value = value
        self.__is_bomb = is_bomb
        self.__is_revealed = is_revealed
        self.__is_flagged = is_flagged

        self.__bomb_symbol = 'X'
        self.__flag_symbol = 'F'

        if self.__is_bomb: # If the cell is a bomb, set the value to the bomb symbol on instantiation (easy one-liner)
            self.__value = self.bomb_symbol

        if self.__is_flagged:
            self.__value = self.__flag_symbol

    def set_bomb(self, is_bomb=True):
        self.__is_bomb = is_bomb
        if self.__is_bomb:
            self.__value = self.__bomb_symbol

    def set_flag(self, is_flagged=True):
        if self.__is_revealed:
            raise ValueError('Input Error: Cannot flag a revealed cell!')
        self.__is_flagged = is_flagged
        if self.__is_flagged: # If the cell is flagged and has not been revealed, set the value to the flag symbol
            self.__value = self.__flag_symbol

    def set_value(self, value=0, is_revealed=True):
        self.__value = value
        self.__is_revealed = is_revealed
        if self.__is_flagged and self.__is_revealed: # Reset Flag status if the cell is revealed
            self.__is_flagged = False

    def set_revealed(self, is_revealed=True):
        self.__is_revealed = is_revealed
        if self.__is_flagged and self.__is_revealed: # Reset Flag status if the cell is revealed
            self.__is_flagged = False

    def get_value(self):
        return self.__value
    
    def is_bomb(self):
        return self.__is_bomb
    
    def is_revealed(self):
        return self.__is_revealed
    
    def is_flagged(self):
        return self.__is_flagged
    
    def __str__(self):
        return str(self.__value)
    
    def __repr__(self):
        return str(self.__value)
    
class Scoring:
    def __init__(self):
        pass

    def get_current_score(self, board_size, num_bombs, time):
        return round((board_size * num_bombs) / time, 2)
    
    def get_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                return float(f.read())
        except FileNotFoundError:
            return 0.0
        
    def set_high_score(self, score):
        with open('high_score.txt', 'w') as f:
            f.write(str(score))

class Board:
# Game is printed as a 1-indexed board, but is handled as a 0-indexed board
    def __init__(self, board_size=None, num_bombs=None):
        self.board_size = board_size
        self.num_bombs = num_bombs
        self.board = None # 2D Matrix of Cell Objects

        if self.board_size and self.num_bombs: # Only create a board implicitly if the board_size and num_bombs are set otherwise we use difficulty level user input
            self.restart_board()

        self.previous_state = None # Previous state of the board for undos
    
    def to_html(self):
        # Convert the board to a list of lists for easy rendering in HTML
        return [[{'is_bomb': cell.is_bomb(), 'is_revealed': cell.is_revealed(), 'is_flagged': cell.is_flagged(), 'value': str(cell)} for cell in row] for row in self.board]

    # Board Initialisation + Setup Functions

    def make_board(self):
        '''
        Initialise the board with a 2D matrix of Cell Objects - of size board_size x board_size
        '''
        self.board = [[Cell(False) for _ in range(self.board_size)] for _ in range(self.board_size)]
    
    def restart_board(self) -> None:
        '''
        Restart the current instance of the board with a new set of bombs
        '''
        self.make_board()
        self.make_bombs()

    def make_bombs(self) -> None:
        '''
        Set bombs randomly on the board
        '''
        # Randomly select positions for bombs from n*n positions
        bomb_positions = random.sample(range(self.board_size * self.board_size), self.num_bombs)

        for _ in bomb_positions:
            self.board[_ // self.board_size][_ % self.board_size].set_bomb()

    def set_difficulty(self, difficulty):
        if difficulty == 'easy':
            self.board_size = 8
            self.num_bombs = 12
        elif difficulty == 'medium':
            self.board_size = 16
            self.num_bombs = 32
        elif difficulty == 'hard':
            self.board_size = 24
            self.num_bombs = 96
        else:
            raise ValueError("Invalid Difficulty Level: Choose 'easy', 'medium', or 'hard'.")
        
        # Reset the board after changing the difficulty
        self.restart_board()


    # Track Game State / Load and Save Game Functions
        
    def save_state(self):
        self.previous_state = copy.deepcopy(self.board)
        # Has to be a deep copy otherwise the previous_state will be a reference to the current state

    def load_state(self):
        if self.previous_state is None:
            raise ValueError('Undo Error: No Previous State to Load!')
        self.board = copy.deepcopy(self.previous_state)
        print('Undo Successful: Reverted to Previous Board State!')
        self.previous_state = None

    # Game Logic Functions
        
    def check_win(self):
        '''
        Set the win condition for the game
        You win if all cells are revealed or flagged except bombs
        '''
        #if self.count_revealed_cells() + self.count_flagged_cells() != self.count_cells() - self.count_bomb_cells():
        #    return False
        # Inefficent - too many loops ; If the number of revealed cells + flagged cells is not equal to the total number of cells - bombs, the game is not over

        for row in self.board:
            for cell in row:
                if cell.is_bomb():
                    if not cell.is_flagged():
                        return False
                #else:
                #    if not cell.is_revealed():
                #        return False
                    
        if self.count_flagged_cells() != self.count_bomb_cells():
            print('You have flagged the wrong cells, reveal some of your flagged cells and to win!')
            return False

        return True
        

    def pick_a_random_cell(self) -> tuple:
        '''
        Pick a random cell from the board that is not a bomb
        '''
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        while self.board[row][col].is_bomb():
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
        return (row, col)

    def reveal_cell(self, row, col, revealed=set()) -> bool:
        '''
        Reveal a cell on the board

        Using a set to keep track of the cells that have been revealed
        This helps to prevent infinite recursion when revealing cells with no neighbouring bombs
        '''        
        # Select the cell from the board by row and col
        cell = self.board[row][col]
        if cell.is_revealed():
            raise ValueError('Cell is already revealed! Try another cell.')
        
        # Index Error - kind of redundant since we check for this in the input handling but just in case someone tries to call this function directly (me)
        if (row < 0 or row >= self.board_size) or (col < 0 or col >= self.board_size ):
            raise IndexError(f'Invalid Range: Please specify a number between 1 and {self.board_size}')
        
        # Time to reveal the cell, but first we need to check if it is a bomb; end the game if it is
        if cell.is_bomb():
            cell.set_revealed()
            return False
        
        # If the cell is not a bomb, reveal it and check if it has any neighbouring bombs
        cell.set_revealed()
        count = 0
        neighbours = self.get_cell_neighbours(row, col) # List of tuples of the form (row, col)

        for r, c in neighbours:
            if self.board[r][c].is_bomb():
                count += 1
        cell.set_value(count)

        if count == 0: # If the cell has no neighbouring bombs, reveal all neighbours
            for r, c in neighbours:
                if (r, c) not in revealed:
                    revealed.add((r, c))
                    self.reveal_cell(r, c, revealed)

        return True
    
    def flag_cell(self, row, col) -> None:
        '''
        Flag a cell on the board
        '''
        # Select the cell from the board by row and col
        cell = self.board[row][col]
        if cell.is_revealed():
            raise ValueError('Cell is already revealed! Try another cell.')
        cell.set_flag() # Set the flag status of the cell to True

    def get_cell_neighbours(self, row, col) -> list:
        '''
        Get the 3x3 neighbours of a cell in the form of a list of tuples of the form (row, col)
        '''
        neighbours = []
        # Loop through the 3x3 grid around the cell - handles out of bound cases by using max and min
        for i in range(max(0, row - 1), min(self.board_size, row + 2)): 
            for j in range(max(0, col - 1), min(self.board_size, col + 2)):
                if (i, j) != (row, col): # Skip our original cell
                    neighbours.append((i, j))
        return neighbours
    
    # Counting functions for various elements on the board

    def count_flagged_cells(self):
        return sum(cell.is_flagged() for row in self.board for cell in row)

    def count_bomb_cells(self):
        return sum(cell.is_bomb() for row in self.board for cell in row)
    
    def count_revealed_cells(self):
        return sum(cell.is_revealed() for row in self.board for cell in row)
    
    def count_ordinary_cells(self):
        return sum(not (cell.is_bomb() or cell.is_flagged()) for row in self.board for cell in row)
    
    def count_cells(self):
        return self.board_size * self.board_size
    
    # Decorators
    
    @staticmethod
    def timer_and_scoring_decorator(func):
        '''
        Wrapper function to time the game
        '''
        def wrapper(*args, **kwargs):
            start_time = time.time()
            callback = func(*args, **kwargs) # Game Loop
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Game Time: {round(elapsed_time, 2)} seconds")

            if callback:
                scoring = Scoring()
                current_score = scoring.get_current_score(args[0].board_size, args[0].num_bombs, elapsed_time) # args[0] is the board object
                high_score = scoring.get_high_score()
                print(f'Current Score: {current_score}')
                if current_score > high_score:
                    print(f'New High Score: {current_score}')
                    scoring.set_high_score(current_score)
            return callback
        return wrapper


    # Printing functions

    def print_board(self, naked=False):
        '''
        Print the board with bombs hidden
        Column and Row Numbering starts from 1; but are handled as 0-indexed
        '''
        print('     ', ' '.join('{:3}'.format(str(i)) for i in range(1, self.board_size + 1)), '\n') # Print the Column Numbers
        if naked:
            '''
            Print the entire naked board
            '''
            for i, row in enumerate(self.board):
                print('{:3}'.format(str(i + 1)), ' ', ' '.join('{:3}'.format(str(cell)) for cell in row), ' ', str(i + 1))
            return
        for i, row in enumerate(self.board): # Print the Row Numbers + the row
            print('{:3}'.format(str(i + 1)), ' ', ' '.join('{:3}'.format(str(cell)) if (cell.is_revealed() or cell.is_flagged()) else '{:3}'.format('#') for cell in row), ' ', str(i + 1))

    # Game Functions + Main Game Loop / Input Handling

    @timer_and_scoring_decorator
    def play(self, test=False):
        '''
        Let the user play the game; loop until the user wins or loses
        '''
        print('Welcome to Minesweeper!\nUse the following commands to play the game:\nq or quit: Quit the game\nreset: Restart the game\nundo: Undo the last move\n')
        
        try:
            if not self.board_size or not self.num_bombs:
                difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
                self.set_difficulty(difficulty)
        except ValueError as e:
            print(str(e), '\n')
            return False
        
        if test:
            self.print_board(True)
            print('\n')

        random_cell = self.pick_a_random_cell() # Pick a random cell to start the game and reveal it
        random_cell_obj = self.board[random_cell[0]][random_cell[1]]
        random_cell_obj.set_revealed()

        time = API()
        
        while True:
            self.print_board()

            print(f'\nNumber of Bombs: {self.count_bomb_cells()}')
            print(f'Number of Flagged Cells: {self.count_flagged_cells()}')
            print(f'Number of Revealed Cells: {self.count_revealed_cells()}')

            current_time = asyncio.run(time.get_local_time())
            formatted_time = current_time.strftime('%A, %B %d, %Y %I:%M:%S %p')
            print('\n', formatted_time, '\n')

            try:
                choice = input('Enter your choice (r/f) to reveal or flag a cell: ').lower()
                if choice not in ['r', 'f', 'q', 'quit', 'reset', 'undo']:
                    raise ValueError(f'Invalid Input: Please specify r or f')
                
                if choice == 'q' or choice == 'quit':
                    print("You quit the game.")
                    break
                if choice == 'reset':
                    self.restart_board()
                    continue
                if choice == 'undo':
                    self.load_state()
                    continue

                try:
                    row = int(input("Enter the row: ")) - 1
                    col = int(input("Enter the column: ")) - 1
                except ValueError as e: # Handles the ValueError raised by the int() casting
                    raise ValueError(f'Invalid Input: Please specify a VALID number between 1 and {self.board_size}') from e
                
                # Check if the row and col are within the range of the board
                if (row < 0 or row >= self.board_size) or (col < 0 or col >= self.board_size ):
                #if (row <= 0 or row > self.board_size + 1) or (col <= 0 or col > self.board_size + 1):
                    raise IndexError(f'Invalid Range: Please specify a number between 1 and {self.board_size}')

                self.save_state() # Save the state of the board before making any changes
                if choice == 'r':
                    if not self.reveal_cell(row, col): # If the cell is a bomb, end the game
                        print("Game Over!")
                        return False
                    # Add a condition to check if the user has won ( all cells revealed or flagged except bombs )
                elif choice == 'f':
                    self.board[row][col].set_flag()

                if self.check_win():
                    print("Congratulations, My Son! You have won!")
                    return True
            except ValueError as e: 
                print(str(e), '\n')
                continue
            except Exception as e:
                print(str(e), '\n')
                continue

if __name__ == '__main__': # Run the game if the file is run directly; otherwise import the class (useful for testing or game just starts without tests)
    board = Board(2, 1)
    board.play(True)

    
'''
        for row in self.board:
            for cell in row:
                if not cell.is_bomb() and not (cell.is_revealed() or cell.is_flagged()):
                # If there is a cell that is not a bomb and is not revealed or flagged, the game is not over
                # TODO: Add some sort of check to ensure user does not flag all cells to win
                    # Could be done by checking if the number of flagged cells is equal to the number of bombs
                    return False
        if self.count_flagged_cells() != self.count_bomb_cells(): # Could do this inline with the above loop but this is more readable
            return False
        return True # If all cells are revealed or flagged except bombs, the game is over
'''