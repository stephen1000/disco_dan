""" CLI for disco dan features """
import argparse

from disco_dan import bot
from disco_dan.cache.models import create_objects
from disco_dan.cache.search_cache import SearchCache


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        help="""Command to run- one of:
    run: start the disco_dan bot
    initdb: initialize the cacheing database (uses environment variable DISCO_DAN_CONNECTION_STRING)
    flush: empties the cache
    """,
        choices=["run", "initdb", "flush"],
    )
    return parser


def handle():
    parser = get_parser()
    args = parser.parse_args()

    if args.command == "run":
        bot.start_loop()
    if args.command == "initdb":
        create_objects()
    if args.command == "flush":
        SearchCache().flush()


if __name__ == "__main__":
    handle()
