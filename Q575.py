## Idea, approach and time complexity:
'''The approach uses a set to identify unique candy types and calculates the total number of candies. If half the total candies is greater than the number of unique 
types, the number of unique types is returned. Otherwise, half the total number of candies is returned. The time complexity of the code is O(n), where n is the length 
of the input list, due to the set conversion which ensures unique elements and the subsequent operations on the list length.'''

## Code:
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        self.l1=len(set(candyType)) #set for unique elements
        self.l2=len(candyType)
        if self.l2//2 > self.l1:
            return self.l1
        else:
            return self.l2//2