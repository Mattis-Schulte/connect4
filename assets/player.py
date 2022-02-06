#!/usr/bin/python3
# -*- coding: utf-8 -*-

from assets.errors import WrongColError


class Player:
    def __init__(self, name, valid_colors, the_color):
        self.name = name
        self.valid_colors = valid_colors.colors
        self.color = the_color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, the_color):
        if the_color in self.valid_colors:
            self._color = the_color
        else:
            raise WrongColError('Invalid color!')

    @color.getter
    def color(self):
        return self._color
