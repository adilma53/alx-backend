#!/usr/bin/python3
""" Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """simple caching """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
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
