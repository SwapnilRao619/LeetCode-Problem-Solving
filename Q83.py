## N
## Idea, approach and time complexity:
'''
The given code defines a method to remove duplicate values from a sorted linked list. It iterates through the list, checking if the current node's value is equal to the 
next node's value; if they are the same, it skips the next node by updating the current node's `next` pointer. This approach maintains the list's order while eliminating 
duplicates. The time complexity is O(n), where n is the number of nodes in the linked list, since it processes each node exactly once.
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while(curr and curr.next):
            if(curr.val==curr.next.val):
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head