""" YouTube accessor """
import asyncio
import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pytube import YouTube

from disco_dan import settings, exceptions


class YoutubeResult(object):
    """ A video id and matching url """

    def __init__(self, query: str, youtube_id: str, start_at: str = "0s"):
        self.query = query
        self.youtube_id = youtube_id
        self.start_at = start_at

    @property
    def url(self):
        return f"https://www.youtube.com/watch?v={self.youtube_id}&t={self.start_at}"

    def __str__(self):
        return self.url

    def __repr__(self):
        return f'<YoutubeResult({self.query}, {self.youtube_id}, {self.start_at})>'


async def search(q, max_results=5, order="relevance", start_at="0s"):
    """ Search youtube for `q` & return first url by `order`, staring at time `start_at` """
    # pylint: disable=no-member

    youtube = build(
        settings.YOUTUBE_API_SERVICE_NAME,
        settings.YOUTUBE_API_VERSION,
        developerKey=settings.YOUTUBE_TOKEN,
    )
    items = youtube.search().list(q=q, part="id,snippet").execute().get("items", [])

    for item in items:
        if "id" in item:
            video_id = item["id"].get("videoId")
            break
    else:
        video_id = None

    result = YoutubeResult(q, video_id, start_at=start_at)
    return result


async def get_audio(youtube_url: str, audio_format="mp4") -> None:
    """ Download a url from Youtube """
    # pylint: disable=no-member
    youtube_video = YouTube(youtube_url)
    audio = youtube_video.streams.get_audio_only(audio_format)
    return audio


async def load_audio(q):
    try:
        result = await search(q)
        audio = await get_audio(result.url)
    except KeyError as e:
        raise exceptions.YoutubeError(
            'Unable to load video for query "%s":\n%s',
            q,
            str(e) + ",".join(str(arg) for arg in e.args),
        )
    return audio

