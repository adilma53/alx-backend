#!/usr/bin/python3
""" Basic dictionary"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """class fifo"""
    def __init__(self):
        """init"""
        super().__init__()
        self.lru = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:

            self.cache_data[key] = item

            if key in self.lru:
                # Update the value and move the key to the end

                value = self.cache.pop(key)
                self.cache[key] = value
            else:
                self.lru[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                last_item_key, last_item_value = self.lru.popitem(last=True)

                self.cache_data.pop(last_item_key)

                print('DISCARD:', last_item_key)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys() and key in self.lru:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache_data.get(key, None)
