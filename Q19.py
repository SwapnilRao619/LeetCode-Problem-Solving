## N
## Idea, approach and time complexity:
'''
The provided solution for removing the N-th node from the end of a linked list uses a two-pass approach. First, it traverses the list to determine its length. Then, it 
iterates again to find the node just before the target node, adjusting the pointers to skip the N-th node from the end. If the list is empty or the only node is to be 
removed, it handles those cases explicitly. The time complexity of this approach is O(L), where L is the length of the list, since it requires two passes through the 
list. The space complexity is O(1) because it uses only a fixed amount of extra space.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length,curr=0,head
        while(curr):
            length+=1
            curr=curr.next
        if(length==1 and n==1):
            return
        if(length==n):
            return head.next
        counter,curr=1,head
        while(curr and counter<(length-n)):
            counter+=1
            curr=curr.next
        curr.next=curr.next.next
        return head