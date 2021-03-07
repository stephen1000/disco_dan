""" Common Errors """

class DiscoDanError(Exception):
    """ Something went wrong with Disco Dan :( """

class MessageParsingErrror(DiscoDanError):
    """ Something went wrong when parsing a message """

class VoiceNotChannelFound(MessageParsingErrror):
    """ Couldn't find a specific voice channel """

class MultipleVoiceChannelsFound(MessageParsingErrror):
    """ Found too many matches for a voice channel """


class YoutubeError(DiscoDanError):
    """ Something went wrong when accessing youtube """