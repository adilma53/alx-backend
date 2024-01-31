#!/usr/bin/python3
""" Basic dictionary"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item

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
