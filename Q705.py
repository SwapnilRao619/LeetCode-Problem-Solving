## N
## Idea, approach and time complexity:
'''
This `MyHashSet` implementation uses an array of linked lists (buckets) to handle hash collisions. Each key is hashed to an index, and if a collision occurs, the key is 
added to a linked list at that index. The `add` method checks if the key is already present, the `remove` method deletes the key, and `contains` checks for key existence 
by traversing the list at the hashed index. The time complexity for `add`, `remove`, and `contains` is O(n), where n is the number of elements in the list at a given 
index. However, with a good hash function, the expected time complexity is O(1). The space complexity is O(N), where N is the total number of elements in the hash set.
'''

class Node:
    def __init__(self,k):
        self.k=k
        self.next=None

class MyHashSet:

    def __init__(self):
        self.hs=[Node(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index=key%(10**4)
        curr=self.hs[index]
        while(curr and curr.next):
            if(curr.next.k==key):
                return
            curr=curr.next
        curr.next=Node(key)

    def remove(self, key: int) -> None:
        index=key%(10**4)
        curr=self.hs[index]
        while(curr and curr.next):
            if(curr.next.k==key):
                curr.next=curr.next.next
            curr=curr.next

    def contains(self, key: int) -> bool:
        index=key%(10**4)
        curr=self.hs[index]
        while(curr and curr.next):
            if(curr.next.k==key):
                return True
            curr=curr.next
        return False