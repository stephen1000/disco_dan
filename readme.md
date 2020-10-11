# Disco Dan
A bot for streaming audio from [YouTube](youtube.com) videos to a [Discord](discord.gg) channel.

# Installation
Create a virtual environment for the application with [virtualenv](https://virtualenv.pypa.io/en/stable/):
``` shell
virtualenv env
```

Install the bot & dependencies:
``` shell
# ssh
pip install git+ssh://git@github.com/stephen1000/disco_dan@master

# https
pip install git+https://github.com/stephen1000/disco_dan@master
```

More ways to install (direct pip package) are incoming.

# Configuration
Settings are managed with environment variables, which can be set for convenience w/ [python-dotenv](https://pypi.org/project/python-dotenv/).

Either set environment variables in the shell used to run `bot.py` or create a `.env` file at the project root

## Discord Registration
The bot requires a Discord Application to authenticate w/ the discord API. You can register for an application in the [developer portal](https://discord.com/developers/applications).

After registering an application, you should be able to copy the discord from the `Bot` tab in the developer portal. Provide that token as `DISCORD_TOKEN` in the environment directly or through `.env`.

To connect your bot to a server, you can use the OAuth2 tab to generate an invite link (for servers where you have the `Add Bot` permission, that is). Required permissions are currently WIP (should be join voice/chat, but this may be out of date).

## Google API Registration
To register for the Google/Youtube API, follow [this guide](https://developers.google.com/youtube/registering_an_application). Provide that token as `YOUTUBE_TOKEN` in the environment directly or through `.env`.

# Usage
Initialize the cacheing database 
```
# Windows
env\Scripts\activate
python src\disco_dan\bot.py

# Mac/Linux
source env/bin/activate
python src/disco_dan/bot.py
```

System specific instructions can be found online for running python processes in the background and/or as a service.

# Roadmap
- Logging
- Containerization

# Further Reading
See docstrings for documentation (full documentation pending)

