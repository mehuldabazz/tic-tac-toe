import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.turn = 'X'
        self.root = root
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.mode = 'AI'  # Default mode is AI
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.grid(row=0, column=0, columnspan=3)

        tk.Label(self.menu_frame, text="Choose Mode", font='normal 20 bold').grid(row=0, column=0, columnspan=3)

        tk.Button(self.menu_frame, text="Player vs Player", font='normal 15', command=self.start_pvp).grid(row=1, column=0, columnspan=3)
        tk.Button(self.menu_frame, text="Player vs AI", font='normal 15', command=self.start_pvai).grid(row=2, column=0, columnspan=3)

    def start_pvp(self):
        self.mode = 'PVP'
        self.menu_frame.destroy()
        self.create_board()

    def start_pvai(self):
        self.mode = 'AI'
        self.menu_frame.destroy()
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='-', font='normal 20 bold', height=2, width=5,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] != '-':
            return

        self.board[row][col] = self.turn
        self.buttons[row][col].config(text=self.turn)

        if self.check_winner():
            messagebox.showinfo("TicTacToe", f"{self.turn} wins!")
            self.reset_board()
            return

        self.turn = 'X' if self.turn == 'O' else 'O'

        if self.mode == 'AI' and self.turn == 'O':
            self.ai_move()

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '-':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '-':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return True
        return False

    def ai_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        while self.board[row][col] != '-':
            row = random.randint(0, 2)
            col = random.randint(0, 2)

        self.make_move(row, col)

    def reset_board(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.turn = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='-')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("TicTacToe")
    game = TicTacToe(root)
    root.mainloop()
