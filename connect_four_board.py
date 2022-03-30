#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system, name

from exceptions.ColumnFullError import ColumnFullError
from exceptions.BoardFullError import BoardFullError

if name == 'nt':
    clear_cmd = 'system("cls")'
else:
    clear_cmd = 'system("clear")'


class ConnectFourBoard:
    """ Board to play ConnectFour. Pos(x,y) | pos(0,0) lower left-hand corner | xmax = 7 ymax = 6 """
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2
    X_MAX = 7  # 7 columns
    Y_MAX = 6  # 6 rows

    identifier = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    def __init__(self):
        self.reset_board()

    def reset_board(self):
        """ Write zeros into every field """
        self.field = [[0 for _ in range(self.Y_MAX)] for _ in range(self.X_MAX)]

    def print_board(self, p1_color='RED', p2_color='YELLOW'):
        """ Show the board in a console grid """
        exec(clear_cmd)
        print('\nVIER GEWINNT\n')

        sep = '+'
        for _ in range(self.X_MAX):
            sep += '------+'
        print(sep)

        translated_colors = {'RED': '🔴', 'GREEN': '🟢', 'YELLOW': '🟡', 'BLUE': '🔵'}

        for row in reversed(range(self.Y_MAX)):
            for column in range(self.X_MAX):
                if self.field[column][row] == self.EMPTY:
                    print('|    ', end='  ')
                elif self.field[column][row] == self.PLAYER1:
                    print(f'|  {translated_colors[p1_color]}', end='  ')
                elif self.field[column][row] == self.PLAYER2:
                    print(f'|  {translated_colors[p2_color]}', end='  ')
            print('|\n' + sep)

        # Print identifiers
        for i in range(self.X_MAX):
            print('    ' + self.identifier[i], end='  ')

        print('\n')
    
    def set_token(self, column: int, token: int):
        """ Check for validity and set the token """
        if self.is_board_full():
            raise BoardFullError('The board is completely filled!')
        elif column > self.X_MAX:
            raise IndexError() from None
        elif self.is_col_full(column):
            raise ColumnFullError('This column is already full!')
        else:
            self.field[column][self.field[column].index(0)] = token

    def get_token(self, x_pos, y_pos) -> int:
        """ Get token at specified position """
        return self.field[x_pos][y_pos]
        
    def is_board_full(self) -> bool:
        """ Check, if the board is full """
        if not any(self.EMPTY in i for i in self.field):
            return True
        else:
            return False

    def is_col_full(self, x_pos) -> bool:
        """ Tell if column is fully occupied """
        if self.EMPTY in self.field[x_pos]:
            return False
        else:
            return True
    
    def is_winning(self) -> bool:
        """ Tell if winning was achieved by a player """
        if self.get_winning_positions(self.field):
            return True
        else:
            return False

    def get_winning_positions(self, board=None) -> tuple:
        if board is None:
            board = self.field
        
        """ Check, if there is a win-situation and return the position """
        # Check horizontally
        for column in range(self.X_MAX - 3):
            for row in range(self.Y_MAX):
                if board[column][row] == board[column + 1][row] == board[column + 2][row] == board[column + 3][row] != self.EMPTY:
                    return ((column, row), (column + 1, row), (column + 2, row), (column + 3, row))

        # Check vertically
        for row in range(self.Y_MAX - 3):
            for column in range(self.X_MAX):
                if board[column][row] == board[column][row + 1] == board[column][row + 2] == board[column][row + 3] != self.EMPTY:
                    return ((column, row), (column, row + 1), (column, row + 2), (column, row + 3))

        # Skip diagonal checks if column count is less than 4
        if self.X_MAX < 4:
            return False
            
        # Check up-diagonally
        for column in range(self.X_MAX - 3):
            for row in range(self.Y_MAX - 3):
                if board[column][row] == board[column + 1][row + 1] == board[column + 2][row + 2] == board[column + 3][row + 3] != self.EMPTY:
                    return ((column, row), (column + 1, row + 1), (column + 2, row + 2), (column + 3, row + 3))

        # Check down-diagonally
        for column in range(self.X_MAX - 3):
            for row in range(3, self.Y_MAX):
                if board[column][row] == board[column + 1][row - 1] == board[column + 2][row - 2] == board[column + 3][row - 3] != self.EMPTY:
                    return ((column, row), (column + 1, row - 1), (column + 2, row - 2), (column + 3, row - 3))

        return False
