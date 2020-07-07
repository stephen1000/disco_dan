""" Message/command parsing for disco dan """

from disco_dan.controller import Controller


class MessageParser(object):
    """ A Message Parser """

    COMMANDS = [
        'play',
        'pause',
        'stop',
    ]

    def __init__(self):
        pass