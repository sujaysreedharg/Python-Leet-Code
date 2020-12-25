class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev =self.next =None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
        
    
    #Remove from the left Node (LRU)
    def remove(self, node):
        prev,nxt = node.prev, node.next 
        prev.next,nxt.prev = nxt, prev
        
    #Insert into the right Node (MRU)
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev
        
    
    #Whenever we get a value, its gonna be updated to the Most Recently Used node and gets updated as the MRU
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value #if key present, then return key.val
        return -1 #if key not present then return -1
        
    #Whenever we put something in make sure that the capacity is not reached:
    #if the capacity has not been reached then we can update it to the desired key by acessing the hashmap(thats why we use a hashmap here.) and the (key value) becomes the MRU i.e it gets updated as the right most node
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # If the key is already present, then update the the new value to the same key by removing it and adding a new node
        self.cache[key]= Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap: #if the length of the hashmap is greater than the capacity then remove the LRU Node but how do we access the LRU, thats why we have the left most pointer (self.left.next) where the next points to the LRU
            LRU =self.left.next
            self.remove(LRU) #removing it from the DLL
            del self.cache[LRU.key]  #removing it the hashmap
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

Costs
Worst Case
space	O(n)
get least recently used item	O(1)
access item	O(1)


Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

