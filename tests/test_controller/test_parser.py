""" Tests for the bot controller parser """

import pytest
from disco_dan.controller import Controller
from disco_dan.settings import DEFAULT_VOICE_CHANNEL


@pytest.fixture
async def parser():
    controller = Controller(client=object())
    parser = controller.get_parser()
    return parser


@pytest.mark.asyncio
def test_parser_play(parser):
    """ Assert the parser behaves properly """
    # standard usage
    args = parser.parse_args(["play", "some_video"])
    assert args.query == ["some_video"]
    assert args.command == "play"


@pytest.mark.asyncio
def test_parser_play_channel(parser):
    # standard + channel
    args = parser.parse_args(["play", "--channel", "some_channel", "some_video"])
    assert args.query == ["some_video"]
    assert args.channel == "some_channel"
    assert args.command == "play"


@pytest.mark.asyncio
def test_parser_play_spaces(parser):
    # spaced query
    args = parser.parse_args(["play", "some", "video", "with", "spaces"])
    assert args.query == ["some", "video", "with", "spaces"]
    assert args.command == "play"


@pytest.mark.asyncio
def test_parser_play_channel_spaces(parser):
    # spaced query + channel
    args = parser.parse_args(
        ["play", "--channel", "some_channel", "some", "video", "with", "spaces"]
    )
    assert args.query == ["some", "video", "with", "spaces"]
    assert args.channel == "some_channel"
    assert args.command == "play"


@pytest.mark.asyncio
def test_parser_pause(parser):
    """ Asert the pause parser behaves properly """
    args = parser.parse_args(["pause"])
    assert args.command == "pause"


@pytest.mark.asyncio
def test_parser_resume(parser):
    """ Asert the resume parser behaves properly """
    args = parser.parse_args(["resume"])
    assert args.command == "resume"


@pytest.mark.asyncio
def test_parser_stop(parser):
    """ Asert the stop parser behaves properly """
    args = parser.parse_args(["stop"])
    assert args.command == "stop"


