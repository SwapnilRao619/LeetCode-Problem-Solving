## N
## Idea, approach and time complexity:
'''
The solution uses a binary search approach to find the minimum capacity required to ship all packages within the given number of days. The key idea is to check if a 
given capacity is sufficient by iterating through the package weights and keeping track of the current capacity and number of days required. The binary search narrows 
down the search range to find the minimum capacity that satisfies the day constraint. The time complexity of this approach is O(n log m), where n is the number of 
packages and m is the sum of all package weights, as the binary search takes O(log m) time and the capacity check takes O(n) time.
'''

class Solution:
    def canShip(self,arr,i):
        s,d=0,1
        for j in arr:
            if(s+j<=i):
                s+=j
            else:
                s=j
                d+=1
        return d

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,h=max(weights),sum(weights)
        res=h
        while(l<h):
            m=(l+h)//2
            if(self.canShip(weights,m)<=days):
                res=min(res,m)
                h=m
            else:
                l=m+1
        return res