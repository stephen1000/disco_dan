.. _youtube:

youtube.py
=======================


.. automodule:: disco_dan.youtube
:members:

Search the YouTube API for video IDs:

.. code-block:: python

    from disco_dan.youtube import search

    video_id = search('nyan cat 10 hours', use_cache=False)
