import unittest
from tkinter import Tk
from minesweeper import Minesweeper

class MinesweeperTests(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.game = Minesweeper(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_setup(self):
        self.game.setup()
        # Assert that the number of tiles is equal to SIZE_X * SIZE_Y
        self.assertEqual(len(self.game.tiles), SIZE_X)
        for x in range(SIZE_X):
            self.assertEqual(len(self.game.tiles[x]), SIZE_Y)
            for y in range(SIZE_Y):
                tile = self.game.tiles[x][y]
                # Assert that each tile has the required attributes
                self.assertIn("id", tile)
                self.assertIn("isMine", tile)
                self.assertIn("state", tile)
                self.assertIn("coords", tile)
                self.assertIn("button", tile)
                self.assertIn("mines", tile)

    def test_restart(self):
        self.game.restart()
        # Assert that the flag count is reset to 0
        self.assertEqual(self.game.flagCount, 0)
        # Assert that the correct flag count is reset to 0
        self.assertEqual(self.game.correctFlagCount, 0)
        # Assert that the clicked count is reset to 0
        self.assertEqual(self.game.clickedCount, 0)
        # Assert that the start time is set to None
        self.assertIsNone(self.game.startTime)
        # Assert that the number of mines is reset to 0
        self.assertEqual(self.game.mines, 0)

    def test_refreshLabels(self):
        self.game.flagCount = 5
        self.game.mines = 10
        self.game.refreshLabels()
        # Assert that the flags label is updated correctly
        self.assertEqual(self.game.labels["flags"].cget("text"), "Flags: 5")
        # Assert that the mines label is updated correctly
        self.assertEqual(self.game.labels["mines"].cget("text"), "Mines: 10")

    def test_gameOver(self):
        # Test game over with win
        self.game.gameOver(True)
        # Assert that the game over message box is displayed
        # (Cannot be tested programmatically)
        # Assert that the game is restarted if the user chooses to play again
        # (Cannot be tested programmatically)
        # Assert that the game is quit if the user chooses not to play again
        # (Cannot be tested programmatically)

        # Test game over with loss
        self.game.gameOver(False)
        # Assert that the game over message box is displayed
        # (Cannot be tested programmatically)
        # Assert that the game is restarted if the user chooses to play again
        # (Cannot be tested programmatically)
        # Assert that the game is quit if the user chooses not to play again
        # (Cannot be tested programmatically)

    def test_getNeighbors(self):
        neighbors = self.game.getNeighbors(0, 0)
        # Assert that the number of neighbors is correct
        self.assertEqual(len(neighbors), 3)
        # Assert that the neighbors are correct
        expected_neighbors = [
            self.game.tiles[0][1],
            self.game.tiles[1][0],
            self.game.tiles[1][1]
        ]
        for neighbor in neighbors:
            self.assertIn(neighbor, expected_neighbors)

    def test_clearSurroundingTiles(self):
        self.game.setup()
        tile = self.game.tiles[0][0]
        tile["mines"] = 0
        self.game.clearSurroundingTiles(tile["id"])
        # Assert that the clicked count is updated correctly
        self.assertEqual(self.game.clickedCount, 9)
        # Assert that the state of the surrounding tiles is updated correctly
        for x in range(3):
            for y in range(3):
                self.assertEqual(self.game.tiles[x][y]["state"], STATE_CLICKED)

if __name__ == "__main__":
    unittest.main()