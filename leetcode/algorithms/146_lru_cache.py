#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 146. LRU Cache

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = dict()
        self.arr = []

    def get(self, key):
        if key in self.map.keys():
            index = self.arr.index(key)
            self.arr = [key]+self.arr[:index]+self.arr[index+1:]
            return self.map.get(key)
        return -1

    def put(self, key, value):
        # index 表示key在arr中的位置
        index = -1
        if key in self.map.keys():
            index = self.arr.index(key)
        elif len(self.arr) < self.capacity:
            self.arr.append(key)
            index = len(self.arr)-1
        elif len(self.arr) == self.capacity:
            index = self.capacity - 1
            self.map.pop(self.arr[index])

        self.arr = [key]+self.arr[:index]+self.arr[index+1:]
        self.map[key] = value


def test_lru_cache():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    print()
    print(cache.get(4))
    print(cache.get(3))
    print(cache.get(2))
    print(cache.get(1))
    cache.put(5, 5)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.get(5))

