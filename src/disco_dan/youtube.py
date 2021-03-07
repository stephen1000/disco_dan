""" YouTube accessor """
import asyncio
import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pytube import YouTube

from disco_dan import settings, exceptions
from disco_dan.cache import SearchCache
from disco_dan.models import YoutubeResult

cache = SearchCache()


async def search(q, max_results=5, order="relevance", start_at="0s", use_cache=True):
    """ Search youtube for `q` & return first url by `order`, staring at time `start_at` """
    # pylint: disable=no-member

    if use_cache:
        hit = await cache.check_text(q)
        if hit:
            return YoutubeResult(hit.query_text, hit.youtube_id,)

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

    if use_cache and video_id:
        await cache.add_result(video_id, q, result.url)

    return result


async def get_audio(youtube_url: str, audio_format="mp4") -> None:
    """ Download a url from Youtube """
    # pylint: disable=no-member
    youtube_video = YouTube(youtube_url)
    audio = youtube_video.streams.get_audio_only(audio_format)
    return audio


async def load_audio(q, use_search_cache=None):
    if use_search_cache is None:
        use_search_cache = settings.USE_SEARCH_CACHE
    try:
        result = await search(q, use_cache=True)
        audio = await get_audio(result.url)
    except KeyError as e:
        raise exceptions.YoutubeError(
            'Unable to load video for query "%s":\n%s',
            q,
            str(e) + ",".join(str(arg) for arg in e.args),
        )
    return audio

