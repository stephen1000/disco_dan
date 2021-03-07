""" Cache search results to reduce API usage """
import datetime as dt

from disco_dan import db
from disco_dan.cache.models import YoutubeQuery


class SearchCache(object):
    """ A cache of search results """
    # pylint: disable=no-member

    def __init__(self, duration: dt.timedelta = dt.timedelta(days=90), Session=None):
        self.duration = duration
        if Session is None:
            self.Session = db.Session
        else:
            self.Session = Session

    async def check_text(self, query_text) -> YoutubeQuery:
        """ Retrieve an entry from db """
        session = self.Session()
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

        # failed and didn't find any matches
        return None

    async def add_result(self, youtube_id: str, query_text: str, url: str) -> YoutubeQuery:
        """ Add a new cache entry for `query_text` """
        session = self.Session()
        entry = YoutubeQuery(
            query_text=query_text,
            youtube_id=youtube_id,
            url=url,
            created_at=dt.datetime.now(),
        )
        session.add(entry)
        session.commit()
        return entry

    def flush(self, expired_only: bool = True):
        """ Flush this cache """
        session = self.Session()
        flush_rows = session.query(YoutubeQuery)
        if expired_only:
            cache_limit = dt.datetime.now() - self.duration
            flush_rows = flush_rows.filter(YoutubeQuery.created_at < cache_limit)
        flush_rows.delete()
        session.commit()

    async def async_flush(self, *args, **kwargs):
        """ Like flush, but async! """
        return self.flush(*args, **kwargs)