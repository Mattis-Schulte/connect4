#!/usr/bin/python3
# -*- coding: utf-8 -*-

class ConnectFourError(Exception):
    """ Indicates that it is a ConnectFourError """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        