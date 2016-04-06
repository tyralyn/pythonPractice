#A cache that evicts the leat recently used item

import collections

class LRUCache:
    def __init__(self,maxSize):
        self.cache = collections.OrderedDict()
        self.capacity = maxSize
        
    def printCache(self):
        print (self.cache)

    def cacheItem(self,k, v):
        if k in self.cache:
            del(self.cache[k])
        elif len(self.cache) > self.capacity:
            self.cache.popitem(True)
        else:
            pass
        self.cache[k]=v

    def accessItem(self, k):
        if k in self.cache:
           retVal = self.cache[k]
           del self.cache[k]
           self.cache[k] = retVal
           return retVal

l = LRUCache(4)
l.cacheItem(1,2)
l.printCache()
l.cacheItem('5',5)
l.cacheItem(9,4)
l.printCache()
l.cacheItem(1,2)
l.cacheItem(12,0)
l.printCache()
l.cacheItem('9',8)
l.accessItem('5')
l.printCache()
l.accessItem(10)
l.printCache()
