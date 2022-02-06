#!/usr/bin/python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from random import choice

from assets.errors import ColumnFullError, AIModeError


class ConnectFourGame:
    """ The actual Game. Gives each player its turn or gets into automatic mode """
    AI = 1
    TWO_PLAYERS = 2

    identifier = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, board, mode):
        self.board = board
        self.game = mode
        self.active_player = 1
        # Init the board
        board.reset_board()

    def set_player1(self, column):
        self.board.set_token(column.upper(), 1)
        self.active_player = 2

    def set_player2(self, column):
        self.board.set_token(column.upper(), 2)
        self.active_player = 1

        if self.game == self.AI:
            raise AIModeError('Game is in automatic mode!')

    def set_ai(self):
        """ The AI ​​algorithm, it wants to either win or avoid losing if neither is possible it will put the token in a random column """
        for win in reversed(range(0,2)):
            for column in range(self.board.X_MAX):
                rowcount = 0
                for row in self.board.field[column]:
                    if row == 0:
                        test_board = deepcopy(self.board.field)
                        # Prioritize winning over avoiding losing
                        if win:
                            test_board[column][rowcount] = 2
                        else:
                            test_board[column][rowcount] = 1

                        if self.board.get_winning_positions(test_board):
                            self.board.set_token(self.identifier[column], 2)
                            self.active_player = 1
                            return
                        break
                    rowcount += 1
        
        # Choose random column
        self.board.set_token(choice(self.identifier[0:self.board.X_MAX]), 2)
        self.active_player = 1

    def play(self, p1, p2):
        _color_helper = {'RED': 'Rot', 'GREEN': 'Grün', 'YELLOW': 'Gelb'}
        if self.active_player == 1:
            # Player one's turn
            self.board.print_board(p1, p2)
            while True:
                try:
                    self.set_player1(input(f'{p1.name} ({_color_helper[p1.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game != self.AI:
            # Player two's turn
            self.board.print_board(p1, p2)
            while True:
                try:
                    self.set_player2(input(f'{p2.name} ({_color_helper[p2.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game == self.AI:
            # AI's turn
            self.board.print_board(p1, p2)
            while True:
                try:
                    self.set_ai()
                    break
                except ColumnFullError:
                    pass