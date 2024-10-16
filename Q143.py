## N
## Idea, approach and time complexity:
'''
The approach for reordering a linked list consists of three main steps. First, we use a slow and fast pointer technique to find the middle of the list. Next, we reverse 
the second half of the list starting from the node after the midpoint. Finally, we merge the two halves by alternating nodes from the first half with nodes from the 
reversed second half. This solution operates in \( O(n) \) time complexity, making it efficient for processing linked lists.
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next,prev=None,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        p1,p2=head,prev
        while p1 and p2:
            tp1=p1.next
            p1.next=p2
            tp2=p2.next
            p2.next=tp1
            p1=tp1
            p2=tp2