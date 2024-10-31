#!/usr/bin/env python3
"""FIFOcache Module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines a caching system with FIFO algorithm
    """
    def __init__(self):
        """Initialising of the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key
        """
        if key is None and Item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key = self.queue.pop()
                del self.cache_data[popped_key]
                print(f"DISCARD: {popped_key}")
            self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """returns value linked to key"""
        return self.cache_data.get(key, None)
