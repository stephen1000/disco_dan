""" Application logger(s) """

import logging
from pathlib import Path

log_dir = Path.cwd() / "logs"
log_dir.mkdir(exist_ok=True, parents=True)

logger = logging.getLogger("disco_dan")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler(log_dir / "debug.log"))
