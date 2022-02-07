#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Connect 4
# Mattis Schulte | Sajan Sivapatham    2022-02-11
# Connect four to win, you can play either against a friend or a primitive AI

# https://github.com/Mattis-Schulte/connect4

from os import system, name
from random import choice

from assets.gameboard import ConnectFourBoard
from assets.color import Color
from assets.errors import WrongColError
from assets.game import ConnectFourGame
from assets.player import Player

if name == 'nt':
    clear_cmd = 'system("cls")'
else:
    clear_cmd = 'system("clear")'

if __name__ == "__main__":
    exec(clear_cmd)
    print('''
              ██╗   ██╗██╗███████╗██████╗   
              ██║   ██║██║██╔════╝██╔══██╗  
              ╚██╗ ██╔╝██║█████╗  ██████╔╝  
               ╚████╔╝ ██║██╔══╝  ██╔══██╗  
                ╚██╔╝  ██║███████╗██║  ██║  
                 ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝  

 ██████╗ ███████╗ ██╗       ██╗██╗███╗  ██╗███╗  ██╗████████╗
██╔════╝ ██╔════╝ ██║  ██╗  ██║██║████╗ ██║████╗ ██║╚══██╔══╝
██║  ██╗ █████╗   ╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║   ██║   
██║  ╚██╗██╔══╝    ████╔═████║ ██║██║╚████║██║╚████║   ██║   
╚██████╔╝███████╗  ╚██╔╝ ╚██╔╝ ██║██║ ╚███║██║ ╚███║   ██║   
 ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝   ╚═╝   
    ''')
    print('Wählen Sie einen Spielmodus:')
    print('(1) Einzelspieler (KI-Modus)')
    print('(2) Zweispieler')

    color_helper = {'RED': 'Rot', 'GREEN': 'Grün', 'YELLOW': 'Gelb', 'BLUE': 'Blau'}
    usr_input = input('>> ')

    # Check if user input is valid
    while usr_input.upper() not in ['1', '2']:
        print('Fehlerhafte Auswahl!')
        usr_input = input('>> ')
    else:
        valid_colors = Color()
        Board = ConnectFourBoard()
        # AI mode selected
        if usr_input.upper() == '1':
            exec(clear_cmd)
            usr_name = 'Spieler 1'
            print('Bitte geben Sie ihren Benutzernamen ein!')
            usr_input = input('>> ')
            if usr_input != '':
                usr_name = usr_input
            exec(clear_cmd)

            # Select color
            print(f'Bitte wählen Sie ihre Farbe ({" oder ".join([", ".join(color_helper[key] for key in valid_colors.colors[:-1]), color_helper[valid_colors.colors[-1]]])})!')
            usr_input = input('>> ')
            while True:
                try:
                    if usr_input.upper() in dict((v.upper(), k) for k, v in color_helper.items()):
                        usr_input = dict((v.upper(), k) for k, v in color_helper.items())[usr_input.upper()]

                    p1 = Player(usr_name, valid_colors, usr_input)
                    valid_colors.colors.remove(usr_input)
                    p2 = Player('Primitive KI', valid_colors, choice(valid_colors.colors))
                    Game = ConnectFourGame(Board, 1)
                    break
                except WrongColError:
                    print('Fehlerhafte Auswahl!')
                    usr_input = input('>> ')
        # Two player mode selected
        elif usr_input.upper() == '2':
            # Loop twice to configure both players
            for i in range(1, 3):
                exec(clear_cmd)
                usr_name = 'Spieler ' + str(i)
                print(f'Spieler {i}:')
                print('Bitte geben Sie ihren Benutzernamen ein!')
                usr_input = input('>> ')
                if usr_input != '':
                    usr_name = usr_input
                exec(clear_cmd)

                # Select color
                print(f'Spieler {i}:')
                print(f'Bitte wählen Sie ihre Farbe ({" oder ".join([", ".join(color_helper[key] for key in valid_colors.colors[:-1]), color_helper[valid_colors.colors[-1]]])})!')
                usr_input = input('>> ')
                while True:
                    try:
                        if usr_input.upper() in dict((v.upper(), k) for k, v in color_helper.items()):
                            usr_input = dict((v.upper(), k) for k, v in color_helper.items())[usr_input.upper()]

                        exec('p' + str(i) + ' = ' + 'Player("' + usr_name + '", valid_colors, "' + usr_input + '")')
                        valid_colors.colors.remove(usr_input)
                        Game = ConnectFourGame(Board, 2)
                        break
                    except WrongColError:
                        print('Fehlerhafte Auswahl!')
                        usr_input = input('>> ')

    # Running the actual game
    while not (Board.is_board_full()) and not (Board.get_winning_positions(Board.field)):
        Game.play(p1, p2)
    else:
        Board.print_board(p1, p2)
        if Board.get_winning_positions(Board.field):
            exec('winner_name = p' + str(Board.is_winning(Board.get_winning_positions(Board.field))) + '.name')
            exec('winner_color = p' + str(Board.is_winning(Board.get_winning_positions(Board.field))) + '.color')
            winner_color = color_helper[winner_color]
            print(f'{winner_name} ({winner_color}) hat mit folgenden Steinen gewonnen: ', end='')
            [print(f'({"|".join(str(x) for x in item)})', end=' ') for item in Board.get_winning_positions(Board.field)]
            print()
        elif Board.is_board_full():
            print('Das Spiel ist unentschieden!')
