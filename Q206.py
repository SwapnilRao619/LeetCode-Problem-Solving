## N
## Idea, approach and time complexity:
'''
## A1:
The provided code reverses a singly linked list iteratively by maintaining three pointers: `prev`, `curr`, and `temp`. The `curr` pointer traverses the list, and for 
each node, it updates the `next` pointer to point to the `prev` node. This continues until the end of the list is reached, with the `prev` pointer ultimately pointing 
to the new head of the reversed list. The time complexity is \(O(n)\), where \(n\) is the number of nodes in the list, as each node is processed once.

##A2:
The provided code implements a recursive solution to reverse a singly linked list. The helping function takes two parameters: prev (the previous node) and curr 
(the current node). It reverses the pointers of the nodes by setting the next of the curr node to prev. If curr is None, it means we've reached the end of the list, and 
we return prev, which will be the new head of the reversed list.
'''

## A1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    
## A2
class Solution:
    def helping(self,prev,curr):
        if(not curr):
            return prev
        temp=curr.next
        curr.next=prev
        newhead=self.helping(curr,temp)
        return newhead
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helping(None,head)
