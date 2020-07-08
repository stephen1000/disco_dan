""" YouTube accessor """
import asyncio
import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pytube import YouTube

from disco_dan import settings, exceptions


async def search(q, max_results=50, order="relevance", start_at="0s"):
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

    youtube_url = f"https://www.youtube.com/watch?v={video_id}&t={start_at}"

    return youtube_url


async def get_audio(youtube_url: str, audio_format="mp4") -> None:
    """ Download a url from Youtube """
    youtube_video = YouTube(youtube_url)
    audio = youtube_video.streams.get_audio_only(audio_format)
    return audio


async def load_audio(q):
    try:
        url = await search(q)
        audio = await get_audio(url)
    except KeyError as e:
        raise exceptions.YoutubeError(
            'Unable to load video for query "%s":\n%s', q, repr(e)
        )
    return audio

