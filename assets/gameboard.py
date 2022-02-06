#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system

from assets.errors import ColumnFullError, BoardFullError


class ConnectFourBoard:
    """ Board to play ConnectFour """
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2
    X_MAX = 7  # 7 columns
    Y_MAX = 6  # 6 rows

    identifier = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self):
        self.field = None

    def reset_board(self):
        """ Write zeros into every field """
        self.field = [[0 for _ in range(self.Y_MAX)] for _ in range(self.X_MAX)]

    def set_token(self, column: str, token: int):
        """  Check for validity and set the token """
        if not any(0 in _i for _i in self.field):
            raise BoardFullError('The board is completely filled!')
        elif column not in self.identifier:
            raise ValueError() from None
        else:
            column = self.identifier.index(column)
            if column > self.X_MAX:
                raise IndexError() from None
            else:
                rowcount = 0
                for row in self.field[column]:
                    if row == 0:
                        self.field[column][rowcount] = token
                        break
                    rowcount += 1
                    if rowcount == self.Y_MAX:
                        raise ColumnFullError('This column is already full!')

    def print_board(self, p1, p2):
        """ Print the board """
        system('clear')
        print('\nVIER GEWINNT\n')

        sep = '+'
        for _ in range(self.X_MAX):
            sep += '------+'
        print(sep)

        translated_colors = {'RED': '🔴', 'GREEN': '🟢', 'YELLOW': '🟡'}

        for row in reversed(range(self.Y_MAX)):
            for column in range(self.X_MAX):
                if self.field[column][row] == 0:
                    print('|    ', end='  ')
                elif self.field[column][row] == 1:
                    print(f'|  {translated_colors[p1.color]}', end='  ')
                elif self.field[column][row] == 2:
                    print(f'|  {translated_colors[p2.color]}', end='  ')
            print('|\n' + sep)

        # Print identifiers
        for _i in range(self.X_MAX):
            print('    ' + self.identifier[_i], end='  ')

        print('\n')

    def is_board_full(self):
        """ Check, if the board is full """
        if not any(0 in _i for _i in self.field):
            return True
        else:
            return False

    def is_winning(self, winning_positions_list):
        """ Check, who is winning """
        return self.field[winning_positions_list[0][0]][winning_positions_list[0][1]]

    def get_winning_positions(self, board):
        """ Check, if there is a win-situation and return the position """
        # Check horizontally
        for column in range(self.X_MAX - 3):
            for row in range(self.Y_MAX):
                if board[column][row] == board[column + 1][row] == board[column + 2][row] == board[column + 3][row] != 0:
                    return [[column, row], [column + 1, row], [column + 2, row], [column + 3, row]]

        # Check vertically
        for row in range(self.Y_MAX - 3):
            for column in range(self.X_MAX):
                if board[column][row] == board[column][row + 1] == board[column][row + 2] == board[column][row + 3] != 0:
                    return [[column, row], [column, row + 1], [column, row + 2], [column, row + 3]]

        # Skip diagonal checks if column count is less than 4
        if self.X_MAX < 4:
            return False
            
        # Check up-diagonally
        for column in range(self.X_MAX - 3):
            for row in range(self.Y_MAX - 3):
                if board[column][row] == board[column + 1][row + 1] == board[column + 2][row + 2] == board[column + 3][row + 3] != 0:
                    return [[column, row], [column + 1, row + 1], [column + 2, row + 2], [column + 3, row + 3]]

        # Check down-diagonally
        for column in range(self.X_MAX - 3):
            for row in range(3, self.Y_MAX):
                if board[column][row] == board[column + 1][row - 1] == board[column + 2][row - 2] == board[column + 3][row - 3] != 0:
                    return [[column, row], [column + 1, row - 1], [column + 2, row - 2], [column + 3, row - 3]]

        return False
