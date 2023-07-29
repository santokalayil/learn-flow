import os
from pathlib import Path

from slogger import SLogger

logger = SLogger(__name__, ".temp/logs")

logger.critical("Testing critical logger")


project_name = "ml project"

list_of_files = [
    ".github/workflows/.gitkeep"
]

for i in list_of_files:
    item = Path(i)
    if not item.parent.is_dir():
        item.parent.mkdir(parents=True)
    if not item.exists():
        item.touch()


