#!/usr/bin/env python3
"""LIFOCache Module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a caching system with LIFO algorithm
    """
    def __init__(self):
        """Initialising of the class"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key, _ = self.keys.pop()
                print(f"DISCARD: {popped_key}")
                del self.cache_data[popped_key]
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns value linked to key"""
        return self.cache_data.get(key)
