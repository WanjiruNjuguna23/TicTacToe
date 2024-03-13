class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def winner(self, letter):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == letter:
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']



# class TicTacToe():
#     def __init__(self):
#         """
#         Initialize the Tic Tac Toe game.
#
#         The game board is represented as a list of 9 elements, where each element
#         corresponds to a square on the board. Each element is initially set to ' '.
#         The current_winner attribute is used to keep track of the winner of the game.
#         """
#         self.board = self.make_board()
#         self.current_winner = None
#
#     @staticmethod
#     def make_board():
#         """
#         Create a new game board.
#
#         Returns:
#         - A list representing the game board, with each element initialized to ' '.
#         """
#         return [' ' for _ in range(9)]
#
#     def print_board(self):
#         """
#         Print the current game board.
#
#         The board is printed as a 3x3 grid, with each element represented by its index.
#         """
#         for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')
#
#     @staticmethod
#     def print_board_nums():
#         """
#         Print the board with square numbers for reference.
#
#         This is used to help the player choose a square to make their move.
#         """
#         number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
#         for row in number_board:
#             print('| ' + ' | '.join(row) + ' |')
#
#     def make_move(self, button_index):
#         button = self.buttons[button_index]
#         if button['state'] == 'normal':  # Check if the button is enabled
#             if self.game.make_move(button_index, self.current_player):
#                 self.update_button(button_index)
#                 button.config(state='disabled')  # Disable the button after it's clicked
#                 if self.game.current_winner:
#                     self.show_game_over_message()
#                     self.reset_game()
#                 elif not self.game.empty_squares():
#                     self.show_game_over_message("It's a tie!")
#                     self.reset_game()
#                 else:
#                     self.current_player = 'O' if self.current_player == 'X' else 'X'
#                     if self.current_player == 'O':
#                         self.make_computer_move()
#
#     # def make_move(self, square, letter):
#     #     """
#     #     Make a move on the board.
#     #
#     #     Parameters:
#     #     - square: The index of the square to make the move in.
#     #     - letter: The player's letter ('X' or 'O') to place in the square.
#     #
#     #     Returns:
#     #     - True if the move is successful, False otherwise.
#     #     """
#     #     if self.board[square] == ' ':
#     #         self.board[square] = letter
#     #         if self.winner(letter):
#     #             self.current_winner = letter
#     #         return True
#     #     return False
#
#     def winner(self, letter):
#         """
#         Check if the specified player has won the game.
#
#         Parameters:
#         - letter: The player's letter ('X' or 'O') to check for.
#
#         Returns:
#         - True if the player has won, False otherwise.
#         """
#         # Check the rows, columns, and diagonals for a winner
#         for i in range(3):
#             if self.board[i] == self.board[i + 3] == self.board[i + 6] == letter:
#                 return True
#             if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] == letter:
#                 return True
#         if self.board[0] == self.board[4] == self.board[8] == letter:
#             return True
#         if self.board[2] == self.board[4] == self.board[6] == letter:
#             return True
#         return False
#
#     def empty_squares(self):
#         """
#         Check if there are any empty squares left on the board.
#
#         Returns:
#         - True if there are empty squares, False otherwise.
#         """
#         return ' ' in self.board
#
#     def num_empty_squares(self):
#         """
#         Count the number of empty squares on the board.
#
#         Returns:
#         - The number of empty squares.
#         """
#         return self.board.count(' ')
#
#     def available_moves(self):
#         """
#         Get a list of available moves (empty squares) on the board.
#
#         Returns:
#         - A list of indices representing the available moves.
#         """
#         return [i for i, x in enumerate(self.board) if x == " "]
