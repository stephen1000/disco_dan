""" Disco Dan's Brain """

from discord import Client
from disco_dan.message_parser import MessageParser


class Controller(object):
    """ Bot controller """

    def __init__(self, client:Client):
        self.client = client
        self.parser = MessageParser()

    async def handle_message(self, message):
        """ Process a new discord message """

    async def play(self, **kwargs):
        pass

        # video_name = re.search(r'"(.+)"', message.content).group(1)
        # channel_name = message.content.split()[-1]
        # voice_channel = [c for c in message.guild.voice_channels if c.name.lower() == channel_name.lower()][0]
        # print(message.content)
        # response = 'Dan says hi!'
        # if message.author.name.lower() == 'muphin':
        #     response = f'Muphin, {response}, you ignorant slut!'
            
        # voice_connection = await voice_channel.connect()
        # # voice_connection.play(discord.FFmpegPCMAudio(executable=r"C:\Program Files\ffmpeg\bin\ffmpeg.exe", source="dial_up.mp3"))
        # pass