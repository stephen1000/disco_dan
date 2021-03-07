""" Ensure `disco_dan.cache.cache` behaves properly """

import pytest
from disco_dan import db, settings, youtube
from disco_dan.cache import SearchCache
from disco_dan.cache.models import YoutubeQuery, create_objects
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
async def cache():
    """ A search cache for testing """
    engine = create_engine(settings.TEST_CONNECTION_STRING)
    create_objects(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    cache = SearchCache(Session=Session)
    await cache.async_flush()
    return cache


@pytest.mark.asyncio
async def test_check_text_hit(cache, known_video):
    """ Assert that check_text retrieves a value """
    youtube_id, query_text, url = ("fake_id", known_video, "http://fake-url.com")
    cache_entry = await cache.add_result(youtube_id, query_text, url)

    hit = await cache.check_text(known_video)
    assert hit.url == cache_entry.url
    assert hit.query_text == cache_entry.query_text


@pytest.mark.asyncio
async def test_check_text_miss(cache, known_video):
    """ Assert that check_text retrieves a value """
    miss = await cache.check_text(known_video + ' aww now im gonna miss :(')
    assert miss is None


@pytest.mark.asyncio
async def test_add_result(cache):
    """ Assert that `add_result` accurately adds an entry """
    session = db.Session()

    youtube_id, query_text, url = ("fake_id", "fake text", "http://fake-url.com")
    await cache.add_result(youtube_id, query_text, url)

    result = (
        session.query(YoutubeQuery)
        .filter_by(youtube_id=youtube_id)
        .filter_by(query_text=query_text)
        .filter_by(url=url)
        .first()
    )

    assert result.youtube_id == youtube_id
    assert result.query_text == query_text
    assert result.url == url
