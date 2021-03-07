"""
Common models
"""


class YoutubeResult(object):
    """ A video id and matching url """

    def __init__(self, query_text: str, youtube_id: str, start_at: str = "0s"):
        self.query_text = query_text
        self.youtube_id = youtube_id
        self.start_at = start_at

    @property
    def url(self):
        return f"https://www.youtube.com/watch?v={self.youtube_id}"

    def __str__(self):
        return self.url

    def __bool__(self):
        return self.youtube_id is not None

    def __repr__(self):
        return f"<YoutubeResult({self.query_text}, {self.youtube_id}, {self.start_at})>"
