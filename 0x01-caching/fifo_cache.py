#!/usr/bin/env python3
"""FIFOcache Module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Defines a caching system with FIFO algorithm
    """
    def __init__(self):
        """Initialising of the class"""
        super().__init__()
        self.cached_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {popped_key}")
            self.cache_data[key] = item

    def get(self, key):
        """returns value linked to key"""
        return self.cache_data.get(key)
