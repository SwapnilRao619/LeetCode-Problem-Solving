## N
## Idea, approach and time complexity:
'''
The solution converts two linked lists into integers by appending their values in reverse order, sums the two integers, and then constructs a new linked list from the 
digits of the resulting sum in reverse order. The approach efficiently handles the addition by leveraging Python's ability to manipulate strings and integers. The time 
complexity is \(O(n + m)\), where \(n\) and \(m\) are the lengths of the two linked lists, as it processes each list and constructs the result.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1,a2=[],[]
        while(l1):
            a1.append(l1.val)
            l1=l1.next
        while(l2):
            a2.append(l2.val)
            l2=l2.next
        d3=int(''.join(map(str,a1[::-1])))+int(''.join(map(str,a2[::-1])))
        a3=[int(digit) for digit in str(d3)][::-1]
        ans=ListNode(a3[0])
        curr=ans
        for i in range(1,len(a3)):
            curr.next=ListNode(a3[i])
            curr=curr.next
        return ans