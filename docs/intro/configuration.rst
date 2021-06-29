.. _configuration:

Configuration
=======================================

Disco Dan requires some environment variables to be set before it can be run. Specifically, you must enable the
following values:

* `DISCORD_TOKEN`- Discord API token granting the bot permission to enter voice channels, post messages, etc.
* `DISCORD_GUILD`- The guild (or server) the bot will operate within
* `DISCO_DAN_CONNECTION_STRING`- a (valid) SQLAlchemy connection string (can use sqlite to avoid setup)
* `FFMPEG_EXECUTABLE`- absolute path to a usable installation of FFMPEG
* `YOUTUBE_TOKEN`- Google Developer API token- used to gain access to the YouTube Search API


.. warning:: Do *NOT* put `DISCORD_TOKEN` or `YOUTUBE_TOKEN` in source control!

.. seealso::
    Module `python-dotenv <https://github.com/theskumar/python-dotenv>`_
        Documentation for Python-Dotenv, a tool for loading environment values.

    Module :ref:`settings`
        More settings to configure.
