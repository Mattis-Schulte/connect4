#!/usr/bin/python3
# -*- coding: utf-8 -*-

from exceptions.ConnectFourError import ConnectFourError


class BoardFullError(ConnectFourError):
    """ Indicates that the board is completely filled with tokens """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
