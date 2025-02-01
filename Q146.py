## N
## Idea, approach and time complexity:
'''
The provided code implements an LRU (Least Recently Used) cache using a combination of a hash map (`hm`) and a doubly linked list (represented by `Node` class). The cache 
has a defined capacity (`c`), and the goal is to efficiently store and retrieve key-value pairs while evicting the least recently used entries when the cache exceeds the 
capacity. The doubly linked list keeps track of the access order: the most recently used item is at the "most recently used" (MRU) end, and the least recently used item 
is at the "least recently used" (LRU) end. When accessing (`get`) or adding (`put`) an item, the node representing the item is moved to the MRU end of the list. If the 
cache exceeds capacity, the LRU item (at the LRU end) is evicted. The approach ensures O(1) time complexity for both `get` and `put` operations by leveraging the hash 
map for constant time lookup and the doubly linked list for efficient insertions and deletions. The space complexity is O(n), where n is the number of keys in the cache, 
and the time complexity of both `get` and `put` is O(1).
'''

class Node:
    def __init__(self,k,v):
        self.k,self.v=k,v
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm={}
        self.c=capacity
        self.lru,self.mru=Node(0,0),Node(0,0)
        self.lru.next,self.mru.prev=self.mru,self.lru

    def remnode(self,node):
        p,n=node.prev,node.next
        p.next,n.prev=n,p

    def insatmru(self,node):
        n,p=self.mru,self.mru.prev
        p.next,n.prev=node,node
        node.prev,node.next=p,n

    def get(self, key: int) -> int:
        if(key in self.hm):
            self.remnode(self.hm[key])
            self.insatmru(self.hm[key])
            return self.hm[key].v
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.hm):
            self.remnode(self.hm[key])
        self.hm[key]=Node(key,value)
        self.insatmru(self.hm[key])
        if(len(self.hm)>self.c):
            lru=self.lru.next
            self.remnode(lru)
            del self.hm[lru.k]