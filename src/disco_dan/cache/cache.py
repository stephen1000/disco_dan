""" Cache search results to reduce API usage """
import datetime as dt

from disco_dan import db
from disco_dan.cache.models import YoutubeQuery
from disco_dan.youtube import search


class SearchCache(object):
    """ A cache of search results """

    def __init__(self, duration: dt.timedelta = dt.timedelta(days=90)):
        self.duration = duration

    def check_text(self, query_text):
        """ Retrieve an entry from db """
        session = db.Session()
        cache_limit = dt.datetime.now() - self.duration
        matches = (
            session.query(YoutubeQuery)
            .filter_by(YoutubeQuery.query_text == query_text)
            .filter_by(YoutubeQuery.youtube_id is not None)
            .filter_by(YoutubeQuery.created_at > cache_limit)
            .order_by(YoutubeQuery.created_at.desc())
        )
        if matches:
            return matches.first().url

        # failed cache hit
        result = search(query_text)
        if result.youtube_id is not None:
            # add found result to cache
            self.add_result(result.youtube_id, result.query_text, result.url)
            return result.url

        # failed and didn't find any matches
        return None



    def add_result(self, youtube_id: str, query_text: str, url:str):
        """ Add a new cache entry for `query_text` """
        session = db.Session()
        entry = YoutubeQuery(
            query_text=query_text, youtube_id=youtube_id, url=url, created_at=dt.datetime.now()
        )
        session.add(entry)
        session.commit()

    def flush(self, expired_only: bool = True):
        """ Flush this cache """
        session = db.Session()
        flush_rows = session.query(YoutubeQuery)
        if expired_only:
            cache_limit = dt.datetime.now() - self.duration
            flush_rows.filter_by(YoutubeQuery.created_at < cache_limit)
        session.delete(flush_rows)
        session.commit()
