import unittest
from mine_sweeper import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(2, 1)

    def test_reveal_cell(self):
        self.board.reveal_cell(0, 0)
        self.assertTrue(self.board.board[0][0].is_revealed())

    def test_flag_cell(self):
        self.board.board[0][0].set_flag()
        self.assertTrue(self.board.board[0][0].is_flagged())

    def test_out_of_range(self):
        with self.assertRaises(IndexError):
            self.board.reveal_cell(-1, 0)
        with self.assertRaises(IndexError):
            self.board.reveal_cell(0, -1)
        with self.assertRaises(IndexError):
            self.board.reveal_cell(self.board.board_size, 0)
        with self.assertRaises(IndexError):
            self.board.reveal_cell(0, self.board.board_size)

    def test_reveal_bomb(self):
        self.board.board[0][0].set_bomb()
        #self.board.reveal_cell(0, 0)
        #self.assertTrue(self.board.board[0][0].is_revealed())
        self.assertTrue(not self.board.reveal_cell(0, 0, {})) # Bomb is both revealed and returns False (game over)

if __name__ == '__main__':
    unittest.main()