""" Tests for the youtube module """

import pytest

from disco_dan import youtube


@pytest.mark.asyncio
async def test_search(known_video):
    """ Assert search finds a known video """
    result = await youtube.search(known_video)
    assert result
    assert result.query_text == known_video
    assert result.url.startswith("https://www.youtube.com/watch?v=")


@pytest.mark.asyncio
async def test_get_audio(known_video):
    """ Assert get_audio retrieves some audio for a known video """
    result = await youtube.search(known_video)
    audio = await youtube.get_audio(result.url)
    assert audio


@pytest.mark.asyncio
async def test_load_audio(known_video):
    """ Assert load_aduio returns audio """
    audio = await youtube.load_audio(known_video)
    assert audio
