#!/usr/bin/python3
# -*- coding: utf-8 -*-

from exceptions.ConnectFourError import ConnectFourError


class WrongColError(ConnectFourError):
    """ Indicates that the user has chosen an invalid color """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
