#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Connect 4
# Mattis Schulte | Sajan Sivapatham    2022-02-11
# Connect four to win, you can play either against a friend or an primitive AI

# https://github.com/Mattis-Schulte/connect4

from os import system
from random import choice


class ConnectFourBoard:
    """ Board to play ConnectFour """
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2
    X_MAX = 5  # 5 columns
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

    def print_board(self):
        """ Print the board """
        system('clear')
        print('\nVIER GEWINNT\n')

        sep = '+'
        for _ in range(0, self.X_MAX):
            sep += '------+'
        print(sep)

        translated_colors = {'RED': '🔴', 'GREEN': '🟢', 'YELLOW': '🟡'}

        for row in reversed(range(0, self.Y_MAX)):
            for column in range(0, self.X_MAX):
                if self.field[column][row] == 0:
                    print('|    ', end='  ')
                elif self.field[column][row] == 1:
                    print(f'|  {translated_colors[p1.color]}', end='  ')
                elif self.field[column][row] == 2:
                    print(f'|  {translated_colors[p2.color]}', end='  ')
            print('|\n' + sep)

        # Print identifiers
        for _i in range(0, self.X_MAX):
            print('    ' + self.identifier[_i], end='  ')

        print('\n')

    def is_board_full(self):
        """ Check, if the board is full"""
        if not any(0 in _i for _i in self.field):
            return True
        else:
            return False

    def is_winnig(self, winning_positions_list):
        """ Check, who is winning"""
        return self.field[winning_positions_list[0][0]][winning_positions_list[0][1]]

    def get_winning_positions(self):
        """ Check, if there is a win-situation and return the position"""
        # Check horizontally
        for column in range(0, self.X_MAX):
            for row in range(0, self.Y_MAX):
                try:
                    if self.field[row][column] == self.field[row][column + 1] == self.field[row][column + 2] == self.field[row][column + 3] != 0:
                        return [[row, column], [row, column + 1], [row, column + 2], [row, column + 3]]
                except IndexError:
                    break

        # Check vertically
        for row in range(0, self.Y_MAX):
            for column in range(0, self.X_MAX):
                try:
                    if self.field[row][column] == self.field[row + 1][column] == self.field[row + 2][column] == self.field[row + 3][column] != 0:
                        return [[row, column], [row + 1, column], [row + 2, column], [row + 3, column]]
                except IndexError:
                    break

        # Check up-diagonally
        for column in range(0, self.X_MAX):
            for row in range(0, self.Y_MAX):
                try:
                    if self.field[row][column] == self.field[row + 1][column + 1] == self.field[row + 2][column + 2] == self.field[row + 3][column + 3] != 0:
                        return [[row, column], [row + 1, column + 1], [row + 2, column + 2], [row + 3, column + 3]]
                except IndexError:
                    break

        # Check down-diagonally
        for column in range(0, self.X_MAX):
            for row in range(0, self.Y_MAX):
                try:
                    if self.field[row][column] == self.field[row + 1][column - 1] == self.field[row + 2][column - 2] == self.field[row + 3][column - 3] != 0:
                        return [[row, column], [row + 1, column - 1], [row + 2, column - 2], [row + 3, column - 3]]
                except IndexError:
                    break

        return False


