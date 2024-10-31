#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with LIFO algorithm
    """
    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop()
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key)
