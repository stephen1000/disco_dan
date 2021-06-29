.. _settings:


settings.py
======================

.. automodule:: disco_dan.settings

.. autodata:: disco_dan.settings.AUDIO_BUFFER_PATH
.. autodata:: disco_dan.settings.AUDIO_BUFFER_NAME
.. autodata:: disco_dan.settings.FFMPEG_EXECUTABLE
.. autodata:: disco_dan.settings.DISCORD_TOKEN
.. autodata:: disco_dan.settings.DISCORD_GUILD
.. autodata:: disco_dan.settings.DISCORD_TEST_GUILD
.. autodata:: disco_dan.settings.DISCO_DAN_CONNECTION_STRING
.. autodata:: disco_dan.settings.TEST_CONNECTION_STRING
.. autodata:: disco_dan.settings.USE_SEARCH_CACHE
.. autodata:: disco_dan.settings.DEFAULT_TEXT_CHANNEL
.. autodata:: disco_dan.settings.DEFAULT_VOICE_CHANNEL
.. autodata:: disco_dan.settings.YOUTUBE_TOKEN
.. autodata:: disco_dan.settings.YOUTUBE_API_SERVICE_NAME
.. autodata:: disco_dan.settings.YOUTUBE_API_VERSION


To quickly configure your setings with `python-dotenv <https://github.com/theskumar/python-dotenv>`_, copy this template
and fill out the value of each setting:

.. literalinclude:: ../../example.env