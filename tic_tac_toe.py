import math
import random


class TicTacToe:
    """
    Tic-Tac-Toe game with three AI difficulty levels.

    Human player: X
    Computer: O

    Difficulty:
        Easy   -> Random moves
        Medium -> Basic strategy
        Hard   -> Minimax
    """

    def __init__(self, difficulty="hard"):
        self.board = [" "] * 9
        self.human = "X"
        self.computer = "O"
        self.difficulty = difficulty.lower()

        self.human_score = 0
        self.computer_score = 0
        self.draws = 0

    def display_board(self):
        """Display the current board."""

        print()
        print("     |     |")
        print(
            f"  {self.board[0]}  |  "
            f"{self.board[1]}  |  "
            f"{self.board[2]}"
        )
        print("_____|_____|_____")
        print("     |     |")
        print(
            f"  {self.board[3]}  |  "
            f"{self.board[4]}  |  "
            f"{self.board[5]}"
        )
        print("_____|_____|_____")
        print("     |     |")
        print(
            f"  {self.board[6]}  |  "
            f"{self.board[7]}  |  "
            f"{self.board[8]}"
        )
        print("     |     |")
        print()

    def available_moves(self):
        """Return indexes of empty cells."""

        return [
            index
            for index, cell in enumerate(self.board)
            if cell == " "
        ]

    def check_winner(self):
        """
        Return:

        X    -> human wins
        O    -> computer wins
        D    -> draw
        None -> game continues
        """

        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in winning_combinations:

            if (
                self.board[a] != " "
                and self.board[a]
                == self.board[b]
                == self.board[c]
            ):
                return self.board[a]

        if not self.available_moves():
            return "D"

        return None

    def winning_move(self, player):
        """Find a move that immediately wins for a player."""

        for move in self.available_moves():

            self.board[move] = player

            if self.check_winner() == player:
                self.board[move] = " "
                return move

            self.board[move] = " "

        return None

    def random_move(self):
        """Choose a random available move."""

        moves = self.available_moves()

        if not moves:
            return None

        return random.choice(moves)

    def medium_move(self):
        """
        Medium AI strategy:

        1. Win if possible.
        2. Block the human if necessary.
        3. Take center.
        4. Take a corner.
        5. Otherwise choose a random move.
        """

        # Try to win.
        move = self.winning_move(self.computer)

        if move is not None:
            return move

        # Block human.
        move = self.winning_move(self.human)

        if move is not None:
            return move

        # Take center.
        if self.board[4] == " ":
            return 4

        # Take a corner.
        corners = [
            move
            for move in [0, 2, 6, 8]
            if self.board[move] == " "
        ]

        if corners:
            return random.choice(corners)

        return self.random_move()

    def minimax(self, maximizing):
        """
        Minimax algorithm.

        Computer win -> +1
        Human win     -> -1
        Draw          -> 0
        """

        result = self.check_winner()

        if result == self.computer:
            return 1

        if result == self.human:
            return -1

        if result == "D":
            return 0

        if maximizing:

            best_score = -math.inf

            for move in self.available_moves():

                self.board[move] = self.computer

                score = self.minimax(False)

                self.board[move] = " "

                best_score = max(
                    best_score,
                    score
                )

            return best_score

        best_score = math.inf

        for move in self.available_moves():

            self.board[move] = self.human

            score = self.minimax(True)

            self.board[move] = " "

            best_score = min(
                best_score,
                score
            )

        return best_score

    def hard_move(self):
        """Calculate the best move using Minimax."""

        best_score = -math.inf
        best_move = None

        for move in self.available_moves():

            self.board[move] = self.computer

            score = self.minimax(False)

            self.board[move] = " "

            if score > best_score:

                best_score = score
                best_move = move

        return best_move

    def computer_move(self):
        """Choose a move based on the selected difficulty."""

        if self.difficulty == "easy":
            move = self.random_move()

        elif self.difficulty == "medium":
            move = self.medium_move()

        else:
            move = self.hard_move()

        if move is not None:
            self.board[move] = self.computer

        return move

    def human_move(self):
        """Ask the human player for a valid move."""

        while True:

            try:

                position = int(
                    input(
                        "Choose a position (1-9): "
                    )
                )

                index = position - 1

                if index not in range(9):

                    print(
                        "Please choose a number from 1 to 9."
                    )
                    continue

                if self.board[index] != " ":

                    print(
                        "That position is already occupied."
                    )
                    continue

                self.board[index] = self.human
                return index

            except ValueError:

                print(
                    "Invalid input. Enter a number from 1 to 9."
                )

    def show_result(self, result):
        """Display and record the game result."""

        if result == self.human:

            self.human_score += 1
            print("🎉 You win!")

        elif result == self.computer:

            self.computer_score += 1
            print("🤖 Computer wins!")

        elif result == "D":

            self.draws += 1
            print("🤝 It's a draw!")

    def show_scoreboard(self):
        """Display current scores."""

        print()
        print("========== SCOREBOARD ==========")
        print(f"👤 You      : {self.human_score}")
        print(f"🤖 Computer : {self.computer_score}")
        print(f"🤝 Draws     : {self.draws}")
        print("================================")
        print()

    def reset_board(self):
        """Reset only the current game board."""

        self.board = [" "] * 9

    def choose_difficulty(self):
        """Allow the user to choose the AI difficulty."""

        print()
        print("Select AI difficulty:")
        print("1. Easy   - Random moves")
        print("2. Medium - Basic strategy")
        print("3. Hard   - Minimax AI")

        while True:

            choice = input(
                "Enter difficulty (1-3): "
            ).strip()

            if choice == "1":
                self.difficulty = "easy"
                break

            if choice == "2":
                self.difficulty = "medium"
                break

            if choice == "3":
                self.difficulty = "hard"
                break

            print("Please enter 1, 2, or 3.")

    def play_round(self):
        """Play one complete round."""

        self.reset_board()

        print()
        print(
            f"Difficulty: {self.difficulty.upper()}"
        )

        while True:

            self.display_board()

            self.human_move()

            result = self.check_winner()

            if result:
                self.display_board()
                self.show_result(result)
                return

            print("🤖 Computer is thinking...")

            self.computer_move()

            result = self.check_winner()

            if result:
                self.display_board()
                self.show_result(result)
                return

    def play(self):
        """Run the complete game with replay support."""

        print("=" * 55)
        print("              🎮 TIC-TAC-TOE AI")
        print("=" * 55)
        print("Human: X")
        print("Computer: O")

        print()
        print("Board positions:")
        print()
        print("     |     |")
        print("  1  |  2  |  3")
        print("_____|_____|_____")
        print("     |     |")
        print("  4  |  5  |  6")
        print("_____|_____|_____")
        print("     |     |")
        print("  7  |  8  |  9")
        print("     |     |")
        print()

        self.choose_difficulty()

        while True:

            self.play_round()
            self.show_scoreboard()

            again = input(
                "Play again? (y/n): "
            ).strip().lower()

            if again not in ("y", "yes"):
                break

        print()
        print("Thanks for playing Tic-Tac-Toe AI! 👋")
        self.show_scoreboard()


def main():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()