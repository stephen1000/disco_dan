""" Tests for the bot controller actions """

import pytest
from discord.message import Message

from disco_dan.controller import Controller
from disco_dan import settings


class DummyChannel(object):
    """ A pretend channel """

    def __init__(self, name):
        self.name = name


class DummyGuild(object):
    """ A pretend guild """

    def __init__(self, voice_channels):
        self.voice_channels = voice_channels


@pytest.fixture
async def controller():
    from disco_dan.bot import controller

    return controller


@pytest.fixture
async def guild():
    return DummyGuild(voice_channels=[DummyChannel("foo"), DummyChannel("bar")])


@pytest.mark.asyncio
async def test_get_bot_command_text():
    """ Assert command text is retrieved properly """
    controller = Controller(object())
    message = f"{controller.START_WORD} play foo"
    command_text = await controller.get_bot_command_text(message)
    assert command_text == "play foo"

    message = "some message without the command word"
    command_text = await controller.get_bot_command_text(message)
    assert command_text is None


@pytest.mark.asyncio
async def test_find_guild_channel(controller):
    """ Assert a guild channel can be found """
    channel_names = ["foo", "Bar", "BAZ"]
    voice_channels = [DummyChannel(name) for name in channel_names]
    guild = DummyGuild(voice_channels)
    for name in channel_names:
        channel = await controller.find_guild_channel(guild, channel_name=name)
        assert channel.name == name


@pytest.mark.asyncio
async def test_get_voice_connection(controller, guild):
    """ Assert a voice connection can be retrieved """
    # voice_connection = await controller.test_get_voice_connection(guild)
    # assert voice_connection


@pytest.mark.asyncio
async def test_play(controller, guild):
    """ Assert the controller can play a video """
    # await controller.play(guild, 'nyan cat')


@pytest.mark.asyncio
async def test_pause(controller, guild):
    """ Assert the controller can pause a video """
    # await controller.pause(guild)


@pytest.mark.asyncio
async def test_resume(controller, guild):
    """ Assert the controller can resume a video """
    # await controller.resume(guild)


@pytest.mark.asyncio
async def test_stop(controller, guild):
    """ Assert the controller can stop a video """
    # await controller.stop(guild)


@pytest.mark.asyncio
async def test_report_error():
    """ Assert the controller reports errors correctly """
