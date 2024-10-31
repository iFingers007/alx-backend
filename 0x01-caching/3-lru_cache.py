#!/usr/bin/env python3
"""LRUcache Module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Defines a caching system with LRU algorithm
    """
    def __init__(self):
        """Initialising of the class"""
        super().__init__()
        self.cached_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if key in self.order:
                del self.order[key]
            self.order[key] = item
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped_key, _ = self.order.popitem(last=False)
                del self.cache_data[popped_key]
                print(f"DISCARD: {popped_key}")

    def get(self, key):
        """returns value linked to key"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cahe_data[key]
        del self.order[key]
        self.order[key] = value

        return value

