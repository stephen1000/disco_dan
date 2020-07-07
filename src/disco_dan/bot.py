""" Disco Dan's heart """
import re

import discord

from disco_dan import settings
from disco_dan.controller import Controller

client = discord.Client()
controller = Controller(client)


@client.event
async def on_ready():
    """ Announce yourself """
    print("Disco Dan is here!")


@client.event
async def on_message(message):
    """ Respond to a message-
    "disco dan, play 'nyan cat' in talkie" -> play "nyan cat" in voice channel "talkie"
    """
    controller.handle_message(message)


def start_loop():
    client.run(settings.DISCORD_TOKEN)


if __name__ == "__main__":
    start_loop()
