## Idea, approach and time complexity:
'''This code snippet aims to find the kth factor of a given integer n. It iterates through all numbers from 1 to n, checking if each number is a factor of n. The factors 
are stored in a list. If the list has at least k elements, it returns the kth factor; otherwise, it returns -1. The time complexity of this approach is O(n), where n is 
the given integer, as it iterates through all numbers from 1 to n to find the factors.'''

## Code:
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        self.s=[]
        for i in range(1,n+1):
            if n%i==0:
                self.s.append(i)
        if len(self.s)>=k:
            return self.s[k-1]
        else:
            return -1