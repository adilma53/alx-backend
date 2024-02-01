#!/usr/bin/python3
""" Basic dictionary"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """class fifo"""
    def __init__(self):
        """init"""
        super().__init__()
        self.first = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if len(self.cache_data) == 0:
            self.first = key

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.first)
                print('DISCARD:', key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)

    def print_cache(self):
        """ Print the cache content
        """
        print("Current cache:")
        for k, v in self.cache_data.items():
            print(f"{k}: {v}")
