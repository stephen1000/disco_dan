""" Pytest configuration """

import pytest
from disco_dan.models import YoutubeResult


@pytest.fixture(
    params=[
        YoutubeResult("nyan cat original", "QH2-TGUlwu4"),
        YoutubeResult("no god please no noooo", "umDr0mPuyQc"),
        YoutubeResult("Charlie Schmidt's Keyboard Cat! - THE ORIGINAL!", "J---aiyznGQ"),
        YoutubeResult("Pokemon Intro", "6xKWiCMKKJg"),
    ],
    ids=["nyan cat", "no god no", "keyboard cat", "pokemon intro"],
)
def known_video(request):
    return request.param
