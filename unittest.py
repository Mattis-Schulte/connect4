import unittest

from connect_four_board import ConnectFourBoard
from connect_four_game import ConnectFourGame
from player import Player
from color import Color


class MyTestCase(unittest.TestCase):
    def test_creation(self):
        board = ConnectFourBoard()

    def test_set_token(self):
        board = ConnectFourBoard()

        # [1, 3, 1, 3, 1, 3, 1]
        [board.set_token(x, Color.GREEN) if x % 2 else board.set_token(x, Color.RED) for x in range(0, board.X_MAX)]

    def test_get_token(self):
        board = ConnectFourBoard()

        [board.set_token(x, Color.GREEN) if x % 2 else board.set_token(x, Color.RED) for x in range(0, board.X_MAX)]
        actual_row = [board.get_token(x, 0) for x in range(0, board.X_MAX)]
        desired_row = [Color.GREEN if x % 2 else Color.RED for x in range(0, board.X_MAX)]
        self.assertEqual(actual_row, desired_row)

    def test_is_board_full(self):
        board = ConnectFourBoard()

        [[board.set_token(x, Color.GREEN) for x in range(0, board.X_MAX)] for _ in range(0, board.Y_MAX)]
        self.assertTrue(board.is_board_full())

    def test_is_board_full_false(self):
        board = ConnectFourBoard()

        self.assertFalse(board.is_board_full())

    def test_is_column_full(self):
        board = ConnectFourBoard()

        [board.set_token(0, Color.GREEN) for _ in range(0, board.Y_MAX)]
        self.assertTrue(board.is_col_full(0))

    def test_is_column_full_false(self):
        board = ConnectFourBoard()

        self.assertFalse(board.is_col_full(0))

    def test_set_token_invalid_column(self):
        board = ConnectFourBoard()

        with self.assertRaises(IndexError):
            board.set_token(board.X_MAX, Color.GREEN)

    def test_row_is_winning_horizontally(self):
        board = ConnectFourBoard()

        [board.set_token(x, Color.GREEN) for x in range(0, 4)]
        self.assertTrue(board.is_winning())

    def test_row_is_winning_vertically(self):
        board = ConnectFourBoard()

        [board.set_token(0, Color.GREEN) for _ in range(0, 4)]
        self.assertTrue(board.is_winning())

    def test_row_is_winning_diagonally_up(self):
        board = ConnectFourBoard()

        [[board.set_token(x, Color.GREEN) if x == y else board.set_token(x, Color.RED) for x in range(0, 4)] for y in range(0, 4)]
        self.assertTrue(board.is_winning())

    def test_row_is_winning_diagonally_down(self):
        board = ConnectFourBoard()

        [[board.set_token(x, Color.GREEN) if 3 - x == y else board.set_token(x, Color.RED) for x in range(0, 4)] for y in range(0, 4)]
        self.assertTrue(board.is_winning())

    def test_get_winning_positions(self):
        board = ConnectFourBoard()

        [board.set_token(x, Color.GREEN) for x in range(0, 4)]
        self.assertEqual(board.get_winning_positions(), [[0, 0], [1, 0], [2, 0], [3, 0]])

    def test_create_player_instance(self):
        player = Player("Test", Color.GREEN)
        self.assertEqual(player.name, "Test")
        self.assertEqual(player.color, Color.GREEN)

    def test_create_game_instance(self):
        player1 = Player("Test1", Color.GREEN)
        player2 = Player("Test2", Color.RED)
        board = ConnectFourBoard()
        game = ConnectFourGame(player1, player2, board)
        self.assertEqual(game.p1, player1)
        self.assertEqual(game.p2, player2)


if __name__ == '__main__':
    unittest.main()
