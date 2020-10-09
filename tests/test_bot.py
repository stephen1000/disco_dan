""" Tests for the bot heart """


import pytest


def test_bot_loads():
    """ Assert the bot module loads """
    from disco_dan import bot

    assert bot.client
    assert bot.controller
