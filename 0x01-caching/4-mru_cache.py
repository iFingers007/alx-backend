#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with MRU algorithm
    """
    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.mru.pop()
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]
            self.mru.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.mru.remove(key)
            self.mru.append(key)
        return self.cache_data.get(key)
