## N
## Idea, approach and time complexity:
'''
The `MyLinkedList` class implements a doubly linked list, allowing for efficient manipulation of nodes for adding, retrieving, and deleting elements at various positions. 
Each node structure contains a value along with pointers to both the next and previous nodes, facilitating bidirectional traversal. To simplify boundary case handling, 
the class uses two sentinel nodes—`left` and `right`—to represent the head and tail of the list, ensuring consistent operations when modifying the ends. The main methods 
include `get(index)`, which traverses the list to return the value at a specified index; `addAtHead(val)` and `addAtTail(val)`, which insert new nodes at the beginning 
and end, respectively; `addAtIndex(index, val)`, which adds a new node at a specific index if valid; and `deleteAtIndex(index)`, which removes a node at the given index 
if it exists. In terms of time complexity, `get`, `addAtIndex`, and `deleteAtIndex` operate in O(n) due to potential traversal, while `addAtHead` and `addAtTail` execute 
in O(1) as they modify the ends directly.
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
    
class MyLinkedList:
    def __init__(self):
        self.left=Node(0)
        self.right=Node(0)
        self.left.next=self.right
        self.right.prev=self.left

    def get(self, index: int) -> int:
        curr=self.left.next
        while(curr and index>0):
            curr=curr.next
            index-=1
        if(index==0 and curr and curr!=self.right):
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newnode,prev,next=Node(val),self.left,self.left.next
        prev.next=newnode
        newnode.prev=prev
        newnode.next=next
        next.prev=newnode

    def addAtTail(self, val: int) -> None:
        newnode,prev,next=Node(val),self.right.prev,self.right
        prev.next=newnode
        newnode.prev=prev
        newnode.next=next
        next.prev=newnode

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.left.next
        while(curr and index>0):
            curr=curr.next
            index-=1
        if(curr and index==0):
            newnode,prev,next=Node(val),curr.prev,curr
            prev.next=newnode
            newnode.prev=prev
            newnode.next=next
            next.prev=newnode

    def deleteAtIndex(self, index: int) -> None:
        curr=self.left.next
        while(curr and index>0):
            curr=curr.next
            index-=1
        if(curr and curr!=self.right and index==0):
            prev,next=curr.prev,curr.next
            prev.next=next
            next.prev=prev