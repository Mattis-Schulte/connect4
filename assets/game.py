#!/usr/bin/python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from random import choice, sample

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
        """ The AI algorithm, it wants to either win or avoid losing if neither is possible it will put the token in a random column """
        valid_columns = [x for x in range(0, len(self.board.field)) if 0 in self.board.field[x]]

        # Check if the game can be won or a loss avoided
        for win in reversed(range(0, 2)):
            for column in sample(valid_columns, len(valid_columns)):
                test_board = deepcopy(self.board.field)
                # Prioritize winning over avoiding losing
                if win:
                    test_board[column][self.board.field[column].index(0)] = 2
                else:
                    test_board[column][self.board.field[column].index(0)] = 1

                if self.board.get_winning_positions(test_board):
                    self.board.set_token(self.identifier[column], 2)
                    self.active_player = 1
                    return
        
        # Check to prevent a random token from being placed in the opponent's favour
        for random_column in sample(valid_columns, len(valid_columns)):
            test_board = deepcopy(self.board.field)
            test_board[random_column][self.board.field[random_column].index(0)] = 2
            if 0 in test_board[random_column]:
                test_board[random_column][self.board.field[random_column].index(0) + 1] = 1
                if not self.board.get_winning_positions(test_board):
                    self.board.set_token(self.identifier[random_column], 2)
                    self.active_player = 1
                    return
            else:
                self.board.set_token(self.identifier[random_column], 2)
                self.active_player = 1
                return

        # Choose random column
        self.board.set_token(self.identifier[choice(valid_columns)], 2)
        self.active_player = 1

    def play(self, p1, p2):
        color_helper = {'RED': 'Rot', 'GREEN': 'Grün', 'YELLOW': 'Gelb', 'BLUE': 'Blau'}
        self.board.print_board(p1, p2)
        if self.active_player == 1:
            # Player one's turn
            while True:
                try:
                    self.set_player1(input(f'{p1.name} ({color_helper[p1.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game != self.AI:
            # Player two's turn
            while True:
                try:
                    self.set_player2(input(f'{p2.name} ({color_helper[p2.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game == self.AI:
            # AI's turn
            self.set_ai()
