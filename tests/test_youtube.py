""" Tests for the youtube module """

import pytest

from disco_dan import youtube
from disco_dan.models import YoutubeResult


@pytest.mark.asyncio
async def test_search(known_video: YoutubeResult):
    """ Assert search finds a known video """
    result = await youtube.search(known_video.query_text, use_cache=False)
    assert result
    assert result.query_text == known_video.query_text
    assert result.url == known_video.url


@pytest.mark.asyncio
async def test_get_audio(known_video: YoutubeResult):
    """ Assert get_audio retrieves some audio for a known video """
    audio = await youtube.get_audio(known_video.url)
    assert audio


