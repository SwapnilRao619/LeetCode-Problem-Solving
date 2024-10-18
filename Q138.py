## N
## Idea, approach and time complexity:
'''
The solution for copying a linked list with random pointers involves two passes over the list. In the first pass, a hash map is used to create a copy of each node, 
mapping original nodes to their duplicates. In the second pass, the algorithm sets the `next` and `random` pointers of the new nodes using this mapping. The time 
complexity is O(n) due to processing each node twice, and the space complexity is also O(n) for storing the mappings.
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm,curr={None:None},head
        while(curr):
            hm[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while(curr):
            clone=hm[curr]
            clone.next=hm[curr.next]
            clone.random=hm[curr.random]
            curr=curr.next
        return hm[head]