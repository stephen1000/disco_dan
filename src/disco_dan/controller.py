""" Disco Dan's Brain """
import argparse
from io import BytesIO
from typing import Optional

import discord

from disco_dan import settings, youtube, exceptions


class Controller(object):
    """ Bot controller """

    COMMANDS = [
        "play",
        "pause",
        "stop",
    ]

    START_WORD = "disco dan"

    def __init__(self, client: discord.Client):
        self.client = client
        self.parser = self.get_parser()

    def get_parser(self):
        """ Builds an argument parser """
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(help="Disco Dan subcommand")

        play_parser = subparsers.add_parser(
            "play",
            help='Play a youtube video in a channel. E.g.: `disco dan play "nyan cat"`, `disco dan play "holy diver" talkie`.',
        )
        play_parser.add_argument(
            "--channel",
            type=str,
            help=f'Channel to play audio in. Default: "{settings.DEFAULT_VOICE_CHANNEL}".',
        )
        play_parser.set_defaults(command="play")

        pause_parser = subparsers.add_parser(
            "pause", help="Pause the currently playing video."
        )
        pause_parser.set_defaults(command="pause")

        stop_parser = subparsers.add_parser("stop", help="Stop playing videos")
        stop_parser.set_defaults(command="stop")

        return parser

    async def handle_message(self, message):
        """ Process a new discord message """

    async def parse(self, message: discord.Message) -> None:
        """ Parses a message and instructs the controller to act accordingly """
        command_text = await self.get_bot_command_text(message)
        if command_text is None:
            return

        args = self.parser.parse_args(command_text)

        if args.command == "play":
            await self.play(guild=message.guild, query=args.query, channel_name=args.channel)

        elif args.command == "pause":
            await self.pause(guild=message.guild)

        elif args.command == "stop":
            await self.stop(guild=message.guild)

    async def get_bot_command_text(self, message: discord.Message) -> Optional[str]:
        """ `True` if message is speaking to Disco Dan """
        if message.content.lower().startswith(self.START_WORD.lower()):
            return message.content[len(self.START_WORD) :]
        return None
        
    async def find_guild_channel(self, guild:discord.Guild, channel_name: Optional[str]=None):
        """ Fetch a voice channel named `channel_name` in `guild`. """
        if channel_name is None:
            channel_name = settings.DEFAULT_VOICE_CHANNEL

        matched_channels = [
            c
            for c in guild.voice_channels
            if c.name.lower() == channel_name.lower()
        ]
        if len(matched_channels) == 0:
            raise exceptions.VoiceNotChannelFound(
                "Couldn't find a voice channel named '%s'", channel_name
            )
        elif len(matched_channels) >= 1:
            raise exceptions.MultipleVoiceChannelsFound(
                "Found multiple matches for a voice channel named '%s': %s",
                (channel_name, ", ".join(matched_channels)),
            )

        return matched_channels[0]

    async def play(self, guild:discord.Guild, query: str, channel_name: Optional[str] = None):
        voice_channel = await self.find_guild_channel(guild, channel_name)
        voice_connection = await voice_channel.connect()

        audio = await youtube.fetch_audio(query)

        with BytesIO() as buffer:
            audio.stream_to_buffer(buffer)
            voice_connection.play(discord)

    async def pause(self, guild:discord.Guild):
        pass

    async def stop(self, guild:discord.Guild):
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

    async def report_error(self, error: exceptions.DiscoDanError):
        """ Inform the user that something went wrong """
