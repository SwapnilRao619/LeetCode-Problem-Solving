## N
## Idea, approach and time complexity:
'''
The `minEatingSpeed` function determines the minimum eating speed (bananas per hour) required for a monkey to finish all banana piles within a specified number of hours, 
`h`. It employs a binary search strategy, where the search space ranges from 1 to the maximum number of bananas in any pile. For each candidate speed, it calculates the 
total hours required to eat all the bananas, adjusting the search boundaries based on whether the total exceeds `h`. The time complexity is \(O(n \log m)\), where \(n\) 
sis the number of piles and \(m\) is the maximum pile size, due to iterating over the piles for each speed check.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while(l<r):
            count=0
            m=(l+r)//2
            for i in piles:
                count+=(ceil(i/m))
            if(count>h):
                l=m+1
            else:
                r=m
        return l