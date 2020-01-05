#/usr/bin/python3

import re
from collections import namedtuple
from operator import itemgetter


__author__ = 'Erik Moqvist'
__version__ = '0.21.1'
__repository__ = 'https://github.com/eerimoq/textparser.git'


class _Mismatch(object):
    pass

MISMATCH = _Mismatch()a
"""
Returned by :func:`~textparser.Pattern.match()` on mismatch.
"""


class _String(object):
    """
    Matches a specific token kind.
    """
    pass

