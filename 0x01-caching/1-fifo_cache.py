#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system with FIFO algorithm
    """
    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {popped_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key)
