## N
## Idea, approach and time complexity:
'''
The solution uses Floyd's Tortoise and Hare algorithm to detect a cycle in a linked list. Two pointers, `slow` and `fast`, traverse the list at different speeds; if they 
meet, a cycle exists. The time complexity is O(n), where n is the number of nodes in the list, as each node is visited at most twice. The space complexity is O(1), as it 
uses only a fixed amount of extra space.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head or not head.next):
            return False
        slow,fast=head,head
        while(fast and fast.next):
            slow,fast=slow.next,fast.next.next
            if(slow==fast):
                return True
        return False