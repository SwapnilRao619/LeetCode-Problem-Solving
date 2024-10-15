## N
## Idea, approach and time complexity:
'''
The provided solution merges two sorted linked lists by using a dummy node to simplify handling of the head of the merged list. It iteratively compares the nodes of both
lists, appending the smaller node to the merged list, and continues until one list is exhausted. The remaining nodes of the non-exhausted list are then linked to the 
merged list. The time complexity is O(n + m), where n and m are the lengths of the two lists.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        ans=dummy
        while list1 and list2:
            if(list1.val<list2.val):
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        dummy.next=list1 if list1 else list2
        return ans.next
