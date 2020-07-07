""" Project Settings """

import os

from dotenv import load_dotenv

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")

YOUTUBE_TOKEN = os.getenv("YOUTUBE_TOKEN")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
