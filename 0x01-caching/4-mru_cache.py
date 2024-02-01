#!/usr/bin/python3
""" Basic dictionary"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """class fifo"""
    def __init__(self):
        """init"""
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:

            self.cache_data[key] = item

            if key in self.mru:
                # Update the value and move the key to the end

                self.mru.pop(self.mru.index(key))
                self.mru.append(key)
            else:
                self.mru.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                discard = self.mru.pop(-2)
                del self.cache_data[discard]

                print('DISCARD:', discard)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys() and key in self.mru:

            self.mru.pop(self.mru.index(key))
            self.mru.append(key)

            return self.cache_data.get(key, None)
