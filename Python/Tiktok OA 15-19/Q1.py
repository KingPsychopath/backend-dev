from collections import deque

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class FIFOCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key not in self.cache:
            if len(self.queue) == self.capacity:
                oldest_key = self.queue.popleft()
                del self.cache[oldest_key]
            self.cache[key] = value
            self.queue.append(key)


import unittest

class TestCaches(unittest.TestCase):
    def test_lru_cache(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)  # evicts key 2
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)  # evicts key 1
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    def test_fifo_cache(self):
        fifo = FIFOCache(2)
        fifo.put(1, 1)
        fifo.put(2, 2)
        self.assertEqual(fifo.get(1), 1)
        fifo.put(3, 3)  # evicts key 1
        self.assertEqual(fifo.get(1), -1)
        self.assertEqual(fifo.get(2), 2)
        fifo.put(4, 4)  # evicts key 2
        self.assertEqual(fifo.get(2), -1)
        self.assertEqual(fifo.get(3), 3)
        self.assertEqual(fifo.get(4), 4)

if __name__ == '__main__':
    unittest.main()