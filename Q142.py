## N
## Idea, approach and time complexity:
'''
The solution to detect a cycle in a linked list uses Floyd's Tortoise and Hare algorithm. Two pointers, slow (`s`) and fast (`f`), traverse the list at different speeds; 
slow moves one step at a time, while fast moves two steps. If a cycle exists, the two pointers will eventually meet inside the cycle. Once a cycle is detected, the slow 
pointer is moved to the head of the list, and both pointers are advanced one step at a time until they meet again, which will be the start of the cycle. The time 
complexity of this approach is **O(n)**, where **n** is the number of nodes in the list, and the space complexity is **O(1)** since only two pointers are used.
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return None
        s,f=head,head
        while(f and f.next):
            s,f=s.next,f.next.next
            if(s==f):
                s=head
                while(s!=f):
                    s,f=s.next,f.next
                return s
        return None