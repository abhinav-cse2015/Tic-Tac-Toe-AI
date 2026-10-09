import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_empty_board(self):
        game = TicTacToe()

        self.assertEqual(
            len(game.available_moves()),
            9
        )

    def test_human_wins(self):
        game = TicTacToe()

        game.board = [
            "X", "X", "X",
            "O", "O", " ",
            " ", " ", " "
        ]

        self.assertEqual(
            game.check_winner(),
            "X"
        )

    def test_computer_wins(self):
        game = TicTacToe()

        game.board = [
            "O", "O", "O",
            "X", "X", " ",
            " ", " ", " "
        ]

        self.assertEqual(
            game.check_winner(),
            "O"
        )

    def test_draw(self):
        game = TicTacToe()

        game.board = [
            "X", "O", "X",
            "X", "O", "O",
            "O", "X", "X"
        ]

        self.assertEqual(
            game.check_winner(),
            "D"
        )

    def test_game_continues(self):
        game = TicTacToe()

        game.board = [
            "X", "O", " ",
            " ", "X", " ",
            " ", " ", "O"
        ]

        self.assertIsNone(
            game.check_winner()
        )

    def test_available_moves(self):
        game = TicTacToe()

        game.board[0] = "X"
        game.board[4] = "O"

        moves = game.available_moves()

        self.assertNotIn(0, moves)
        self.assertNotIn(4, moves)
        self.assertEqual(len(moves), 7)

    def test_minimax_computer_winning_move(self):
        game = TicTacToe()

        game.board = [
            "O", "O", " ",
            "X", "X", " ",
            " ", " ", " "
        ]

        game.computer_move()

        self.assertEqual(
            game.board[2],
            "O"
        )

    def test_ai_blocks_human(self):
        game = TicTacToe()

        game.board = [
            "X", "X", " ",
            "O", " ", " ",
            " ", " ", "O"
        ]

        game.computer_move()

        self.assertEqual(
            game.board[2],
            "O"
        )

    def test_easy_difficulty(self):
        game = TicTacToe("easy")

        self.assertEqual(
            game.difficulty,
            "easy"
        )

        move = game.random_move()

        self.assertIn(
            move,
            game.available_moves()
        )

    def test_medium_difficulty(self):
        game = TicTacToe("medium")

        self.assertEqual(
            game.difficulty,
            "medium"
        )

    def test_hard_difficulty(self):
        game = TicTacToe("hard")

        self.assertEqual(
            game.difficulty,
            "hard"
        )

    def test_medium_ai_takes_winning_move(self):
        game = TicTacToe("medium")

        game.board = [
            "O", "O", " ",
            "X", "X", " ",
            " ", " ", " "
        ]

        game.computer_move()

        self.assertEqual(
            game.board[2],
            "O"
        )

    def test_medium_ai_blocks_human(self):
        game = TicTacToe("medium")

        game.board = [
            "X", "X", " ",
            "O", " ", " ",
            " ", " ", "O"
        ]

        game.computer_move()

        self.assertEqual(
            game.board[2],
            "O"
        )

    def test_scoreboard_initial_values(self):
        game = TicTacToe()

        self.assertEqual(
            game.human_score,
            0
        )

        self.assertEqual(
            game.computer_score,
            0
        )

        self.assertEqual(
            game.draws,
            0
        )

    def test_reset_board(self):
        game = TicTacToe()

        game.board[0] = "X"
        game.board[4] = "O"

        game.reset_board()

        self.assertEqual(
            game.board,
            [" "] * 9
        )


if __name__ == "__main__":
    unittest.main()