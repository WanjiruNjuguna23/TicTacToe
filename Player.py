import random
import math


class Player:
    """
    Base class for a player in the Tic Tac Toe game.
    """

    def __init__(self, symbol):
        """
        Initialize the player with a symbol ('X' or 'O').

        Parameters:
        - symbol: The symbol representing the player ('X' or 'O').
        """
        self.symbol = symbol

    def get_move(self, game):
        """
        Get the player's move.

        Parameters:
        - game: The current game state.

        Returns:
        - The index of the square to move to.
        """
        pass


class HumanPlayer(Player):
    """
    Class representing a human player in the Tic Tac Toe game.
    """

    def __init__(self, symbol):
        """
        Initialize the human player with a symbol ('X' or 'O').

        Parameters:
        - symbol: The symbol representing the player ('X' or 'O').
        """
        super().__init__(symbol)

    def get_move(self, game):
        """
        Get the human player's move.

        Parameters:
        - game: The current game state.

        Returns:
        - The index of the square to move to.
        """
        valid_square = False
        move = None
        while not valid_square:
            square = input(self.symbol + "'s turn. Enter your move (0-8): ")
            try:
                move = int(square)
                if move not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move. Please try again.')
        return move


class RandomComputerPlayer(Player):
    """
    Class representing a random computer player in the Tic Tac Toe game.
    """

    def __init__(self, symbol):
        """
        Initialize the random computer player with a symbol ('X' or 'O').

        Parameters:
        - symbol: The symbol representing the player ('X' or 'O').
        """
        super().__init__(symbol)

    def get_move(self, game):
        """
        Get the random computer player's move.

        Parameters:
        - game: The current game state.

        Returns:
        - The index of the square to move to.
        """
        move = random.choice(game.available_moves())
        return move


class SmartComputerPlayer(Player):
    """
    Class representing a smart computer player in the Tic Tac Toe game.
    """

    def __init__(self, symbol):
        """
        Initialize the smart computer player with a symbol ('X' or 'O').

        Parameters:
        - symbol: The symbol representing the player ('X' or 'O').
        """
        super().__init__(symbol)

    def get_move(self, game):
        """
        Get the smart computer player's move.

        Parameters:
        - game: The current game state.

        Returns:
        - The index of the square to move to.
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.symbol)['position']
        return square

    def minimax(self, state, player):
        """
        Implement the minimax algorithm to determine the best move.

        Parameters:
        - state: The current game state.
        - player: The player to calculate the best move for.

        Returns:
        - A dictionary containing the best move position and score.
        """
        max_player = self.symbol
        other_player = 'O' if player == 'X' else 'X'

        if state.winner(self.symbol):
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if player == max_player else -1 * (
                    state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


