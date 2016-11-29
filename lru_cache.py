"""Implementation of Least Recently Used Cache data structure.

Need both key/value paradigm of hash table as well as ordered paradigm
of queue. This is a great use case in Python for collections.OrderedDict.
"""

from __future__ import unicode_literals
from collections import OrderedDict
import re


SIZE_PAT = re.compile(r'^SIZE\s(?P<size>\d+)')


class LRUCache(object):
    """Data cache providing key/value access limited by size."""

    def __init__(self, size):
        """Initialize the cache with given size."""
        self._size = size
        self._cache = OrderedDict()

    def set():
        pass

    def get():
        pass

    def exit():
        pass


def session():
    """Provide an interactive session to use a new LRU cache."""
    cache = None
    while cache is None:
        command = raw_input()
        size_match = SIZE_PAT.match(command)
        if size_match is None:
            error()
            continue
        size = int(size_match.groupdict()['size'])
        cache = LRUCache(size)

    while True:
        command = raw_input()
        # In Python 3 only, there is a great syntax to unpack one and rest:
        # first, *rest = a_list
        command_parts = command.split(' ')
        method_name = command_parts[0].lower()
        try:
            method = getattr(cache, method_name)
        except AttributeError:
            if method_name == 'exit':
                break
            else:
                error()
        else:
            result = method()
            print(result)


def error():
    print('ERROR')

if __name__ == '__main__':
    session()
