""" Disco Dan's heart """
import re

import discord

from disco_dan import settings, controller, exceptions
from disco_dan.loggers import logger

client = discord.Client()
controller = controller.Controller(client)


@client.event
async def on_ready():
    """ Announce yourself """
    logger.info("Disco Dan is here!")


@client.event
async def on_message(message: discord.message.Message):
    """ Respond to a message 
    
    :param message: A discord message object to respond to
    :type message: discord.message.Message

    :raises: exceptions.DiscoDanError: Something went wrong with Disco Dan D:

    :return: None
    :rtype: None
    """
    try:
        await controller.handle_message(message)
    except exceptions.DiscoDanError as e:
        await controller.report_error(e, message.channel)


def start_loop():
    client.run(settings.DISCORD_TOKEN)


if __name__ == "__main__":
    start_loop()
