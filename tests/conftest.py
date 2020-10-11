""" Pytest configuration """

import pytest


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
