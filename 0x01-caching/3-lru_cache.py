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
                self.lru[key] = item
                self.lru.move_to_end(key)

                self.cache_data[key] = item
            else:
                self.lru[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                first_item_key, first_item_value = self.lru.popitem(last=False)

                self.cache_data.pop(first_item_key)

                print('DISCARD:', first_item_key)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys() and key in self.lru:
            self.lru.move_to_end(key)
            return self.cache_data.get(key, None)
