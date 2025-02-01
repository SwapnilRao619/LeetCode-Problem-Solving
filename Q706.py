## N
## Idea, approach and time complexity:
'''
The `MyHashMap` uses an array of linked lists to store key-value pairs, with each key mapped to an index using `key % 10^4`. The `put` method adds or updates a key-value 
pair, the `get` method retrieves a value, and `remove` deletes a pair by traversing the list at the calculated index. The time complexity for `put`, `get`, and `remove` 
is O(N), where N is the length of the list at an index (due to collisions). Typically, it's O(1) with good hash distribution. Space complexity is O(m), where m is the 
number of buckets (10,000).
'''

class Node:
    def __init__(self,k,v):
        self.k,self.v=k,v
        self.next=None

class MyHashMap:

    def __init__(self):
        self.hm=[Node(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index=key%(10**4)
        curr=self.hm[index]
        while(curr.next):
            if(curr.next.k==key):
                curr.next.v=value
                return
            curr=curr.next
        curr.next=Node(key,value)

    def get(self, key: int) -> int:
        index=key%(10**4)
        curr=self.hm[index]
        while(curr.next):
            if(curr.next.k==key):
                return curr.next.v
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % (10**4)
        curr = self.hm[index]
        while(curr and curr.next):
            if(curr.next.k==key):
                curr.next=curr.next.next
                return
            curr=curr.next