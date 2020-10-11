""" Cache search results to reduce API usage """
import datetime as dt

from disco_dan import db
from disco_dan.cache.models import YoutubeQuery
from disco_dan.youtube import search


class SearchCache(object):
    """ A cache of search results """

    def __init__(self, duration: dt.timedelta = dt.timedelta(days=90)):
        self.duration = duration

    async def check_text(self, query_text) -> YoutubeQuery:
        """ Retrieve an entry from db """
        session = db.Session()
        cache_limit = dt.datetime.now() - self.duration
        matches = (
            session.query(YoutubeQuery)
            .filter(YoutubeQuery.query_text == query_text)
            .filter(YoutubeQuery.youtube_id is not None)
            .order_by(YoutubeQuery.created_at.desc())
            .filter(YoutubeQuery.created_at > cache_limit)
        )
        if matches.first():
            return matches.first()

        # failed cache hit
        search_result = await search(query_text)
        if search_result.youtube_id is not None:
            # add found result to cache
            result = await self.add_result(search_result.youtube_id, search_result.query_text, search_result.url)
            return result

        # failed and didn't find any matches
        return None

    async def add_result(self, youtube_id: str, query_text: str, url: str) -> YoutubeQuery:
        """ Add a new cache entry for `query_text` """
        session = db.Session()
        entry = YoutubeQuery(
            query_text=query_text,
            youtube_id=youtube_id,
            url=url,
            created_at=dt.datetime.now(),
        )
        session.add(entry)
        session.commit()
        return entry

    async def flush(self, expired_only: bool = True):
        """ Flush this cache """
        session = db.Session()
        flush_rows = session.query(YoutubeQuery)
        if expired_only:
            cache_limit = dt.datetime.now() - self.duration
            flush_rows = flush_rows.filter(YoutubeQuery.created_at < cache_limit)
        flush_rows.delete()
        session.commit()
