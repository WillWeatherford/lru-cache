"""Implementation of Least Recently Used Cache data structure."""

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
        """Set the given key/value pair in the cache.

        First try to pop the item out of the cache, in order to then re-set its
        position as the most recently used item if it is already present.

        If the setting operation will cause the cache to be larger than its
        size limit, pop off the last used item.
        """
        try:
            self._cache.pop(key)
        except KeyError:
            pass
        self._cache[key] = value
        if len(self._cache) > self._size:
            # popitem() method of OrderedDict with last=False will pop items in
            # first-in, first-out order
            self._cache.popitem(last=False)

    def get(self, key):
        """Return the value for the given key in the cache.

        First try to pop the item out of the cache, in order to then re-set its
        position as the most recently used item if it is already present.
        """
        try:
            value = self._cache.pop(key)
        except KeyError:
            raise KeyError('Key not found in cache: {}'.format(key))
        else:
            self._cache[key] = value
            return value


def session():
    """Provide an interactive session to use a new LRU cache."""
    cache = initialize_cache()

    while True:
        command = raw_input().split(' ')
        # In Python 3 only, there is a better syntax to unpack first and rest:
        # first, *rest = a_list
        method = command[0]
        args = command[1:]
        if method == 'SET':
            try:
                cache.set(*args)
            except TypeError:
                error()
            else:
                print('SET OK')

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


def initialize_cache():
    """Sub-loop to ensure that cache is initialized by SIZE command first."""
    while True:
        command = raw_input()
        size_match = SIZE_PAT.match(command)
        if size_match is None:
            error()
            continue
        size = int(size_match.groupdict()['size'])
        cache = LRUCache(size)
        print('SIZE OK')
        break
    return cache


def error():
    """Simple function to print error."""
    print('ERROR')


if __name__ == '__main__':
    session()
