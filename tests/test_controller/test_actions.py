""" Tests for the bot controller actions """

import pytest
from disco_dan.controller import Controller

@pytest.mark.asyncio
def test_get_bot_command_text():
    """ Assert command text is retrieved properly """


@pytest.mark.asyncio
def test_find_guild_channel():
    """ Assert a guild channel can be found """


@pytest.mark.asyncio
def test_get_voice_connection():
    """ Assert a voice connection can be retrieved """


@pytest.mark.asyncio
def test_play():
    """ Assert the controller can play a video """


@pytest.mark.asyncio
def test_pause():
    """ Assert the controller can pause a video """


@pytest.mark.asyncio
def test_resume():
    """ Assert the controller can resume a video """


@pytest.mark.asyncio
def test_stop():
    """ Assert the controller can stop a video """


@pytest.mark.asyncio
def test_report_error():
    """ Assert the controller reports errors correctly """
