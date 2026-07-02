class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,node):
        self.right.prev.next=node
        node.prev=self.right.prev
        node.next=self.right 
        self.right.prev=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        elif key not in self.cache:
            return -1
        
    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        
        self.insert(self.cache[key])
        if self.capacity < len(self.cache):
            LRU=self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        print(self.cache)
        




lrucache = LRUCache(2)
lrucache.put(1, 1)
lrucache.put(2, 2)
print(lrucache.get(1))
lrucache.put(3, 3)
print(lrucache.get(2))
lrucache.put(4, 4)







