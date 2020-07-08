# Disco Dan
A bot for streaming [YouTube](youtube.com) videos to a [Discord](discord.gg) channel.

# Installation
Get the code for this repo and move to the project root:
``` shell
git clone <https or ssh url>
cd disco_dan
```

Create a virtual environment for the application in the project root with [virtualenv](https://virtualenv.pypa.io/en/stable/):
``` shell
virtualenv env
```

Install the bot & dependencies:
``` shell
pip install .
```

More ways to install are incoming.

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
Presently, the only way to run Disco Dan is to start a python process:
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
- Tests (pytest)
- Logging
- CLI
- Better installation
- Pi service config via systemd
- Containerization

# Further Reading
See docstrings for documentation (full documentation pending)

