## N
## Idea, approach and time complexity:
'''
The approach uses binary search to efficiently find the first bad version in a range from 1 to n. By checking the middle version, if it is not bad, the search continues 
in the right half; otherwise, it narrows down to the left half. This reduces the search space logarithmically. The time complexity is \(O(\log n)\) due to the halving 
of the search space with each iteration.
'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,h=1,n
        while(l<h):
            m=(l+h)//2
            if(isBadVersion(m)==False):
                l=m+1
            else:
                h=m
        return l