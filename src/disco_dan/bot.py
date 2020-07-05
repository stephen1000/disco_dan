""" Disco Dan's brain """

from disco_dan import settings

import discord


client = discord.Client()

@client.event
async def on_ready():
    """ Announce yourself """
    print('Disco Dan is here!')


@client.event
async def on_message(message):
    """ Respond to a message """
    if message.content.startswith('Disco Dan'):
        print(message.content)
        await message.channel.send('Dan says hi!')


client.run(settings.DISCORD_TOKEN)