class ConnectFourError(Exception):
    """Indicates that it is a ConnectFourError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class ColumnFullError(ConnectFourError):
    """Indicates that the column is completely filled with tokens."""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class BoardFullError(ConnectFourError):
    """Indicates that the board is completely filled with tokens."""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class Player:
    def __init__(self, name, the_color):
        self.name = name
        self.color = the_color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, the_color):
        if the_color in valid_colors.colors:
            self._color = the_color
        else:
            raise WrongColError('Invalid color!')

    @color.getter
    def color(self):
        return self._color


class Color:
    def __init__(self):
        # Valid colors
        self.colors = ['RED', 'GREEN', 'YELLOW']


class ConnectFourGame:
    """The actual Game. Gives each player its turn or gets into automatic mode."""

    AI = 1
    TWO_PLAYERS = 2

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

        if self.game == ConnectFourGame.AI:
            raise AIModeError('Game is in automatic mode!')

    def set_ai(self):
        self.board.set_token(choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'][0:self.board.X_MAX]), 2)
        self.active_player = 1

    def play(self):
        _color_helper = {'RED': 'Rot', 'GREEN': 'Grün', 'YELLOW': 'Gelb'}
        if self.active_player == 1:
            # Player one's turn
            self.board.print_board()
            while True:
                try:
                    self.set_player1(input(f'{p1.name} ({_color_helper[p1.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game != ConnectFourGame.AI:
            # Player two's turn
            self.board.print_board()
            while True:
                try:
                    self.set_player2(input(f'{p2.name} ({_color_helper[p2.color]}) ist am Zug >> '))
                    break
                except(ValueError, IndexError):
                    print('Fehlerhafte Auswahl!')
                except ColumnFullError:
                    print('Diese Spalte ist schon voll!')
        elif self.active_player == 2 and self.game == ConnectFourGame.AI:
            # AI's turn
            self.board.print_board()
            while True:
                try:
                    self.set_ai()
                    break
                except ColumnFullError:
                    pass


class AIModeError(ConnectFourError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class WrongColError(ConnectFourError):
    """Indicates that the user has choosen a invalid color."""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


if __name__ == "__main__":
    print('''
██╗   ██╗██╗███████╗██████╗    ██████╗ ███████╗ ██╗       ██╗██╗███╗  ██╗███╗  ██╗████████╗
██║   ██║██║██╔════╝██╔══██╗  ██╔════╝ ██╔════╝ ██║  ██╗  ██║██║████╗ ██║████╗ ██║╚══██╔══╝
╚██╗ ██╔╝██║█████╗  ██████╔╝  ██║  ██╗ █████╗   ╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║   ██║   
 ╚████╔╝ ██║██╔══╝  ██╔══██╗  ██║  ╚██╗██╔══╝    ████╔═████║ ██║██║╚████║██║╚████║   ██║   
  ╚██╔╝  ██║███████╗██║  ██║  ╚██████╔╝███████╗  ╚██╔╝ ╚██╔╝ ██║██║ ╚███║██║ ╚███║   ██║   
   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝   ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝   ╚═╝   
        ''')
    print('Wählen Sie einen Spielmodus:')
    print('(1) Einzelspieler (KI-Modus)')
    print('(2) Zweispieler')

    usr_input = input('>> ')

    # Check if user input is valid
    while usr_input.upper() not in ['1', '2']:
        print('Fehlerhafte Auswahl!')
        usr_input = input('>> ')
    else:
        valid_colors = Color()
        # AI mode selected
        if usr_input.upper() == '1':
            system('clear')
            usr_name = 'Spieler 1'
            print('Bitte geben Sie ihren Benutzernamen ein!')
            usr_input = input('>> ')
            if usr_input != '':
                usr_name = usr_input
            system('clear')

            # Select color
            color_helper = (' '.join(valid_colors.colors).replace('RED', 'Rot').replace('GREEN', 'Grün').replace('YELLOW', 'Gelb')).split()
            print(f'Bitte wählen Sie ihre Farbe ({" oder ".join([", ".join(color_helper[:-1]), color_helper[-1]])})!')
            usr_input = input('>> ')
            while True:
                try:
                    usr_input = usr_input.upper().replace('ROT', 'RED').replace('GRÜN', 'GREEN').replace('GELB', 'YELLOW')
                    p1 = Player(usr_name, usr_input)
                    valid_colors.colors.remove(usr_input)
                    p2 = Player('Primitive KI', choice(valid_colors.colors))
                    Board = ConnectFourBoard()
                    Game = ConnectFourGame(Board, 1)
                    break
                except WrongColError:
                    print('Fehlerhafte Auswahl!')
                    usr_input = input('>> ')
        # Two player mode selected
        elif usr_input.upper() == '2':
            # Loop twice to configure both players
            for i in range(1, 3):
                system('clear')
                usr_name = 'Spieler ' + str(i)
                print(f'Spieler {i}:')
                print('Bitte geben Sie ihren Benutzernamen ein!')
                usr_input = input('>> ')
                if usr_input != '':
                    usr_name = usr_input
                system('clear')

                # Select color
                print(f'Spieler {i}:')
                color_helper = (' '.join(valid_colors.colors).replace('RED', 'Rot').replace('GREEN', 'Grün').replace('YELLOW', 'Gelb')).split()
                print(f'Bitte wählen Sie ihre Farbe ({" oder ".join([", ".join(color_helper[:-1]), color_helper[-1]])})!')
                usr_input = input('>> ')
                while True:
                    try:
                        usr_input = usr_input.upper().replace('ROT', 'RED').replace('GRÜN', 'GREEN').replace('GELB', 'YELLOW')
                        exec('p' + str(i) + ' = ' + 'Player("' + usr_name + '", "' + usr_input + '")')
                        valid_colors.colors.remove(usr_input)
                        Board = ConnectFourBoard()
                        Game = ConnectFourGame(Board, 2)
                        break
                    except WrongColError:
                        print('Fehlerhafte Auswahl!')
                        usr_input = input('>> ')

    # Running the actual game
    while not (Board.is_board_full()) and not (Board.get_winning_positions()):
        Game.play()
    else:
        Board.print_board()
        if Board.get_winning_positions():
            exec('winner_name, winner_color = p' + str(Board.is_winnig(Board.get_winning_positions())) + '.name, p' + str(Board.is_winnig(Board.get_winning_positions())) + '.color')
            winner_color = winner_color.replace('RED', 'Rot').replace('GREEN', 'Grün').replace('YELLOW', 'Gelb')
            print(f'{winner_name} ({winner_color}) hat mit folgenden Steinen gewonnen: ', end='')
            [print(f'({"|".join(str(x) for x in item)})', end=' ') for item in Board.get_winning_positions()]
            print()
        elif Board.is_board_full():
            print('Das Spiel ist unentschieden!')
