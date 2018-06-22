import os
import re
from typing import List
from typing import Pattern
from typing import Tuple

import colorlog


class EqualityMixin:  # pragma: no cover
    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


def compile_exclusions(exclusions: str) -> List[Pattern]:  # pragma: no cover
    return [re.compile(excl) for excl in exclusions]


def file_walker(path, on_error=None):  # pragma: no cover
    """ Walk through all the files in a path and yield their names one-at-a-time,
    relative to the "path" value passed in.
    """
    for root, dirs, files in os.walk(path, onerror=on_error):
        for f in files:
            yield os.path.join(root, f)


def get_color_logger(name):  # pragma: no cover
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(name)s:%(message)s'))
    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    return logger


def sha_to_path(sha: str) -> Tuple[str, ...]:
    return (sha[:2], sha[2:4], sha[4:])
