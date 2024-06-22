import random

class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.turn = 'X'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def make_move(self, row, col):
        if self.board[row][col] != '-':
            return False

        self.board[row][col] = self.turn

        if self.check_winner():
            return True

        self.turn = 'X' if self.turn == 'O' else 'O'

        return True

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
        # TODO: Implement a better AI algorithm
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        while not self.make_move(row, col):
            row = random.randint(0, 2)
            col = random.randint(0, 2)

    def play_game(self):
        while not self.check_winner():
            self.print_board()

            if self.turn == 'X':
                row, col = input('Enter your move (row, col): ').split()
                self.make_move(int(row), int(col))
            else:
                self.ai_move()

        self.print_board()

        winner = 'X' if self.turn == 'O' else 'O'
        print(f'{winner} wins!')

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()