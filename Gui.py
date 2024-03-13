# import tkinter as tk
# from tkinter import messagebox
# from Player import HumanPlayer
# from Player import SmartComputerPlayer
# from TicTac import TicTacToe

import tkinter as tk
from tkinter import messagebox
from Player import HumanPlayer, SmartComputerPlayer
from TicTac import TicTacToe


class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.game = TicTacToe()
        self.current_player = 'X'

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text='', font=('Arial', 20), width=6, height=3,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.update_board()

        self.window.mainloop()

    def make_move(self, button_index):
        button = self.buttons[button_index]
        if button['text'] == '':
            if self.game.make_move(button_index):
                button.config(text=self.current_player)
                if self.game.winner(self.current_player):
                    messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                    self.reset_game()
                elif not self.game.empty_squares():
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.reset_game()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
                    if isinstance(self.game.current_player, SmartComputerPlayer) and self.current_player == 'O':
                        self.make_computer_move()

    def make_computer_move(self):
        move = self.game.current_player.get_move(self.game)
        self.game.make_move(move)
        self.update_board()
        if self.game.winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
        elif not self.game.empty_squares():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if isinstance(self.game.current_player, SmartComputerPlayer) and self.current_player == 'O':
                self.make_computer_move()

    # def make_computer_move(self):
    #     move = self.game.current_player.get_move(self.game)
    #     self.game.make_move(move)
    #     self.update_board()
    #     if self.game.winner(self.current_player):
    #         messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
    #         self.reset_game()
    #     elif not self.game.empty_squares():
    #         messagebox.showinfo("Game Over", "It's a tie!")
    #         self.reset_game()
    #     else:
    #         self.current_player = 'O' if self.current_player == 'X' else 'X'
    #         if isinstance(self.game.current_player, SmartComputerPlayer) and self.current_player == 'O':
    #             self.make_computer_move()

    def update_board(self):
        for i, button in enumerate(self.buttons):
            button['text'] = self.game.board[i]

    def reset_game(self):
        self.game = TicTacToe()
        self.current_player = 'X'
        self.update_board()


if __name__ == "__main__":
    TicTacToeGUI()
