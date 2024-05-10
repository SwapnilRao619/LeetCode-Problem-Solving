## Idea, approach and time complexity:
'''The code initializes an object with a list of weights w in the __init__ method. It computes prefix sums of the weights and stores them in the prefixsums list. 
Additionally, it calculates the total sum of weights and stores it in the total attribute. The pickIndex method randomly selects an index based on the probability 
proportional to the weights. It generates a random target value between 0 and the total sum of weights. Then, it performs a binary search on the prefixsums list to 
find the index corresponding to the target value. Overall, the approach efficiently selects an index proportional to the weights of the elements using binary search, 
achieving a time complexity of O(log n), where n is the number of elements in the input list w.'''

## Code:
class Solution:

    def __init__(self, w: List[int]):
        total=0
        self.prefixsums=[]
        for wt in w:
            total+=wt
            self.prefixsums.append(total)
        self.total=total
        
    def pickIndex(self) -> int:
        target=random.uniform(0,self.total)
        l,r=0,len(self.prefixsums)-1
        while(l<r):
            m=(l+r)//2
            if target>self.prefixsums[m]:
                l=m+1
            else:
                r=m
        return l