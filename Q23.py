## N
## Idea, approach and time complexity:
'''
The provided code defines a solution for merging `k` sorted linked lists. The approach uses a divide-and-conquer strategy, where pairs of lists are merged using the 
`mtl` (merge two lists) function until only one merged list remains. This reduces the problem size iteratively, and at each step, the time complexity for merging two 
lists is linear relative to their total length. Overall, the time complexity of merging `k` lists with a total of `n` nodes is O(n log k), since each merge operation is 
O(n) and there are log k merge operations due to the pairwise merging.
'''

class Solution:
    def mtl(self,l1,l2):
        dummy=ListNode()
        curr=dummy
        while(l1 and l2):
            if(l1.val<l2.val):
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        curr.next=l1 if l1 else l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists or len(lists)==0):
            return None
        while(len(lists)>1):
            ml=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                ml.append(self.mtl(l1,l2))
            lists=ml
        return lists[0]