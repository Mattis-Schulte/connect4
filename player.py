#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name, color):
        """ Create a player with name and color from color class """
        self.name = name
        self.color = color
        self.winnings = 0
        self.loses = 0
        self.draws = 0

    def __str__(self):
        return self.name

    def inc_winnings(self):
        self.winnings += 1

    def inc_losings(self):
        self.loses += 1

    def inc_draws(self):
        self.draws += 1

    def set_win(self, win):
        self.winnings = win

    def set_lose(self, lose):
        self.loses = lose
