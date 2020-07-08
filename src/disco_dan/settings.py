""" Project Settings """

import os

from dotenv import load_dotenv

load_dotenv()

FFMPEG_EXECUTABLE = os.getenv('FFMPEG_EXECUTABLE')

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
DEFAULT_TEXT_CHANNEL = os.getenv('DEFAULT_TEXT_CHANNEL')
DEFAULT_VOICE_CHANNEL = os.getenv('DEFAULT_VOICE_CHANNEL')

YOUTUBE_TOKEN = os.getenv("YOUTUBE_TOKEN")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
