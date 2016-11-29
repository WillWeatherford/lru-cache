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

    def set(self, key, value):
        """."""
        try:
            self._cache.pop(key)
        except KeyError:
            pass
        self._cache[key] = value
        if len(self._cache) > self._size:
            # popitem() method of OrderedDict with last=False will pop items in
            # first-in, first-out order
            self._cache.popitem(last=False)
        return key

    def get(self, key):
        """."""
        try:
            value = self._cache.pop(key)
        except KeyError:
            raise KeyError('Key not found in cache: {}'.format(key))
        else:
            self._cache[key] = value
            return value


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
        print('SIZE OK')

    while True:
        command = raw_input().split(' ')
        # In Python 3 only, there is a better syntax to unpack first and rest:
        # first, *rest = a_list
        method = command[0]
        args = command[1:]
        if method == 'SET':
            try:
                result = cache.set(*args)
            except TypeError:
                error()
            else:
                print('SET {}'.format(result))
        elif method == 'GET':
            try:
                result = cache.get(*args)
            except TypeError:
                error()
            except KeyError:
                print('NOTFOUND')
            else:
                print('GOT {}'.format(result))
        elif method == 'EXIT':
                break
        else:
            error()


def error():
    print('ERROR')

if __name__ == '__main__':
    session()
