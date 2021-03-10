""" Assert that `disco_dan.cache.models` loads without issue """

import pytest


def test_models():
    """ Assert that `disco_dan.cache.models` loads without issue """
    from disco_dan.cache import models

    assert models
