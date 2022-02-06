#!/usr/bin/python3
# -*- coding: utf-8 -*-

class ConnectFourError(Exception):
    """ Indicates that it is a ConnectFourError """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class ColumnFullError(ConnectFourError):
    """ Indicates that the column is completely filled with tokens """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class BoardFullError(ConnectFourError):
    """ Indicates that the board is completely filled with tokens """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class AIModeError(ConnectFourError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class WrongColError(ConnectFourError):
    """ Indicates that the user has chosen an invalid color """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
