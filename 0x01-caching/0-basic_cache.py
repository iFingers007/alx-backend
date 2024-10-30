#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """assign to the dictionary self.cache_data the item for the key"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
