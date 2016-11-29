# Least Recently Used Cache

Implementation of Least Recently Used Cache data structure.

This data structure requires both the key/value paradigm of a hash table as
well as the ordered paradigm of a queue. This is a great use case in Python
for `collections.OrderedDict` from the standard library.

This module defines class `LRUCAche` to represent the data structure, which in
turn uses composition of `collections.OrderedDict`.

The `get` and `set` methods on the `LRUCache` both try to pop and set again the
given key. `OrderedDict` keeps the order in which keys are added, meaning a key
which is popped and then re-set is the most recently added/used key.

When the size of the `OrderedDict` exceeds the size given upon initialization
of the `LRUCache`, `OrderedDict.popitem(last=True)` is used to remove the last
recently used item.

This module can be activated from the command line with `python lru_cache.py`,
which opens a REPR loop to interact with a new cache.

The following commands can be used in the REPR:
`SIZE <n>`: Initialize a new cache of size n
`SET <key> <val>`: Set key and value in the cache
`GET <key>`: Gives the value associated to the given key in the cache
`EXIT`: Close the REPR loop.

The class definition and REPR loop are decoupled by intention, such that the
LRUCache class can be used independently as needed.

Time Complexity:
As with a hash table, get and set are constant O(1) operations. Since each
operation will both pop and set a key/value to adjust the order of keys, it
will be twice as slow as a regular hash table.

Space Complexity:
Proportional to the number of keys/size of values added to the cache.
