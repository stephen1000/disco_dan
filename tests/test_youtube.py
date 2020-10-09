""" Tests for the youtube module """

import pytest

from disco_dan import youtube


@pytest.fixture(
    params=[
        "nyan cat original",
        "no god no",
        "Charlie Schmidt's Keyboard Cat! - THE ORIGINAL!",
        "Pokemon Intro",
    ]
)
def known_video(request):
    return request.param


@pytest.mark.asyncio
async def test_search(known_video):
    """ Assert search finds a known video """
    url = await youtube.search(known_video)
    assert url
    assert isinstance(url, str)
    assert not url.endswith("&t=")
    assert url.startswith("https://www.youtube.com/watch?v=")


@pytest.mark.asyncio
async def test_get_audio(known_video):
    """ Assert get_audio retrieves some audio for a known video """
    url = await youtube.search(known_video)
    audio = await youtube.get_audio(url)
    assert audio



@pytest.mark.asyncio
async def test_load_audio(known_video):
    """ Assert load_aduio returns audio """
    audio = await youtube.load_audio(known_video)
    assert audio