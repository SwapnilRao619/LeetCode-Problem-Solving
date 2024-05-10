## Idea, approach and time complexity:
'''The code implements a binary search algorithm to find the square root of a given integer x in the mySqrt method. It initializes two pointers l and r to 0 and x, 
respectively. Then, it iteratively updates the middle pointer m and compares the square of m with x. If m*m is greater than x, it adjusts the r pointer to m - 1. 
If m*m is less than x, it adjusts the l pointer to m + 1 and updates the res variable to the current value of m. If m*m is equal to x, it returns m. The loop continues 
until l exceeds r. Overall, the approach efficiently finds the integer square root of x using binary search, achieving a time complexity of O(log n), where n is the 
value of x.'''

## Code:
class Solution:
    def mySqrt(self, x: int) -> int:
        res=0
        l,r=0,x
        while(l<=r):
            m=(l+r)//2
            if m*m>x:
                r=m-1
            elif m*m<x:
                l=m+1
                res=m
            else:
                return m #perfect squares
        return res
        