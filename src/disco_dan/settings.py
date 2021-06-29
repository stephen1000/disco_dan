""" Project Settings """

import os

from dotenv import load_dotenv

load_dotenv()

#: Path to current audio buffer
AUDIO_BUFFER_PATH = os.getenv("AUDIO_BUFFER_PATH", "buffer")
#: Name of current audio buffer fule
AUDIO_BUFFER_NAME = os.getenv("AUDIO_BUFFER_NAME", "now_playing.mp4")
#: Path to FFMPEG install location
FFMPEG_EXECUTABLE = os.getenv("FFMPEG_EXECUTABLE")

#: Discord API Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
#: Discord guild to operate within
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
#: Discord guild to test stuff in (optional)
DISCORD_TEST_GUILD = os.getenv("DISCORD_TEST_GUILD", DISCORD_GUILD)

#: SQLAlchemy connection string for disco dan backend
DISCO_DAN_CONNECTION_STRING = os.getenv("DISCO_DAN_CONNECTION_STRING")
#: SQLAlchemy connection string for disco dan *test* backend
TEST_CONNECTION_STRING = os.getenv("TEST_CONNECTION_STRING")
#: Set to True to cache Youtube API calls
USE_SEARCH_CACHE = not (DISCO_DAN_CONNECTION_STRING is None)

#: Set to text channel where messages will go (if not responding to a particular user)
DEFAULT_TEXT_CHANNEL = os.getenv("DEFAULT_TEXT_CHANNEL")
#: Set to voice channel to join (if no channel is specified and requester is not in a voice channel)
DEFAULT_VOICE_CHANNEL = os.getenv("DEFAULT_VOICE_CHANNEL")

#: Youtube API Token
YOUTUBE_TOKEN = os.getenv("YOUTUBE_TOKEN")
#: Name of the youtube API
YOUTUBE_API_SERVICE_NAME = "youtube"
#: Version of the youtube API
YOUTUBE_API_VERSION = "v3"

