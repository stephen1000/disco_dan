""" Disco Dan's Brain """
import argparse
from io import BytesIO
from typing import Optional

import discord

from disco_dan import settings, youtube, exceptions


class Controller(object):
    """ Bot controller """

    START_WORD = "disco dan"

    def __init__(self, client: discord.Client):
        self.client = client
        self.parser = self.get_parser()
        self.voice_connection = None

    def get_parser(self):
        """ Builds an argument parser """
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(help="Disco Dan subcommand")

        play_parser = subparsers.add_parser(
            "play",
            help='Play a youtube video in a channel. E.g.: `disco dan play "nyan cat"`, `disco dan play "holy diver" talkie`.',
        )
        play_parser.add_argument(
            "query",
            type=list,
            nargs=argparse.REMAINDER,
            help="Text used to find a video on youtube",
        )
        play_parser.add_argument(
            "--channel", type=str, help=f"Channel to play audio in.",
        )
        play_parser.set_defaults(command="play")

        pause_parser = subparsers.add_parser(
            "pause", help="Pause the currently playing video."
        )
        pause_parser.set_defaults(command="pause")

        stop_parser = subparsers.add_parser("stop", help="Stop playing videos")
        stop_parser.set_defaults(command="stop")

        resume_parser = subparsers.add_parser("resume", help="Resume playing video")
        resume_parser.set_defaults(command="resume")

        return parser

    async def handle_message(self, message: discord.Message) -> None:
        """ Parses a message and instructs the controller to act accordingly """
        command_text = await self.get_bot_command_text(message.content)
        if command_text is None:
            return

        try:
            args = self.parser.parse_args(command_text.split())
        except SystemExit:
            raise exceptions.MessageParsingErrror("Disco Dan's head hurts :(")

        if args.command == "play":
            query = " ".join(str(x) for x in args.query)
            await message.channel.send(
                f'Playing "{query}" (requested by {message.author.mention})!'
            )
            await self.play(guild=message.guild, query=query, channel_name=args.channel)

        elif args.command == "pause":
            await message.channel.send(
                f"Pausing playback (requested by {message.author.mention})..."
            )
            await self.pause(guild=message.guild)

        elif args.command == "resume":
            await message.channel.send(
                f"Resuming playback (requested by {message.author.mention})..."
            )
            await self.resume(guild=message.guild)

        elif args.command == "stop":
            await message.channel.send(
                f"Stopping playback (requested by {message.author.mention})..."
            )
            await self.stop(guild=message.guild)

    async def get_bot_command_text(self, message: str) -> Optional[str]:
        """ `True` if message is speaking to Disco Dan """
        if message.lower().startswith(self.START_WORD.lower()):
            return message[len(self.START_WORD) :].strip()
        return None

    async def find_guild_channel(
        self, guild: discord.Guild, channel_name: Optional[str] = None
    ):
        """ Fetch a voice channel named `channel_name` in `guild`. """
        if channel_name is None:
            channel_name = settings.DEFAULT_VOICE_CHANNEL

        matched_channels = [
            c for c in guild.voice_channels if c.name.lower() == channel_name.lower()
        ]
        if len(matched_channels) == 0:
            raise exceptions.VoiceNotChannelFound(
                "Couldn't find a voice channel named '%s'", channel_name
            )
        elif len(matched_channels) > 1:
            raise exceptions.MultipleVoiceChannelsFound(
                "Found multiple matches for a voice channel named '%s': %s",
                (
                    channel_name,
                    ", ".join(str(channel.name) for channel in matched_channels),
                ),
            )

        return matched_channels[0]

    async def get_voice_connection(
        self, guild: discord.Guild, create_in_channel: Optional[str] = None
    ):
        """ Return the current bot voice connection for `guild`. """
        connection = guild.voice_client

        if connection is None and create_in_channel is not None:
            voice_channel = await self.find_guild_channel(guild, create_in_channel)
            connection = await voice_channel.connect()

        return connection

    async def play(
        self, guild: discord.Guild, query: str, channel_name: Optional[str] = None
    ):
        voice_connection = await self.get_voice_connection(
            guild, create_in_channel=channel_name
        )

        if voice_connection.is_playing:
            await self.stop(guild)

        audio = await youtube.load_audio(query)
        audio_path = audio.download(
            output_path=settings.AUDIO_BUFFER_PATH,
            filename=settings.AUDIO_BUFFER_NAME,
            skip_existing=False,
        )

        player = discord.FFmpegPCMAudio(
            executable=settings.FFMPEG_EXECUTABLE, source=audio_path
        )
        await voice_connection.play(player)

    async def resume(self, guild: discord.Guild):
        """ Resume audio playback """
        voice_connection = await self.get_voice_connection(guild)
        if voice_connection is not None:
            await voice_connection.resume()

    async def pause(self, guild: discord.Guild):
        """ Pause the current audio """
        voice_connection = await self.get_voice_connection(guild)
        if voice_connection is not None:
            await voice_connection.pause()

    async def stop(self, guild: discord.Guild):
        """ Stop the current audio """
        voice_connection = await self.get_voice_connection(guild)
        if voice_connection is not None:
            await voice_connection.stop()

    async def report_error(
        self, error: exceptions.DiscoDanError, channel: discord.TextChannel
    ):
        """ Inform the user that something went wrong """
        self.stop(channel.guild)
        print(repr(error))
        if len(error.args) == 0:
            error_message = error.__doc__
        elif len(error.args) == 1:
            error_message = error.args[0]
        else:
            error_message = error.args[0] % error.args[1:]
        await channel.send(f"I ran into an error :(-\n {type(error)} {error_message}")

